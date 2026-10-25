# Macro edior and enter a name for your macro

Version: DaVinci Resolve 21 New Features Guide. Context: Compositing.
[Chapter index](INDEX.md) / [Previous section](krokodove-tools-and-mapped-3d-duplication.md) / [Next section](uprojector-controls.md)
<a id="source-choosing-the-fairlight-animator-modifier"></a> <a id="source-enter-a-name-for-your-macro-1"></a> <a id="source-font-improvements-including-color-fonts-and-emojis"></a> <a id="source-fusion-animation-can-be-creatively-driven-by-fairlight-audio"></a> <a id="source-improved-multitext-for-position-pivot-alignment-and-csv-import"></a> <a id="source-macro-editor-option-menu"></a> <a id="source-support-for-ograf-html-graphics-and-lottie-animations"></a> <a id="source-support-for-usd-sdk-2511-with-hydra-20-api-for-storm-renderer"></a> <a id="source-text-and-multitext-support-spell-checking"></a> <a id="source-the-fairlight-animator-controls"></a> <a id="source-the-macro-edior"></a> <a id="source-usd-projector-and-usd-catcher-tools"></a> <a id="source-usd-support-for-3d-matte-objects-and-textures"></a>

### The Macro Edior

Over on the left lives the macro editor proper. It lays out, in column view, every parameter belonging to each tool you picked. A checkbox in the Export Column accompanies every parameter; ticking it folds that parameter into your macro, while clearing it leaves the parameter out. The Macro Editor Columns:

- Tool/Input: Fusion’s internal name for the parameter, or the Input connection.
- Export: Tick this box to include the parameter in your macro; clear it to leave the parameter out.
- Name: A text field for naming or renaming how this parameter’s title reads in the macro.
- Type: The kind of data this parameter is set up to accept.
- Default: A field where you preset the parameter’s default value.
- Minimum: A field for setting the parameter’s lowest permitted value.
- Maximum: A field for setting the parameter’s highest permitted value.

### Enter a name for your macro

On the right sits the live Inspector Preview, mirroring how your macro will appear as you assemble it. That visualization earns its keep, letting you add, remove, or edit controls while the macro takes shape. Doubling as an interactive space, the live preview lets you drag and drop controls within it to reshuffle their order. A parameter can be dragged up or down the list, or even moved to a different page. You may also add a fresh page of parameters or rename one that exists. The layout buttons at the Macro Editor’s lower left fine-tune your macro’s appearance further: Add Separator: Drops a separator line into the macro to divide unrelated controls; clear its export box to remove it. Add Spacer: Drops a blank gap into the macro to divide unrelated controls; clear its export box to remove it. Add Nest: Drops a nested disclosure list into the macro. Place the nest, then drag in the parameters you want kept out of sight until the disclosure icon is clicked. Its starting open or closed state comes from the Default column (1 for open, 0 for closed); clear its export box to remove it. While assembling your macro, testing it live within the node editor — without saving and re-importing each round — is handy. From the Macro Editor’s three-dot option menu, choose Copy Macro mid-build, then paste your work in progress straight into the node editor to watch how it truly behaves in Fusion.

After your Macro is complete, the option menu offers several ways to commit it back into Fusion.

### Macro Editor Option Menu

The Macro Editor’s Option Menu:

- Open: Pulls an existing macro into the Macro Editor.
- Save: Commits the work currently in progress.
- Save As Macro: Stores the active macro (one node carrying custom parameters).
- Save As Group: Stores the active macro as a group (a shell of separate nodes you can expand again later).
- Save to Edit Template: Stores the macro as an edit template that surfaces in the effects list on the Cut or Edit pages. Your choices span Title, Generator, Effect, or Transition templates.
- Choose Thumbnail: Lets you load an image to stand in as the macro’s thumbnail picture.
- Show in Folder: Reveals the file location holding your saved macro.
- Copy Macro: Grabs the macro’s present state so you can paste it into the node tree for testing.

### Fusion Animation can be Creatively Driven by Fairlight Audio

