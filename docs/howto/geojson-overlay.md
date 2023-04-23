# How To Use a GeoJSON Map Overlay

This tutorial will walk through how to create a GeoJSON file to include in your Juncture essay. For more background information on what GeoJSON is, visit [this page](https://juncture-digital.org/resources/geojson) in the documentation.

## Creating a GeoJSON File
[geojson.io](https://geojson.io) is a free, open source tool for creating and viewing GeoJSON files. Using [this](https://geojson.io) page, create the desired overlay for your map. You can also edit the JSON directly in the panel on the right, as well as customize properties for your visualization, such as color and fill size, using the pop up interface in geojson.io.

<ve-media src="gh:juncture-digital/media/videos/geojson1.gif" no-caption no-info-icon width="60%"></ve-media>

<ve-media src="gh:juncture-digital/media/videos/geojson2.gif" no-caption no-info-icon width="60%"></ve-media>

Once you have added and edited your data, download the JSON file by navigating to the `Save` tab in the top right and clicking `GeoJSON`.

<ve-media src="gh:juncture-digital/media/videos/geojson_save.gif" no-caption no-info-icon width="60%"></ve-media>

## Implementing GeoJSON into Juncture
To add your GeoJSON file to a map in Juncture, add the following code as a list item under the `.ve-map` tag, replacing `URL` for the URL to your GeoJSON file:
``` markdown
    - geojson=URL layer="Label for Layer"
```

Here is an example of the GeoJSON file that was created in the videos above. The file below is saved in Github, but the geojson attribute will accept the URL to any valid JSON file, and there are pre-existing open access GeoJSON files available elsewhere.

<ve-snippet label="Map with a GeoJSON overlay" prefix="juncture-digital/juncture" path="examples/geojson">
    .ve-map 39.7392,-104.9903 5
        - demo_map.geojson layer="Demo GeoJSON Overlay"
</ve-snippet>
