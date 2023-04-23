<style> 
    .markdown-section h3 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
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

# The Juncture Actions Framework

## Overview

The Juncture actions framework provides a way to trigger actions in a viewer component from essay text.  A text-to-viewer interaction is created by marking the text to use as a trigger and adding a specific attribute that is recognized by the target viewer component.  The interaction is typically triggered by clicking the marked text, but some interactions may also be triggered by hovering over marked text, or by scrolling a marked paragraph into the active portion of the browser window.

The example below demonstrates a simple `zoomto` action which is commonly used with the media viewer.  In this example, the text "leaf beetle" is marked and associated with an image region.  This action is triggered when a user clicks on the marked text (`leaf beetle`).  When the action is triggered the viewer will zoom in on the specified region. 

<ve-snippet>
    .ve-media wc:The_Bug_Peek.jpg right
    In the image at the right, zoom in on the region containing the ==leaf beetle=={zoomto=1005,507,1676,1117}
</ve-snippet>

The `flyto` action performed by the map viewer works similarly.  Instead of specifying an image region, in the map viewer `flyto` action a location and zoom level are provided.  For example,

<ve-snippet>
    .ve-map right
        - 25.783,-80.217 Miami
    In the map at the right, "fly to" ==Miami=={flyto=25.783,-80.217,10}
</ve-snippet>

## Viewer actions

| Viewer | Key | Value | Behavior |
| ------ | --- | ----- | -------- |
| Media  | `zoomto` | Image region bounding box | Zooms the image to the specified image region |
| Media  | `anno` | Annotation ID | Opens an annotation text box |
| Media  | `zoomto` | Image region bounding box **and** Annotation ID | Zooms the image to the specified image region **and** opens an annotation text box |
| Media  | `play` | Time to start (and optionally stop) an audio or video | Plays an audio or video clip from the specified time |
| Map  | `flyto` | Geographic coordinates and optional zoom level | Centers a map at the specified coordinates and sets zoom level |
| Map  | `flyto` | Wikidata QID | Centers a map at the coordinates associated with the entity identified by the provided QID |

## Marking text

### Marking a word or phrase

The essay text to be used as an action trigger is wrapped with double equal signs `==`.  The action to be performed is then defined in an attribute that is connected to the wrapped text.  The actions may be defined using either key-value notation or as a single value.  The keys and values used are specific to each viewer. 

### Marking an entire paragraph

Using paragraph position as an action trigger is typically used in combination with a viewer that has been set to `sticky`.  When a viewer is set to `sticky` and positioned with a `left` or `right` attribute a 2-column layout is created for the parent section.  In this 2-column layout, the viewer will stick to the top of the viewer window and the paragraphs will scroll in the other column.  As each paragraph enters the active portion of the window the associated action is triggered.  The "active" portion of the screen is defined as a section near the top of the screen such the majority of a paragraph is visible.

A paragraph is "marked" by appending an attributes block to the paragraph.  The attributes block can include `enter` and `exit` attributes to trigger actions when the paragraph enters or leaves the active area of the screen.

In the example below a map and 3 paragraphs are defined.  Each of the paragraphs corresponds to a location - New York, Paris, and London.  As each of these paragraphs is scrolled into the "active" portion of the browser window a `flyto` action is triggered to reposition the map to the associated location.  In this example, the `show-active` class is added to the section containing the sticky map and text paragraphs.  The `show-active` class adds a gray border to the left side of the active paragraph as a visual indicator.  The example also uses Wikidata QIDs for the `flyto` actions.  Lat/Lng coordinates could have also been used.

<ve-snippet collapsible label="Using paragraph position as an action trigger" height="600px">
    # {.show-active}
    
    .ve-map Q60 8 sticky right
        - Q60
        - Q90
        - Q84

    **New York**, often called New York City or NYC, is the most populous city in the United States. With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2), New York City is also the most densely populated major city in the United States and is more than twice as populous as second-place Los Angeles. New York City lies at the southern tip of New York State and constitutes the geographical and demographic center of both the Northeast megalopolis and the New York metropolitan area, the largest metropolitan area in the United States both by population and by urban landmass. 
    {enter=flyto:Q60}

    **Paris** is the capital and most populous city of France, with an estimated population of 2,165,423 residents in 2019 in an area of more than 105 km² (41 sq mi), making it the 30th most densely populated city in the world in 2020. Since the 17th century, Paris has been one of the world's major centres of finance, diplomacy, commerce, fashion, gastronomy, and science. For its leading role in the arts and sciences, as well as its very early system of street lighting, in the 19th century it became known as "the City of Light". Like London, prior to the Second World War, it was also sometimes called the capital of the world.
    {enter=flyto:Q90}

    **London** is the capital and largest city of England and the United Kingdom, with a population of just under 9 million. It stands on the River Thames in southeast England at the head of a 50-mile (80 km) estuary down to the North Sea, and has been a major settlement for two millennia. The City of London, its ancient core and financial centre, was founded by the Romans as Londinium and retains its medieval boundaries.[note 1] The City of Westminster, to the west of the City of London, has for centuries hosted the national government and parliament. Since the 19th century, the name "London" has also referred to the metropolis around this core, historically split between the counties of Middlesex, Essex, Surrey, Kent, and Hertfordshire, which since 1965 has largely comprised Greater London, which is governed by 33 local authorities and the Greater London Authority.
    {enter=flyto:Q84}

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

