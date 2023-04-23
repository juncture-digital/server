# Juncture Editor

The Juncture Editor provides a quick and convenient means for creating a Juncture essay.  Note that Juncture text files can be created and managed in Github using a number of approaches, including using the built-in Github web editor.  The advantages of using the Github editor include:

- Handling all interactions with Github for creating, reading, writing, and deleting text files used by Juncture
- Helpful aids for Markdown text formatting
- Automatic Juncture viewer tag creation using copy-paste and drag-drop user actions
- Essay preview for rapid iteration of changes
- Editor content is preserved between page visits making it convenient to incrementally work on an essay without fear of losing changes

## Two modes of use

After logging in with Github the Juncture editor can be used in one of two ways.

- As a separate window launched from a button found in the left sidebar. The advantage of this approach is that the various code snippets found in the documentation can be easily added to the editor using drag-and-drop.
- An embedded viewer found on [this page](/embedded-editor). This approach has the advantage of reducing desktop clutter with one less window.

Both of these activation methods are linked in the top section of the left navigation sidebar menu.

!> The editor works identically in either mode.  **Try to avoid using both simultaneously as divergent edits may result in Github merge conflicts when saving.**

## Using the editor

### Editor layout

<ve-media src="gh:juncture-digital/media/images/Juncture_Editor.jpg" anno-base="juncture-digital/juncture/docs/tools" right></ve-media

This section provides an overview of the Juncture editor.

1. <mark zoomto="0,0,504,749,c67efb55">Github content tool</mark>.  The Github content tool provides basic content management support for interacting with Github.  By default the content tool reads and writes files from the `essays` repository in a users primary Github account.  Other accounts and repositories may be used if desired.  The content tool provides drop down menus for selecting other Github accounts and repositories.  For many users the default `essays` repository is probably a good option changing Github accounts and/or repositories will not be required.
2. <mark zoomto="0,0,504,749,442d8b11">Markdown toolbar</mark> - The Markdown toolbar provides convenient tagging for common Markdown formatting.  The icon for the desired formatting is pressed after the text to be formatted has been selected.
    - <mark zoomto="0,0,504,749,490ccb15">Mark</mark> - Used for Marking essay text for viewer interactions
3. <mark zoomto="504,0,504,749,665f09a2">Juncture toolbar</mark>
    - <mark zoomto="504,0,504,749,b6d6e746">Save</mark> - The save button will write the essay text to Github
    - <mark zoomto="504,0,504,749,ea5bd304">Share</mark> - The share button will display the essay in a new tab
4. <mark zoomto="0,0,1081,1602,134e67a0">The main editor window</mark> - Text is entered using keyboard input.  External resources (images, videos, text) from other sites may also be dragged into the window.  For recognized items Juncture will automatically create an appropriate tag.  A user override or supplement this as needed.
5. <mark zoomto="533,793,474,705,0e305489">Preview</mark> - The preview button will toggle the Juncture editor between edit and preview modes.
6. A sample <mark zoomto="0,0,1007,1498,3f63ff16">Viewer tag</mark>

### Saving text to Github

The editor will periodically save a copy of essay text to browser internal storage.  Note that this auto-save feature only saves a copy locally.  A permanent save to Github must be explicitly initiated by pressing the `save` button in the Juncture toolbar. 