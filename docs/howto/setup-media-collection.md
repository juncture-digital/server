# Setting up a Personal Media Collection

This guide describes an approach for hosting IIIF media content in a Github repository.  In this approach media files and IIIF properties files are stored in a Github repository. Juncture is able to dynamically generate IIIF presentation manifests and serve IIIF image tiles for this content.

?> Where possible, users are encouraged to use a purpose-built sharing site for hosting and sharing media files.  [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) is one such (free to use) site for hosting and sharing media files.  While Wikimedia Commons (and some other file sharing sites) do not yet support IIIF, the same Juncture services that are used to generate IIIF manifests and serve images from Github repositories also works with many of these sites.  More information finding and using IIIF media resources can be found [here](/resources/media)

# Using Github as an IIIF Media Repository

The Juncture IIIF services are able to serve IIIF media from files stored in Github.  In many cases all that is required is a media file (image, audio, or video) stored in a public Github repository, where the file name conforms to a few simple naming conventions.  In cases where more descriptive metadata is needed a simple key-value properties file can be associated with a single file or a group of files located in a Github folder.

In the simplest case, 

- A IIIF label property is created from the Github file name
- The IIIF reuse rights property defaults to http://creativecommons.org/licenses/by/4.0/ with an auto-generated attribution statement that uses the Github username associated with the Github repository hosting the file
- Other IIIF properties, such as a thumbnail URL, are automatically created by Juncture

# Options for managing a media collection

## Using the Juncture Media Tool

The Juncture Media tool is convenient for browsing Github hosted media collections.  It can also be used to upload media files to Github and define some custom metadata that cannot be inferred by Juncture.  When used from a smartphone, the media tool provides a convenient way to upload photos to Github.

## Uploading files to Github

### Image only

The easiest method for hosting an IIIF media file is to simply upload the file to a Github repository using a file name that can be used to generate the image label.  In cases where something other than the default license (`CC-BY`) is needed, the file name can be augmented with a reuse rights code, for instance, `CC0`.

The convention for file naming when used for IIIF media serving by Juncture is:

- The file name will be converted to an IIIF label and can optionally include a rights code.
- Underscore characters (`_`) in the file name are converted to spaces in the IIIF label.
- The label and optional rights code are separated using `--` in the file name. For instance, an image file named `A_Shared_Image--CC0.jpg` would result in a IIIF manifest label of `A Shared Image` and a reuse rights code of `CC0` (Public Domain Dedication).
- A double underscore (`__`) can be used to signify the end of a label in a Github file name.  This can be useful if multiple images in a Github folder will use the same label.  For instance, `A_Shared_Image__1--CC0.jpg` and `A_Shared_Image__2--CC0.jpg`.  In this example both image files have a unique Github file name but can be associated with the same label.

The reuse rights for a file is defined by appending a Creative Commons or Rights Statements code to the end of the file name (but before the file extension).  The reuse rights code is one of the [Creative Commons](https://creativecommons.org/licenses/) or [RightsStatements.org](https://rightsstatements.org/page/1.0/) codes defined in [Reuse Rights](#reuse-rights) section below.  If a rights code is not provided in the file name a default value is used.  The default value is obtained from properties files found in the folder hierarchy in which the image file is located.  If rights metadata is available in multiple properties files the value in the file that is closest to the image takes precedence.  For instance, if a properties file at the root of the repository defined the reuse rights as `CC BY` and then another properties file in a parent/ancestor folder of the image defined the reuse rights as `CC BY-SA`, the `CC BY SA` value would take precedence and would be used in the generated IIIF manifest.

### Media and properties file

In situations where it is desired to associate richer metadata with an image a supplemental properties file may be used.

### Properties file only

In situations where an image is hosted on another web site that does not provide a IIIF manifest a properties file is used to define the IIIF metadata in a generated IIIF manifest.  When using this method the URL to the externally hosted image is included in the properties file in addition to the usual IIIF metadata properties.

# Reuse Rights

The IIIF Presentation Manifests provide a flexible approach for asserting the reuse rights for an image and any attribution (or other) statements that must be displayed when the image is used.

`Rights` refers string that identifies a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image. The value must be drawn from the set of [Creative Commons](https://creativecommons.org/licenses/) license URIs or [RightsStatements.org](https://rightsstatements.org/page/1.0/) rights statement URIs.

## Creative Commons Licenses

- `CC0`: [Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/)
- `CC-BY`: [Attribution](http://creativecommons.org/licenses/by/4.0/)
- `CC-BY-SA`: [Attribution-ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/)
- `CC-BY-ND`: [Attribution-NoDerivs](http://creativecommons.org/licenses/by-nd/4.0/)
- `CC-BY-NC`: [Attribution-NonCommercial](http://creativecommons.org/licenses/by-nc/4.0/)
- `CC-BY-NC-SA`: [Attribution-NonCommercial](http://creativecommons.org/licenses/by-nc-sa/4.0/)
- `CC-BY-NC-ND`: [Attribution-NonCommercial-NoDerivs](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## Rights Statements

- `InC`: [In Copyright](http://rightsstatements.org/vocab/InC/1.0/)
- `InC-OW-EU`: [In Copyright - EU Orphan Work](http://rightsstatements.org/vocab/InC-OW-EU/1.0/)
- `InC-EDU`: [In Copyright - Educational Use Permitted](http://rightsstatements.org/vocab/InC-EDU/1.0/)
- `InC-NC`: [In Copyright - Non-Commercial Use Permitted](http://rightsstatements.org/vocab/InC-NC/1.0/)
- `InC-RUU`: [In Copyright - Rights-Holder(s) Unlocatable or Unidentifiable](http://rightsstatements.org/vocab/InC-RUU/1.0/)
- `NoC-CR`: [No Copyright - Contractual Restrictions](http://rightsstatements.org/vocab/NoC-CR/1.0/)
- `NoC-NC`: [No Copyright - Non-Commercial Use Only](http://rightsstatements.org/vocab/NoC-NC/1.0/)
- `NoC-OKLR`: [No Copyright - Other Known Legal Restrictions](http://rightsstatements.org/vocab/NoC-OKLR/1.0/)
- `NoC-US`: [No Copyright - United States](http://rightsstatements.org/vocab/NoC-US/1.0/)
- `CNE`: [Copyright Not Evaluated](http://rightsstatements.org/vocab/CNE/1.0/)
- `UND`: [Copyright Undertermined](http://rightsstatements.org/vocab/UND/1.0/)
- `NKC`: [No Known Copyright](http://rightsstatements.org/vocab/NKC/1.0/)
