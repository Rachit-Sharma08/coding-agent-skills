# Tiktok deliver page preset and presentations preset

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](presets-for-fast-rendering-and-render-presets-selection.md) / [Next section](h-264-master-and-h-265-master.md)
<a id="source-deliver-and-upload-to-social-media"></a> <a id="source-dropbox-or-dropbox-replay-720p1080p2160p"></a> <a id="source-presentations-preset"></a> <a id="source-prores-master"></a> <a id="source-review-before-upload"></a> <a id="source-setting-up-video-sharing-uploads"></a> <a id="source-tiktok-deliver-page-preset"></a> <a id="source-waiting-for-your-movie-to-upload"></a>

### TikTok Deliver Page Preset

A dropdown offers two separate resolutions you can render to and picks the right settings for exporting your program as a file ready to be uploaded to TikTok plus many additional video file sharing services. The preset outputs one clip and applies the parameters below:

- Resolution: 1920x1080 HD
- Use Vertical Resolution: Unchecked. Tick this box when you wish to deliver your video in portrait

mode for proper display on phones. This should be on for TikTok.

- Frame rate: The frame rate you picked for your timeline. This too can be overridden so you set another

frame rate manually.

- Format: MP4
- Video Codec: H.264
- Encoding Profile: Auto
- Audio: Bus 1
- Audio Codec: AAC
- Data burn-in: Same as Project
- Use Proxy Media: Points your final render at the proxy media in lieu of the original source camera

files. Worth it where a fast result beats a high-quality one.

- Upload directly to TikTok: Tick this and the completed render heads automatically up

to your TikTok account, after which the parameters listed next appear. Title: Enter the title of your video. Visible To: Here you pick who is permitted to watch this video. The choices are Private, Public, and Friends. Allow comments: Ticking this box permits commenting on your TikTok video. Clearing this box blocks comments on your video. Allow Duet: Ticking this box lets your video appear side-by-side with another creator's video in TikTok through the Duet function. Allow Stitch: Ticking this box lets your video be trimmed and joined with another creator's video in TikTok through the Stitch function.

### Presentations Preset

This setting gives you a way to flag and format timelines for use with Presentations in Blackmagic Cloud. In contrast to the other presets, it offers no codec settings at all. The setting merely attaches whatever metadata Presentations needs in order to share your timeline. A Presentation must already exist in Blackmagic Cloud before this setting becomes usable.

- File Name: Pick which timeline name gets sent up to Presentations.
- Upload To: Pick which existing Blackmagic Cloud Presentation receives the upload.
- Use Proxy Media: Treat the Proxy Media as what feeds the compression and the push up to

Blackmagic Cloud in place of the original media.

### Dropbox or Dropbox Replay 720p/1080p/2160p

A dropdown offers three separate resolutions you can render to and picks the right settings for exporting your program as a file ready to be uploaded to Dropbox plus many additional video file sharing services. The preset outputs one clip at the timeline’s frame rate and applies the parameters below:

- Format: MP4
- Video Codec: H.264
- Encoding Profile: Auto
- Audio: Bus 1
- Audio Codec: AAC
- Data burn-in: Same as Project
- Use Proxy Media: Substitutes the proxy media into your final render instead of the original source camera

files. A good trade when getting it done fast beats top quality.

- Upload directly to Dropbox: Tick this and the completed render automatically goes

upload to your Dropbox account.

### Setting Up Video Sharing Uploads

DaVinci Resolve carries account integration with YouTube, Vimeo, TikTok, Dropbox, and Frame.io, letting you render and push files straight to each one. There's an Internet Accounts panel within the System tab of the DaVinci Resolve Preferences that lets you log into your YouTube, Vimeo, Dropbox, and Frame.io accounts and also name a local cache location for media being kept in sync with Frame.io. Every service you log into brings up a floating window holding the interface where you supply your login name and password to switch on integration, then complete any two-factor identification and the remaining required steps. After you've entered them, DaVinci Resolve logs into each of these services on its own whenever DaVinci Resolve launches. Every service you log into also surfaces the service’s upload parameters inside the Custom Export Video settings on the Deliver page. That way you can build your own custom file settings able to override the usual formats permitted by the service presets, while still enjoying the all-in-one convenience of uploading and description entry that the preset provides.

Inside the DaVinci Resolve Preferences window, the Internet Accounts panel sits under its System tab NOTE: With Frame.io, the local cache location holds clips you bring into a DaVinci Resolve project from the Frame.io volume within the Media Storage panel of the Media page.

### Deliver and Upload to Social Media

After arranging YouTube, Vimeo, TikTok or Dropbox access within the System Preferences, over in the Internet Accounts panel, you'll find the YouTube, Vimeo, and Dropbox presets reveal an “Upload directly to YouTube/Vimeo/TikTok/Dropbox” checkbox that decides whether the rendered output is uploaded automatically. Pick the export options you want, then press the Add to Render Queue button so this job joins the Render Queue just like any other export. As soon as that job finishes rendering, it moves on by itself to upload to the chosen video sharing service, and an upload percentage indicator shows up in the job listing reporting the progress of this upload. Because this upload runs in the background, you're free to keep doing other tasks in DaVinci Resolve as the file uploads. To check how much longer the upload needs from any other page, pick Workspace > Background Activity and open the Background Activity window.

### Waiting for your movie to upload

After the upload completes, you're able to watch the file right on the social media site through a web browser by right-clicking the job in the Render Queue and choosing Reveal in Browser.

### Review Before Upload

To add one more layer of quality control before your video goes out live across the internet, you can pick Review Before Upload from the Render Queue option menu. Choosing this halts the automatic upload sequence once the file has finished rendering and shows a message, “Waiting for Upload.” At that point you can right-click the job in the Render Queue and pick Reveal in Finder to open and review your video. After you've reached a decision, from that same menu you can pick either Upload to (service name) to release your video, or Cancel Upload if you've reconsidered.

### ProRes Master

Use this for rapidly outputting ProRes Master files covering an entire program. Once chosen, it defaults to single clip mode rendering, the Format becomes QuickTime, the Codec becomes Apple ProRes, and the Type becomes Apple ProRes 422 HQ. For audio the Codec defaults to Linear PCM with the Bit Depth at 16.
