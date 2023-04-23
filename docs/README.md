<style>
a.cta {
  background-color: #FFE55A;
  border-radius: 50px;
  font-family: Roboto, Helvetica, sans-serif;
  font-weight: normal;
  font-size: 1.6rem;
  padding: 12px 60px;
  margin: auto;
  margin-top: 0;
  text-align: center;
  color: #0b0080;
  text-decoration: None;
}
.splash-end img, .splash-end a {
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
}
.splash-start p {
  display: flex;
  align-items: center;
  gap: 6px;
}
.splash-start p img {
  height: 30px;
}
p {
  display: flow-root;
}

</style>

<div class="splash">
<div class="splash-start">

<div class="splash-logo" style="display:flex;align-items:center;">
    <img src="https://juncture-digital.github.io/juncture/static/images/favicon.svg" style="margin:-12px 0 0 -12px;height:90px">
    <div style="font-size:3rem;color:#455;margin-top:-10px;font-weight:bold;">Juncture</div>
</div>

<h3 style="line-height:1.3;margin-top:1rem;"><i>Create and share rich, interactive essays in minutes!</i></h3>

- Quickly create single essays or full web sites
- Minimal setup and no ongoing administration
- Easy-to-use drag-n-drop editor with preview
- Flexible content viewers for displaying images, video, audio, maps, diagrams, and more
- Use web-based resources and your own content
- Image and text annotation tools
- IIIF-enabled features for using high-quality, attributed digital objects
- WordPress compatible
- Open source and built on open tools and data formats

