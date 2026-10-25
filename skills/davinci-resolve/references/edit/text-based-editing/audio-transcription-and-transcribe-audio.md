# Audio transcription and transcribe audio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text based editing.
[Chapter index](INDEX.md) / [Next section](transcription-silence-speakers-and-export.md)
<a id="source-audio-transcription-of-timelines"></a> <a id="source-audio-transcription-studio-version-only"></a> <a id="source-editing-text"></a> <a id="source-editing-text-in-the-transcription-window"></a> <a id="source-selecting-text"></a> <a id="source-text-based-editing"></a> <a id="source-text-based-editing-part-1"></a> <a id="source-the-transcribing-audio-window"></a> <a id="source-the-transcription-window"></a> <a id="source-transcribe-audio"></a>

### Text Based Editing

Improvements in Machine Learning now let you sort, trim, and polish clips by examining the dialog that's spoken and turning that speech into written text. This chapter walks through how DaVinici Resolve's Text Based Editing toolset is used.

### Audio Transcription (Studio Version Only)

Knowing what was actually said in a clip is among the most valuable pieces of metadata you can have. A complete transcript of a take helps on narrative projects by letting you locate particular clips from script dialog, yet it matters even more on unscripted documentary and news shoots — both for grasping which parts of the story made it to camera and for assorted organizational, creative, and legal needs. Not long ago, producing a transcript meant a person sat listening to a clip at normal speed and typed the spoken words into a log sheet by hand. Thanks to progress in the DaVinci Resolve Neural Engine, that monotonous transcription chore is now handled by your computer for each clip, done automatically and — what counts most — with precision. On top of that, attaching text transcripts to your project's clips unlocks fresh text-based editing capabilities for choosing, finding, and dropping clips onto your timeline.

### Transcribe Audio

Reachable from the Media Pool on the Media, Cut, Edit, and Fairlight pages, the Transcribe Audio feature runs entirely on its own.

The Transcribe Audio icon in the Media and Edit pages To have a clip's audio transcribed automatically: 1. In the Media Pool, pick one or more clips that contain audio you wish to transcribe. 2. Right-click any clip you've selected and choose AI Tools > Audio Transcription > Transcribe from the contextual menu. As an alternative, click the Transcribe Audio icon on the Media Pool toolbar.

### The Transcribing Audio window

Now the Transcribing Audio window opens, telling you the count of clips still awaiting analysis, how fast the analysis is running compared to real time, and roughly the remaining time before the chosen clips finish. A button lets you abort the process whenever you like.

The speech balloon icon showing that a clip has been transcribed Whenever a clip carries a transcription, a tiny speech balloon icon shows up at the bottom left of that clip's thumbnail within the Media Pool. To strip a transcription off a clip: 1 In the Media Pool, choose the clip whose transcription you intend to remove. 2 Right-click the chosen clips and pick AI Tools > Audio Transcription > Clear Transcription from the contextual menu.

### Audio Transcription of Timelines

Beyond clips, Audio Transcription functions for timelines too, operating exactly as outlined earlier. Putting a timeline into text form serves a number of real-world legal and organizational purposes. That said, when your goal is producing subtitles or captions for the Timeline, a purpose-built tool exists just for that. To read up on the Create Subtitles from Audio feature, turn to Chapter 52, "Subtitles and Closed Captioning."

### The Transcription Window

Holding the displayed text together with its timecode, options, and editing tools is the job of the Transcription window. To keep things convenient, you can drag the Transcription window anywhere across the GUI, including onto a second display.

The Trascription window with several clips displayed and the Search pane open. Yellow marks the text that was searched for. Teal marks the clip's In and Out range, while a red triangle points out where the playhead currently sits in the Viewer. To open the Transcription window:

- Right-click any transcribed clip or clips, then choose Transcribe Audio from the contextual menu. You can instead click the Transcribe Audio icon found on the Media Pool toolbar.

Here are the sections and tools the Transcription window contains: Export: Pressing this icon opens a file browser in which you can store a .txt file holding the transcription results so other programs can read them. Search: Pressing this icon brings up a Search and Replace dialog that lets you track down particular words or phrases throughout every selected clip in the Clips panel. Matching words turn yellow. Partial-word search and replace is supported within the Transcription window as well. To adjust how the search behaves, open the search bar and choose either Contains or Full Word from the drop-down menu on the left.

Partial-word searches are also possible inside the Transcription window when you pick the Contains option.

