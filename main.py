#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python app for Juncture site.
Dependencies: bs4 fastapi html5lib lxml Markdown==3.3.6 mdx-breakless-lists prependnewline pymdown-extensions requests uvicorn git+https://github.com/rdsnyder/mdx_outline.git git+https://github.com/rdsnyder/markdown-customblocks.git

'''

import logging

logging.basicConfig(format='%(asctime)s : %(filename)s : %(levelname)s : %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import os
import sys
import re
import argparse

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(SCRIPT_DIR)

BASEDIR = SCRIPT_DIR
STATICDIR = f'{BASEDIR}/static'
logger.info(f'BASEDIR={BASEDIR} STATICDIR={STATICDIR}')

from bs4 import BeautifulSoup

import markdown

from generators import default

from typing import Optional

import uvicorn

from fastapi import FastAPI
from fastapi.responses import Response

from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse
app = FastAPI(title='Juncture API', root_path='/')
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=['*'],
  allow_headers=['*'],
  allow_credentials=True,
)

import requests
logging.getLogger('requests').setLevel(logging.INFO)

def convert_urls(soup, base, acct, repo, ref, ghp=False):
  logger.info(f'convert_urls: base={base} acct={acct} repo={repo} ref={ref} ghp={ghp}')
  
  # remove Github badges
  for img in soup.find_all('img'):
    if 've-button.png' in img.attrs['src']:
      img.parent.decompose()
  
  # convert absolute links
  for elem in soup.find_all(href=True):
    if elem.attrs['href'].startswith('http'):
      elem.attrs['target'] = '_blank'
    orig = elem.attrs['href']
    if elem.attrs['href'].startswith('/'):
      if ghp:
        base = f'/{repo}/'
      else:
        base_elems = [elem for elem in base.split('/') if elem]
        if len(base_elems) >= 2 and base_elems[0] == acct and base_elems[1] == repo:
          base = f'/{acct}/{repo}/'
        else:
          base = '/'
      converted = base + elem.attrs['href'][1:] + (f'?ref={ref}' if ref else '')
      elem.attrs['href'] = converted
    else:
      if ref:
        elem.attrs['href'] += f'?ref={ref}'
    logger.debug(f'orig={orig} base={base} converted={elem.attrs["href"]}')
  
  # convert image URLs
  for elem in soup.find_all(src=True):
    if elem.attrs['src'].startswith('http') or elem.name.startswith('ve-'): continue
    base_elems = base.split('/')[6:-1]
    src_elems = [pe for pe in re.sub(r'^\.\/', '', elem.attrs['src']).split('/') if pe]
    up = src_elems.count('..')
    gh_path = '/'.join(base_elems[:-up] + src_elems[up:])
    elem.attrs['src'] = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{gh_path}'

def _config_tabs(soup):
  for el in soup.find_all('section', class_='tabs'):
    # el_heading = next(el.children) 
    # el_heading.decompose()
    for idx, tab in enumerate(el.find_all('section', recursive=False)):
      heading = next(tab.children)
      # tab_id = tab.attrs['id'] if 'id' in tab.attrs else sha256(heading.text.encode('utf-8')).hexdigest()[:8]
      tab_id = f'tab{idx+1}'
      content_id = f'content{idx+1}'
      input = soup.new_tag('input')
      input.attrs = {'type': 'radio', 'name': 'tabs', 'id': tab_id}
      tab.attrs['class'].append('tab')
      if idx == 0:
        input.attrs['checked'] = ''
      label = soup.new_tag('label')
      label.string = heading.text
      label.attrs = {'for': tab_id}
      el.insert(idx*2, input)
      el.insert(idx*2+1, label)
      tab.attrs['class'].append(content_id)
      heading.decompose()
  
def _config_cards(soup):
  for el in soup.find_all('section', class_='cards'):
    cards_wrapper = soup.new_tag('section')
    el.attrs['class'] = [cls for cls in el.attrs['class'] if cls != 'cards']
    cards_wrapper.attrs['class'] = ['cards', 'wrapper']
    for card in el.find_all('section', recursive=False):
      heading = next(card.children)
      if 'href' in card.attrs:
        card_title = soup.new_tag('a')
        card_title.attrs['href'] = card.attrs['href']
        if card.attrs.get('target') == '_blank' or card.attrs['href'].startswith('http'):
          card_title.attrs['target'] = '_blank'
      else:
        card_title = soup.new_tag('span')
      card_title.attrs['class'] = 'card-title'
      card_title.string = heading.text
      card.insert(0,card_title)
      heading.decompose()

      if card.p.img:
        
        img_style = {
          'background-image': f"url('{card.p.img.attrs['src']}')",
          'background-repeat': 'no-repeat',
          'background-size': 'cover',
          'background-position': 'center'
        }
        style = '; '.join([f'{key}:{value}' for key,value in img_style.items()]) + ';'
        img = soup.new_tag('div')
        img.attrs['class'] = 'card-image'
        img.attrs['style'] = style
        card.insert(1,img)
        card.p.decompose()

      if card.ul:
        card.ul.attrs['class'] = 'card-metadata'
        for li in card.ul.find_all('li'):
          if li.text.split(':')[0].lower() in ('coords', 'eid', 'qid'):
            li.attrs['class'] = 'hide'
  
      if card.p:
        card.p.attrs['class'] = 'card-abstract'

      card.attrs['class'].append('card')
      cards_wrapper.append(card)
    el.append(cards_wrapper)

mark_regexes = {
  'anno': re.compile(r'^[0-9a-f]{8}$'),
  'zoomto': re.compile(r'^(pct:)?\d+,\d+,\d+,\d+(,[0-9a-f]{8})?$'),
  'play': re.compile(r'^[0-9:]+(,[0-9:]+)?$'),
  'flyto': re.compile(r'^[\-+]?[0-9\.]+,[\-+]?[0-9\.]+(,[0-9\.]+)?$'),
  'qid': re.compile(r'^Q[0-9]+$')
}

def _set_mark_attrs(soup):
  for mark in soup.find_all('mark'):
    _revised = {}
    for k,v in mark.attrs.items():
      if k in mark_regexes:
        _revised[k] = v
      elif v.split(':',1)[0] in mark_regexes:
        _revised[v.split(':',1)[0]] = v.split(':',1)[1]
      else:
        regex_match = None
        for attr_key, regex in mark_regexes.items():
          regex_match = regex.match(v)
          if regex_match:
            _revised[attr_key] = v
            break
        if not regex_match:
          _revised[k] = v
    mark.attrs = _revised
    # logger.info(mark.attrs)

def add_link(soup, href, attrs=None):
  link = soup.new_tag('link')
  link.attrs = {**{'href':href}, **(attrs if attrs else {})}
  soup.head.append(link)

def add_script(soup, src, attrs=None):
  script = soup.new_tag('script')
  script.attrs = {**{'src':src}, **(attrs if attrs else {})}
  soup.body.append(script)

def add_meta(soup, attrs=None):
  meta = soup.new_tag('meta')
  meta.attrs = attrs
  soup.head.append(meta)

def merge_entities(tag, qids=None):
  qids = qids or []
  qids = qids + [qid for qid in tag.attrs.get('entities','').split() if qid not in qids]
  return merge_entities(tag.parent, qids) if tag.parent else qids

def find_qids(text):
  return re.findall(r'\b(Q[0-9]+)\b', text) if text else []

def set_entities(soup):
  for p in soup.find_all('p'):
    if p.parent.name == 've-mermaid': continue
    qids = find_qids(p.string)
    if qids:
      p.string = re.sub(r'\b(Q[0-9]+)\b', '', p.string).rstrip()
      if p.string:
        p.attrs['entities'] = ' '.join(qids)
      else:
        p.parent.attrs['entities'] = ' '.join(qids)
        p.decompose()
    
    if p.string:
      lines = [line.strip() for line in p.string.split('\n')]
      if len(lines) > 1:
        cursor = 1
        match = re.match(r'\d{2}:\d{2}:\d{2}', lines[0])
        if match:
          new_p = BeautifulSoup(f'<p data-start={match[0]} entities="{" ".join(qids)}"><mark play="{match[0]}"><b>{lines[0]}</b></mark></br>{" ".join(lines[1:2])}</p>', 'html5lib')
          cursor = 2
        else:
          new_p = BeautifulSoup(f'<p entities="{" ".join(qids)}">{" ".join(lines[:1])}</p>', 'html5lib')
        new_p = new_p.find('p')
        new_p.attrs = {**new_p.attrs, **p.attrs}
        if len(lines) > cursor:
          new_p.attrs['data-media'] = ' '.join(lines[cursor:])
        p.replace_with(new_p)
  
  for tag in ('p', 'section', 'main'):
    for el in soup.find_all(tag):
      qids = merge_entities(el)
      if qids:
        el.attrs['entities'] = ' '.join(qids)
        for child in el.find_all(recursive=False):
          if child.name.startswith('ve-'):
            child.attrs['entities'] = ' '.join(qids)

def j1_to_j2_md(src):
  """Convert Juncture version 1 markdown to HTML"""
  return ''

def j1_md_to_html(src, **args):
  """Convert Juncture version 1 markdown to HTML"""
  base_url = args.pop('base', '')
  ghp = args.pop('ghp', False)
  acct = args.pop('acct', None)
  repo = args.pop('repo', None)
  ref = args.pop('ref', 'main')
  path = args.pop('path', None)
  # prefix = args.pop('prefix', f'{acct}/{repo}')
  prefix = ''
  
  logger.info(f'j1_md_to_html: base_url={base_url}, ghp={ghp}, acct={acct}, repo={repo}, ref={ref}, path={path}, prefix={prefix}')

  def replace_empty_headings(match):
    return re.sub(r'(#+)(.*)', r'\1 &nbsp;\2', match.group(0))
  
  md = re.sub(r'^#{1,6}(\s+)(\{.*\}\s*)?$', replace_empty_headings, src, flags=re.M)
    
  html = markdown.markdown(
    md,
    extensions=[
      'customblocks',
      'extra',
      'pymdownx.mark',
      'mdx_outline',
      'codehilite',
      'prependnewline',
      'fenced_code',
      'mdx_breakless_lists',
      'sane_lists'
      # 'mdx_urlize'
    ],
    extension_configs = {
      'customblocks': {
        'fallback': default,
        'generators': {
          'default': 'md.generators:default'
        }
      }
    }
  )

  def em_repl(match):
    return match.group(0).replace('<em>','_').replace('</em>','_')

  html = re.sub(r'<h[1-6]>\s*&nbsp;\s*<\/h[1-6]>', '', html)
  html = re.sub(r'(\bwc:\S*<\/?em>.*\b)', em_repl, html)
  
  soup = BeautifulSoup(html, 'html5lib')

  convert_urls(soup, base_url, acct, repo, ref, ghp)

  for el in soup.findAll(re.compile("^ve-.+")):
    el.attrs = dict([(k,v if v != 'true' else None) for k,v in el.attrs.items()])
  
    if el.name in ('ve-image', 've-video'):
      el.name = 've-media'

  add_hypothesis = soup.find('ve-add-hypothesis') or soup.find('ve-annotate')
  custom_style = soup.find('ve-style')
  footer = soup.find('ve-footer')
  first_heading = soup.find(re.compile('^h[1-6]$'))
  
  _config_tabs(soup)
  _config_cards(soup)
  _set_mark_attrs(soup)

 # insert a 'main' wrapper element around the essay content
  main = soup.html.body
  main.attrs = soup.html.body.attrs
  main.name = 'main'
  main.attrs['id'] = 'juncture'
  body = soup.new_tag('body')
  contents = main.replace_with(body)
  body.append(contents)

  footnotes = soup.find('div', class_='footnote')
  if footnotes:
    footnotes.name = 'section'
    contents.append(footnotes)

  if footer: main.append(footer)

  set_entities(soup)

  # api_static_root_js = f'http://{host}:8000/static' if env == 'DEV' else 'https://api.juncture-digital.org/static'

  meta = soup.find('param', ve_config='')
  template = open(f'{STATICDIR}/v1/index.html', 'r').read()
  if prefix: template = template.replace('const PREFIX = null', f"const PREFIX = '{prefix}';")
  if ref: template = template.replace('const REF = null', f"const REF = '{ref}';")
  template = BeautifulSoup(template, 'html5lib')
  for el in template.find_all('component'):
    if 'v-bind:is' in el.attrs and el.attrs['v-bind:is'] == 'mainComponent':
      el.append(contents)
      break
  
  '''
  css = open(f'{STATICDIR}/v1/css/main.css', 'r').read()
  base = template.find('base')
  if base:
    base.attrs['href'] = base_url
  
  style = soup.new_tag('style')
  style.attrs['data-id'] = 'default'
  style.string = css
  template.body.insert(0, style)

  script = soup.new_tag('script')
  script.attrs['type'] = 'module'
  script.string = open(f'{STATICDIR}/v1/js/main.js', 'r').read()
  template.body.append(script)
  '''

  if meta:
    for name in meta.attrs:
      if name == 'title':
        if not template.head.title:
          template.head.append(template.new_tag('title'))
        template.head.title.string = meta.attrs[name]
      elif name not in ('author', 'banner', 'layout'):
        add_meta(template, {'name': name, 'content': meta.attrs[name]})
    if meta.name == 've-meta':
      meta.decompose()
  
  if not (template.head.title and template.head.title.string) and first_heading:
    title = soup.new_tag('title')
    title.string = first_heading.text
    template.head.append(title)

  # html = str(template)
  html = template.prettify()
  html = re.sub(r'\s+<p>\s+<\/p>', '', html) # removes empty paragraphs
  return html

def j2_md_to_html(src, **args):
  """Convert Juncture version 2 markdown to HTML"""
  
  base_url = args.pop('base', '')
  ghp = args.pop('ghp', False)
  acct = args.pop('acct', None)
  repo = args.pop('repo', None)
  ref = args.pop('ref', 'main')
  path = args.pop('path', None)
  # prefix = args.pop('prefix', f'{acct}/{repo}')
  prefix = ''
  
  logger.info(f'j2_md_to_html: base_url={base_url}, ghp={ghp}, acct={acct}, repo={repo}, ref={ref}, path={path}, prefix={prefix}')

  def replace_empty_headings(match):
    return re.sub(r'(#+)(.*)', r'\1 &nbsp;\2', match.group(0))
  
  md = re.sub(r'^#{1,6}(\s+)(\{.*\}\s*)?$', replace_empty_headings, src, flags=re.M)
    
  html = markdown.markdown(
    md,
    extensions=[
      'customblocks',
      'extra',
      'pymdownx.mark',
      'mdx_outline',
      'codehilite',
      'prependnewline',
      'fenced_code',
      'mdx_breakless_lists',
      'sane_lists'
    ],
    extension_configs = {
      'customblocks': {
        'fallback': default,
        'generators': {
          'default': 'md.generators:default'
        }
      }
    }
  )

  def em_repl(match):
    return match.group(0).replace('<em>','_').replace('</em>','_')

  html = re.sub(r'<h[1-6]>\s*&nbsp;\s*<\/h[1-6]>', '', html)
  html = re.sub(r'(\bwc:\S*<\/?em>.*\b)', em_repl, html)
  
  soup = BeautifulSoup(html, 'html5lib')

  convert_urls(soup, base_url, acct, repo, ref, ghp)

  for el in soup.findAll(re.compile("^ve-.+")):
    el.attrs = dict([(k,v if v != 'true' else None) for k,v in el.attrs.items()])
  
    if el.name in ('ve-image', 've-video'):
      el.name = 've-media'

  add_hypothesis = soup.find('ve-add-hypothesis') or soup.find('ve-annotate')
  custom_style = soup.find('ve-style')
  footer = soup.find('ve-footer')
  first_heading = soup.find(re.compile('^h[1-6]$'))
  
  _config_tabs(soup)
  _config_cards(soup)
  _set_mark_attrs(soup)

 # insert a 'main' wrapper element around the essay content
  main = soup.html.body
  main.attrs = soup.html.body.attrs
  main.name = 'main'
  main.attrs['id'] = 'juncture'
  body = soup.new_tag('body')
  contents = main.replace_with(body)
  body.append(contents)

  footnotes = soup.find('div', class_='footnote')
  if footnotes:
    footnotes.name = 'section'
    contents.append(footnotes)

  if footer: main.append(footer)

  set_entities(soup)

  css = ''
  # api_static_root_js = f'http://{host}:8000/static' if env == 'DEV' else 'https://api.juncture-digital.org/static'
  meta = soup.find('ve-meta')
  footer = soup.find('ve-footer')

  if prefix:
    for el in soup.find_all('ve-media'):
      el.attrs['anno-base'] = prefix + (f'/{path}' if path != '/' else '')
    for el in soup.find_all('ve-map'):
      if prefix:
        el.attrs['essay-base'] = f'{prefix}/{ref}/' + (f'{path}' if path != '/' else '')
  
  template = open(f'{STATICDIR}/v2/index.html', 'r').read()
  if prefix: template = template.replace('window.PREFIX = null', f"window.PREFIX = '{prefix}';")
  if ref: template = template.replace('window.REF = null', f"window.REF = '{ref}';")
  template = BeautifulSoup(template, 'html5lib')
  template.body.insert(0, contents)
    
  if custom_style:
    css_href = custom_style.attrs.get('href')
    if css_href:
      if not css_href.startswith('http'):
        _path = f'{prefix}/{path}{css_href[1:]}'
        content = get_gh_file(_path)
        if content:
          css = content.markdown

    custom_style.decompose()
    
  if add_hypothesis:
    add_hypothesis.decompose()
    add_script(template, 'https://hypothes.is/embed.js', {'async': 'true'})
    
  if soup.head.style:
    template.body.insert(0, soup.head.style)

  base = template.find('base')
  if base:
    base.attrs['href'] = base_url
  
  if css:
    # add css as style tag
    style = soup.new_tag('style')
    style.attrs['data-id'] = 'default'
    style.string = css
    # template.head.append(style)
    template.body.insert(0, style)

  '''
  script = soup.new_tag('script')
  script.attrs['type'] = 'module'
  script.string = open(f'{STATICDIR}/v2/js/main.js', 'r').read()
  template.body.append(script)
  '''

  if meta:
    for name in meta.attrs:
      if name == 'title':
        if not template.head.title:
          template.head.append(template.new_tag('title'))
        template.head.title.string = meta.attrs[name]
      elif name not in ('author', 'banner', 'layout'):
        add_meta(template, {'name': name, 'content': meta.attrs[name]})
    if meta.name == 've-meta':
      meta.decompose()
  # else:
    # add_meta(template, {'name': 'robots', 'content': 'noindex'})
  
  if not (template.head.title and template.head.title.string) and first_heading:
    title = soup.new_tag('title')
    title.string = first_heading.text
    template.head.append(title)
    
  # html = str(template)
  html = template.prettify()
  html = re.sub(r'\s+<p>\s+<\/p>', '', html) # removes empty paragraphs
  
  return html

def html_to_wp(src):
  """Convert J1 HTML to WordPress"""
  return ''

def detect_format(src):
  """Detect format of source file"""
  params = re.findall(r'<param', src)
  return 'j1_md' if params else 'j2_md'

def read(src):
  """Read source file"""
  if src.startswith('https://raw.githubusercontent.com'):
    url = src if src.endswith('.md') else src + '.md'
    resp = requests.get(url)  
    if (resp.status_code == 404):
      url = src + '/README.md'
      resp = requests.get(url)
    return resp.text
  else:
    with open(src, 'r') as f:
      return f.read()

def convert(**args):
  """Convert source file to specified format"""
  src = args.pop('src')
  if src.startswith('https://raw.githubusercontent.com'):
    path_elems = src.split('/')[3:]
    acct, repo, ref, *path_elems = path_elems
    path = '/' + '/'.join(path_elems)
    args = {**args, 'acct': acct, 'repo': repo, 'ref': ref, 'path': path}

  fmt = args.pop('fmt')
  contents = read(src)
  in_fmt = detect_format(contents)

  if in_fmt == 'j1_md':
    if fmt == 'j2_md':
      return j1_to_j2_md(contents)
    elif fmt == 'html':
      return j1_md_to_html(contents, **args)
    elif fmt == 'wp':
      return html_to_wp(j1_md_to_html(contents))
  elif in_fmt == 'j2_md':
    if fmt == 'html':
      return j2_md_to_html(contents, **args)
    elif fmt == 'wp':
      return html_to_wp(j2_md_to_html(contents))
    else:
      return contents
  elif in_fmt == 'html':
    if fmt == 'wp':
      return html_to_wp(contents)

@app.get('/docs/')
@app.get('/')
def main():
  return RedirectResponse(url='/docs')

template = '''<!doctype html>
<html lang="en">
  <head>
    <title>Markdown</title>
  </head>
  <body>
    <ve-source-viewer src="%s"></ve-source-viewer>
    <script src="https://cdn.jsdelivr.net/npm/juncture-digital/docs/js/index.js" type="module"></script>
  </body>
