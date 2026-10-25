# Fade in and out to playhead and creating crossfades with overlapping fades

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](audio-clip-layering-and-audio-compound-clips.md) / [Next section](exporting-audio-clips-to-external-files.md)
<a id="source-changing-clip-color-in-the-timeline"></a> <a id="source-creating-crossfades-with-overlapping-fades"></a> <a id="source-editing-audio-clips-in-external-editors"></a> <a id="source-fade-in-and-out-to-playhead"></a> <a id="source-finding-clips-in-the-media-pool"></a> <a id="source-the-resulting-crossfade"></a> <a id="source-the-resulting-crossfade-1"></a> <a id="source-using-crossfades-from-the-edit-page"></a>

### Fade In and Out to Playhead

In the Trim menu sit two commands: park the playhead over a clip, and from where it sits you can call “Fade In to Playhead” or “Fade Out to Playhead.” Both the Edit and Fairlight pages support these.

(Left) Parking the playhead at the spot where a fade in should finish, (Right) Calling Fade In to Playhead

### Creating Crossfades With Overlapping Fades

Where a fade eases a single track of audio up or down, a crossfade eases two overlapping clips at once — one clip up and another down — for the aural equivalent of a cross dissolve. Two ways of building a crossfade exist in the Fairlight page right now. Both lean on clip layering so you can hold overlapping fades over overlapping clips. Here is how to build a crossfade by overlapping two clips: 1 Put a fade out on the end of one clip and a fade in on the start of another. Every fade added this way is linear by default, though you can reset them to whatever gain you like.

Adding fades to adjacent clips 2 Drag the first clip so it overlaps the second by the length of the fade you’ve built.

Dragging the clips into overlap; clip layering keeps the overlapping parts intact 3 Drop the clip. Clip layering keeps both overlapping fades intact, and a crossfade turns up in the Timeline.

### The resulting crossfade

Here is how to build a crossfade over two clips already layered: Drag the fader handle sitting at either the start or end of a layered clip, and a crossfade turns up on its own.

Creating a crossfade by adjusting the fader handle of a layered clip

### Using Crossfades From the Edit Page

You can add crossfades in the Edit page too, but they show in the Fairlight page as transitions in the Edit page style.

### The resulting crossfade

### Finding Clips in the Media Pool

On any clip in the Timeline, a right-click plus Find in Media Pool picks that clip out in the Media Pool for you — handy for times you’d like to cut another copy of it elsewhere in the Timeline, or work a different segment of it back into the same spot. NOTE: Automation Follows Edit whenever clips bearing embedded automation get moved or pasted out of the Timeline. Pull those same automation-bearing clips from the Media Pool instead and they show up in their default state, no automation attached.

### Changing Clip Color in the Timeline

With one or more clips selected in the Timeline, a right-click lets you recolor them and stay better organized. You might, for instance, set production audio clips holding dialog from different actors to different colors, or set clips with dialog, music, and effects to different colors so each clip’s purpose stands out at a glance.

### Editing Audio Clips in External Editors

While you’re working in the Fairlight page, you can process an audio file through a third-party application when needed — for those times you must lean on another application’s strengths to build an effect or fix an issue the Fairlight page can’t handle on its own. Setting this up starts with adding one or more applications to the External Audio Process list, which lives in the Audio Plugins panel of the System Preferences.

The External Audio Process list configured to send audio to Adobe Audition Here is how to add an external audio process: 1 In the DaVinci Preferences, open the System tab and pick the Audio Plugins panel. 2 Within the “Setup External Audio Processes” section, click the Add button. 3 Want a different name for the audio process? Double-click in the Name column and key one in. 4 In the new process’s empty Path column, double-click, then from the dialog pick an application to bind to that process. 5 From the dropdown menu in the Type column, settle on the kind of process you want it to be. With one or more external audio applications set up in Preferences, any clip in the Fairlight page can run through them: right-click the audio clip, then off the contextual menu’s External Audio Process submenu pick whichever application you want. Doing so makes a duplicate of that clip’s media, copied (bounced) into the directory spelled out by the “Save clips to” field within the Capture and Playback panel of the Project Settings. The external application then either opens or fires off as a command-line command — which one depends on how that external application was set up in Preferences. As soon as the bounced audio opens in the external application, process it however you need, then commit the changes by saving/rendering/outputting and overwriting the original copied audio media file. Changes don’t go unnoticed; DaVinci Resolve picks them up and reimports the altered result automatically as one more audio layer over the original clip in the Timeline. How an audio application is set up in the DaVinci System Preferences dictates how the bounced audio file gets handed to the external program. Three choices exist:

- Command Line: As a command line parameter, when your audio application can be run from the Terminal.
- Clipboard: By dropping the path to the bounced file on the clipboard, so you can paste it into the application that’s been launched automatically, or bring it in via a File > Open dialog.
- Reveal: By revealing the bounced copy in your workstation’s file manager, so you can drag and drop it onto the application that’s been launched automatically.
