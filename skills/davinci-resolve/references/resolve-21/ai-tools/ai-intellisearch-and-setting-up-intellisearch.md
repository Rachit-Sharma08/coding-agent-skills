# Ai intellisearch and setting up intellisearch

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Next section](speech-generator-custom-voices-and-voice-convert.md)
<a id="source-ai-intellisearch"></a> <a id="source-ai-speech-generator"></a> <a id="source-ai-tools"></a> <a id="source-ai-tools-part-1"></a> <a id="source-analyzing-media-in-intellisearch"></a> <a id="source-choose-faster-or-better-mode-for-intellisearch"></a> <a id="source-downloading-the-intellisearch-models"></a> <a id="source-face-gallery"></a> <a id="source-intellisearch-ai-model-packages-for-download"></a> <a id="source-selecting-the-intellisearch-mode"></a> <a id="source-setting-up-intellisearch"></a> <a id="source-the-intellisearch-toolbar"></a> <a id="source-the-speech-generator-tool"></a> <a id="source-using-ai-speech-generator"></a> <a id="source-using-intellisearch"></a>

### AI Tools

### AI IntelliSearch

DaVinci Resolve 21 brings a capable new media organization tool named IntelliSearch. Leaning on AI technology, IntelliSearch delivers a thorough, near-instant media search for people and objects. The payoff in finding precisely the media you’re after, faster, is genuine and immediate. For all those moments when you wondered “where was that clip of …?” you can now simply ask DaVinci Resolve and it will track it down for you.

### Setting up IntelliSearch

Being an AI-driven operation, IntelliSearch needs an AI model downloaded from the Extras Download Manager. With that installed, you then have to analyze the media in your media pool before you can use IntelliSearch from the search bar in the Media Pool.

### Downloading the IntelliSearch Models

The IntelliSearch models can be grabbed from DaVinci Resolve > Extras Download Manager. Two models exist, one for the Faster Mode and one for the Better Mode. You’re free to grab one or both, but your available modes will be capped by whichever packages you’ve installed.

### IntelliSearch AI model packages for download

### Selecting the IntelliSearch Mode

To start, you’ll have to settle on whether you want IntelliSearch running in Faster or Better mode. What you’re trading off is processing time against the size of the model download. Once analysis wraps up, both models run equally quickly. Better can take a good deal longer to analyze your clips, but it returns more accurate results. You might begin by running a Faster analysis, then come back for a Better mode pass once your workstation is sitting more idle. The pick between Faster and Better lives in the Media Pool three-dot option menu, under IntelliSearch Mode.

### Choose Faster or Better mode for IntelliSearch

### Analyzing Media in IntelliSearch

With your model chosen, the IntelliSearch analysis still has to be run on your Media Pool clips, and that happens from the AI Clip Analysis tool. From this single spot you can selectively turn the various AI analysis models loose on your Media Pool clips for the whole spread of AI-driven features in DaVinci Resolve. By default the tool works through every clip in the Media Pool, yet the drop-down menu off to the right lets you confine it to only the selected clips. The AI Clip Analysis Icon in the Media Pool To set the IntelliSearch Analysis going, check that the toggle switch next to Analyze for IntelliSearch is on. An optional checkbox named Identify Faces is also there; switch it on and IntelliSearch can pick out individual humans. From there you can feed their names in as search criteria within the Manage Faces window of the IntelliSearch interface.

(Left) Confirm the toggle beside Analyze for IntelliSearch is switched on, (Right) The AI Clip Analysis progress bar Then simply hit the Analyze button and let your computer work through the analysis. A progress window pops up to give you a rough idea of when the process will wrap up. Once done, clips that got analyzed will carry the AI Analysis icon in their thumbnail, so at a glance you can tell which clips are already processed.

This icon appears after a clip has been analyzed for IntelliSearch

### Using IntelliSearch

You reach IntelliSearch just by clicking the search icon (magnifying glass) in the Media Pool. Doing so opens a search bar plus the toolset around it.

### The IntelliSearch toolbar

