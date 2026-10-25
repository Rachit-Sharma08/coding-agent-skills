# Font browser toolbar and show font previews preference

Version: DaVinci Resolve 21 New Features Guide. Context: Editing.
[Chapter index](INDEX.md) / [Previous section](affinity-layered-file-support.md) / [Next section](replay-titles-and-audio-track-display.md)
<a id="source-emoji-and-color-fonts-for-text-and-multitext"></a> <a id="source-multicam-and-nested-clip-match-frame-improvements"></a> <a id="source-multicam-clips-can-include-all-audio-tracks-for-each-angle"></a> <a id="source-multicam-clips-can-use-full-clip-extents-on-creation-and-during-sync"></a> <a id="source-recent-five-minute-icon"></a> <a id="source-replay-control-to-limit-view-to-the-last-5-minutes"></a> <a id="source-replay-editor-allows-timeline-selection-from-search-dial"></a> <a id="source-replay-now-allows-independent-start-and-end-stingers"></a> <a id="source-replay-title-palette-allows-up-to-six-favorite-titles"></a> <a id="source-show-font-previews-preference"></a> <a id="source-spell-checking-for-all-text-elements"></a> <a id="source-the-font-browser-toolbar"></a>

### The Font Browser Toolbar

- All Fonts: Click this tab to display every font installed on your machine.
- Favorites: Click this tab to display only the fonts you’ve favorited by clicking their star.
- Scale: This slider grows or shrinks the size of the font boxes.
- Thumbnail View: Lays out fonts as a run of square thumbnails.
- List View: Lays out fonts as a run of long rectangles.
- Search Bar: When you know the name, or even a piece of the name, of the font you’re after, you can type it

here so only fonts matching those results come back.

- Light / Dark Mode: Pick light or dark text set against the opposite background.
- Filter: Tick individual classification and weight parameters to narrow fonts to just those types.
- Option Menu: Pick from the following options:

Display Default Text: Shows the “The Quick Brown Fox…” text string within the font windows. Display User Custom Text: Lets you key in your own text to show within the font windows. Reset User Custom Text: Clears any custom text you’ve keyed in.

### Show Font Previews Preference

While the Font Browser lets you weigh a range of fonts in fine detail, now and then you simply want a fast glance at the typefaces before you commit. That’s where the Preview Fonts preference steps in. Switched on by default, Preview Fonts displays an expanded window holding the font name, then the font name again rendered in that very typeface. Pick a font from this window and it drops into the Font Field across a range of text tools. You can switch this behavior off if you like by heading to DaVinci Resolve > Preferences > User > UI Settings and clearing the “Show font previews” box.

Choosing a font with the Show Font Previews preference turned on

### Spell Checking for all Text Elements

As a welcome quality-of-life lift for the spelling-challenged, DaVinci Resolve 21 ships a multi-language text spell checker. Spelling slip-ups get marked red in both the viewer and inspector. Right-click a word to peek at suggested swaps or to ignore the word.

A red underline marks each misspelled word. Right-click one and you’ll get a list of suggested fixes plus the choice to ignore it. A matching preference set also exists for Spell Checking under DaVinci Resolve > Preferences > User > Language and Spelling. The Spelling and Formatting Tool here lets you adjust the spell checker.

- Spelling Check: Tick this box to switch the spell checker on or off across the whole of DaVinci Resolve.
- Ignore Words: Opens a text box where you can feed words into the spell checker’s ignore list.
- Ignore words with numbers: Won’t flag a misspelled word when it contains numbers.
- Ignore words with ALL CAPS: Won’t flag a misspelled word when it’s in all capital letters.

TIP: You can switch off every red underline in the viewer to keep previews clean by choosing View > Show Spelling Errors on Viewer.

### Emoji and Color Fonts for Text+ and MultiText

Emoji support comes to both Text+ and MultiText, handing you the freedom to drop expressive icons and visual accents right inside your text for designs that feel more lively and engaging. Emoji go straight into the text fields with a keystroke: Control-Command-Space on macOS, and Windows key-. (period) on Windows. Beyond that, Text+ and MultiText carry sturdier font support; their handling improves for color fonts, bitmap fonts, and font styles. Where a color font is supported, extra controls for Color Palettes appear in the Text+ inspector under Advanced Controls, and there you can pick display options for the font.

### Multicam Clips can Include All Audio Tracks for Each Angle

When building a Multicam Clip there’s now an option to fold in every audio track from all the various angle source clips into the Multicam Clip. To go this route, set the Multicam Audio dropdown to “All Angles” within the New Multicam Clip dialog box. So if angle A carried four audio tracks while angle B carried five, all nine audio tracks would be on hand inside the Multicam Clip.

### Multicam Clips can Use Full Clip Extents on Creation and During Sync

When building a Multicam Clip there’s now an option to have every angle picked for the multicam clip use its full length (extents) no matter the length of the multicam clip. To go this route, tick “Use full clip extents” in the New Multicam Clip dialog box.

### Multicam and Nested Clip Match Frame Improvements

DaVinci Resolve 21 has further sharpened how match framing behaves with multicam and nested clips. Choose Clip > Match Frame to Source Clip and the underlying source clip for compound clips and multicams is located automatically. Depending on where the UI focus sits, this function operates on either the source or timeline viewer, and it will also drop out of source timeline mode automatically when that mode is active.

### Replay Control to Limit View to the Last 5 Minutes

The Replay Viewer interface gains a new Recent Five Minute button. Press it and only the last five minutes of a growing live file open in the viewer, letting you view, add markers, and so on, to just the newest five minutes of footage. This comes in especially handy when you’re cutting a long live event and need to spot something that just happened without scrubbing through the entire clip in the viewer.

### Recent Five Minute icon

### Replay Editor Allows Timeline Selection from Search Dial

You can now view and pick up to the last ten timelines in the Replay Editor. To do it, just hold the timeline button down and spin the search dial to the timeline you want on the monitor.

Replay timeline selection using Timeline button and the Search Dial.

### Replay now Allows Independent Start and End Stingers

When laying out stingers for Replay, you can now run different stingers for the start and end animations. To do it, just click the link icon to clear it, then drag the animations you want onto the start and end boxes in the interface. To go back to the default of matching start and end stingers, just click the link icon once more. Whatever animation sits in the start box copies automatically into the end box.

Once the Start and End Stinger link is broken (circled red), separate stingers can play on the way in and on the way out

### Replay Title Palette Allows Up to Six Favorite Titles

Within Replay, a six-slot favorite titles palette opens when you pick Show Titles Palette out of the Titles tab option menu. After that, just drag the title template you want into one of the numbered slots below. After that you can fire off that title template by pressing the matching title button on the Replay Editor.
