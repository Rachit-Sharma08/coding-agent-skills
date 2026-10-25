# File inspector parameters and tips for editing metadata

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using clip metadata.
[Chapter index](INDEX.md) / [Previous section](editing-clip-metadata-and-automatically-imported-metadata.md) / [Next section](media-pool-metadata-import-and-export.md) / [Continue Importing and Exporting Media Pool Metadata / The Metadata Import Dialog](media-pool-metadata-import-and-export.md)
<a id="source-analyzing-an-audio-clip"></a> <a id="source-audio-classification-for-clips-studio-version-only"></a> <a id="source-creating-custom-metadata-groups"></a> <a id="source-custom-metadata-categories-drop-down-menu"></a> <a id="source-face-detection-to-generate-people-keywords"></a> <a id="source-importing-and-exporting-media-pool-metadata"></a> <a id="source-the-file-inspector-parameters"></a> <a id="source-tips-for-editing-metadata"></a>

### The File Inspector parameters

### Tips for Editing Metadata

Editing metadata is rather like taking your vitamins. No one is eager to, yet you sense you ought to. To nudge you into tackling it so the rewards follow, here are a handful of pointers.

- Hold off on editing until you've screened your footage and tagged it with metadata. Make a habit of logging your clip metadata before the edit absorbs your attention, and you'll be far better placed to edit quickly using organizational tools that draw on the metadata you've supplied.
- Begin metadata entry with batches of clips before drilling down to individual ones. Because the Metadata Editor accepts metadata for several selected clips simultaneously, it's simple to gather groups of clips by their thumbnails and log details — among them Scene designations along with Character, Framing, and Interior or Exterior keywords. You'll be amazed how quickly it goes and how valuable this information turns out to be afterward, for both editing and grading.
- Once you've logged as much metadata as you can across batches of clips, shift to clip-by-clip metadata such as Shot designations, Take numbers, action descriptions, and other clip-specific keywords.
- No method of editing or applying metadata is inherently right or wrong, but inconsistency erodes its value. For instance, when you're labeling each clip set at the same diner, stick to one keyword or descriptive phrase. Call half the shots “diner” and the rest “restaurant,” and your ability to easily round up all the diner shots takes a hit.

### Audio Classification for Clips (Studio Version Only)

You can task DaVinci Resolve’s Neural Engine with analyzing the audio of any clip in the Media Pool, after which it automatically gives the clip a Category and records keywords describing its contents in the clip’s Subcategory audio metadata. This lets you sort and organize huge quantities of audio clips with great efficiency, handing the computer the tedious chore of listening to all the media and tagging it with metadata for you. Naturally, you're free to then tweak or replace whatever metadata you need within the Metadata Editor should the computer have gotten a category wrong.

### Analyzing an audio clip

Every clip that gets analyzed receives Audio Category and Subcategory metadata. Audio Categories are kinds of audio frequently encountered in post-production; at the time of writing the choices on offer are: Dialogue, Effect, Music, Silence, and Uncategorized. Subcategories are finer-grained keywords assigned according to which sounds the Neural Engine manages to detect in the clip. A Subcategory might be anything — sirens, water, dog, and so on. Audio Category and Subcategory both function as Smart Bin filters, letting you swiftly build persistent folders for any blend of Categories and Subcategories you like. For instance, you could set up a Smart Bin holding every clip that carries both Dialogue (category) plus sirens and dogs (subcategories). To Automatically Classify an Audio Clip: 1 Pick the clip or clips in the Media Pool whose audio you want classified. 2 Right-click any of the chosen clips and pick AI Tools > Audio Classification > Analyze from the contextual menu. DaVinci Resolve works through analyzing all the selected clips and automatically writes the metadata into the Audio Metadata for each one. 3 If you like, you can afterward look over each clip's Audio Metadata and correct, delete, or tack on extra metadata yourself.

The results of the analysis in Category and Subcategory

Every Category and Subcategory turned up by this process spawns Smart Bins automatically inside the Collections folder, keyed to that metadata. You're also free to craft your own Smart Bins from combinations of these keywords.

A Subcategories folder listing that displays the folders the analysis produced To Remove Classification Metadata from an Audio Clip: 1 Pick the clip or clips carrying Category and Subcategory metadata you wish to clear. 2 Right-click any of the chosen clips and pick Audio Classification > Clear Classification from the contextual menu, then click Remove in the warning dialog that surfaces. This feature offers no undo.

### Face Detection to Generate People Keywords

You can grab several clips in the Media Pool, right-click the selection, and pick AI Tools > Analyze clips for people from the context menu to have the DaVinci Neural Engine analyze every selected clip automatically, spotting faces that can aid in organizing your media. A progress dialog reports how much time remains before the analysis wraps up (and you can cancel the operation if you need to). When it finishes, the People Management window opens to present the results, sorted automatically into a set of bins along a sidebar.

