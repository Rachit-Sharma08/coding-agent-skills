# Adr panel on the Fairlight page and adr interface

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adr automated dialog replacement.
[Chapter index](INDEX.md) / [Next section](adr-session-setup-and-cue-lists.md)
<a id="source-adr-automated-dialog-replacement"></a> <a id="source-adr-automated-dialog-replacement-1"></a> <a id="source-the-adr-interface"></a> <a id="source-the-adr-panel-on-the-fairlight-page"></a> <a id="source-the-list-panel"></a> <a id="source-the-list-panel-of-the-adr-interface"></a> <a id="source-the-record-panel"></a> <a id="source-the-record-panel-of-the-adr-interface"></a> <a id="source-the-setup-panel"></a> <a id="source-the-setup-panel-of-the-adr-interface"></a>

### ADR (Automated Dialog Replacement)

DaVinci Resolve's Fairlight page provides a refined interface for performing ADR, or automated dialog replacement, in an orderly and approachable way. It is both easy to use and capable: the ADR panel brings together Cue list management, industry-standard audio beeps and visual cues, plus thorough take management featuring star ratings and layered take organization, so you can produce and oversee re-recorded dialog for any program. Thanks to that careful organization and layering, stitching the strongest moments from every take back into your program becomes simple.

When you click the ADR button on the Interface toolbar, the Fairlight ADR panel appears, giving you a fully professional automated dialog replacement workflow. For anyone unfamiliar, dialog replacement describes how audio professionals invite actors back to re-record unusable dialog takes within their recording studios, one line after another and with plenty of patience.

### The ADR panel on the Fairlight page

The goal of the Fairlight page is to keep this process orderly and approachable. Though easy to use, it remains capable: Cue list management helps you quickly build out a re-recording plan. Through your BMD video output device, industry-standard audio beeps and visual cues assist the performers in the booth so they hit their cues and deliver their lines on time. After that, thorough take management with star ratings and layered take organization in the Timeline lets you handle the recordings that result and select the strongest moments from each take while editing.

### The ADR Interface

To the left of the Timeline, the ADR interface presents three panels: a List panel, a Record panel, and a Setup panel. Their controls are covered below following the sequence in which you'd normally use them..

### The Setup Panel

True to its name, the Setup panel is the place where you prepare your ADR session.

### The Setup panel of the ADR interface

You'll find these controls in this panel:

- Pre Roll and Post Roll: Sets how many seconds of playback occur before and after the In and Out points you've assigned to each cue, so actors can hear what precedes and follows the cue and get ready. Should you switch on the Beep options further down, those beeps act as a countdown throughout the chosen pre-roll.
- Record Source: Use this dropdown menu to pick which audio input gets recorded, which forms a patch to the Record Track. That said, the menu stays inactive until a track is chosen in the Record Track dropdown menu.
- Record Track: Pick the destination track for your recording here. Choosing it patches the Record Source to the Record Track and flips Record Enable on for you automatically.
- Guide Track: From this dropdown, select the track that holds the production audio you intend to replace. While recording their new performance, the talent listens to the playback from this track as a reference.
- Record File Name: Enter a filename for the audio you record using this text field.
- Character Setup: Here you list the character names you plan to re-record, which streamlines creating and handling cues. Use the Add button to type in a fresh character name. Removing a character is done by selecting its name in the list and then clicking the Remove button.
- Beep to In Point: Switches on a three-beep sequence the talent hears as the recording approaches. So the beeps can be heard, the Beeps channel of the System Generator has to be patched to your audio outputs through Fairlight > Patch Input/Output.
- Beep at In Point: Switches on a single final beep right at the In point. So that beep can be heard, the Beeps channel of the System Generator has to be patched to your audio outputs through Fairlight > Patch Input/Output.
- Count In: Shows an onscreen counter ticking down toward the moment the cue begins.
- Video Streamer: Gives the talent something to watch during pre-roll so they're primed to record. Two vertical lines overlaid on the program sent to video slide toward each other across your video output display throughout the pre-roll leading into the cue. That gives the talent a visual sense of how much time remains before they should speak. As the beeps sound, those lines grow taller. The two lines meet at the Time In frame, where a cross indicates that recording has begun.
- On Screen Cue Text Style: Clicking this heading exposes a group of parameters that let you set the appearance and positioning of onscreen text cues.
- Smart Timeline: With this enabled, the playhead jumps automatically to each cue the moment you select it in the Cue list, and the view zooms to fit that cue's length within the Timeline.
- Mixing Control: Turns on automatic switching of audio playback so you can separately govern what the talent and the audio engineer hear across the various phases of ADR recording. As one example, when this is on, the Guide track won't route to the Control room while the engineer reviews a take.

