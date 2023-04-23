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

# ve-header

The `.ve-header` tag is used to define an optional header that appears at the start of the essay.  The header can be used to:

- Define a title and subtitle for the essay
- Display a banner image
- Create a navigation menu for linking to sections within the current essay, to other essays, or to arbitrary web pages

As with the images displayed by the `.ve-media` tag, the banner image used by the `.ve-header` tag is a IIIF image and can be cropped or otherwise manipulated when displayed in the header.

## Attributes

**[label](#basic)** (_string_):  Essay title.

**[subtitle](#basic)** (_string_):  Essay subtitle, tagline, author name(s), etc.  The subtitle is displayed below the label attribute in a smaller font.

**[background](#background)** (_string_):  Either a color (name or code) or an IIIF image URL to be used for the header background.

**[options](#basic)** (_string_):  The options attribute is used to define the [IIIF image request parameters](https://iiif.io/api/image/2.1/#image-request-parameters) for the background banner image. This attribute is most commonly used to define a coordinates for displaying a cropped image region.

**[logo](#logo)** (_url_):  URL to an image to use for a logo in the navigation bar.

**[url](#logo)** (_url_):   Optional URL to associate with the logo.

**[contact](#contact)** (_string_):  Email address used in the contact form.  The display of the contact form is triggered by clicking an a menu item that includes the text `contact` or a `/contact` URL if the menu item is defined as link.

**[searchDomain](#search)** (_string_):  The domain name used in Google site search results that are displayed from a search menu embedded in the navigation bar,

**[sticky](#sticky-header)** (_boolean__):  If set, the header will collapse into a condensed form and remain fixed at the top of the page.

**[height](#basic)** (_number__):  Header height in pixels.

**[position](#basic)** (_string_):  The portion of a cropped banner image to display. The default is _center_. Other recognized values are _top_ and _bottom_. 

## Defining Menu items

Menu items are defined in a Markdown list of links following the `.ve-header` tag.  The links in the menu are used for navigating to internal pages or external sites.  If the URL for a menu item link includes the text `contact` the contact form will be displayed if accompanied with a `contact` attribute defining the destination email address.

## Examples

### Basic

<ve-snippet collapsible label="A basic header with a title">
    .ve-header "Essay Title"
</ve-snippet>

### Logo

<ve-snippet collapsible label="Header with a logo, url and custom background color">
    .ve-header "Essay Title" logo=https://raw.githubusercontent.com/juncture-digital/juncture/main/static/images/juncture-logo.png url=# background=#5B152E
</ve-snippet>

### Contact

<ve-snippet collapsible label="Header with a contact form" height=10rem>
    .ve-header Example background=#5B152E contact=someone@example.net
        - Contact Us
</ve-snippet>

### Search

<ve-snippet collapsible label="Header with a search form">
    .ve-header Example background=#5B152E search-domain=kent-maps.online
        - [Home](/home)
        - [About](/about)
</ve-snippet>

### Background

This example shows the use of a basic header with a title and custom background color.  In this example the custom background color `LightCoral` is used.  Any valid HTML color name or hex code may be used for a background color.  HTML supports 140 [standard color names](https://www.w3schools.com/colors/colors_names.asp).  The full range of colors can be at a number of online sites, including  [https://htmlcolorcodes.com](https://htmlcolorcodes.com/)

<ve-snippet collapsible label="A basic header with a custom background color">
    .ve-header "Essay Title" background=LightCoral
</ve-snippet>

<ve-snippet collapsible label="A header with a background image">
    .ve-header "Essay Title" wc:Sunflower.jpg
</ve-snippet>
### Sticky header

A sticky header defined with positional attributes and navigation menu options in a nested Markdown list.

<ve-snippet collapsible fill label="A sticky header with a cropped background image and menu">
    .ve-header "Essay Title" wc:Sunflower.jpg "Essay subtitle" pct:10,25,80,60 center sticky
        - [Home](/)
        - [About](/about)
</ve-snippet>
