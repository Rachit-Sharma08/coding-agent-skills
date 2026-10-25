# Presets for fast rendering and render presets selection

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Next section](tiktok-deliver-page-preset-and-presentations-preset.md)
<a id="source-custom"></a> <a id="source-render-presets-selection"></a> <a id="source-rendering-media"></a> <a id="source-rendering-media-part-1"></a> <a id="source-social-media-presets"></a> <a id="source-using-presets-for-fast-rendering"></a> <a id="source-vimeo-720p1080p2160p"></a> <a id="source-youtube-720p1080p1440p2160p"></a>

### Rendering Media

Here you'll find the controls offered for delivering files. The procedure is straightforward: pick the format along with the rest of the settings that govern how media gets rendered, mark out a span of clips within whichever session is active, then submit a job carrying those settings into the Render Queue. As many separate render jobs as you wish can be lined up, and each one may carry its own formats, output choices, and clip spans according to your goal. After everything is set, just press the Start Render button.

### Using Presets for Fast Rendering

At the head of the Render Settings list sits a collection of presets covering most of the everyday rendering workflows you're likely to tackle. Should you prefer to build your own configuration instead, pick custom. Every preset arranges the parameters required and disables any settings irrelevant to rendering that particular kind of media.

### Render presets selection

### Custom

Selecting custom leaves nothing pre-configured, and every standard media rendering option stays accessible apart from any tied specifically to individual presets. The settings and options you require must be picked by hand. All Render settings are stored on a per‑project basis.

### Social Media Presets

With these presets you can render media tailored to video sharing services, and they give you the choice of automatically uploading the resulting files.

### YouTube 720p/1080p/1440p/2160p

A dropdown offers four separate resolutions you can render to and picks the right settings for exporting your program as a file ready to be uploaded to YouTube plus many additional video file sharing services. The preset outputs one clip at the timeline’s frame rate and applies the parameters below:

- Format: MP4
- Video Codec: H.264
- Encoding Profile: High
- Audio: Main 1
- Audio Codec: AAC
- Data burn-in: Same as Project
- Normalize Audio: Ticking here brings the clip’s audio level up to the standard YouTube expects.
- Use Proxy Media: Has your final render draw on the proxy media in place of the original source camera

files. Handy when speed matters more than quality.

- Render without Timecode: For those running particular mobile-device editing apps that struggle

with timecode, ticking here makes the render omit it.

- Upload directly to YouTube: With this ticked, the completed render goes automatically up to your YouTube account, and the parameters described below then unlock. Where your account holds several YouTube Channels, you may decide which channel takes the upload.

Title: Type in the heading for your clip. Description: Supply a write-up describing the clip. Chapters from Markers: Enabling this drops chapter markers into the YouTube video lined up with both the marker color you chose and the spot the marker occupies on the Timeline. Upload Thumbnail: Enabling this brings up a file browser where a still image can be chosen to act as the thumbnail shown for your clip on YouTube. Visibility: This is where you set how accessible the clip is on YouTube. Category: This is where the clip’s YouTube category gets assigned.

### Vimeo 720p/1080p/2160p

A dropdown offers three separate resolutions you can render to and picks the right settings for exporting your program as a file ready to be uploaded to Vimeo plus many additional video file sharing services. The preset outputs one clip at the timeline’s frame rate and applies the parameters below:

- Format: MP4
- Video Codec: H.264
- Encoding Profile: Auto
- Audio: Bus 1
- Audio Codec: AAC
- Data burn-in: Same as Project
- Use Proxy Media: Draws on the proxy media for your final render rather than the original source camera

files. Helpful where quick turnaround outweighs quality.

- Upload directly to Vimeo: Tick this and the completed render goes automatically up

to your Vimeo account, with the parameters described below then unlocking. Title: Type in the heading for your clip. Description: Supply a write-up describing the clip. Visible To: Set how accessible the clip is on Vimeo here, password protection among the choices.
