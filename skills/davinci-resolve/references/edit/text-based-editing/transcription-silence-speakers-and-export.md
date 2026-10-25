# Transcription silence speakers and export

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text based editing.
[Chapter index](INDEX.md) / [Previous section](audio-transcription-and-transcribe-audio.md) / [Next section](transcription-based-timeline-editing.md)
<a id="source-audio-transcription-supported-languages"></a> <a id="source-detect-speakers-during-transcription-studio-version-only"></a> <a id="source-export-audio-transcriptions-with-speaker-and-timecode-information-studio-version-only"></a> <a id="source-intelliscript-for-creating-timelines-from-scripts-studio-version-only"></a> <a id="source-transcription-and-speaker-detection-in-timelines"></a> <a id="source-understanding-silence--in-the-transcription-window"></a>

### Understanding Silence (…) in the Transcription Window

For the majority of shots, a sizable stretch of the audio clip carries no spoken dialog whatsoever. The Transcription window flags these quiet stretches with ellipses (…). Locating where the talking happens matters, but so does spotting where it doesn't. Within the Transcription window these silences (…) behave much like words do, so you're free to delete them and leave them out of any editing operation. Imagine, for instance, a lengthy interview broken up by repeated gaps between questions. One way would be to chop that long clip apart by hand, dropping In and Out points and isolating each question and answer individually. Yet if you run Audio Transcription, delete every silence (…) in the Transcription window, and then edit that span into the Timeline, you'd immediately end up with a string of separate clips containing nothing but the questions and the answers. That way the program drops in all the pertinent clips for you in one move, sparing you the tedious scrubbing and edit-point placement for each single portion of the clip in the Viewer.

Shown here are the original Interview clip (Tracks V1, A1 violet) plus the identical media after every silence was stripped via the Transcription window (Tracks V2, A2). Observe how it splits on its own into separate question and answer clips.

Stripping silences inside the Transcript window proves handy both when exporting a transcript and during text based editing, which is why a dedicated tool exists to clear them all at once.

To delete all the silences (…) in the Transcription window:

- Click the Remove Silent Portions icon sitting immediately to the left of the Font Controls,

in the Transcription window.

- Click the Option menu (three dots) at the top right of the Transcription window, then

select Remove Silent Portions from the contextual menu.

- Highlight the range you intend to use in the transcription window.
- Cut the range into the timeline by clicking one of the editing icons at the lower right of the

transcription window.

### Detect Speakers During Transcription (Studio Version Only)

While transcribing a clip, DaVinci Resolve is now able to recognize separate speakers, presenting each speaker's individual timecode span alongside their text. Aside from yielding richer text transcription exports, speaker detection can serve as a reference for text based editing. Because Speaker Detection operates per project, once you switch it on it stays active for every later transcription job, whether on clips or timelines.

Switching on Speaker Detection from a clip's context menu. To Enable Speaker Detection for Transcriptions:

- Right-click a clip or timeline, then choose AI Tools > Audio Transcription >

Speaker Detection.

- Or select Speaker Detection from the Transcription window's Option menu.
- Click on the Transcribe option to start the operation.

### Transcription and Speaker Detection in Timelines

There's also the option to Transcribe and Detect Speakers for a timeline. Doing so examines the timeline and transcribes the media underneath. It then hands you a timeline transcription drawn from the In and Out points of each timeline clip and tags every segment with a speaker. Timeline Transcriptions are opened in Timeline Transcription mode, as described below.