</ve-snippet>

### Getting action values

This section describes techniques for obtaining action values.  In many cases, the values can be obtained from the respective viewer when in editor preview mode.

  When using the Juncture editor to develop an essay, action values for the image `zoomto` and map `flyto` actions can be easily obtained from the respective component while in editor preview mode.   

### Adding action values to marked text

The `Mark text` icon in the editor formatting toolbar is also convenient for marking text and inserting action values.  When using this approach, first add the coordinates to the clipboard as described above.  Exit preview mode and then select the text to be marked by dragging your cursor over the text in the editor window.  After the text has been selected, press the `Mark text` icon in the formatting toolbar.  This will result in the text being marked with the desired coordinates.

#### Image region

An image region can be expressed in absolute pixel values or as a percent of the full image size.  The table below describes the format of the value in each approach.

| Approach | Format | Description |
| -------- | ------ | ----------- |
| Absolute pixels | x,y,w,h     | The region of the full image to be returned is specified in terms of absolute pixel values. The value of x represents the number of pixels from the 0 position on the horizontal axis. The value of y represents the number of pixels from the 0 position on the vertical axis. Thus the x,y position 0,0 is the upper left-most pixel of the image. w represents the width of the region and h represents the height of the region in pixels. |
| Pct of full image | pct:x,y,w,h | The region to be returned is specified as a sequence of percentages of the full image’s dimensions, as reported in the image information document. Thus, x represents the number of pixels from the 0 position on the horizontal axis, calculated as a percentage of the reported width. w represents the width of the region, also calculated as a percentage of the reported width. The same applies to y and h respectively. These may be floating point numbers. |

Percentage values can often be determined with an initial approximation and a little iterative fine-tuning using the viewer.  However, in most cases, it is probably quickest and easiest to use pixel values that can be copied from the viewer.  This is accomplished by using the media viewer controls to position the image to reflect its desired appearance following the `zoomto` action.  Once the image is in the desired position, hover your cursor over the bottom-right corner of the media viewer.  When hovering over the bottom-right corner, the region coordinates will become visible.  Clicking on them will copy the values onto the clipboard.  Once that is done they can then be pasted directly into the essay text (after toggling out of preview mode).  The value can also be added to text using the `Mark text` helper in the editor formatting toolbar.

The example below shows the use of a `zoomto` action using both percent and absolute pixel values.  In both cases, the same image region should be displayed following the action.

<ve-snippet>
    .ve-media wc:The_Bug_Peek.jpg right
    
    - ==Full image=={pct:0,0,100,100}
    - ==Zoomto using image percent=={pct:17,16,30,30}
    - ==Zoomto using absolute pixels=={923,580,1630,1085}
</ve-snippet>

#### Image annotation ID

After an image has been annotated (as described in [this tutorial](tutorials/annotating-images)) the annotation ID can be obtained by clicking on the annotation.  When clicking on the annotation the annotation ID is copied onto the clipboard.  Once that has been accomplished the value can then be pasted into the essay text directly or by using the `Mark text` helper located in the editor formatting toolbar. 

#### Map coordinates

#### Map location ID

## Examples

### Media viewer actions

#### Zoom to image region

<ve-snippet collapsible label="Zoom to image region (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right
The image depicts a ==leaf beetle=={zoomto=1005,507,1676,1117} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Zoom to image region (using value only)">
.ve-media wc:The_Bug_Peek.jpg right
The image depicts a ==leaf beetle=={1005,507,1676,1117} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

#### Show annotation

<ve-snippet collapsible label="Show annotation (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={anno=386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Show annotation (using value only)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

#### Zoom to image region and show an annotation

<ve-snippet collapsible label="Zoom to image region and show annotation (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={zoomto=167,1,3352,2233,386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Zoom to image region and show annotation (using value only)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={167,1,3352,2233,386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

#### Play at time

<ve-snippet collapsible label="Play at a time (using key-value notation)">
.ve-media https://www.youtube.com/watch?v=Zy3K2Lcw7hQ right
Start playing video at ==time=={play=10}
</ve-snippet>

<ve-snippet collapsible label="Play at a time (using value only)">
.ve-media https://www.youtube.com/watch?v=Zy3K2Lcw7hQ right
Start playing video at ==time=={10}
</ve-snippet>

### Map viewer actions

<ve-snippet collapsible label="Fly to a location using lat/lng coordinates">
.ve-map Q60 8 right
    - 48.857,2.352 Paris
Fly to ==Paris=={flyto:48.857,2.352}
</ve-snippet>

<ve-snippet collapsible label="Fly to a location using Wikidata ID">
.ve-map Q60 8 right
    - Q90
Fly to ==Paris=={flyto:Q90}
</ve-snippet>

<ve-snippet collapsible label="Fly to a location with specified zoom level">
.ve-map Q60 8 right
    - Q60
    - Q90
Fly to ==Paris=={flyto:Q90,7}
</ve-snippet>