Options Menu: Brings up the Transcription window options. Speaker Detection: Switching this on analyzes a particular voice and gives it a speaker number. That speaker is then retained across every clip in a project. Display Speakers: Toggles the Speaker column on or off within the Transcription window. Transcribe Missing Clips in Timeline: When the timeline holds clips not yet run through speech to text (transcription pending), choosing this option transcribes them and slots them correctly into the Transcription window. Remove Silent Portions: Clears every silence (…) the Transcription window has detected. Create Subtitles from Audio (Timeline only): Builds a fresh Subtitle track and lays subtitles down for you. To read up on the Create Subtitles from Audio feature, consult Chapter 52, "Subtitles and Closed Captioning." Import Subtitles (Clip only): Lets you bring in a subtitle saved as .srt format (covered further on in this chapter). Export Subtitles: Lets you send out your subtitles as .srt format (covered further on in this chapter). Reset Speaker Data: Wipes every stored speaker detection record from the project. Clips: This pane displays each selected clip whose transcription you elected to view. Clicking a thumbnail brings that clip's transcription into the Transcript window. An orange outline marks the active clip. Should you have picked only a single clip, this pane is hidden. Transcript: Shows the transcription text. This box also serves to position the playhead and to fix a clip's in and out points, as covered in the Text Based Editing section below. Remove Silent Portions: Clears every detected silence (…) from the transcript. Text View Controls: Lets you govern the font size along with the high contrast settings of the text inside the Transcript window.

Create Subclip: Produces a new subclip of the shot from the In and Out points that the highlight in the Transcript window establishes. Marker: Drops a marker at the word position highlighted in red; should an In/Out range be highlighted instead, it lays down a duration marker spanning that range. Stop: Halts playback of the clip within the Viewer. Play: Runs the clip forward at realtime in the Viewer. Play in to Out: Plays forward only across the set In and Out range.

Place on Top: Carries out a Place on Top edit of the chosen range into the timeline. Insert: Carries out an Insert edit of the chosen range into the timeline. Append: Carries out an Append edit of the chosen range onto the end of the timeline.

### Editing Text in the Transcription Window

Some of what gets transcribed from a clip's audio isn't helpful or desired in the finished transcription. You can strip out crew chatter, blown lines, and lengthy pauses, and you can also correct slip-ups that the Audio Transcription process itself produced.

### Selecting Text

Before you can edit any text, it has to be selected within the Transcription window. Several approaches exist, varying with how much text you intend to grab. To pick out one particular word in the transcription: Double-click that word, which selects it and turns it teal. To grab a span of transcription text: Drag across the text you wish to edit, selecting it and tinting it teal. To capture a whole sentence in the transcription: Click any word in the sentence and hit the X key, selecting the entire sentence and shading it teal. To grab a full paragraph in the transcription: Triple-click any word in the paragraph, selecting the whole paragraph and coloring it teal. To select the transcription's entire text: Hit Command-A, which selects all the text and highlights it teal. To clear the all-text selection in the transcription: Press Option-X to drop the selection of all the text and highlight it in teal.

### Editing Text

With any text selected (highlighted in teal), a right-click on it surfaces the editing choices. The action runs the moment you click one of the editing tools.

Right-clicking any selected text surfaces these editing tools of the Transcription window (l-r): Edit, Delete, Undelete, Copy, and Assign To.

Edit: Choosing this tool opens a text field in which you can make minor corrections to the selected text. It's good for fixing wrong words, spelling errors, and tidying up proper names in the transcription. Drastically rewriting the text — say, swapping a full paragraph for a two- or three-word summary — produces erratic results when used for editing. The action can be undone. Delete: Unlike a word processor, this tool doesn't erase the selected text from the Transcription window; rather, it tags the text orange with a strike-through. Text marked that way stays out of the exported transcript and won't have its range placed into the Timeline by any edit operation. As a result, a cut shows up in the Timeline at the spot where the deleted text range sits in the transcript. Because every word is still present in the audio clip exactly as recorded, it's often clearer to regard this as an "exclude" operation instead of a true deletion. Undelete: Picking this tool undoes a prior deletion. It restores the orange strike-through text to normal text, lets it back into the exported transcription, and brings its range back in for editing. Copy: Duplicates the selected range so it can be used in other applications. The Transcription window has no Paste command. Assign To: When the automatic speaker detection has misidentified who spoke a line, you can hand-assign it to another speaker by choosing one from the drop-down menu.
