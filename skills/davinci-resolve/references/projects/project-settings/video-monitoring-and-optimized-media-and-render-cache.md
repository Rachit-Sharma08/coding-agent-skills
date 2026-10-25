# Video monitoring and optimized media and render cache

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](project-settings-editing.md) / [Next section](blackmagic-cloud-and-project-media-location.md)
<a id="source-frame-interpolation"></a> <a id="source-optimized-media-and-render-cache"></a> <a id="source-project-settings-part-2"></a> <a id="source-video-monitoring"></a> <a id="source-working-folders"></a>

### Video Monitoring

The settings in this group steer the signal sent out by the video output interface attached to your workstation, letting you state which signal standard goes out and along which signal path. Out of the box, the frame size and frame rate echo whatever sits in the Timeline resolution and Playback frame rate options. Should you need to, though, you can shift these settings to match the external display you monitor on. For instance, if your files are 2K bound for 2K output yet you grade on a high definition monitor set to 1080, you can pick the right HD standard for that monitor without touching the Timeline Resolution settings.

- Video Resolution: Picks a standard video frame size for output through the video output interface you've connected.
- Format: Picks a standard video frame rate sent out across the video output interface you've connected.
- Video connection checkboxes: Sets which signal standard travels from your connected video output interface over to the video monitor. Be sure the standard you pick is one both your video interface and your monitor handle.

Here are the options: Use 1080PsF: Puts progressive video out as 1080i so older HDTV sets can take it. Use 4:4:4 SDI: A signal path for feeding image data to monitors that handle 4:4:4 chroma sampling, usually across SDI connections. Use Level A for 3Gb SDI output: A signal path that carries image data over one 3 Gb/s SDI connection. Use dual outputs on SDI output: Every DaVinci Resolve system can build a side-by-side display deliverable to a Stereoscopic monitor through the HD-SDI output of an UltraStudio 4K or DeckLink card. With dual SDI 3D monitoring switched on, each eye goes out separately at full resolution. While in this mode, split-screen wipes and cursors stay hidden on the grading monitor.

- SDI Configuration: Picks between Single Link, Dual Link, and Quad Link SDI according to what your display can take.
- Data Levels: Only the data levels leaving the video interface that links the DaVinci Resolve workstation to your external display are touched by this setting. It does nothing to the data DaVinci Resolve handles internally, nor to the files written when you render on the Deliver page. The option you pick in DaVinci Resolve absolutely has to match the data range your external display is set to. Otherwise the video signal will look wrong, even while the internal data keeps being processed correctly by DaVinci Resolve.

Two options exist: Video: This is the right pick when your broadcast display is set to the Rec. 709 video standard. Full: Use this option when your monitor or projector can show "full range" video signals and you want to monitor the entire 10-bit data range (0–1023) as you work. For more on data levels, turn to Chapter 9, "Data Levels, Color Management, and ACES."

- Retain sub-black and super-white data: Switch this checkbox on and DaVinci Resolve sends the undershoots (sub-black) and overshoots (super-white) that live within the headroom of video encoded data levels out to video. Switch it off and those out-of-bounds values get clipped in the video output.
- Video bit depth: Pick the bit depth that suits what your display can handle. The choice is between 8-bit and 10-bit. Monitoring at 10-bit taxes the processor more, but it's the better pick for avoiding the look of banding that may not actually exist in the image data DaVinci Resolve is processing.
- Monitor scaling: Sits at basic by default and only kicks in to soften the edges of video shown on a projector across very large screens. These settings cut down high frequency artifacts that might otherwise appear. The effect can also show when you've got a 2K or HD project but you're monitoring on an SD monitor. Its other option, Bilinear, treats the monitored image differently depending on your display device, so you may want to confirm it suits your setup.
- Use Rec601 Matrix for 4:2:2 SDI output: Leave this checkbox alone unless its purpose is already clear to you. You know who you are.
- Enable HDR metadata: (only available in Studio version) Tick this checkbox to output the metadata needed for High Dynamic Range signals to travel over HDMI 2.0a and be decoded properly by an HDR-aware video display. With this checkbox on, it's advisable to switch on the "HDR mastering is for X nits" checkbox on the Color Management page as well, and dial the "nit" level (slang for cd/m2) to whatever peak luminance your HDMI-connected HDR display can reach.

### Optimized Media and Render Cache

The resolution and codec of the optimized media DaVinci Resolve can build for stronger real time performance are set by these settings, along with the cached media produced by the Smart and User Cache.

