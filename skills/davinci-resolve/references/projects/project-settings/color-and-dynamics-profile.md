# Color and dynamics profile

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](display-lut-and-raw-image-data.md) / [Next section](capture-and-playout.md)
<a id="source-camera-raw"></a> <a id="source-capture-and-playback"></a> <a id="source-color"></a> <a id="source-deck-settings"></a> <a id="source-dynamics-profile"></a> <a id="source-versions"></a>

### Color

These settings shape clip versions and timeline behavior while you work on the Color page.

- Automatically label gallery stills using: Once turned on, DaVinci Resolve auto-builds labels for every gallery still you grab, drawing on the controls below:

Naming drop-down: Lets you settle on what name new stills should carry. Among the choices you'll find Clip Name, then Clip Version Name, plus Source Timecode, alongside Timeline Timecode, as well as Timeline Name, together with Display LUT Name, and finally Custom Label Using Tags (drawing on metadata variables). Append still number on export checkbox: Once turned on, each fresh still picks up an appended still number. Where that number lands depends on the radio buttons below. As Suffix/As Prefix buttons: Let you settle on placing still numbers at the tail of an auto generated gallery label or at its head.

- Luminance mixer defaults to zero: Picking this option drives the Y channel of the YRGB parameters down to zero across every grade. It's a prerequisite for exporting a compliant ASC-CDL, and it touches every grade relying on the Lum Mix control.
- Use legacy Log grading ranges and curve: DaVinci Resolve 12.5 brought in a change to the Log grading controls that yields smoother, more agreeable results from the same controls. To keep older projects working as before, the Color panel of the Project Settings carries a "Use legacy Log grading ranges and curve" checkbox that toggles a given project across the older Log control behavior versus the newer one. When DaVinci Resolve opens an older project, this checkbox comes on by default, while a freshly created project comes with it off by default.
- Use S-curve for contrast: Enabled by default, this checkbox makes the contrast control in the Color Wheels palette lay an "S-curve" over the image, so a signal's shadows and highlights won't clip as you raise the value. Should you rather have those contrast adjustments applied linearly, with the signal permitted to clip once it hits the top and bottom limits of the video signal, you can switch this checkbox off.
- Use legacy sizing interactions for windows and effects: In version 14.1.1, DaVinci Resolve reworked how window tracking lays down its transformations, letting it now handle things like pixel aspect ratio (par) correctly. New projects ought to keep this setting off, though older projects ought to keep this checkbox on so tracking and transforms stay applied the way they were beforehand.
- Apply stereoscopic convergence to windows and effects: Once turned on, DaVinci Resolve correctly holds the position of a window that's been properly set over each eye while convergence shifts in the 3D palette. Switching this checkbox on also surfaces an extra Convergence parameter in the Window palette that lets you build properly aligned convergence for a window placed atop a stereoscopic 3D clip, as the screenshot below shows.

l Within the Transform section of the Window palette, the Convergence control surfaces once "Apply stereoscopic convergence to windows and effects" is switched on

- Use local version for new clips in timeline: Automatically configures every new clip added to existing timelines, plus every clip added to new timelines brought in through AAF, EDL, or XML, to default to local grades. Should you want every clip added to new timelines to lean on remote grades instead, the way DaVinci Resolve version 9 and earlier did, you can switch this checkbox off.
- Automatically match master timeline with media pool: Switch this option on before importing any media into the Media Pool, or before importing any timelines that will themselves pull media into the Media Pool, and you can build projects holding a Master Timeline. Once enabled, clips join and leave the Master Timeline as they join and leave the Media Pool, so the Master Timeline forever holds all media within the Media Pool. After media has been brought into a project, this setting can no longer be altered.
- Save timeline thumbnails with project: To keep project size down and saving and loading projects fast, you ought to leave this checkbox off. Tick the checkbox and all of your Timeline thumbnails get tucked inside every project, rather than in the default directory normally set aside for stills, throughout both Save and Auto Save operations. That gives you a solid record of the project but takes far longer to finish and eats more hard disk space.
- Use BGR pixel order for DPX v2: Lets you settle on a different pixel order for projects relying on DPX version 2 media.
- Embed timecode in audio output: Switch this on and DaVinci Resolve sends out LTC timecode riding on channel 16 within the SDI stream plus channel 2 of the analog audio output that comes off your video interface.
- Use Timelines Bin: You can only change this option before adding clips to the Media Pool; once you've added clips, it's no longer available. Switching Use Timelines Bin on builds a dedicated Timelines bin within the Media Pool, sitting at the top of the Bin List. Once enabled, the Timelines bin holds every timeline in a project, and you're blocked from dropping timelines into any other bin in the Media Pool. Each time you create or import a new timeline, it shows up automatically in the Timelines bin. You're free to add subfolders beneath the Timelines bin for finer organization.