The Transcription window shown with Display Speakers active. To rename a speaker, double-click the name and type a replacement into the text field. Once Speaker Detection is on, every following audio transcription you produce for clips and timelines will identify the separate speakers. The project keeps all of a speaker's voice signatures stored across multiple clips. Should you return the following day to bring more audio clips into your project, DaVinci Resolve recalls the voices it analyzed earlier and tags them to the correct speaker on its own. To clear the stored speakers from your project, choose Reset Speaker Data from the Transcription window's Option menu. Inside the Transcription window, speakers start out labeled by number (Speaker 1, 2, 3 etc.). Renaming a speaker is done by double-clicking the speaker name and typing a fresh name into the text field. Every other appearance of that speaker updates to the new name. When Speaker Detection misjudges who's talking, you can hand-reassign a passage of text to a different speaker: select the text, right-click it, and pick the Assign To icon from the pop-up menu. A second dialog box then opens so you can shift the attribution to any of the other detected speakers.

Reassigning a speaker by hand is done by right-clicking the text and choosing the Assign To icon.

Should you want to conceal the speakers once more to tidy up the Transcription Window, you can switch their display on or off through the Transcription window's Option menu under Display Speakers. Flipping this setting leaves intact whatever speaker associations have already been made.

### Export Audio Transcriptions with Speaker and Timecode Information (Studio Version Only)

When you export a transcription in DaVinci Resolve Studio, the text file you get back carries the speaker name plus timecode details for every speech block. Having that information makes searching through and moving around transcriptions far simpler.

Transcripts include speaker and timecode information for dialog blocks.

### Audio Transcription Supported Languages

The language used to build the transcription is chosen in the Project Settings > Subtitle and Transcription> Transcription Setup section. Pick any of the supported language models, or leave it set to Auto and let DaVinci Resolve work out who's saying what. At the time of writing, Audio Transcription and Text-Based Editing handle these languages:

- English, French, German, Dutch, Danish, Swedish, Norwegian, Italian, Spanish, Portuguese, Russian, Japanese, Korean, and Mandarin (Simplified Traditional).
- A great many additional languages can be obtained through the Extended AI Transcription Support Package found in the Extras Downloads Manager. Among them: Arabic, Afrikaans, Armenian, Azerbaijani, Belarusian, Bulgarian, Bosnian, Croatian, Catalan, Czech, Finnish, Estonian, Galician, Greek, Hindi, Hebrew, Hungarian, Indonesian, Icelandic, Kazakh, Kannada, Lithuanian, Latvian, Malay, Macedonian, Maori, Marathi, Nepali, Polish, Persian, Romanian, Slovak, Serbian, Slovenian, Swahili, Tamil, Tagalog, Turkish, Thai, Urdu, Ukrainian, Vietnamese, and Welsh.

### IntelliScript for Creating Timelines from Scripts (Studio Version Only)

In DaVinci Resolve 20, the capable AI-driven IntelliScript tool taps the Transcription Engine to align an original script and build a timeline from it. The feature lets you rapidly put together rough cuts of scenes and even sorts multiple takes for you within the timeline. IntelliScript grasps context well enough that if your performer improvises with a comparable phrase rather than the precise wording in the script, it should locate it anyway.

A simple text file script to feed into IntelliScript To put IntelliScript to work building a timeline from a script: 1 Build a script file as plain text (.txt) holding only the spoken words. IntelliScript wants nothing but the bare spoken text with full stops (.) closing each sentence. Conventional script formatting — scene descriptions, parentheticals, character names — is apt to trip up transcription. 2 Highlight every clip you mean to feed IntelliScript, right-click, and pick AI Tools > Create New Timeline Using IntelliScript. 3 At that point DaVinci Resolve asks you to load the text script file. Press Open. After the transcription finishes, IntelliScript builds a fresh timeline and, on track one, arranges the strongest clips in sequence according to the dialog in the script file. Alternate takes land on extra tracks generated for them, switched off by default. With the timeline assembled, you can examine the top take on track one and audition alternate takes across particular regions, turning them on and off as you go.

The IntelliScript results in the timeline. Strongest takes go on track one, alternates onto separate tracks, all of them off by default. Here, at the very end, we overrode its picks and manually switched on the take we judged best. NOTE: IntelliScript settles on the "best" take purely by matching spoken dialog. It draws on no good take metadata and bases its decisions on nothing beyond dialog matching.