Juncture was developed and is maintained by [![JSTOR](https://raw.githubusercontent.com/juncture-digital/juncture/main/static/images/labs.jpg)](https://labs.jstor.org)

</div>
<div class="splash-end">
    <div style="display:flex; flex-direction:column; align-items:center; gap:2rem;">
        <img class="splash-image" src="https://iiif-image.juncture-digital.org/iiif/2/e058046a1379d7dfc9a4daee11a9a6ca1b7ac9bafd78fd30d40ff92fef99ce86/full/500,/0/default.jpg" alt="Juncture graphic">
        <div><a href="#/getting-started" class="cta">Get Started</a></div>
    </div>
</div>
</div>

# Welcome to Juncture

**Juncture** is a suite of tools and services that enable anyone to easily create engaging web pages with rich visualizations, including interactive images, videos, maps, and more.  

Juncture is developed and maintained by the friendly folks at [JSTOR Labs](https://labs.jstor.org) and [grew out of a project](https://www.doaks.org/research/mellon-initiatives/plant-humanities-initiative) that used visual essays for a form of digital storytelling.  Visual essays are text narratives augmented with interactive visualizations providing depth and context.  

This version of Juncture represents the second generation of the Juncture concept.  It's a complete rewrite of the Juncture code base and documentation.  The rendering engine in version 2 is backward compatible with visual essays written for version 1, so if you're an existing Juncture user, no worries, your Juncture essays will continue to work.  

?> Documentation for Juncture version 1 can be found [here](https://github.com/jstor-labs/juncture/wiki).

In its current form, Juncture is still well-suited for the type of digital storytelling emphasized in version 1 but can now be more easily used for generating web pages that are less text-centric, such as an image exhibition.

This [demo essay](https://www.juncture-digital.org/showcase/bedroom-in-arles) provides an example of what is possible in a Juncture essay.  This essay includes multiple high-res images, a YouTube video, an interactive map, and some text-to-viewer interactions.  The essay also includes many information popovers for entities (people, places, works, etc) mentioned in the text.  Other examples may be found in the [Juncture Showcase](/showcase).

# What problem does this solve?

Juncture's primary goal is to make the use of modern web technology (deep-zoom and panning for high-resolution images, interactive maps, etc) accessible to anyone with an interest in sharing something on the web, regardless of background or technical skills. In the [Quick Start guide](/quick-start), you can give it a try and see for yourself. All that is required for this quick start (and to use Juncture generally) is an active Github account. If you already have one, the "hard" part is done. If not, you'll need to take a couple of minutes to signup with Github. Signing up for a Github account is free and painless.

If you're looking for a set of easy-to-use tools for quickly creating web pages with engaging and interactive content with minimal setup and zero ongoing administration, Juncture might be exactly what you need.

# Some Juncture uses

1. **Education**. Juncture is able to support a range of teaching and learning use cases, including:
    - Use by instructors in the development of resources for classroom or remote instruction.  The [Hypothes.is](https://web.hypothes.is/) annotation tool can be easily added to any essay for class discussion or other uses. 
    - Use by students for individual or group projects.  Juncture can be used as tool for simple essay development or as tool for building broader skills in the use of digital technologies for information creation and sharing.

2. **Simple blog or travelogue**.  The ability to quickly create a web page with text and images makes Juncture a convenient tool for blog style content authoring.  With the addition of interactive maps, connected with text and images, Juncture is well-suited for creating rich and engaging travelogues.  Images, with geolocation data when available, can easily be transferred from a smartphone into a Juncture essay.

3. **Creation of full website with themed essays**.  Multiple Juncture essays can be easily aggregated and linked to create full websites, with a custom domain if desired.  Examples of themed websites created with Juncture include [Plant Humanities Lab](https://lab.plant-humanities.org/) and [Kent Maps Online](https://kent-maps.online/).

4. **Many others**.  As a general-purpose tool there are any number of interesting ways in which Juncture could be applied. We'd love to hear how you use Juncture.  Please connect with us from our [Contact](/contact) page if you come up with some innovative or interesting use of Juncture that we could share with others.  You might also consider submitting essays for inclusion on the Juncture Showcase site.

# About Juncture and IIIF

Juncture is built using many great technologies and tools, many of which can be seen on the Juncture [attribution](/attribution) page.  A cornerstone in the Juncture design and value proposition is IIIF.  The [International Image Interoperability Framework](https://iiif.io/) (IIIF, spoken as 'triple-I-eff') defines several APIs (Application Programming Interfaces) that define a standardized method of describing and delivering media over the web.  IIIF is arguably the most important technology used by Juncture.  Understanding what IIIF is and how it is used will be useful background before diving into the creation of an essay, especially those incorporating images, audio, and video.  

The [IIIF Get Started](https://iiif.io/get-started/) page is the best place to start for good understanding of IIIF.  In this section a top-level overview is provided.  Much of the information provided consist of excerpts from the official IIIF site.  Users interested in learning more are encouraged to visit the IIIF site.

## Why IIIF?

The benefits of using IIIF include:

- **Rich image delivery**.  Fast, rich zoom & pan delivery of images via the Internet, with options for size, scale, region of interest, rotation, quality and format.
- **Plug and play software**.  Use any IIIF-compatible software for viewing, comparing and manipulating images from any IIIF-compatible image site, regardless of the back-end server. Swap parts of the stack at any time, or run multiple components in parallel at once.
-**Publish once, reuse often**.  Deliver images from your own site for many uses; host a single copy and embed in other sites. No need to transfer images to others for them to locally load and use them for one off analysis or republishing.
-**Remix content**.  Assemble and reuse IIIF resources from across the Web, regardless of source. Compare pages, import into tools, build exhibits, or view items served from different sites in one place.
-**Annotate**.  IIIF has native compatibility with the [W3C Web Annotation model](https://www.w3.org/TR/2017/REC-annotation-model-20170223/), which supports annotating content on the Web. Comment on, transcribe, and mark up resources using the Web’s inherent architecture–even for Audiovisual resources.
-**Cite and share**.  IIIF APIs give portable views onto images or any of its regions, and provide incentive for URIs that persist through image server migrations. Cite an image with a stable URI, or share it for reference by others–or yourself in a different environment.
-**Support for attribution and access control**.  Built in API calls support attribution and access control: the Authentication API (http://iiif.io/api/auth/), is integral and consistent with the IIIF conception.

## IIIF use in Juncture

The "Why IIIF?" list of benefits provides a compelling case for using IIIF over standard images, audio, and video.  The benefits provided by IIIF support for interoperability, annotation, and its ability to clearly articulate reuse rights and attribution are especially important capabilities leveraged by Juncture.

It's hard to argue against the benefits of using IIIF.  Unfortunately, for most users the technology has been out of reach as the tools and infrastructure needed are often not available or are hard or confusing to use.  That's where Juncture comes in.  It can deliver the IIIF benefits with minimal effort.  If fact, using IIIF can often be as simple as dragging an image into the Juncture editor.  If the image is not a native IIIF image Juncture can often turn it into one automatically and transparently.
