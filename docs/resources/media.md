<style>
    .markdown-section h2 span,
    .markdown-section h3 span {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .markdown-section h2 span img,
    .markdown-section h3 span img {
        height: 40px;
    }

</style>

# Media Providers

This page collects information for finding media resources for use in Juncture essays.  These are typically images but some sites, such as Wikimedia Commons, also provide audio and video content that can be dynamically wrapped in an IIIF manifest for easy use in a Juncture essay.  In most cases an image or media file found on a site listed below can be added to a Juncture essay by dragging the image from the hosting site into the Juncture essay editor.  When using the drag-and-drop or copy-paste method of adding a IIIF resource to a Juncture essay the corresponding `.ve-media` or `.ve-header` tag with the correct IIIF URL is automatically created.

## Sites providing IIIF resources

The [IIIF website](https://iiif.io/) provides a helpful guide for [finding IIIF resources](https://iiif.io/guides/finding_resources/).  The guide list more than 50 sites that provide IIIF resources.

## Media sharing sites

In addition to using IIIF resources exposed by the sites mentioned above, Juncture is able to dynamically create IIIF images from a number of image hosting sites that do not currently provide IIIF versions of hosted content.  In most cases these sites do provide a public API that can be used to obtain metadata that can be used to construct an IIIF manifest. 

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/80px-Commons-logo.svg.png) Wikimedia Commons

 [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) is an online repository of free-to-use images, audio, and video files.  Much of the content hosted by Wikimedia Commons is either public domain or available with an open Creative Commons license providing flexible reuse.  Wikimedia Commons provides a IIIF image server which is used to render the IIIF images.  Juncture uses the Wikimedia Commons API to obtain metadata for dynamically constructing the IIIF presentation manifest.

Wikimedia Commons IIIF URLs are formed by combining the `wc:` prefix with the Wikimedia Commons file name.  For example, the image found at [https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg](https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg) has the file name "Holy_SURP_Hovhannes_Church.jpg" (note that spaces in the file name are converted to underscores).  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/wc:Holy_SURP_Hovhannes_Church.jpg/manifest.json](https://iiif.juncture-digital.org/wc:Holy_SURP_Hovhannes_Church.jpg/manifest.json).  A short-form version of the URL with just the prefix and file name can be used in a Juncture essay, for instance - `wc:Holy_SURP_Hovhannes_Church.jpg`.

<ve-snippet collapsible label="Wikimedia Commons - Image example">
    .ve-media wc:Holy_SURP_Hovhannes_Church.jpg right

    [Holy SURP Hovhannes Church](https://commons.wikimedia.org/wiki/File:Holy_SURP_Hovhannes_Church.jpg)

    Saint John Church of Sohrol, a 5th or 6th century Armenian Catholic church in Sohrol, Iran, rebuilt by Samson Makintsev (Sam Khan) in 1840

    [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) [Picture of the Year](https://commons.wikimedia.org/wiki/Commons:Picture_of_the_Year) for 2021
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - Audio example">
    .ve-media wc:Interview_with_Warren_Hanson_regarding_Hundred_Flowers.ogg right

    [Interview with Warren Hanson regarding Hundred Flowers](https://commons.wikimedia.org/wiki/File:Interview_with_Warren_Hanson_regarding_Hundred_Flowers.ogg)

    This is an oral history interview with Warren Hanson conducted as part of a West Bank oral history project. He recalls the challenges of getting the Hundred Flowers underground newspaper printed in 1969 at a time when small town newspaper presses in Minnesota were unwilling to print the anti-war, civil rights, counter-culture publication, forcing the paper to be printed in Milwaukee, until one civil libertarian owned press in Minnesota finally volunteered their services in the spirit of free speech.
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - Video example">
    .ve-media wc:Aerial_views_of_Shoalhaven_Heads,_NSW,_Australia_in_June_2016.webm right autoplay

    [Aerial views of Shoalhaven Heads, NSW, Australia in June 2016](https://commons.wikimedia.org/wiki/File:Aerial_views_of_Shoalhaven_Heads,_NSW,_Australia_in_June_2016.webm)
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons - GIF example">
    .ve-media wc:DART-impact-SAAO-Lesedi-Mookodi.gif right

    [DART impact SAAO-Lesedi-Mookodi](https://commons.wikimedia.org/wiki/Template:Motd/2022-12#/media/File:DART-impact-SAAO-Lesedi-Mookodi.gif)

    The impact of Double Asteroid Redirection Test (DART) spacecraft's intentional collision with asteroid Dimorphos and its corresponding plumule as seen by using the Mookodi instrument on the SAAO's 1-m Lesedi telescope. NASA's first flight mission for planetary defense, DART seeks to test and validate a method to protect Earth in case of an asteroid impact threat.
</ve-snippet>

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Flickr.svg/256px-Flickr.svg.png) Flickr

[Flickr](https://www.flickr.com/) is an image and video hosting service, as well as an online community, founded in Canada and headquartered in the United States. It was created by Ludicorp in 2004 and was a popular way for amateur and professional photographers to host high-resolution photos. It has changed ownership several times and has been owned by SmugMug since April 20, 2018.

Flickr IIIF URLs are formed by combining the `flickr:` prefix with the Flickr image ID.  For example, the image found at [https://www.flickr.com/photos/mgaylard/52736840054/](https://www.flickr.com/photos/mgaylard/52736840054/) has the image ID "52736840054".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/flickr:52736840054/manifest.json](https://iiif.juncture-digital.org/flickr:52736840054/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `flickr:52736840054`  

<ve-snippet collapsible label="Flickr image">
    .ve-media flickr:52736840054 right

    [Yarmouth Ferry Terminal](https://www.flickr.com/photos/mgaylard/52736840054/)
</ve-snippet>

### ![](https://about.jstor.org/wp-content/themes/aboutjstor2017/static/JSTOR_Logo2017_90.png) JSTOR

[JSTOR](https://jstor.org) is a digital library of academic journals, books, and primary sources. JSTOR hosts both restricted access and open content. Open access images on JSTOR can be queried using this [open content search expression](https://www.jstor.org/action/doBasicSearch?Query=cc_reuse_license%3A%22public+domain%22+OR+cc_reuse_license%3A%22Creative+Commons%22+-cc_reuse_license%3A%28NonCommercial+OR+NoDerivs%29&efqs=eyJjdHkiOlsiWTI5dWRISnBZblYwWldSZmFXMWhaMlZ6Il0sImRpc2MiOltdfQ%3D%3D&searchkey=1677864936160&pagemark=eyJwYWdlIjoyLCJzdGFydHMiOnsiSlNUT1JCYXNpYyI6MjV9fQ%253D%253D).  A more targeted search can then be performed using the Search Bar in the navigation menu on the left side of the page.

JSTOR IIIF URLs are formed by combining the `jstor:` prefix with the JSTOR content ID.  For example, the image found at [https://www.jstor.org/stable/community.18615405](https://www.jstor.org/stable/community.18615405) has the content ID "community.18615405".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/jstor:community.18615405/manifest.json](https://iiif.juncture-digital.org/jstor:community.18615405/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `jstor:community.18615405` 

<ve-snippet collapsible label="JSTOR image">
    .ve-media jstor:community.18615405 right

    [Portal of a Venetian Palace](https://www.jstor.org/stable/community.18615405)
</ve-snippet>

### ![](https://upload.wikimedia.org/wikipedia/commons/9/93/Internet_Archive_logotype.png) Internet Archive

The [Internet Archive](https://archive.org/) is a digital library with the stated mission of "universal access to all knowledge." It provides free public access to collections of digitized materials, including websites, software applications/games, music, movies/videos, moving images, and millions of books. 

The Internet Archive provides both IIIF presentation manifests and an IIIF image server.  IIIF links are not exposed or easily found but can easily be created using the item identifier.  For instance, the item identifier for associated with the Interview Archive URL https://archive.org/details/sunflowergirlwithdog would be `sunflowergirlwithdog`.  Internet Archive IIIF URLs use the structure `https://iiif.archivelab.org/iiif/<IDENTIFIER>/manifest.json`.

Using our example the IIIF URL for this item would be https://iiif.archivelab.org/iiif/sunflowergirlwithdog/manifest.json.  When adding an Internet Archive item to a Juncture essay editor using drang-and-drop or copy-paste the correct IIIF URL is automatically created, a manual conversion is not required.

<ve-snippet collapsible label="Internet Archive - image">
    .ve-media https://iiif.archivelab.org/iiif/sunflowergirlwithdog/manifest.json right

    [Sunflower Girl With Dog (1907)](https://archive.org/details/sunflowergirlwithdog)
</ve-snippet>

<ve-snippet collapsible label="Internet Archive - Journal article">
    .ve-media https://iiif.archivelab.org/iiif/jstor-457078/manifest.json right

    [_The Theme of Paradise Lost_](https://archive.org/details/jstor-457078) an article from PMLA, Volume 29.
</ve-snippet>

### ![](https://seeklogo.com/images/M/metropolitan-art-museum-logo-3B8686F789-seeklogo.com.png) The Metropolitan Museum of Art 

The Metropolitan Museum of Art in New York City, colloquially "the Met", is the largest art museum in the Americas and the most-visited museum in the Western Hemisphere. Its permanent collection contains over two million works, divided among 17 curatorial departments.

In 2017, The Metropolitan Museum of Art implemented [a new policy known as Open Access](https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources), which makes images of artworks it believes to be in the public domain widely and freely available for unrestricted use, and at no cost, in accordance with the Creative Commons Zero (CC0) designation and the Terms and Conditions of this website.

MET IIIF URLs are formed by combining the `met:` prefix with the MET content ID.  For example, the image found at [https://www.metmuseum.org/art/collection/search/435809](https://www.metmuseum.org/art/collection/search/435809) has the content ID "435809".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/met:435809/manifest.json](https://iiif.juncture-digital.org/met:435809/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `met:435809` 

<ve-snippet collapsible label="MET Image">
    .ve-media met:435809 right

    [The Harvesters](https://iiif.juncture-digital.org/met:435809/manifest.json)
</ve-snippet>

### ![](https://harvardartmuseums.org/assets/images/logos/logo.svg) Harvard Art Museums

[The Harvard Art Museums](https://harvardartmuseums.org/) make their collections interoperable through several [IIIF compatible services](https://iiif.harvard.edu/collaborators/harvard-art-museums/) and tools. The museum’s services build on the Harvard libraries implementation of the IIIF image API on the Harvard Digital Repository Service (DRS). The Harvard Art Museums exposes collection image URLs and IIIF URIs to the DRS services as part of the dataset accessible through the museum’s API. In conjunction with exposing IIIF compatible image URIs the museums run a presentation service that exposes IIIF compatible manifests and collections. The museums manifest server is based on software that was developed for HarvardX.

<ve-snippet collapsible label="Harvard Art Museums Image">
    .ve-media https://iiif.harvardartmuseums.org/manifests/object/336791 right

    [Winter on Fifth Avenue](https://harvardartmuseums.org/collections/object/336791)
</ve-snippet>

### ![](https://i0.wp.com/wordpressfoundation.org/content/uploads/2022/02/openverse.jpeg) OpenVerse

[Openverse](https://openverse.org/) searches across more than 300 million images from open APIs and the [Common Crawl dataset](https://commoncrawl.org/). It aggregates results across multiple public repositories into a single catalog, and facilitates reuse through features like machine-generated tags and one-click attribution.

OpenVerse URLs are formed by combining the `cc:` prefix with the OpenVerse content ID.  For example, the image found at [https://openverse.org/image/91d578af-785e-4e8c-924b-b511f48ea873]https://openverse.org/image/91d578af-785e-4e8c-924b-b511f48ea873) has the content ID "91d578af-785e-4e8c-924b-b511f48ea873".  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/cc:91d578af-785e-4e8c-924b-b511f48ea873/manifest.json](https://iiif.juncture-digital.org/cc:91d578af-785e-4e8c-924b-b511f48ea873/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `cc:91d578af-785e-4e8c-924b-b511f48ea873` 

<ve-snippet collapsible label="OpenVerse Image">
    .ve-media cc:91d578af-785e-4e8c-924b-b511f48ea873 right

    [Sunflower 'Strawberry Blonde'](https://openverse.org/image/91d578af-785e-4e8c-924b-b511f48ea873)
</ve-snippet>

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/320px-Wikidata-logo.svg.png) Wikidata

[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) is a free and open knowledge base that can be read and edited by both humans and machines.
Wikidata acts as central storage for the structured data of its Wikimedia sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource, and others.

Wikidata URLs are formed by combining the `wd:` prefix with the Wikidata entity ID (aka "Q" ID).  For example, the Wikidata entity for the earth is 'Q2'.  In this example the resulting IIIF URL would be [https://iiif.juncture-digital.org/wd:Q2/manifest.json](https://iiif.juncture-digital.org/wd:Q2/manifest.json).  The short-form IIIF URL for use in Juncture essays would be `wd:Q2` 

Note that images associated with Wikidata entities are hosted in Wikimedia Commons.  Each image returned by a Wikidata QID is actually mapped to a Wikimedia Commons file.  The associated Wikimedia Commons file URL can be seen in the generated IIIF manifest by hovering over the info icon located at the top-right corner of the image.

<ve-snippet collapsible label="Wikidata Image">
    .ve-media wd:Q2 right

    The [Earth](https://www.wikidata.org/wiki/Q2)
</ve-snippet>

### ![](https://edison.rutgers.edu/templates/sas-red/images/rutgers/sas_red_header_MOBILE.png) Edison Papers

The [Thomas A. Edison Papers Project](https://edison.rutgers.edu/), a research center at Rutgers School of Arts and Sciences, is one of the most ambitious editing projects ever undertaken by an American university. For decades, the 5 million pages of documents that chronicle the extraordinary life and achievements of Thomas Alva Edison remained hidden and inaccessible to members of the general public. Since the massive project began in 1978, a team of editors/scholars has been turning this incomparable trove of Edisonia into a premier educational and research resource.

Edison Papers provides both IIIF presentation manifests and an IIIF image server.  Where available, IIIF links for Edison Papers content are easily found on the item page.

<ve-snippet collapsible label="Edison Papers Image">
    .ve-media https://edisondigital.rutgers.edu/iiif/SB178C right

    [Publication, Edison and Murray, 1874](https://edisondigital.rutgers.edu/document/SB178C)
</ve-snippet>

## Streaming Video

This section lists streaming video content providers.

### ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Youtube.png/320px-Youtube.png) YouTube

[YouTube](https://www.youtube.com/) is a global online video sharing and social media platform headquartered in San Bruno, California. It is owned by Google and is the second most visited website, after Google Search. YouTube has more than 2.5 billion monthly users, who collectively watch more than one billion hours of videos each day. As of May 2019, videos were being uploaded at a rate of more than 500 hours of content per minute.

YouTube is the exception to the media providers described on this page in that IIIF manifests are not used for rendering the resource with the Juncture `.ve-media` viewer.  The video content is streamed from YouTube directly using the YouTube API.  The `src` attribute used by the `.ve-media` viewer for YouTube content is simply the YouTube URL for the video.

<ve-snippet collapsible label="YouTube video">
    .ve-media https://www.youtube.com/watch?v=Zy3K2Lcw7hQ right

    [Who was Vincent van Gogh?](https://www.youtube.com/watch?v=Zy3K2Lcw7hQ)

</ve-snippet>

## ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/240px-Octicons-mark-github.svg.png) Github hosted media

Juncture is able to use Github hosted media in an essay.  Juncture can automatically generate an IIIF manifest for media files hosted in Github.  The Juncture IIIF image server is used for delivering the media content.


You can use any image from a GitHub repository in a Juncture essay and a IIIF manifest will be generated by Juncture for GitHub hosted image. A helpful tool in managing your images is the [Juncture Media Tool](/embedded-media). The [setting up a media collection](/howto/setup-media-collection) guide provides detailed information on using the media tool to manage a personal media collection.
