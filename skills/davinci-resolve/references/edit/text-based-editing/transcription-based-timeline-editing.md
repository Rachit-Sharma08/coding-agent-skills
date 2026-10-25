# Text based video editing and edit timelines based on source clip transcription

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text based editing.
[Chapter index](INDEX.md) / [Previous section](transcription-silence-speakers-and-export.md) / [Next section](import-and-export-transcriptions-using-srt-files.md)
<a id="source-adding-clips-to-timeline-transcriptions"></a> <a id="source-edit-timelines-based-on-source-clip-transcription"></a> <a id="source-text-based-editing-part-2"></a> <a id="source-text-based-video-editing-studio-version-only"></a>

### Text-Based Video Editing (Studio Version Only)

Following a Transcribe command, DaVinci Resolve now has the precise timecode location of every word in the clip, and that knowledge unlocks several handy text-based editing tools through the Transcription window. Text-based video editing can be used on both the Cut and Edit pages. A link exists between the Transcription window's cursor and the Viewer's playhead. Moving the cursor through the text drives the playhead to the matching spot in the Viewer's clip. That way you can drop the playhead with precision on whatever spot you choose by the text word, instead of scrubbing forward and back across the audio track. To send the playhead to a particular word in the clip:

- Click a word in the Transcript window and a red arrow highlights it. The viewer playhead then leaps straight to the end of that word within the clip in the Viewer. Besides the cursor and playhead being tied together, a clip's In and Out points are likewise tied to whatever text range you select in the Transcription window.

To set an In and Out range in the clip:

- Drag across the text in the Transcription window to tint it teal. The clip's In point lands just ahead of the first word, and its Out point lands just past the last word in the highlighted text.

To set a sentence's In and Out range:

- Click any word in the sentence and hit the X key, which selects the full sentence and shades it teal.

Highlighting a span of text in the Transcription window (R) sets In and Out points for that span automatically on the Viewer's clip (L). With an In and Out range in place, the Transcription window's editing tools let you perform a handful of everyday editing and media management chores. The Create Subclip and Add Marker tools in the Transcription window To make a fresh subclip out of a selected range: 1 In the Transcription window, drag to highlight a span of text in teal. 2 Hit the Create Subclip icon at the lower left of the Transcription window. 3 Within the Create Subclip window, type a name for the subclip and click the Create button. To put a marker on a clip: 1 For a standard marker, pick a single word in the Transcription window (red arrow); for a duration marker, drag to highlight a span of text in teal. 2 Click the Marker icon sitting at the Transcription window's lower left. Within the Transcription window, the Place on Top, Insert, and Append Edit icons To cut an In and Out range into the current timeline: 1 In the Transcription window, drag to highlight a span of text in teal. 2 Click one of the Edit icons at the lower right of the Transcription window. Place on Top: Drops the chosen edit range onto a track above whichever one is currently active in the timeline. Insert Edit: Slots the chosen edit range into the timeline at the timeline In point. Append: Tacks the chosen edit range onto the timeline's end.

### Edit Timelines Based on Source Clip Transcription

The transcription you produced from the original source clip can afterward be used to alter that same clip on the timeline. Switching to this mode in the Transcription window lets you pick, cut, and paste text and then push those edits through to the timeline. For Timeline mode to work in the Transcription window, the timeline clips have to be transcribed back in the Media Pool. You enter Timeline Transcription mode by clicking the Timeline icon at the top left of the Transcription window.

The Timeline Transcription Mode icon, located at the upper right of the Transcription window Once Timeline Transcription mode is active, the window's text editing tools become usable and the edits you make appear on the timeline too. As an example, in the clip below we chose a sentence within the Transcription window, and as shown, that sentence's In and Out points were set automatically in the Timeline sitting behind it.

Choosing a sentence in the Transcription window establishes the matching In and Out points on the timeline. Once the text is selected, you can manipulate that selection with the usual Cut, Copy, Paste, and Delete tools and have those edits reflected on the timeline. The example below has us slicing one sentence out of a clip and relocating it to an earlier place in the timeline.

Choosing the second clip's first sentence, then right-clicking and applying the Cut tool Here the sentence has been excised from the timeline and swapped for silence (…) inside the Transcription window.

Next we fix the new In point on the timeline by choosing the first clip's opening sentence fragment within the Transcription window. We then right-click and select the Paste command.

The footage of the sentence we removed gets pasted into that location and now leads off the Transcription window.

Now we target the timeline gap left behind where the sentence was first cut, selecting the (…) silence in the Transcription window. Then right-click and pick Delete.

The finished timeline, sentence relocated and gap closed. Achieved entirely by working the text inside the Transcription window.

### Adding Clips to Timeline Transcriptions

You're free to keep dropping un-transcribed clips into the timeline as you edit. Whenever an un‑transcribed clip turns up, the Transcription window labels it "Transcription Pending"; in that situation just choose "Transcribe Missing Clips in Timeline" from the Option menu to kick off the transcription of every missing clip.

If you drop a clip that hasn’t been transcribed onto the timeline, the Transcription window marks it Transcription Pending
