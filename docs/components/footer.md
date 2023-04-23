<style> 
    .markdown-section h2 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
    .markdown-section table { 
        margin-left:3rem; 
        width: calc(100% - 6rem); 
        border:1px solid #555;
    }
    .markdown-section td, .markdown-section th {
        border:1px solid #555;
        padding: 8px;
        line-height: 1.2;
    }
    .markdown-section th {
        background-color:#E2F0F7;
        font-weight:bold !important;
        text-align:center !important;
    }
</style>

# ve-footer

The `.ve-footer` tag is used to define an optional footer that appears at the bottom of the essay.  The footer contains a horizontal list of items.  Footer items may include logos, links or other informational items such as a license.

## Attributes

**[sticky](#sticky-footer)** (_boolean__):  If set, the header will collapse into a condensed form and remain fixed at the top of the page.

## Defining Footer items

Footer items are defined in a Markdown list.

## Examples

### Basic

<ve-snippet collapsible label="Footer with linked image, license badge, and About page link">
    .ve-footer
        - Powered by: [![Juncture Logo](https://juncture-digital.github.io/juncture/static/images/juncture-logo.png)](https://juncture-digital.org)
        - [![CC BY](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
        - [About](/about)
</ve-snippet>

### Sticky footer