Fusion tools now carry a fresh Fairlight Animator modifier. This potent addition wires Fusion into Fairlight’s audio engine so animation can run automatically off audio analysis. Drawing audio from timeline clips or media pool sources, the Fairlight Animator reads audio levels and pipes them into any numerical control. Reach the tool by right-clicking a fusion parameter and picking Modify With > Fairlight Animator from the context menu.

### Choosing the Fairlight Animator modifier

Its controls come into view once you click the Modifiers tab over in the inspector.

### The Fairlight Animator controls

### Support for OGraf HTML Graphics and Lottie Animations

On macOS and Windows, DaVinci Resolve 21 introduces support for OGraf (.json) and Lottie (.lottie) HTML-based animation. Whether you sourced the animation online or built it yourself, it now drops straight onto your timeline. Just export your .json or .lottie file and drag-and-drop it into your Media Pool the way you would any other media. It also goes right into the timeline, where Resolve recognizes it and handles it as a fully rendered animation clip. Because the alpha background is recognized too, transparency carries through. Lay the clip over another layer and it composites cleanly, which makes it a natural fit for a stinger or transition. Beyond that, Fusion gains a new node named OGrafLoader, a convenient way to pull your OGraf or Lottie files straight into your composition.

### Text+ and MultiText Support Spell Checking

As a welcome quality-of-life touch for the spelling-challenged, DaVinci Resolve 21 bundles a multi-language text spell checker covering Text+ and MultiText inside Fusion. Misspellings get flagged in red across both the viewer and the inspector. Right click a word to peek at suggested fixes or to skip it.

### Font Improvements Including Color Fonts and Emojis

Both Text+ and MultiText now accept emoji, so you can drop expressive icons and visual accents right into your text for livelier, more engaging designs. Insert emoji straight into the text fields with Control-Command-Space on macOS and Windows key-. (period) on Windows. On top of that, Text+ and MultiText carry sturdier font handling, with better treatment of color fonts, bitmap fonts, and font styles. When a color font is supported, the Text+ inspector surfaces extra Color Palettes controls beneath Advanced Controls, where the font’s display options are chosen. Some emoji fonts — Noto Color Emoji among them — hold only emoji glyphs and no letters, so typing Latin characters in such a font leaves nothing in the text. Type emoji while a regular font is active and Fusion spots it, switching to an emoji font on its own; the reverse swap, however, doesn’t happen. A Fusion preference settles which emoji font gets used.

### Improved MultiText for Position, Pivot, Alignment and CSV Import

Fusion’s MultiText gains refinements to its position and alignment controls and to CSV import, plus new pivot adjustments on the Layout tab.

### Support for USD SDK 25.11 with Hydra 2.0 API for Storm Renderer

Fusion now runs on USD SDK 25.11 with the Hydra 2.0 API behind the Storm renderer. The upgrade delivers a better Fusion USD environment plus a welcome uRenderer addition named Neye. That new AOV yields camera-relative normals, opening up still more flexibility in your workflow.

### USD Support for 3D Matte Objects and Textures

Our USD geometry tools pick up fresh “Is Matte” controls for added creative latitude. Baked straight into the USD geometry tools, these controls also turn up in the uReplaceMaterial tool. Behaving much like Fusion 3D tools, the Is Matte feature lets you hide background objects or carve tidy alpha channel cutouts by punching holes wherever they’re needed.

### USD Projector and USD Catcher Tools

Say hello to the new USD Projector and uCatcher tools. Through the uProjector node you project images straight onto USD geometry, throwing imagery across any objects in your USD scene and reshaping how those USD objects appear in an instant. Partnered with the uProjector, the uCatcher tool grabs the texture-mode projections and turns them into textures that drop cleanly onto your connected geometry. In concert, these tools unlock creative avenues for dynamic texture mapping across your USD workflows. The uCamera tool gains projection too; wire an image into the new Image Input and additional tabs surface. Just as with Camera 3D, those tabs carry Image and Material as well, handily affording a camera-matched image plane. Fuller descriptions of these tools sit below.