### The List Panel

This is the spot where you assemble the list of cues that need re-recording, whether you build them directly on the Fairlight page or bring them in from a .csv file.

### The List panel of the ADR interface

Within this panel you'll find the following controls:

- Cue editing controls: Shows the information for whichever cue is currently selected (or one you've only just made). The In and Out timecode fields hold the Timeline In and Out points captured when the cue was made, though you can adjust them by hand for fine tuning. A Character dropdown menu lets you assign that dialog line to a particular character. A text entry field is where you type the dialog cue slated for re-recording, giving both you and the talent a reference.
- New Cue button: Pressing this button drops a new cue into the list, using whatever In and Out points are currently set in the Timeline plus whichever character was selected most recently.
- Cue list: Every cue that has been typed in or imported. You can narrow the Cue list down with the Filter dropdown menu near the top-right of the ADR panel (beside the option menu). You're free to display cues for every character or for whatever mix of characters you pick. You can also opt to conceal every cue flagged as done, enjoying how the list keeps getting shorter the nearer you get to wrapping up.

On top of that, the ADR interface option menu carries three commands tied to the List panel:

- Import Cue List: Allows you to bring in a correctly formatted .csv file so cues prepared in a spreadsheet become usable. The proper layout for cue lists you intend to import uses no headers, one line per cue, and four separate columns holding In timecode, Out timecode, Character Name, and Dialog.
- Export Cue List: Allows you to write the Cue list out to a .csv file, whether for sharing or safe‑keeping.
- Clear Cue List: Wipes every cue from the Cue list. Exporting a backup of your Cue list before erasing it entirely is advised, just in case you ever want to return to a cue.

### The Record Panel

This is the place where you actually carry out the ADR recording session you've prepared, drawing on the dialog cues you loaded into the Cue list.

### The Record panel of the ADR Interface

You'll find these controls in this panel:

- Record and rehearse controls: A set of four transport controls and two buttons gives you command over recording throughout ADR sessions. These remain inactive until you've picked a cue from the Cue list to record.

Rehearse: Plays the portion of the Timeline a cue defines without committing any recording, letting the talent walk through their dialog and rehearse their timing and delivery. No beeps or on-screen streamers occur during a rehearsal. Play: Plays whichever take is currently chosen in the Take list (covered further down). With nothing selected, the newest recording sitting at the top is played. Stop: Halts rehearsal, playback, or recording right away. Record: Begins recording the cue onto the chosen audio track, complete with cue beeps and video streamer cues. Keep Playing: Once a take finishes you might want playback to continue so the talent hears the upcoming part of the track. Hitting the Keep Playing button at any moment, even mid-recording, causes post roll to be skipped and ordinary playback to resume past the cue's Out time. Keep Recording: Once a take finishes you might want recording to continue until you halt it yourself. Hitting the Keep Recording button at any moment, even mid-recording, causes the current cue's Out point to be skipped and recording to carry on until you stop it.

- Take list: The Take list displays every take captured for the active cue, listing the take number, name, and a five-star rating you can assign to track which takes succeeded and which fell short. Older takes sit at the bottom of the list while newer ones rise to the top (matching the order the corresponding layered audio clips occupy in the Timeline track they were recorded onto).
- Cue list: Every cue that has been typed in or imported. You can narrow the Cue list down with the Filter dropdown menu near the top-right of the ADR panel (beside the Option menu). You're free to display cues for every character or for whatever mix of characters you pick. You can also opt to conceal every cue flagged as done, enjoying how the list keeps getting shorter the nearer you get to wrapping up.
- Cue list Done column: A sixth column shows up exclusively in the Record panel, titled Done. It holds check boxes for every cue that you can enable to record which cues you've completed successfully.

On top of that, the ADR interface Option menu carries one command tied to the Record panel:

- Record Early In: Permits recording to happen during pre-roll, useful when you're working with talent who prefer to jump in early.