- A “People” bin lists every face recognized as a distinct individual. Click, pause, then click once more beneath any thumbnail to change that person's name or role. A name has to be assigned before a keyword for that individual will turn up in the People field of the Metadata Editor. Supplying names renames the bins tied to each discovered person and makes retagging possible to correct a mistaken identification.

The Face Recognition window seen immediately after a Face Recognition operation

- Per-person bins gather every clip featuring a given individual, letting you judge whether the contents were identified correctly. Spot a wrongly identified clip and you can right-click it to re-tag it from the contextual menu, or pick “Untag” when it's a new person not yet identified at all.

A bin for a particular person lets you evaluate the contents

- An “Other People” bin holds all the faces that couldn't be identified. Right-click any of them to re-tag it as one of the already-identified people, or pick New Person when it's someone missed at first (which can happen when several people share very similar features).

The Face Recognition window seen immediately after a Face Recognition operation Pressing the Close button shuts this window and writes the names you edited, as keywords, into the “Shot & Scene” group's People field within the Metadata Editor. Clips containing multiple identified people receive multiple keywords.

The Shot & Scene group's People keywords field in the Metadata Editor, filled in with who appears in that shot Once People keywords sit on one or more of your clips, a People smart category of smart bins can appear by itself inside the Media Pool's Smart Bins sidebar, so you can immediately start turning up clips that show particular individuals. Building this People Smart Bin is a matter of ticking the “Automatic Smart Bins for People Metadata” box, found under Preferences > User > Editing. Should you wish to make edits later, reopen the Face Recognition window through Workspace > People. Wiping every face is done from the People Management Option menu via “Reset Face Database.” NOTE: Within the Option menu of the Face Recognition window sits a Reset Face Database command that discards all analyzed results whenever they fall short and you'd prefer not to retain the metadata they produced.

### Creating Custom Metadata Groups

Through the Metadata panel in the User Preferences you can assemble custom sets of metadata parameters that will surface in the Metadata Editor. This panel lets you build tailored subsets of metadata geared to your specific needs. The presets you make are reachable from the Option menu sitting just left of the Metadata categories drop-down menu. Selecting any custom preset limits the Metadata Editor to displaying only that preset's metadata fields. To see every custom metadata field you've stored in a given preset, set the Metadata Categories drop-down menu to All Groups. To bring the entire set of metadata fields back, simply pick default presets from that same drop-down.

### Custom Metadata Categories drop-down menu

Creating and handling metadata presets is straightforward. To create a new metadata preset: 1 Open the Metadata panel within the User pane of the Preferences window and click New. 2 Tick the checkbox of each metadata tag you'd like in this preset, or tick a group name's checkbox in the list to pull in every metadata tag it holds. Each metadata tag offered in DaVinci Resolve sits inside one of several groups shown as a list. To expand a group and view its contents, hover the pointer over that group’s row in the list and click the Open button once it shows. 3 With that finished, press the Save button below Metadata Options. 4 Then press the Save Button belonging to the User Preferences. To edit an existing metadata preset: 1 Pick a preset from the list and click Edit. 2 Toggle checkboxes on and off to add or drop whatever tags you need. 3 Hit the Save button situated under Metadata Options. 4 Lastly, hit the User Preferences Save Button. To delete a metadata preset: Pick a preset from the list and click Delete.

### Importing and Exporting Media Pool Metadata

After you've gone to the effort of tagging your project's clips with metadata, DaVinci Resolve lets you export metadata from one project's Media Pool and import it into another project's clips, for those times when metadata needs to travel between projects. As an example, a DIT may have loaded a great deal of metadata into the DaVinci Resolve project used to generate dailies, only for a hurried editor to spin up a separate project to start cutting those dailies. Rather than making the editor retype every clip's metadata from scratch, you can pull the metadata out of the project belonging to the DIT and load it into the project the editor just made, letting the relevant metadata line up automatically against each matching clip. To export Media Pool metadata: 1 Open whichever project holds the Media Pool metadata you intend to export. 2 If you wish, pick which Media Pool clips you want metadata exported for. 3 Choosing File > Export Metadata From > Media Pool covers every clip there, whereas File > Export Metadata From > Selected Clips limits the export to the clips you marked back in step 2. 4 Once the Export Metadata dialog opens, type a name, pick where the file should be saved, then click Save. Every bit of metadata exports into a .csv file you can open and edit in any spreadsheet application, or into an Avid Log Exchange (.ale) file when you need Avid Media Composer compatibility. Open the resulting metadata .csv file and its first line is a header naming what metadata appears for each item in the document, and in what sequence. Only metadata fields filled in for at least one clip get exported and named in that header; metadata fields left empty in the Metadata Editor or Media Pool are skipped. That file can then be imported into another project file to reattach the metadata to those same clips.