- Proxy media resolution: Through a drop-down list, you decide whether proxy media is built at each clip's Original size, at Half, Quarter, One-Eighth, or One-Sixteenth of the original media's resolution, or whether DaVinci Resolve picks this for you automatically from your timeline settings.
- Proxy media format: Names the format the proxy media files get written in. A range of Uncompressed, ProRes, and DNxHD formats is open to you, per your needs.
- Optimized media resolution: A drop-down list is where you decide whether optimized media is built at each clip's Original size, at Half, Quarter, One-Eighth, or One-Sixteenth of the original media's resolution, or whether DaVinci Resolve picks it automatically from your timeline settings.
- Optimized media format: Names the format the optimized media files get written in. Pick from a range of Uncompressed, ProRes, and DNxHD formats, per your needs.
- Render cache format: Names the format the render cache files get written in. A range of Uncompressed, ProRes, and DNxHD formats is available, per your needs.
- Enable background caching after X seconds: Sets the stretch of idle time after which automatic background caching kicks off. A row of checkboxes lets you push particular effect types into the cache when you run the User Cache, a more selective form of caching than the Smart Cache. Among them: Automatically cache transitions in user mode: When you're in User mode and find your workstation can't play transition effects in real time, you can compel these effect categories into the Sequence Cache so they're cached while you use the User mode of caching.

Automatically cache composites in user mode: When you're in User mode and find your workstation can't play composite mode or opacity effects in real time, you can compel these effect categories into the Sequence Cache so they're cached while you use the User mode of caching. Automatically cache Fusion effects in user mode: When you've built effects for a clip on the Fusion page and find your workstation can't play that clip in real time, you can compel these effect categories into the Sequence Cache so they're cached while you use the User mode of caching.

### Working Folders

Which folders receive cache and gallery files is what these fields let you set.

- Project media location: Lets you pick a particular folder on your system to house every piece of generated media made for that project. Generated media covers things like fresh audio files born of the Voiceover tool and Voice Convert, or really any new media DaVinci Resolve itself creates. This keeps all of a project's media gathered in one shared spot, which eases handing off, moving, or relinking media instead of leaving some inside DaVinci Resolve's internal file structure and some out on a media drive. DaVinci Resolve spins up new subfolders at your chosen media location by media type on its own, which makes shipping some or all generated media elsewhere easy. This location can also be assigned in the Create New Project dialog as you set up a new project.

Within the project media location, DaVinci Resolve builds subfolders by itself to keep any media generated inside the program organized.

- Proxy generation location: Every proxy media file you produce is written to the directory path this field names.
- Cache files location: Every render cache file you make is stored at the directory path this field names. By default that path points to a hidden "CacheClip" directory created at the spot of the first Media Storage Volume you designate in the DaVinci Resolve Preferences window.
- Gallery stills location: By default each still you save is written in the DPX format and dropped at the directory path this field names. By default that path points to a hidden ".gallery" directory created at the spot of the first Media Storage Volume you designate in the DaVinci Resolve Preferences window.

NOTE: Should the volume you've chosen for the cache go offline, DaVinci Resolve raises a warning dialog.

### Frame Interpolation

The default behavior of every retiming and speed change effect, mixed frame rate timeline clips included, is decided by these settings.

- Retime Process: From this drop-down menu you set a default way of handling clips that don't line up with the project frame rate in mixed frame rate timelines, plus clips carrying speed effects (fast forward or slow motion), across the whole project. Because every clip in every timeline starts at "Project Settings," altering this setting changes how most mixed frame rate and speed-affected clips are handled, apart from those given custom settings.

Three options exist: Nearest: The least sophisticated yet most processor-efficient approach; frames get dropped for fast motion or duplicated for slow motion. Frame Blend: Likewise easy on the processor but capable of smoother output; neighboring duplicated frames are dissolved into each other to even out slow or fast motion effects. When Optical Flow throws up unwanted artifacts, this option can do better. Optical Flow: The most processor intensive yet highest quality way of handling speed effects. Through motion estimation, fresh frames are built from the original source frames to make slow or fast motion effects. When a clip's motion runs linear, the outcome can be remarkably smooth. Two elements crossing in opposite directions, or erratic camera movement, can however bring on unwanted artifacts.

- Motion estimation mode: Whether you're running mixed frame rate clips in a timeline with Optical Flow retiming on, leaning on Optical Flow to handle speed change effects, or working the Image Stabilization or Temporal Noise Reduction controls on the Color page, the Master Settings' Motion Estimation dropdown (over in the Project Settings window) hands you options that balance speed against quality.

The “Motion estimation mode” drop-down, found in the Master Settings panel of the Project Settings, exposes extra “Enhanced” Optical Flow choices. Carried over unchanged from earlier DaVinci Resolve releases, the “Standard Faster” and “Standard Better” entries place lighter demand on the processor while still delivering quality good enough for the majority of jobs. By contrast, the “Enhanced Faster” and “Enhanced Better” entries tend to outperform the standard pair almost any time those exhibit artifacts, though they ask more of the system and therefore run slower on typical hardware. For top-tier slow-motion work driven by the DaVinci Neural Engine, reach for “Speed Warp Faster” and “Speed Warp Better.” How well this performs depends on what the clip contains, but under favorable conditions it produces cleaner, higher-fidelity output with fewer artifacts than even the Enhanced Better choice.

- Motion range: For timelines set to Optical Flow retiming that include clips of mixed frame rates, or whenever Optical Flow drives speed-change effects, this drop-down sets the default magnitude — small, medium or large motion — applied across every speed and motion

related computation, letting you tune the outcome to suit the kind of movement present in your source footage. You may also adjust this per clip from the Edit page Inspector.

Newly upgraded Motion estimation mode controls within the Project Settings’ Master Settings panel
