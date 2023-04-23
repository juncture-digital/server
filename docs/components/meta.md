# ve-meta
The `.ve-meta` tag is used to define metadata attributes for the page.  Defining _.ve-meta_ tag in an essay enables the rendered essay to be indexed by search engines.  When the tag is not found in an essay a _noindex_ tag is added to the generated page by default.

## .ve-meta Attributes

- **title** (_text string_):  A short title for the page.  This title will be added to the browser window or tab.  When indexed by search engines this title will also appear in the search results item.   
- **description** (_text string_):  A short description of the page.  When indexed by search engines this description will appear in the search results item. 

###  Example

```Markdown
.ve-meta title="The Page Title" description="A brief description of the page. This will appear in Google search results."
```
