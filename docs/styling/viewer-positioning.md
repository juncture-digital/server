# Viewer positioning

When displayed on a desktop, laptop or tablet the default behavior for the Juncture viewers (`.ve-media`, `.ve-map`, `-ve-mermaid`) is to render the full width of the essay page.  This behavior can be altered using positioning attributes that explicitly set the width to a specific size or to a size that is half of the essay width.  When displayed on a smartphone or other type of small screen the viewers will always attempt to use the full screen width.

## Using positioning attributes

Note that when used they are only applied when an essay is rendered on a desktop, laptop, or tablet. 

- **full** (_default_): Sets the viewer width to the full width of the essay.  For the `.ve-media` viewer for an image or video, tje the height is automatically determined to maintain aspect ratio of the source item.
- **left**: Sets the viewer width to 50% of the essay width and aligns it with the left margin.
- **right** Sets the viewer width to 50% of the essay width and aligns it with the left margin.

<ve-snippet collapsible label="Full width (default) positioning">
.ve-media wc:The_Bug_Peek.jpg
</ve-snippet>

<ve-snippet collapsible label="Left positioning">
.ve-media wc:The_Bug_Peek.jpg left
</ve-snippet>

<ve-snippet collapsible label="Right positioning">
.ve-media wc:The_Bug_Peek.jpg right
</ve-snippet>

When using `left` or `right` positioning text will flow around the image unless the `sticky` position attribute is also used.  The example below shows a right aligned image with wrap around text.

<ve-snippet collapsible label="Right positioning with text wrap">
    .ve-media wc:The_Bug_Peek.jpg right

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.
</ve-snippet>

### sticky

The `sticky` attribute may be used alone or in combination with `full`, `left`, or `right` positioning.  Sticky positioning causes the viewer to pause scrolling at the top of the page while other text in the same section scrolls through the viewport.  This behavior can be useful when long portions of text are referencing the viewer content and keeping the viewer visible while the text is scrolled is desired.  When combined with the `left` or `right` positioning attribute this has the effect of creating a 2-column layout for the containing section.

To see this behavior, select the `Rendered` tab in the snippet viewer below and scroll the text in the preview window.  Notice how the .ve-media viewer with the image "sticks" to the top of the preview window until all of the text in the same section (`Section 1`) has entered the visible portion of the window.  

<ve-snippet collapsible label="Right positioning with sticky viewer" height="500px">

    ### Section 1
    .ve-media wc:The_Bug_Peek.jpg right sticky

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.

    ### Section 2

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.

</ve-snippet>

In this next example the `sticky` attribute is used with a full-width viewer.  In this mode the text scrolls behind the viewer until all text in the containing section has been seen.

<ve-snippet collapsible label="Full width with sticky viewer" height="800px">
    .ve-media wc:The_Bug_Peek.jpg sticky

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.

    Felis eget nunc lobortis mattis aliquam faucibus purus. Massa enim nec dui nunc mattis. Lacus sed viverra tellus in hac habitasse platea dictumst. Tellus integer feugiat scelerisque varius. Accumsan tortor posuere ac ut. Lacus laoreet non curabitur gravida arcu. Gravida cum sociis natoque penatibus et magnis dis parturient montes. Eget sit amet tellus cras. Diam sollicitudin tempor id eu nisl nunc. Aliquet enim tortor at auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla. Dignissim convallis aenean et tortor at risus viverra. Sagittis aliquam malesuada bibendum arcu vitae elementum. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Tristique senectus et netus et malesuada fames ac turpis. Purus non enim praesent elementum facilisis. In fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Turpis tincidunt id aliquet risus feugiat in ante. Nulla aliquet porttitor lacus luctus accumsan. Velit laoreet id donec ultrices tincidunt arcu non.
</ve-snippet>

In the example above you may have noticed that the viewer did not actually take the full width of the available window.  When the `sticky` attribute is used with a viewer in full-width mode, Juncture scales the width and height of the viewer to ensure that a scrollable portion of the viewport remains after the viewer has been rendered.  If this was not the case it would be impossible to scroll the content through the viewport.  This behavior can be overridden by explicitly setting the width to 100% but is not recommended.

## Explicitly setting a viewer height and/or width

In most cases using the `left` or `right` positioning attributes (with or without the `sticky` attribute) is sufficient to achieve the desired layout.  In situations where more control is needed the width and/or height may set to a specified value.  The value may be stated as an absolute size (in pixels) or as a percentage.  

<ve-snippet collapsible label="Viewer width as percentage of essay width">
    .ve-media wc:The_Bug_Peek.jpg width=60%
</ve-snippet>

<ve-snippet collapsible label="Viewer width set as pixel value">
    .ve-media wc:The_Bug_Peek.jpg width=300px
</ve-snippet>

When setting a width **or** a height for a viewer the other dimension is automatically calculated.  For items that have a natural aspect ration (images and videos) the ratio is preserved.  When setting both a width **and** a height for an image or videp the viewer aspect ratio will unlikely match that of the source item.  In those cases the default behavior for the viewer is to display the entire item and use left-right or top-bottom letter boxing.

<ve-snippet collapsible label="Both width and height set, shows automatic letter boxing">
    .ve-media wc:The_Bug_Peek.jpg height=400px width=50%
</ve-snippet>

Depending on your browser width, the example above will probably include top-bottom letter boxing to display the entire image.  This default behavior can be overridden with the `fit` attribute.  Setting `fit=cover` will result in the item to fill the viewer window.  

<ve-snippet collapsible label="Both width and height set, fit=cover used for viewer fill">
    .ve-media wc:The_Bug_Peek.jpg height=400px width=50% fit=cover
</ve-snippet>
