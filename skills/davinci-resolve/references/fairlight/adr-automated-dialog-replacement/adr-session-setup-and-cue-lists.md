# Setting up to record an adr session and creating and importing adr cue lists

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adr automated dialog replacement.
[Chapter index](INDEX.md) / [Previous section](adr-panel-on-the-fairlight-page-and-adr-interface.md)
<a id="source-ai-create-adr-cues-studio-version-only"></a> <a id="source-create-adr-cues"></a> <a id="source-create-adr-cues-with-speakers"></a> <a id="source-creating-and-importing-adr-cue-lists"></a> <a id="source-importing-cues"></a> <a id="source-manually-creating-an-adr-cue-list"></a> <a id="source-new-adr-cues"></a> <a id="source-recording-adr-to-the-timeline"></a> <a id="source-setting-up-to-record-an-adr-session"></a> <a id="source-timeline-clip-contextual-menu-for-creating-adr-cues"></a>

### Setting up to Record an ADR Session

Preparing to record ADR is uncomplicated though it involves several steps. Creating tracks in preparation to record ADR: 1 Within the Timeline, add a new audio track that will receive your ADR recording. Confirm its channel configuration suits your recording (mono is the usual choice for dialog). 2 When recording ADR onto your main timeline, consider applying Solo to the Record track as well as the Guide track; that way, you and the talent stay focused on the audio being re-recorded instead of hearing every other track in the present mix. You're now set to configure the Setup panel. Configuring the Setup panel: 1 Launch the ADR interface, then open the Setup panel. 2 Pick the Pre Roll and Post Roll values you want, measured in seconds. Allowing a pre roll of at least 3 seconds is suggested to give the talent room to prepare. 3 In the Record Source dropdown menu, select the microphone you patched earlier. 4 In the Record Track dropdown menu, select the Record track you built. 5 In the Guide Track dropdown menu, select the track carrying the original production audio you're swapping out. 6 Down at the foot of this panel, enable whichever Preroll Cue options you and the talent want active as each cue is recorded. The choices include: a) Beep to In Point and Beep at In Point deliver an audible count down toward when performing should start. b) An animated Video Streamer counts down to the start time, indicates the length of the cue being recorded, and additionally puts the dialog text for that cue on screen for the actor, letting them keep their gaze on the screen instead of a script. After that, if you've turned on Beep to In Point and Beep at In Point, the Fairlight oscillator must be patched to your output channels so the talent can hear the preview beeps.

Patching the Oscillator to play beeps over your audio output: 1 Select Fairlight > Patch Input/Output to bring up the Patch Input/Output window. 2 Pick System Generator in the Source dropdown menu, then click to highlight Beeps. 3 Pick Audio Outputs in the Destination dropdown, and select the left/right outputs through which you want these preview beeps to play. Dragging a bounding box lets you pick several outputs at once, which links the mono Beeps input to a stereo output for easier listening. 4 Click Patch to establish the connection, then dismiss the Patch Input/Output window.

### Creating and Importing ADR Cue Lists

To use the ADR interface correctly you need a list of cues ready. You can build a Cue list to record from in two ways: assemble one from the ground up on the Fairlight page, or import one. Both approaches are supported by the ADR panel.

### AI Create ADR Cues (Studio Version Only)

AI Create ADR Cues belongs to DaVinci Resolve's Intellicut feature set, which bundles two additional features as well: Remove Silence and AI Checkerboard to New Tracks. To learn more about Remove Silence and AI Checkerboard to New Tracks, refer to Chapter 175, “Editing Basics in the Fairlight Page.” There's a long-running joke that ADR isn't truly automatic. Even so, this feature examines and transcribes a chosen group of timeline clips on a track and then builds individual ADR cues on its own, offering the two output choices described below.

### Timeline clip contextual menu for creating ADR cues

NOTE: The dialogue has to be spoken in one of the languages supported under the Project Settings at Subtitles and Transcriptions > Language. To learn more about the Subtitles and Transcription settings, refer to Chapter 6, “Project Settings.” ADR cues are produced in whichever language is chosen in the Project Settings beneath Subtitles and Transcriptions. By default the choice is “Auto,” which carries your computer's operating-system language setting across to every project. Yet if, say, you deliberately pick English as the project language and then build ADR cues for dialog delivered in French, the cues you end up with will be in English.

### Create ADR Cues

When you right-click a chosen group of timeline clips on a track and pick AI Tools > Create ADR Cues from the contextual menu, the Transcribing Audio dialog appears and tracks how the analysis and transcription are progressing. After the dialog goes away, the transcribed cues land on the List page within the ADR panel, accompanied by their Cue ID, Time In/Out, and Durations.