### Dynamics Profile

Establishes, for keyframed effects on the Color page, the default move from a given dynamic keyframe across to the one after it. By default that move is linear, the "Dynamic profile start" and "Dynamic profile end" parameters sitting at 1 apiece. That said, when you need to change the acceleration of how values interpolate from one dynamic keyframe to the next, you can alter that keyframe's Dissolve Type to "ease" the effect transition you're building. What these settings hold corresponds to the graph curves shown in the Dynamic Attributes dialog as you edit keyframes on the Color page. To learn more, refer to Chapter 148, "Keyframing in the Color Page." within ""Changing Dynamic Attributes"".

### Versions

Ten text fields give you a means of assigning automatic names for the versions of grades you pick on the Color page. Beside every text field sits a drop-down menu letting you pull a name from a convenient list of predefined terms that's been supplied. Alternatively, you can just click any field and type a custom name of your own. Once you rename a version on the Color page, whatever names you configured in this list show up through a drop-down menu inside the Version Name dialog. Working with the named drop-down while renaming a version Relying on a ready-made list of names for your different versions heads off the typos that can later cause folder naming trouble once you turn to the "Commercial Workflow" options for rendering your media on the Deliver page.

### Camera Raw

This panel holds groups of parameters lining up with every camera raw media format DaVinci Resolve supports. Working with the controls inside the Camera Raw panel, you're able to supersede whatever original camera metadata got written down at the moment of capture, and tune every camera raw clip at once by way of the "project" raw settings. For fuller detail, these settings get their own dedicated chapter. For more information, see Chapter 130, "Camera Raw Palette."

### Capture and Playback

All of this panel's settings let you shape the behavior of capture and playout to tape using device-controlled VTRs tied into your Resolve workstation via whichever video capture and output interface is attached. To read up on deck capture, turn to Chapter 24, "Ingesting From Tape." To read up on video output to tape, turn to Chapter 189, "Delivering to Tape."

### Deck Settings

Both capture and playback come under these settings whenever you rely on the tape ingest controls of the Media page or the tape output controls of the Deliver page.

- Video capture and playback: From this drop-down menu you can pick the video format (frame size and frame rate) to output to tape with. An HD timeline can be downconverted to SD, while an SD timeline can be upconverted to HD by way of the format conversion built into your DeckLink card.
- Use left and right eye SDI: A checkbox letting supported video interfaces ingest and output muxed stereoscopic video when paired with supported VTRs, such as HDCAM SR decks running 4:2:2 x 2 mode. (As muxed stereoscopic signals come in, each eye splits into separate left-eye and right-eye image files.) This parameter shows up only when your hardware is configured for it.
- Video connection operates as: Picks among the signal options on offer: Use 4:4:4 SDI and Enable Single Link. Which options you see hinges on which video capture card you're running.
- Data Levels: Lets you set the data range (normally Video or Full) applied while ingesting from or outputting to tape. This option flips the data range of the signal your video capture card outputs, but solely during capture from tape on the Media page, or output to tape on the Deliver page. Whenever neither capture nor output is in progress, your video capture card falls back on the same-named data range setting over in the Master Project Settings pane, the one controlling how you monitor whatever signal gets sent to an external broadcast display or projector.
- Video bit depth: Pick the bit depth that suits what your deck can handle. According to how your workstation is configured, the options are 8-bit or 10-bit. Going with 10-bit puts more load on the processor, yet yields higher quality on compatible devices, and serves as the default setting.
- Use deck autoedit: When your video deck supports it, this is the best way to record video to the deck, since it lets the deck roll the edit using the specified preroll and govern the edits through serial device control. Switch this checkbox off and the deck falls back on a basic edit On/Off mode, with a chance of frame inaccuracies should the "Non auto edit timing" setting not be dialed in properly.
- Non auto edit timing: Tunes the edit synchronization of the connected deck while auto edit is off.
- Deck preroll: Sets how many seconds of preroll to use. What's right depends on how your deck performs.
- Video output sync source: With a DeckLink card this sits at Auto. With other capture cards you may have to point the sync source at "Reference" for playout and at "Input" for ingest. You'll see this setting only if a DVS card is installed on your system.
- Add 3:2 pulldown: Inserts or removes the 3:2 pulldown that's required whenever 23.98 fps media has to be recorded onto, or played back off, a 29.97 tape format.
