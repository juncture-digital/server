# ve-annotate

The `ve-annotate` adds the [Hypothes.is](https://web.hypothes.is/) annotation client to an essay.  The Hypothes.is annotation tool is [widely used in education](https://web.hypothes.is/education/).  It is open source and based on standards developed by the W3C Web Annotation Working Group. 

The `.ve-annotate` does not use any attributes.  Simply add the tag anywhere in your essay text and the annotation client will be added to the rendered essay.  That's it.  Using the annotation client from a rendered essay will require logging into Hypothes.is.  New Hypothes.is users will need to [signup for a free Hypothes.is account](https://web.hypothes.is/start/).


?> Note that the annotation client is not added to an essay when displayed in an example snippet or in preview mode in the Juncture editor.  The example below demonstrates how to add the `.ve-annotate` tag.

<ve-snippet>
    # My Essay

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    .ve-annotate

</ve-snippet>