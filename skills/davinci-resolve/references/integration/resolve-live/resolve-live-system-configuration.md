# More about resolve live and configuring your system for resolve live

Version: DaVinci Resolve 20.3 Reference Manual. Context: Resolve live.
[Chapter index](INDEX.md) / [Next section](snapshot-and-resolve-live-audio-monitoring.md)
<a id="source-configuring-your-system-for-resolve-live"></a> <a id="source-going-live"></a> <a id="source-grading-live"></a> <a id="source-more-about-resolve-live"></a> <a id="source-resolve-live"></a> <a id="source-resolve-live-1"></a> <a id="source-setting-up-davinci-resolve-for-resolve-live"></a> <a id="source-setting-up-your-camera-and-hardware-for-resolve-live"></a> <a id="source-using-freeze"></a> <a id="source-video-inputoutput-options-in-the-system-preferences"></a>

### Resolve Live

There's an extra mode on the Color page built to help you run DaVinci Resolve in on-set grading workflows. Switching on the Resolve Live option drops DaVinci Resolve into a live grading state where a video feed arriving from a camera can be watched and graded as a shoot happens.

### More About Resolve Live

Resolve Live was built so you can apply the full toolset of DaVinci Resolve to grading these on-set previews, and along the way store video snapshots holding a frozen image, your grade, and reference timecode pulled from the camera. The concept is that, with Resolve Live, you can collaborate with the cinematographer to shape looks and trial lighting setups on the material being shot, then afterward apply those looks toward building dailies and as a jumping-off point for the final grade once editing wraps. On top of that, you can pair Resolve Live with other Color page tools like the Alpha output to assemble test composites that vet green screen shots, holding them up against imported background images to help with camera placement and lighting tweaks. The signal levels of the incoming video can also be watched through the built-in video scopes. And lastly, 1D and 3D LUTs let you monitor and grade log-encoded footage arriving from the camera.

### Configuring Your System for Resolve Live

### Setting up your Camera and Hardware for Resolve Live

Getting Resolve Live going is uncomplicated. Tower workstation or laptop, it doesn't matter—any Blackmagic Design DeckLink or UltraStudio video interface can link your DaVinci Resolve workstation to a camera and a separate video display. The key thing to remember is this: to take in a live feed and simultaneously send that feed out for monitoring, you'll need either two distinct DeckLink PCIe cards or UltraStudio Thunderbolt interfaces, or one DeckLink card/Ultrastudio that carries several independent inputs and outputs on a single PCIe card/device. As the shoot runs, the digital cinema camera being used has to feed your DaVinci Resolve workstation's video input over HD-SDI or HDMI, set up to carry both the picture and timecode that matches the timecode stamped onto each recorded clip. The majority of cameras can output timecode across HD-SDI and HDMI, and DeckLink and UltraStudio interfaces alike can hand that timecode off to DaVinci Resolve. Lacking a solid timecode reference, you'll miss out on the shortcut of auto-syncing your stored Snapshots to recorded camera original media via ColorTrace, though grades can always be applied by hand. Resolve Live hardware checklist:

- Put in place and bring up to date whichever Blackmagic Design Decklink card or Ultrastudio device will handle live video input on your DaVinci Resolve workstation (consult your Blackmagic Design hardware documentation for the specifics).
- Run the SDI or HDMI video output of the video camera into the video input on the Blackmagic device. Confirm that embedded timecode leaving the camera is switched on too.
- Within the Blackmagic Desktop Video Setup application on your machine, pick the right video input for your device.

Video input choices shown in the Blackmagic Desktop Video Setup. NOTE: The resolution and frame rate your camera sends down the SDI/HDMI cable.

### Setting up DaVinci Resolve for Resolve Live

With the hardware in place, you'll want to confirm how DaVinci Resolve is configured so you can tap into the live grading abilities of Resolve Live. The first thing to set is picking the right video input hardware under the Video I/O settings. Within the System Preferences, the Video I/O panel offers two groups of choices for setting up video interfaces wired to your computer—one covering capture, the other covering monitoring. Resolve Live draws on whichever video hardware input is chosen as the capture device. Should you alter any of these settings, a restart of DaVinci Resolve is required.

### Video input/output options in the System Preferences

After that, kick things off with a fresh empty project. Configure the new project's Timeline and Video Monitoring settings so they line up with the format and frame rate your camera produces.

IMPORTANT: In the project’s Master Settings, the resolution and frame rate of your new project’s Timeline format and Video Monitoring format have to be set to match the resolution and frame rate of the video your camera is producing.

In the Master Settings, confirm your Timeline format along with the Video Monitoring size and frame rate align with your camera's video output. Then drop in a new empty timeline, because the live grading workflow records live graded snapshots onto an otherwise empty timeline. A solid way to keep a shoot's live grades organized is to spin up a new project for each shooting day. Doing it this way keeps snapshots grabbed during shoots that span all 24 hours of time-of-day timecode from clashing with one another. On top of that, keeping projects separate can smooth the path to using ColorTrace later for copying grades off your live grade snapshots onto the camera original media you'll build dailies from. TIP: An empty Media Pool and Timeline don't stop you from loading handy LUTs and pre-loading reference stills and saved grades into the Gallery, all of which can speed up your on-set grading. After your new project exists, you also have to pick the disk where every snapshot you grab gets stored. Out of the box, snapshots land on the scratch disk sitting at the top of the Scratch Disks list within the Media Storage panel of the System Preferences. They're written automatically into a folder bearing the exact name of the current project, tucked inside a folder named Resolve Live.

Resolve Live software checklist:

- Under the Video Input/Output options in the System Preferences, set the Capture Device that will take in the video signal.
- Create a New Project.
- Confirm that the size and frame rate of your Timeline format plus Video Monitoring line up with your

camera’s video output, set inside the project’s Master Settings.

- Create a New Timeline.

### Grading Live

With your camera and computer properly wired and set up, working in Resolve Live is uncomplicated. What follows walks through the live grading workflow the way it was meant to run. As you grow comfortable with what Resolve Live can do, you may land on your own approaches that fit the demands of whatever project you're on.

### Going Live

After your day's project exists, you need to switch Resolve Live on before starting. Enabling it takes two steps: 1 head into the Color page. 2 Choose Color > Resolve Live (Command-R). Up in the Viewer, a red Resolve Live badge tells you Resolve Live is running, and the transport controls give way to the Freeze and Snapshot buttons.

The red badge indicates Resolve Live is live and relaying the feed arriving from the camera.

From here, the feed from the linked camera ought to appear inside the Viewer, the camera timecode ought to read out in the Viewer's timecode window, and you can put the full Color page toolset to work grading whatever sits onscreen, Gallery splitscreens for matching and comparing included. Whatever color tweaks are live across all palettes get pushed automatically onto both the Viewer image and the video sent to an external display (where one exists). With Resolve Live running, a large chunk of DaVinci Resolve's non-grading functions go dark, so once you wrap, remember to shut Resolve Live down. To turn off Resolve Live, do one of these:

- Hit the Exit button down in the lower left-hand corner of the Viewer.
- Choose Color > Resolve Live (Command-R).

### Using Freeze

While in Resolve Live mode, the Freeze button (shaped like a snowflake) locks the current arriving video frame, letting you grade it without motion from the shoot pulling your focus away. After you dial in the change you need, you can release playback to get ready for grabbing a snapshot. To freeze incoming video:

- Click the Freeze button (that looks like a snowflake).
- Choose Color > Resolve Live Freeze (Shift-Command-R).

Hitting the snowflake button holds the picture still so a specific frame can be graded.
