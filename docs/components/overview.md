# Juncture Tagging Overview

Juncture tags provide an extension to Markdown for defining visualizations or to otherwise instruct Juncture in the rendering of a generated web page.  Juncture must be added at the start of a line and include a `.ve-` prefix.  Commonly used tags include the `.ve-media` tag for creating image and video viewers and the `.ve-map` tag for adding an interactive map.

## Viewer Tags

- [.ve-media](/components/media) - The `.ve-media` tag creates a viewer that is able to display IIIF images, video, and audio. The viewer can also be used to display streamed videos from YouTube and Vimeo.
- [.ve-map](/components/map) - The `.ve-map` tag is used to insert an interactive map into the essay.  A map can optionally include one ore more overlays consisting of markers, GeoJSON feature sets, and georeferenced images (for historic maps).
- [.ve-header](/components/header) - The `.ve-header` is used to define an optional header that appears at the start of the essay. The header can be used to define a title and subtitle for the essay, display a banner image, and create a navigation menu.
- [.ve-footer](/components/footer) - The `.ve-footer` tag is used to override the default footer that Juncture automatically adds to a rendered essay.
- [.ve-iframe](/components/iframe) - The `.ve-iframe` allows arbitrary web pages to be embedded in an essay.
- [.ve-mermaid](/components/mermaid) - The `.ve-mermaid` tag uses the [Mermaid.js](https://mermaid.js.org/) JavaScript library to create diagram visualizations.
- [.ve-plant-specimen](/components/plant-specimen) - The `.ve-plant-specimen` tag is used to display one or more plant specimens obtained from [JSTOR Global Plants](https://plants.jstor.org/).

## Other Tags

- [.ve-annotate](/components/annotate) - The `.ve-annotate` tag adds the [Hypothes.is](https://web.hypothes.is/) annotation client to an essay. 
- [.ve-meta](/components/metadata) - The `.ve-meta` tag is used to define metadata attributes for the page. 