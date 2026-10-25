# Data burn in metadata and custom output options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Metadata burn in.
[Chapter index](INDEX.md) / [Previous section](data-burn-in-and-data-burn-in-window.md) / [Next section](metadata-burn-in-prefixes.md)
<a id="source-custom-output-options"></a> <a id="source-data-burn-in-metadata"></a> <a id="source-gang-rendered-text-styles"></a>

### Data Burn-In Metadata

Running down the far-left column of the Data Burn-In window is a roster of every option you can lay onto the video output as a window burn. A checkbox beside each option toggles it on or off. The Option drop-down also lets you decide whether the item name prints as a prefix ahead of the burn-in data. NOTE: When a pair of clips overlaps on the Timeline, the metadata shown in the window burn belongs to whichever clip is currently visible in the Viewer.

- Record Timecode: Timecode measured against the Timeline, configured under the Conform Options section within the General Options panel of the Project Settings.
- Record Frame Number: How many frames sit between this point and the Timeline’s opening frame.
- Source Timecode: The individual timecode belonging to each clip.
- Source Frame Number: How many frames sit between this point and the clip’s opening frame.
- Record TC & Frame Num: A single line holding both metadata options together.
- Source TC & Frame Num: A single line holding both metadata options together.
- Source & Record TC: A single line holding both metadata options together.
- Feet + Frames 35mm: Shows a Feet + Frames translation of the program’s record timecode,

worked out for 35mm film.

- Feet + Frames 16mm: Shows a Feet + Frames translation of the program’s record timecode,

worked out for 16mm film.

- Audio Timecode: The timecode belonging to the clip’s audio track.
- Keycode: Sometimes called edge-code, these are the identification codes printed along the edge of film stocks, supplying a fixed reference that maps which digital frames line up with which film frames.
- Source File Name: The complete file path — file name included — of the media file tied to the present clip.
- Record File Name: Whatever file name is set within the Render Settings list over on the Deliver page.
- Source Clip Name: The media file’s file name that’s tied to the present clip,

minus the file path.

- Synced Audio File Name: The file name belonging to the audio clip synced against this clip.
- Synced Audio Timecode: The timecode belonging to the audio clip synced against this clip.
- Custom Text1: A line of text you key into the Text field within the Custom Output parameters.

Whatever characters you wish are fair game. As you edit any of the three custom text fields on offer, you can drop in “metadata variables” — graphical tags you add to surface clip metadata. As an example, dropping in the matching metadata variable tags %scene*%shot*%take makes the custom text read “12_A_3” when the metadata happens to be “scene 12,” “shot A,” “take 3.” For a deeper look at using variables, along with the full roster of variables that DaVinci Resolve provides, see Chapter 16, “Using Variables and Keywords.”

- Custom Text2: A second line of text open to customization.
- Custom Text3: A third line of text open to customization.
- Logo1: Lets you lay a graphic over the picture at a position you choose. Among the

graphics formats it accepts are PNG, TGA, TIF, BMP, and JPG. For transparency within logos, alpha channels work too.

- Logo2: Lets you lay a second graphic over the picture.
- Logo3: Lets you lay a third graphic over the picture.
- Reel Name: Whatever reel number is presently assigned to the current clip.
- Shot: Shot metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Scene: Scene metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Take: Take metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Angle: Angle metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Day: Day metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Date: Date metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Good Take: Maps to Good Take metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Camera: Maps to the Camera metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Roll/Card: Maps to the Roll/Card metadata, should a camera have written it to the file, or should it have been keyed into the Metadata Editor over on the Media page.
- Clip Flags: Sends out whatever colored flags are attached to the clip.
- Clip Color: Sends out whatever color is attached to the clip.

### Custom Output Options

Using the parameters within the Custom Output panel, you can adjust the appearance, placement, and at times the content, of the chosen metadata item. Each metadata item carries its own adjustable Pan and Tilt.

- Display During First x frames: Switching this checkbox on lets you set a frame count over which the present metadata item shows before it dissolves out across one second. Once enabled, the present metadata item cuts on screen as each fresh clip starts, holds on screen for the span you set, and then dissolves away.
- Display During Last x frames: Switching this checkbox on lets you set a frame count, just ahead of every clip’s end, across which the present metadata item shows up on screen after fading in over one second, then cuts away as the clip ends.
- Font: Starts out as Courier, though you may pick any font present on your system.
- Size: Starts out at 48, though you may pick standard increments from 6 to 72.
- Alignment: Starts out as Center. Left is the sole alternative.
- Font (color): Starts out white, though a spread of predefined colors is available from this drop-down menu.
- Background: Starts out black, though the visible color shifts with the Opacity setting. For a louder look, a spread of predefined colors is available from this drop-down menu.
- Text Opacity: Starts out at 1.00. Lets you set how transparent the burned-in metadata’s text is.
- Background Opacity: Starts out at 1.00. Lets you set how transparent the burned-in metadata’s background color is.
- X-Y Position: Lets you shift the present metadata item’s horizontal and vertical placement. By default the horizontal value lands at the frame’s center, measured against the current project’s frame size. That first metadata item sits centered vertically close to the frame’s bottom, just over Action Safe. Each later metadata item you enable drops in automatically above the earlier metadata item, no matter its sequence within the “Add to Video Output” list.
- Text: (shown only when one of the Custom Text options carries a check) A text field where you key in custom text to appear as one of three available custom text items.
- Logo: (only if one of the Logo options is checked) A field showing the file path of whichever graphic is presently selected for display as one of the three available Logo graphics. The graphics formats it accepts include PNG, TGA, TIF, BMP, and JPG. For transparency within logos, alpha channels are supported as well.
- Import File button: (only when one of the Logo options carries a check) Lets you pick a graphics file to serve as a logo.

### Gang Rendered Text Styles

Whether each metadata item can be styled on its own hinges on whether the Gang Render Text Styles option carries a check within the Data Burn-In window’s Option menu. Switched on, every text metadata item shares one font, size, color, background, justification, and opacity. Switched off, each metadata item may carry its own settings.