Search Parameters: Choose which flavor of search analysis to apply to your search terms. Search All: Hands back results drawn from every kind of AI analysis plus any metadata you entered. Search Visual Only: Hands back results drawn solely from the image analysis. This Visual search lets you hunt for objects and other things present in the scene. Search Transcript Only: Hands back results drawn solely from the audio transcript. This Transcription search confines the hunt to transcribed audio, handy when you’re after exact phrases. Metadata Search: Hands back results drawn from any, or all, of the metadata fields. This Metadata search lets you filter on keywords and other metadata (custom metadata included) along with clip properties. The mode also gives you a dropdown menu to scan every field, or narrow it to file name, timecode, and other metadata fields. Search Field: Here you type whatever you’re after, and it can be just about anything, an object, a person, a color, a camera number, even a line of dialog. Add as SmartBin: Hitting this icon opens the Create Smart Bin tool with the parameters you picked already loaded into the Smart Bin criteria. That lets you spin up a lasting Smart Bin holding your search results. Show Face Gallery: Brings up a thumbnail view of every human face that got detected. Click a thumbnail to see every shot featuring that human, or narrow a search result down to that human. Manage Faces: Opens the Manage Faces tool, which lets you label and curate the various faces detected. Search In: Lets you decide where the hunt runs, All Bins: Combs through every bin in the project. Selected Bins: Combs only through bins you’ve selected. Display: Decide how results show up (for Search All, Visual only, and Transcript only). Full Clips: Hands back the whole clip as a match, a yellow line flagging where the search term applies. Hover the thumbnail, then Press “X” to set an in-out range off that yellow line. Segments: Hands back only the matching stretch where the search term applies, in effect turning it into a subclip.

### Face Gallery

Click the Show Face Gallery icon over in the IntelliSearch bar and a thumbnail view of every human face spotted in your clips opens. Click a face and the search results narrow to just that human. As an example, you can click a face labeled “Chloe,” shown as a face thumbnail, then type “red dress” into the search bar. The search results then come back showing only images of Chloe in a red dress and none of the other actresses. By default the Face Gallery, with the woman’s face picked, shows only clips she appears in. Should you want to pin a name onto the face, head over to the Manage Faces tool. There you can label the faces by clicking beneath the face thumbnail and typing the name into the field. That name now becomes metadata attached to that face under the People field.

The Manage Faces tool; typing a name beneath the thumbnail pins it onto a face.

If Face Detection got something wrong, you can also patch that up in the Manage Faces tool. An automated process runs when you press the Improve Faces Grouping Result button, which will ask you to confirm who it reckons that person is. You can likewise assign a face by hand simply by right-clicking the thumbnail, picking “Not XXX,” and reassigning it to a different face from the dropdown menu.

The Improve Faces Grouping Result tool offers an automated yes / no interface for confirming faces.

Right-clicking on a thumbnail lets you reassign the face manually.

### AI Speech Generator

Speech Generator turns written text into high-quality spoken-word output, so you can build your own natural-sounding VO or narration for a project, drawing on a range of voices and performances you tailor to the edit. Timeline > AI Tools > Speech Generator Downloading the Speech Generator Model Since it’s an AI-driven tool, the Speech Generator Model has to be downloaded ahead of use. You can grab the Speech Generator model from DaVinci Resolve > Extras Download Manager.

### Using AI Speech Generator

Fire up the AI Speech Generator by heading to Timeline > AI Tools > Speech Generator. Next, type the text you’d like generated into the Text Input field. Speech Generator works best with shorter sentences or paragraphs. Feed it text that runs too long and the generated voice can wander into odd territory after a while. So keep it brief, or where you’ve got a big chunk of text, split it into smaller pieces. Then settle on the Voice Model you want reading your text. Four built-in voices are licensed for use, or you can craft your own custom voice as described below. You can shape the voice by tweaking the parameters in the settings section. Lastly you can name the generated audio clip’s file and decide which audio track the clip drops into. Press the Generate button and the Speech Generator processes and builds a new audio clip from your input, dropping it into your Media Pool.

### The Speech Generator tool

- Speech Input: This section feeds in the text and settles which voice will read it. Text Input: Enter, in this spot, the words you’d like the Speech Generator to voice. Briefer sentences and paragraphs fare better. Punctuation does shape the timing of the reading. Periods (full stops) make longer pauses, commas shorter ones. A carriage return may stretch a pause that follows a period. Voice Model: Pick a voice model to read your text from the dropdown list. Choosing Custom opens a file requester to load an audio file holding the voice you’d like to use (see Creating a Custom Voice below).
- Settings: These settings govern the voice’s modulation and performance. Speed: Tunes how fast the reading goes. Variation: Governs how much the reading’s prosody (the rhythm and intonation of speech) and emotion vary, with 0 staying closest to the prosody of the reference voice source.

Pitch: Governs how high or low the voice sits. Positive values push it higher, negative ones lower. Generation ID: Picture this number as a performance or take. Each number stands for a different reading carrying its own prosody. Choosing the very same number hands you the very same performance, so it comes in handy when you want to try other variations yet hold onto the same prosody, emotional emphasis included. Randomize: Tick this box to draw a random number for the Generation ID.

- File Name: The label given to the new Speech Generator audio file. A default label is provided, with a numeric suffix tacked on automatically. In its place you can type your own label for the front of the string. Speech Generator audio files land in the DaVinci Resolve Media location you’ve designated, filed under their project name.
- Insert into Timeline: Ticking this box drops the reading in at the playhead spot on your timeline automatically.
- Audio Track: Pick which audio track on your timeline the reading lands on.
