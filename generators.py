import logging
from re import L
logging.basicConfig(format='%(asctime)s : %(filename)s : %(levelname)s : %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from urllib.parse import quote
import markdown

positional_defaults = {
  've-card': ['label', 'image', 'href', 'description'],
  've-header': ['label', 'background', 'subtitle', 'options', 'position'],
  've-iframe': ['src'],
  've-image': ['src', 'options', 'seq', 'fit'],
  've-map': ['center', 'zoom', 'overlay'],
  've-media': ['src'],
  've-meta': ['title', 'description'],
  've-spacer': ['height'],
  've-style': ['href'],
  've-video': ['src', 'caption'],
}

class_args = {
  've-component': [],
  've-entities': ['text-left', 'text-right'],
  've-image': ['text-left', 'text-right', 'col2', 'col3'],
  've-map': ['text-left', 'text-right'],
  've-media': ['text-left', 'text-right', 'col2', 'col3'],
  've-video': ['text-left', 'text-right'],
}

boolean_attrs = {
  've-component': ['sticky',],
  've-entities': ['full', 'left', 'right', 'sticky'],
  've-footer': ['sticky',],
  've-header': ['sticky',],
  've-iframe': ['allow', 'allowfullscreen', 'full', 'left', 'right', 'sticky'],
  've-image': ['cards', 'compare', 'curtain', 'full', 'grid', 'left', 'right', 'sticky', 'sync', 'zoom-on-scroll'],
  've-map': ['cards', 'full', 'left', 'marker', 'prefer-geojson', 'popup-on-hover', 'right', 'sticky', 'zoom-on-scroll', 'zoom-on-click'],
  've-media': ['autoplay', 'cards', 'compare', 'full', 'grid', 'left', 'muted', 'no-caption', 'no-info-icon', 'right', 'small', 'static', 'sticky'],
  've-media-selector': ['full', 'left', 'right', 'sticky'],
  've-mermaid': ['full', 'left', 'right', 'sticky'],
  've-video': ['full', 'left', 'right', 'sticky']
}

def default(ctx, *args, **kwargs):
  logger.debug(f'args={args} kwargs={kwargs}')
  if len(args) > 0:
    _classes = []
    idx = 0
    for arg in args:
      if ctx.type in boolean_attrs and arg in boolean_attrs[ctx.type]:
        kwargs[arg] = 'true'
      elif ctx.type in class_args and arg in class_args[ctx.type]:
        _classes.append(arg)
      elif ctx.type in positional_defaults and idx < len(positional_defaults[ctx.type]):
        kwargs[positional_defaults[ctx.type][idx]] = arg
        idx += 1
    if len(_classes) > 0:
      kwargs['class'] = ' '.join(_classes)
  logger.debug(f'{ctx.type} {kwargs}')
  # kwargs = [f'{k}="{quote(v)}"' for k,v in kwargs.items()]
  kwargs = [f'{k}="{v}"' for k,v in kwargs.items()]
  if ctx.type == 've-iframe':
    kwargs = [v.replace('&','&amp;') for v in kwargs]
  
  html = f'<{ctx.type} {" ".join(kwargs)}>{markdown.markdown(ctx.content)}</{ctx.type}>'
  return html