### New ADR cues

### Create ADR Cues with Speakers

When you right-click the timeline clip selection and choose AI Tools > Create ADR Cues with Speakers from the contextual menu, the transcribed cues are added to the List page just as described above, with each Speaker's name appearing in the Character column.

New ADR cues with speaker names added to the Character column

### Manually Creating an ADR Cue List

If all your dialog editing has happened inside DaVinci Resolve, you can simply build a list by marking the Timeline sections you need to re-record and generating cues from those timings. For cues to come out right, begin by entering, in the Setup panel, the name of every character you'll make a cue for. Having those names makes entering cues easier and helps you filter and sort the list down the line as needed. To add character names before entering cues: 1 Within the ADR interface, bring up its Setup panel. 2 Click Add New. 3 As soon as a highlighted entry shows up in the Character Setup list, type a name. 4 Hit Return when finished. To edit the Character Setup list, do one of the following:

- Should you mis-spell a name, double-click any name in the list to revise it.
- To remove a name, select it and click Remove to drop it. After you've built a full roster of character names, you can start assembling your Cue list.

To manually add cues to the Cue list: 1 Within the ADR interface, bring up its List panel. Every control for creating and editing cues lives here. 2 Within the Timeline, place In and Out points to mark the dialog section you want to make into a cue. Those timecode values appear inside the List panel's Cue Editing section. 3 Use New Cue to drop a blank cue into the Cue list. 4 Over in the Cue Editing section, pick the character who speaks that cue from the Character dropdown (only names already entered in the Setup tab show up in this list). 5 If needed, click the text field below and type the dialog requiring re-recording. 6 Repeat steps 2 through 5 until every cue you mean to re-record has been built. To revise any cue, just click to select it and edit it within the Cue Editing section above.

### Importing Cues

When you or an assistant has already assembled a Cue list inside a spreadsheet, with its own columns for character names, dialog, plus In/Out timecode values, a Cue list can also be produced by pulling that data in from an exported .csv file. To bring a .csv file into the Cue list: 1 From the ADR option menu, choose Import Cue List; then, through the dialog, navigate to the .csv file holding the Cue list you received, and click Open. 2 An ADR Setup dialog opens, presenting the .csv file's data previewed as a set of columns. This lets you check whether every column of incoming data is mapped correctly. If it isn't, you can reassign each incoming data column to its proper column in the ADR panel. The proper layout for Cue lists you intend to import is no header text, with information entered one row per cue across four separate columns holding In timecode, Out timecode, Character Name, and Dialog. Should any of these columns be swapped around, fix it by picking the right data type for each column from the dropdown menus up top.

Dialog for rearranging columns of cue data, if necessary 3 Press Import CSV. At that point the cues ought to appear within the Cue list.

To export a .csv file from the Cue list: Pick Export Cue List from the ADR option menu, choose a place to save the file, and click Save.

### Recording ADR to the Timeline

After you've set up your workstation for recording and prepared a Cue list to work from, it's time to begin capturing each cue. To capture one of the cues you've assembled: 1 Within the ADR interface, bring up its Record panel. 2 To record a specific character's cues, you can click each character you don't need in the ADR Option menu to uncheck it, which hides that character's dialog in the Cue list. 3 With the list displaying the character cues you want, pick the cue you'd like to begin recording. That cue holds the timecode that determines which portion of the Timeline gets recorded to, and the playhead shifts on its own to that part of the Timeline. 4 Click the Rehearse button a couple of times to walk through the cue alongside the talent. Clicking Rehearse plays both the audio and video tied to that cue, including pre roll and post roll, together with every beep and onscreen cue. 5 When the talent is set to attempt a take, click the Record button and let the Fairlight page handle playing through pre roll with beep notifications and visual streamer cues, starting the recording, and then halting it automatically once the cue ends. To capture another take, just click the Record button once more. Each completed recording adds a take to the Take list. Several recordings produce several takes in the list. Within the Timeline, every new take shows up as layered audio, so you can record as many takes as you wish into the very same stretch of the Timeline. After you've wrapped up recording takes, you'll hold a tidy stack of alternate takes to pull from while editing the strongest moments of each recording together. 6 Should you or the talent want to hear a given take again, select it in the Take list and click Play. The 5-star ratings control lets you track how much you liked each take. 7 When you've finished recording a cue, click the Done checkbox beside it and pick the next cue you intend to record. Once you're done re-recording dialog, simply close the ADR interface.
