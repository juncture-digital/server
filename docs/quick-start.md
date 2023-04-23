# Juncture Quick Start

In this Quick Start guide you'll create your own version of the `Hello, Juncture` demo essay.  This quick start consists of 5 easy steps and should only require a couple of minutes to complete if you already have a Github account.  A few minutes more if not.

?> After completing this quick start, visiting the more comprehensive [Getting Started](/getting-started) guide would be a great next step in becoming acquainted with Juncture features and use.  The Getting Started guide provides more information and many helpful examples.

Click this button to see what we're going to create. <ve-modal button-label="Hello, Juncture" src="juncture-digital/juncture/examples/hello-juncture"></ve-modal> 

While this is a simple essay it illustrates the basic steps in creating an essay.  The generated essay could also be used as a starting point for more involved essays.

?> **Show me** buttons - Some of the steps in this guide include a "Show me" button below the step's instruction text.  Clicking this button will open a popup with a short animation demonstrating the actions to be performed.  Clicking this button is optional, but can often help clarify something that may not be clear from the text alone.

### 1. First things, first...

If you haven't already done so, you'll need to,

- [Signup for a Free Github account](https://github.com/join), and 
- **Login to Github from Juncture**.  There's a login button at the top left of this page that can be used to login to Github.  In the initial login you will be asked to authorize Juncture to make changes on your behalf (via the Juncture Editor tool).  

<ve-modal label="Initial Github Login" button-icon="play-circle" style="margin-left:1rem;" width="640px">
.ve-media gh:juncture-digital/media/videos/Login.gif no-caption no-info-icon
</ve-modal>

After the initial login has been performed, the login/logout process is a single button click.  Note that You will remain logged-in between sessions unless an explicit logout is performed.

### 2. Open the Juncture Editor

Once you've successfully logged in with Github (and authorized Juncture access), open the Github Editor in a new window. <ve-window href="/editor" button-label="Open the Juncture Editor" button-icon="pencil"></ve-window>

### 3. Create a new essay file on Github

In the Github navigation toolbar at the top of the Editor window (located just below the header), select the `Add File` icon and enter the name of the essay to be created (for example, `hello-juncture`) in the input dialog that appears.  Press the `Add` button to create a new essay.  

?> When a file extension (such as `.md`) is not included in the name, a folder with the specified name is created with a single child file named `README.md`.  **README.md** is the Github convention for naming index files in a folder.  While we could have used the file name `hello-juncture.md` for our new essay (which would have worked perfectly fine), creating a parent folder for the essay has advantages and is generally recommended.  The main benefit is that is folder provides a convenient location for storing other files that may eventually be associated with the essay.  This could include annotation files and map overlays, among others.

<ve-modal label="Create new Juncture Essay" button-icon="play-circle" style="margin-bottom:1rem;">
.ve-media gh:juncture-digital/media/videos/Add_Essay.gif no-caption no-info-icon
</ve-modal>

### 4. Add some content

Now that we have an essay file created we're ready to add some content.  For this quick start, we'll just copy (or drag) some prepared text into the editor.  

Before we add our new text delete any existing text found in the editor pane.  This should be the placeholder `# README.md` header text.

The text we're going to add can be found in the snippet viewer below.  The text can be copied into the clipboard by clicking on the `Copy` button that appears at the top-right corner when hovering over the snippet viewer.  You can also click-and-drag the window into the editor.  In either case, ensure the snippet viewer is showing the Markdown formatted text.

<ve-modal label="Add Content (using drag-n-drop)" button-icon="play-circle" >
.ve-media gh:juncture-digital/media/videos/Add_Content.gif no-caption no-info-icon
</ve-modal>

<ve-snippet label="Code snippet">
    # Hello, Juncture

    This Juncture essay illustrates the use of a few Markdown formatting tags and the incorporation of an image and a map into a Juncture essay.

    ## Aulacophora indica

    .ve-media wc:The_Bug_Peek.jpg right

    The image depicts a leaf beetle (Aulacophora indica) (Family: Chrysomelidae; subfamily: Galerucinae) looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.

    This image is hosted on [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Bug_Peek.jpg) and was runner-up for Wikimedia Commons Picture of the Year for 2021.

    Image controls are located in the top-left corner of the image and can be seen when hovering over the image.  These controls support image zoom, rotation, full-screen viewing, and repositioning to the start position.  Panning can be performed with keyboard arrow keys or by mouse click-and-drag.

    Image information can be seen when hovering the cursor over the info icon located in the top-right corner of the image.  The Image information popover includes the image title, description, attribution statement, and reuse rights.

    ## Chitwan National Park, Nepal

    .ve-map Q1075023 right

    The map is centered on the Chitwan National Park in Nepal, which is the location associated with the image above.  The Wikidata identifier for Chitwan National Park is `Q1075023`.  When a map location is specified using a Wikidata ID (or QID) Juncture can automatically retrieve the geographic coordinates for map centering.

    An alternative to using a Wikidata identifier for map positioning is to use regular latitude and longitude coordinates.  In that approach the QID would be replaced with the coordinates `27.5,84.333`, resulting in an identical map.
    
    Similar to the image viewer, map zooming is controlled using the buttons located in the top-left corner of the map viewer.  Panning is performed with the keyboard arrow keys or by mouse click-and-drag.
</ve-snippet>

### 5. Preview and save the essay

After copying (or drag-and-dropping) the text into the editor pane, click the `Preview` icon in the tool panel located near the top-right corner of the editor window.  This will display the rendered version of the essay.

Next, click the `Save` icon in the tool panel to save the updated contents of our new essay file to our Github repository.

?> Note that previewing an essay from the editor does not require that it is first saved to Github.  The preview and save actions may be performed in any order.  When previewing an in-process essay the text used for the preview comes from the editor directly, not from Github.

<ve-modal label="Preview and Save" button-icon="play-circle" width="520px">
.ve-media gh:juncture-digital/media/videos/Preview_and_Save.gif no-caption no-info-icon
</ve-modal>

Congratulations, you've just created your first Juncture essay. 
