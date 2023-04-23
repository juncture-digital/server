# ve-map

<style> 
    .markdown-section h3 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
    .markdown-section table { 
        margin-left:3rem; 
        width: calc(100% - 6rem); 
        border:1px solid #555;
    }
    @media (max-width: 480px) {
        .markdown-section table { 
            margin-left: 0;
            width: 100%;
        }
    }

    .markdown-section td, .markdown-section th {
        border:1px solid #555;
        padding: 8px;
        line-height: 1.2;
        line-height: 1.4;
        color: #444;

        /* These are technically the same, but use both */
        overflow-wrap: break-word;
        word-wrap: break-word;

        -ms-word-break: break-all;
        /* This is the dangerous one in WebKit, as it breaks things wherever */
        word-break: break-all;
        /* Instead use this non-standard one: */
        word-break: break-word;

        /* Adds a hyphen where the word breaks, if supported (No Blink) */
        -ms-hyphens: auto;
        -moz-hyphens: auto;
        -webkit-hyphens: auto;
        hyphens: auto;
    }
    .markdown-section th {
        background-color:#E2F0F7;
        font-weight:bold !important;
        text-align:center !important;
    }
</style>

The `.ve-map` tag creates a map viewer that displays a base map with optional map layers.  The map viewer supports zooming and panning.  The base map defaults to [OpenStreetMap](https://www.openstreetmap.org/) but can easily be set to a number of [others](#baselayers).  

The base map can be augmented with one or more optional map layers. Juncture supports 3 types of layers:

- **Location layer** - A location layer contains all of the individual locations defined for a map.  Locations are defined in a list following the _.ve-map_ tag.  Locations may defined with explicit geographic coordinates, a Wikidata entity ID that corresponds to a location, or an IIIF image that contains geographic coordinates in the manifest metadata.  An IIIF manifest created by Juncture will include geographic coordinates if they are found in the [Exif](https://en.wikipedia.org/wiki/Exif) metadata embedded in the source image.  Locations are displayed as map pins.  If the location is specified using a Wikidata ID and the Wikidata entity associated with the location links to a GeoJSON resource the corresponding shape may be displayed instead of the pin by including the `prefer-geojson` attribute in the list item.  By default, all locations are aggregated into a single layer.  the `layer` attribute may be used to organize locations into separate layers.
- **GeoJSON layer** - [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) is an open standard format designed for representing simple geographical features, along with their non-spatial attributes. It is based on the JSON format.  A GeoJSON layer is added by including a URL to a GeoJSON file in the list following the _.ve-map_ tag.
- **Georeferenced image** - A georeferenced image may also be used as a map layer.  [Georeferencing](https://en.wikipedia.org/wiki/Georeferencing) is a type of coordinate transformation that binds a digital image that represents a geographic space (often a scanned map or aerial photograph) to a spatial reference system, thus locating the digital data in the real world.  One common use of a georeferenced image layer is to create an historic map overlay. Juncture supports the use of georeferenced IIIF images created by [allmaps](https://allmaps.org/).  Adding an allmaps georeferenced image to a Juncture map is accomplished by including the text `allmaps=<ALLMAPS ID>` in a list item following the _.ve-map_ tag.

## Attributes

### Core attributes 

**[basemaps](/components/basemaps)** (_string_):  The name of an optional base map to be used.  A list of supported base maps can be seen [here](/components/basemaps)

**[caption](#basic-map-examples)** (_string_):  A caption to use in the viewer caption bar.

**[center](#basic-map-examples)** (_string_):  Defines the initial center of the rendered map.  This can be defined using latitude and longitude coordinates or with a Wikidata QID.

**[marker](#basic-map-examples)** (_boolean_):  If true a Marker will be added to the map center point.

**[popup-on-hover](#basic-map-examples)** (_boolean_):  Show location popup when hovering over the location (marker pin or GeoJSON shape).  The default behavior is to show the popup when clicking on the location.

**[prefer-geojson](#basic-map-examples)** (_boolean_):  Display a GeoJSON shape rather than a pin marker when available.

**[scroll-wheel-zoom](#basic-map-examples)** (_boolean_):  Enable map zoom behavior when scrolling over a map.  This is disabled be default.

**[zoom](#basic-map-examples)** (_number_):  Defines the initial zoom level of the rendered map.

**[zoom-on-click](#basic-map-examples)** (_boolean_):  Increase zoom level on a location after clicking on a location marker pin or shape. 

### Viewer positioning attributes

**[left](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the left half of the viewport and scale the width proportionally.  Text will wrap around the viewer unless the _sticky_ attribute is included.

**[right](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the right half of the viewport and scale the width proportionally. Text will wrap around the viewer unless the _sticky_ attribute is included.

**[full](/styling/viewer-positioning)** (_boolean_):  Use the fill width of the browser viewport for the image.  Scale the image height proportional to the source image.  By default, the image will be auto-sized such that its height is not more than 40% of the viewport height.

**[sticky](/styling/viewer-positioning)** (_boolean_):  The _sticky_ attribute causes the viewer to "stick" to the top of the viewing area when the essay text is scrolled.  The viewer will stick in position until all content in the enclosing section has scrolled through the viewing area.

**[height](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer height.  The default behavior is to use the full width of the available window and scale the viewer height to retain the aspect ratio of the source item (image or video).

**[width](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer width.  The default behavior is to use the full width of the available window.

### Layer attributes

**[allmaps](#layer-examples)** (_string_):  Allmaps ID of a georeferenced image.

**[coords](#layer-examples)** (_string_):  Location coordinates.

**[description](#layer-examples)** (_string_):  Location description used in a popup.

**[disabled](#layer-examples)** (_boolean_):  Location is not displayed initially.  This attribute must be used in conjunction with the `layer` attribute.

**[geojson](#layer-examples)** (_string_):  URL to a GeoJSON file.

**[iiif](#layer-examples)** (_string_):  IIIF manifest URL containing geographic coordinates.

**[image](#layer-examples)** (_string_):  Location image used in a popup thumbnail.

**[label](#layer-examples)** (_string_):  Location label used in a popup.

**[layer](#layer-examples)** (_string_):  Layer name to associate with the location.  Multiple locations can use the same layer name.  When a layer name is specified the layer may be hidden when the map is initially rendered by including the `disabled` attribute on one of the layer locations.

**[marker-type](#layer-examples)** (_string_):  Type of marker to render.  Recognized values are 'circle'.

**[prefer-geojson](#layer-examples)** (_boolean_):  When using a Wikidata ID to define a location a GeoJSON shape may be used rather than a pin marker when available.

**[qid](#layer-examples)** (_string_):  Wikidata entity ID of a location.

**[zoom](#layer-examples)** (_number_):  Location zoom level when `zoom-on-click` behavior is enabled.

### Geojson styling attributes

**[color](#geojson-examples)** (_string_): Line color

**[weight](#geojson-examples)** (_number_): Line weight

**[opacity](#geojson-examples)** (_number_): Line opacity level (0-1)

**[fillColor](#geojson-examples)** (_string_):  Fill color

**[fillOpacity](#geojson-examples)** (_number_): Opacity level (0-1) of the fill color.

## Layers

Map layers are defined in a Markdown list following the `.ve-map` tag.  Items in the layer list may define markers, GeoJSON file URLs or [allmaps](https://allmaps.org/) IDs for georeferenced images. Note that a blank space must be present between the `-` in the Markdown list and the layer item. Please view the examples at the bottom of the page for clarification if needed. 

### Marker layer

A single marker layer is created by aggregating all of the ve-map list items that are not GeoJSON URLs or allmaps references.  A marker can be defined in 3 ways,

- With explicit geographic (latitude and longitude) coordinates.  An optional label may also be specified for the marker.
- With a Wikidata ID that corresponds to an entity associated with a location.
- With an IIIF image that includes geographic coordinates in the manifest metadata

### GeoJSON layer

A GeoJSON layer is defined by including a URL to a GeoJSON file in a .ve-map layer list item.  The URL to the GeoJSON file can be defined in 3 ways:
- **An absolute URL** - This would be a URL to any web-accessible GeoJSON file, such as https://data.whosonfirst.org/147/772/818/1/1477728181.geojson
- **A URL relative to the essay** - This is a relative URL path from the referencing essay file.  For example, if the file `my-overlay.geojson` was located in the same Github folder as the essay file the URL would simply be `my-overlay.geojson`.
- **A Github path** - In this notation the relative URL consists of the Github account, repository, and path to the GeoJSON file.  For instance, `/juncture-digital/juncture/examples/geojson/demo-map.geojson`

### Georeferenced Image layer

A Georeferenced image layer is defined by including an allmaps ID in a .ve-map layer list item. 

##

## Examples

### Basic map examples

<ve-snippet collapsible label="Basic map with default center and zoom">
    .ve-map width=50%
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using lat/lng coordinates">
    .ve-map 42.281,-83.748 9 width=50%
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using the Wikidata QID for New York City">
    .ve-map Q60 8 width=50%
</ve-snippet>

<ve-snippet collapsible label="Map center defined using a Wikidata QID with marker attribute">
    .ve-map Q60 8 marker width=50%
</ve-snippet>

### Layer examples

<ve-snippet collapsible label="Location defined with coordinates">
    .ve-map 42.281,-83.748 9 width=50%
        - 42.281,-83.748
</ve-snippet>

<ve-snippet collapsible label="Location defined with coordinates and label">
    .ve-map 42.281,-83.748 10 width=50%
        - 42.281,-83.748 "Ann Arbor, Michigan"
</ve-snippet>

<ve-snippet collapsible label="Location defined with coordinates, label, and description">
    .ve-map 42.281,-83.748 9 width=50%
        - 42.281,-83.748 "Ann Arbor, Michigan" "Ann Arbor is a city in the U.S. state of Michigan and the county seat of Washtenaw County."
</ve-snippet>

<ve-snippet collapsible label="Location defined with coordinates, label, description, and image">
    .ve-map 42.281,-83.748 9 width=50%
        - 42.281,-83.748 "Ann Arbor, Michigan" "Ann Arbor is a city in the U.S. state of Michigan and the county seat of Washtenaw County." wc:Ann_Arbor_sunset_2018.jpg
</ve-snippet>

<ve-snippet collapsible label="Location defined with Wikidata ID">
    .ve-map 42.281,-83.748 10 width=50%
        - Q485172
</ve-snippet>

<ve-snippet collapsible label="Map with multiple basemaps">
    .ve-map 37.16032,-79.45313 5 width=50% basemaps=OpenStreetMap,Esri_WorldPhysical,Stamen_Watercolor
</ve-snippet>

This example includes a terrain basemap with multiple markers for cities and national parks.  Each location is defined using a Wikidata ID.

<ve-snippet collapsible label="Terrain basemap with multiple locations">
    .ve-map 37.84,-108.92 6 basemaps=Esri_WorldPhysical width=50%
        - Q16554
        - Q49258
        - Q23337
        - Q79842
        - Q777183
        - Q220289
        - Q205325
        - Q219562
        - Q223969
</ve-snippet>

This builds on the previous example by organizing the location markers into two layers, a "Cities" layer and a "National Parks" layer.  The layers may be toggled on and off using the layer control located at the top-right of the map.

<ve-snippet collapsible label="Multiple locations organized into layers">
    .ve-map 37.84,-108.92 6 basemaps=Esri_WorldPhysical width=50%
        - Q16554 layer=Cities
        - Q49258 layer=Cities
        - Q23337 layer=Cities
        - Q79842 layer=Cities
        - Q777183 layer="National Parks"
        - Q220289 layer="National Parks"
        - Q205325 layer="National Parks"
        - Q219562 layer="National Parks"
        - Q223969 layer="National Parks"
</ve-snippet>

<ve-snippet collapsible label="IIIF image as marker">
    .ve-map Q223969 5 right
        - wc:Double-O-Arch_Arches_National_Park_2.jpg

    This example uses [an image from Wikimedia commons](https://commons.wikimedia.org/wiki/File:Double-O-Arch_Arches_National_Park_2.jpg) for a marker.  The image used in this example includes embedded Exif (Exchangeable image file format) data with geographic coordinates.

    Hover over the marker or click here to see the image.

    ==The marker image will also appear when hovering over this text.  Clicking on this text will also cause the map to zoom in on the marker location.=={flyto=wc:Double-O-Arch_Arches_National_Park_2.jpg,14}
</ve-snippet>

<ve-snippet collapsible label="Map with a GeoJSON overlay">
    .ve-map 44.50434,-85.39673 7
        - geojson=https://raw.githubusercontent.com/glynnbird/usstatesgeojson/master/michigan.geojson layer="State of Michigan"
</ve-snippet>

<ve-snippet collapsible label="Map with a historic map overlay" disable-drag>
    .ve-map 51.39257,0.50752 14 width=50%
        - allmaps=911e307b5cecc423
</ve-snippet>

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

### Geojson examples

<ve-snippet collapsible label="Custom GeoJSON fill color">
    .ve-map 44.50434,-85.39673 7
        - geojson=https://raw.githubusercontent.com/glynnbird/usstatesgeojson/master/michigan.geojson layer="State of Michigan" fillColor=red
</ve-snippet>

<ve-snippet collapsible label="Custom GeoJSON with outline only">
    .ve-map 44.50434,-85.39673 7
        - geojson=https://raw.githubusercontent.com/glynnbird/usstatesgeojson/master/michigan.geojson layer="State of Michigan" color=blue weight=3 fillOpacity=0
</ve-snippet>
