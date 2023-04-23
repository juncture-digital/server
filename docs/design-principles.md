# Juncture design principles

In developing Juncture we were guided by a few key principles.

1. **Juncture will not store user data.** **  We just want to make it easier for you to use it to create and share great web content.
    - Many web hosting services store a copy of the source files used to render a web page or site.  Juncture does not.  It is principally an HTML rendering engine and set of authoring tools.  Content is stored in a Github repository that is user-owned and managed.  Juncture only requires read access to the Github repository to access the files for rendering.
    - The Juncture tool suite includes an optional browser-based editor that may be used to create and modify user files in Github.  When using the Juncture editor a user will first need to authorize the editor to perform Github file updates on their behalf.  This authorization can be easily revoked by a user at any time.
    - ** The only caveat to the "Juncture does not retain user data" principle is that an optimized copy of user-hosted image files used in a rendered page is cached by the Juncture image server for a fixed period of time for performance reasons.
2. **Juncture will use open and non-proprietary tools and data where possible.**  This includes:
    - Markdown (with a few Juncture extensions) for visual essay definitions
    - The International Image Interoperability Framework (IIIF) for media (image, video, audio) rendering
    - GeoJSON for map features and overlays
    - Various data and services provided by the Wikimedia Foundation, including text from Wikipedia, Linked Open Data (LOD) from Wikidata, and images and other media from Wikimedia Commons
3. **Support and promote the responsible use of web resources**  All resources used in a visual essay include attribution when required and clearly define reuse rights. 
4. **Minimal setup and administration by a user.**  Some initial work is needed by a user to create a home for the content to be rendered by Juncture.  That's where Github comes in.  To get started a user must signup for a Github account and link it to the Juncture editor.  For many users, that's it.  There is no ongoing administration required of a user.  No cloud infrastructure provisioning, no server management, nothing of that sort. A user can focus time and energy on creating great content. The only exception to this would be the setup of a custom domain for a Juncture website if that was desired.  A step-by-step build is provided for custom domain setup. It would typically require no more than a few minutes.   