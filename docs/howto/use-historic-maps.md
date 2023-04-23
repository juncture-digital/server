# Historic Map Overlays

This guide will walk through using the [AllMaps](https://allmaps.org/) editor on a historic map to overlay your map in a Juncture essay.

## Creating an AllMaps ID
In order for your image to be placed in the right location on a map, there must be georeference points that indicate where the image should be overlayed. This can be done using the [AllMaps Editor](https://editor.allmaps.org/#/). To use this, you need a IIIF Manifest URL. Enter it into the input box and once it is loaded in AllMaps, navigate to the 'Georeference' tab. 

<ve-media src="gh:juncture-digital/media/videos/Using_AllMapsEditor.gif" no-caption no-info-icon width="60%"></ve-media>

Once in the 'Georeference' tab, zoom into the map on the right to the place where you would like the image overlay. Note that clicking on the map will place a marker but you can delete any accidental or unwanted markers from the list icon at the bottom of the map. Once the map is in position, add pins to the image and it's corresponding place on the map, as shown below.
<ve-media src="gh:juncture-digital/media/videos/Using_AllMaps1.gif" no-caption no-info-icon width="60%"></ve-media>
<ve-media src="gh:juncture-digital/media/videos/Using_AllMaps2.gif" no-caption no-info-icon width="60%"></ve-media>

After the reference points have been added, you will need the AllMaps ID to include in the markdown for your Juncture essay. To locate the AllMaps ID, navigate to the 'Results' tab at the top of the AllMaps Editor. On that page you will find the template URL to your map that will look something like `https://allmaps.xyz/maps/911e307b5cecc423/{z}/{x}/{y}.png`. Copy the ID that follows `/maps/` in the URL. In this case, the AllMaps ID is `911e307b5cecc423`.
<ve-media src="gh:juncture-digital/media/videos/Finding_AllMapsID.gif" no-caption no-info-icon width="60%"></ve-media>

## Adding the Historic Overlay to Your Map
To add the image overlay to your map, list the AllMaps ID under the `.ve-map` tag using the syntax `- allmaps=XXX` as shown below in the code example. Note that the list must be indented once to the right.

<ve-snippet label="Map with AllMaps Overlay and WikiData QID" disable-drag>
  .ve-map Q507517 15
      - allmaps=911e307b5cecc423 layer="Dickensland Map"
</ve-snippet>
