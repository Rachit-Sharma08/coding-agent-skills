# Capture and playout

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](color-and-dynamics-profile.md) / [Next section](general-audio-sample-rate.md)
<a id="source-capture"></a> <a id="source-fairlight"></a> <a id="source-fusion"></a> <a id="source-playout"></a> <a id="source-subtitles-and-transcription"></a>

### Capture

These settings come into play while you use the Capture mode on the Media page to capture clips off tape into the Media Pool.

- Capture: Lets you settle on capturing both Video and Audio, or Video Only.
- Video Format: The format scanned film frames are saved as. When capturing from tape, the

choices on offer are DPX and QuickTime. While capturing from the Cintel film scanner, this is held to Cintel Raw Image (CRI); that's a raw data format which DaVinci Resolve debayers on its own into a Cineon log-encoded image ready for grading.

- Codec: The codec applied while writing captured media. Capturing off tape, the choices span the assorted Apple ProRes variants, plus 8- and 10-bit YUV 422, then 10-bit RGB, together with the assorted DNxHD variants. Cintel Raw Image files default to rgb.
- Save in folder path: A row of checkboxes lets you spell out what additional information to draw on for the directory hierarchy that will hold the captured media. Each checkbox you turn on adds another directory whose name comes from that checkbox's metadata. You can pick any or all of these: Program name, Clip number, Reel number, and Roll/Card.
- Apply reel number to: Lets you settle on how the reel name gets written. Two checkboxes let you write the reel number into the file's name and/or into the Header data.
- Use prefix: A field lets you type a prefix to use within the media file's name. This lets you tack on text identification that makes the media easier to spot and search for.
- Apply prefix to: A pair of checkboxes let you choose to apply whatever prefix you entered within the file name and/ or within the folder name.
- Use frame number with: While capturing to image sequences, you can settle on how many digits to use while writing the frame number into each frame file's name.
- Set batch ingest handles to: While capturing to image sequences off a batch list, defines how many frames of extra handles to ingest alongside each logged clip.
- Input: Lets you settle on how many tracks of audio to capture, from 2 to 16.

### Playout

These settings shape only the video signal output while you use the Edit to Tape mode of the Deliver page.

- Output: Lets you settle on outputting both Video and Audio, Video Only, or Audio Only when you're doing an audio layback.
- Output Source Timecode: Switch this checkbox on to output each clip's own source timecode. This option applies solely while assemble editing to tape.
- Output LTC: With a Blackmagic Design DeckLink or UltraStudio device on HD-SDI, longitudinal timecode (LTC) rides on track 16 of the HD-SDI video signal, making it simple to use a Mini Converter de-embedder to pull this analog timecode audio signal off and feed it straight into a recording device. That's especially handy when you've got outboard video processing gear such as a noise reducer or format converter that passes the VITC timecode through.
- Delay LTC by x frames: When you send LTC out so it bypasses outboard processing hardware (a noise reducer or format converter, say), you're able to make up for the processing delay by pushing the timecode back by some frames, ensuring the processed image and its timecode land at the deck at the same moment. With a DVS card there's a separate timecode output.
- Offset audio by x frames: Lets you set an offset between the audio track and video to land proper A/V sync in cases where outboard processing hardware is delaying the video.
- Output x channels of audio: Pick how many audio tracks to output to tape.
- Set batch playout head handle to x seconds: While batch outputting multiple clips, you can spell out a number of frames ahead of each clip's In point to be output as well.
- Set batch playout tail handle to x seconds: While batch outputting multiple clips, you can spell out a number of frames past each clip's Out point to be output as well.

### Subtitles and Transcription

The Subtitles panel lets you tune presets governing subtitles being built within subtitle tracks of the timeline.

- Max Character Per Line: Defaults to 60. Lets you settle on the largest number of characters permitted on a single line within a subtitle.
- Minimum Caption Duration: Defaults to 3 seconds. Lets you settle on the shortest duration permitted for subtitles in the timeline.
- Maximum Characters Per Second: Defaults to 30. Automatically works out the largest allowable characters per second from a subtitle clip's duration.

The Transcription setup panel lets you pick the language DaVinci Resolve relies on to analyze audio clips for transcription. Language: Pick one of the supported languages here. Picking Auto lets DaVinci Resolve study the audio clip and settle on the language being spoken.

### Fusion

Fusion permits consistent frame numbering across all compositions, trimmed clips included. What this means is that any composition built in Fusion can begin from the same start frame number. In new projects you can alter the default start frame for Fusion compositions within the project settings.

- Legacy Fusion Composition Frame Count: Pins the Fusion composition at zero frames to the first frame of the composition's source media.
- Default Start Frame: Lets you type a default frame number to begin your fusion comps in this project on.

This aids Visual FX workflows three ways:

- Matching existing keyframes to the right frame offsets—while swapping in an asset whose

frame offsets don't line up (for instance a sub clip, a differing format or round trip, or VFX connect workflows where the handles fail to match).

- Rendering to specific frame ranges—when conforming to the delivery standards of commercial workflows (for instance, having compositions begin at sequence frame 1000).
- Consistent Referenced Comp behavior—indispensable while applying a referenced composition to different clips with different trims.
- Downscale to Timeline Resolution for Timeline Clip Compositions: To lift playback performance on complex fusion projects, you can tick this box to automatically downscale all media to the timeline resolution ahead of fusion operations running. This does not work with .exr media however.

### Fairlight

Through the Fairlight panel you can establish the audio sample rate for your project, as well as configure a range of audio-specific tools found on the Fairlight page.