</html>'''

@app.get('/favicon.ico')
async def ignore():
  return Response(status_code=404)

@app.get('/{path:path}/')
@app.get('/{path:path}')
@app.get('/')
async def serve(
    path: Optional[str] = None,
    ref: Optional[str] = 'main',
    fmt: Optional[str] = 'html'
  ):
  logger.info(f'path={path}')
  logger.info(path.split('/'))
  acct, repo, *path_elems = path.split('/') if path else ('juncture-digital', 'juncture', '')
  gh_path = '/'.join(path_elems)
  # gh_path += 'README.md' if gh_path.endswith('/') else '/README.md'
  src = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{gh_path}'
  
  resp = convert(src=src, fmt=fmt)

  if fmt == 'html':
    # return resp, 200
    return Response(status_code=200, content=resp, media_type='text/html')
  else:
    return template % f'{acct}/{repo}/{gh_path}', 200
    # return Response(resp, mimetype='text/markdown')

if __name__ == '__main__':
  logger.setLevel(logging.INFO)
  parser = argparse.ArgumentParser(description='Juncture content converters')
  parser.add_argument('--src', help=f'Path to source file')
  parser.add_argument('--fmt', default='html', help='Output format')
  parser.add_argument('--ghp', type=bool, default=False, help='Hosted on Github Pages')
  parser.add_argument('--acct', help='Github account')
  parser.add_argument('--repo', help='Github repo')
  parser.add_argument('--ref', help='Github ref')
  parser.add_argument('--path', help='Github path')
  parser.add_argument('--prefix', help='Github path')
  
  parser.add_argument('--serve', type=bool, default=False, help='Serve converted content')
  parser.add_argument('--reload', type=bool, default=False, help='Reload on change')
  parser.add_argument('--port', type=int, default=8080, help='HTTP port')

  args = vars(parser.parse_args())
  logger.info(args)
  
  if args['serve']:
    uvicorn.run('main:app', port=args['port'], log_level='info', reload=args['reload'])
  else:
    print(convert(**dict([(k,v) for k,v in args.items() if v])))
  
