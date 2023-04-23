# General Styling

Custom styles may be applied to a Juncture essay in few ways.

- Reference an external stylesheet
- Style tag in essay
- In-line element style

## Reference an external stylesheet

The `.ve-style` tag can be used to link to an external stylesheet.  The .ve-style tag requires a `href` attribute defining the stylesheet URL.  The href attribute may be included using positional or key-value notation.  The URL may be absolute or relative.

<ve-snippet collapsible label="Using external style sheet" prefix="rsnyder/essays" path="styling">

    .ve-style ./custom.css

    # Heading

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>

## Style tag in essay

An HTML `style` tag with CSS properties may be added in the essay text.

<ve-snippet collapsible label="Custom styling using HTML style tag">

<style>
    #juncture h1 { color: red; }
</style>

    # Heading

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>

In this example a `style` tag is used to load and use an external font.

<ve-snippet collapsible label="Style tag with font import">

<style>
    @import url(//fonts.googleapis.com/css?family=Montserrat);
    #juncture { font-family: Montserrat; }
    #juncture h1 { color: red; }
</style>

    # Heading

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>

## In-line element styling

In-line styling may also be applied to elements by appending an attributes block to an element.  An attributes block is defined with curly braces contaning key-value attribute definitions.  A CSS style attribute is defined with a `style` key and a value containing the CSS properties to be appliied.  For example, the attribute block `{style="border:1px solid red; padding:6px"}` sets CSS border and padding properties on an element.  

When applying an attibute block to a paragraph the block is included on a new line following the paragraph text.  

To apply CSS properties to an entire section the attribute block is included on the same like as the section heading with a space separting the attribute block from the heading text.  

It is not possible to apply inline styling to a section heading using the in-line styling.  To style a section heading element a `style` tag must be used.  The style tag example in the preceding section shows the use of a style tag to style a heading.

<ve-snippet collapsible label="Custom paragraph styling using attributes block">

    # Heading

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    {style="border:1px solid red; padding:6px"}

</ve-snippet>

<ve-snippet collapsible label="Custom section styling using attributes block">

    # Heading {style="border:1px solid red; padding:6px"}

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>