# Display LUT and raw image data

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](output-scaling-and-color-management.md) / [Next section](color-and-dynamics-profile.md)
<a id="source-broadcast-safe"></a> <a id="source-camera-raw-decoding"></a> <a id="source-color-page-image-processing"></a> <a id="source-conform-options"></a> <a id="source-deliver-page-output-media"></a> <a id="source-display-lut"></a> <a id="source-general-options"></a> <a id="source-input-lut"></a> <a id="source-output-lut"></a> <a id="source-project-settings-part-3"></a> <a id="source-raw-image-data"></a>

### DISPLAY LUT

### Raw Image Data

### Camera Raw Decoding

### INPUT LUT

### Color Page Image Processing

### OUTPUT LUT

### Deliver Page Output Media

Bear in mind that because 1D and 3D LUTs can both be applied at once, the 1D LUTs at any given step always run ahead of the 3D LUTs.

- Input Lookup Table: A pair of drop-down menus lets you attach 1D and/or 3D LUTs that act on the current Timeline ahead of every other image processing operation in DaVinci Resolve.
- Output Lookup Table: A pair of drop-down menus lets you attach 1D and/or 3D LUTs that act on the current Timeline after the Color page operations finish, yet ahead of the briefly applied Display LUT.
- Video Monitor Lookup Table: A pair of drop-down menus lets you attach 1D and/or 3D LUTs that act on the current Timeline after every other image processing operation in DaVinci Resolve. That said, Display LUTs apply only briefly for monitoring purposes; they never touch rendered media nor the signal sent to tape via the Deliver page controls. Display LUTs prove especially handy for applying a film print emulation LUT inside a Log workflow, or for applying a monitor calibration LUT when you output to one display and lack dedicated outboard calibration hardware.

Here’s an example. When grading toward film output under a Log workflow, it’s typical to reach for the Display LUT drop-down menu and apply a film emulation LUT that mimics how the image emerges from the film recorder — factoring in the film lab and print stock involved — so that the image you’re grading sits as near as it can to how the final release print will appear on the cinema screen.

- Color Viewer Lookup Table: A pair of drop-down menus lets you attach 1D and/or 3D LUTs that act on the picture shown in the Viewer on your computer display, apart from the Display LUT used for output to your broadcast display. By default this tracks the Video Monitor LUT setting, though you may also use this option to apply a particular calibration transform for your computer monitor. As an alternative, you might use it to strip color from the GUI Viewer so you can judge image contrast specifically, or to avoid quarreling with your client over which display reads correctly.
- Scopes Lookup Table: Normally, the internal software video scopes in DaVinci Resolve deliver an unbiased read of the genuine video data levels inside the Resolve image processing pipeline. You can, however, direct the software scopes to adopt the Video Monitor LUT selection, or any other LUT present on your system, so this read reflects the monitored output.
- 3D Lookup Table Interpolation: Picks the processing quality used for both LUT and DCTL operations across DaVinci Resolve. 3D Lookup tables (LUTs) are three-dimensional grids of red, green, and blue values, each input color mapped to an output color value, thus offering a way to perform color transformations from pre-calculated data. Powerful though they are, 3D LUTs hold finite detail; one might, say, carry a 17x17x17 LUT defining 4913 individual color transforms. Applied to a floating point image holding more data than the LUT defines transforms for, the color values that land between the 17x17x17 color transforms named by the LUT must be interpolated. Two methods are available, each weighing processing efficiency against greater quality:

Trilinear: (Default) Trilinear stays backward compatible with grades relying on LUTs from earlier DaVinci Resolve versions and reproduces how those LUTs appear within other applications. Tetrahedral: Tetrahedral leans a touch harder on the processor, but it yields finer image quality in LUT and DCTL processing with less color-banding. Tetrahedral suits projects that have no need for backward compatibility with earlier DaVinci Resolve versions or with LUTs built in other applications.

- Update Lists button: Reloads the LUT drop-down menus whenever you’ve added new LUTs to your system after DaVinci Resolve was already running.
- Open LUT Folder button: Choosing this opens the master folder within your file system, as covered in the list of DaVinci Resolve LUT paths shown above.

Adding Lookup Tables to Your DaVinci Resolve Installation The drop-down menus inside the Color Management panel carry a set of factory preset LUTs shipped alongside DaVinci Resolve, plus whatever LUTs DaVinci Resolve has produced or that you’ve dropped into the correct directory for your operating system.

- On macOS: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/
- On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT
- On Linux: /opt/resolve/LUT Should you have grabbed the non-studio edition of DaVinci Resolve through the Apple App Store, the LUTs reside in a separate spot so that DaVinci Resolve stays completely self-contained. Here, clicking the “Open LUT Folder” button within the Lookup Tables panel of the Project Settings opens a Finder window right where those LUTs live. From that window, you can duplicate LUTs you’d like Resolve to reach, or remove LUTs you no longer want. Drop a LUT into one of these directories once DaVinci Resolve is already open and you can click the Update Lists button to reload the drop-down menu contents. Both 1D and 3D LUTs are used by DaVinci Resolve. The 3D LUTs that DaVinci Resolve generates come in the .cube format, set up as 33x33x33 cubes with 32-bit floating point processing. DaVinci Resolve is likewise able to read and apply LUTs in the Shaperlut format.

### Broadcast Safe

You can switch on Broadcast Safe settings during grading to hold the video signal’s luma and chroma alike within three permitted bands of overshoot and undershoot tolerance. Broadcast safe IRE (mV) levels: From this drop-down menu, pick one among three intensities for clamping the signal. Pick whichever range fits your QC requirements. Make Broadcast Safe: A checkbox toggling broadcast safe limiting on or off. NOTE: The clipping that Broadcast Safe applies carries no inherently soft roll‑off of its own. To get the best outcome, pair Broadcast Safe with the Soft Clip controls over in the Color page.

### General Options

A range of general preferences shaping the interface and behavior of DaVinci Resolve is gathered in this panel.

### Conform Options

How clips are conformed so imported project files line up with source media on disk — by pulling timecode, reel names, file names, file paths, and the like — is decided by the settings in this cluster. Conforming and relinking get fuller treatment over in Chapter 56, “Conforming and Relinking Clips.”

- Use Timecode: Governs the way DaVinci Resolve pulls timecode out of the media files it references. You get two choices: Embedded in the source clip: The setting most projects should favor, since it conforms automatically and carries grades onto the clips it produces. Provided DaVinci Resolve can read the timecode from either a media file's timecode track or the header metadata of the frames within a DPX sequence, you're able to lean on timecode to reconform clips, or even swap out entirely the media file a clip points at. From the source clip frame count: A handy option whenever the source media carries no timecode metadata and the only thing on hand is a frame count that labels frames through sequentially numbered integer values.
- Conform partial clips with black gaps: Drops black frames in wherever you conform a clip that's missing some of the frames it needs. With this option turned on, partial clips get marked in the Edit page by a P inside the thumbnail of whichever clip is short on frames.
- Automatically conform missing clips added to Media Pool: On by default; you have to switch it off to run a collaborative workflow. While this checkbox is on, DaVinci Resolve keeps a live link between the clips in the Media Pool and the ones across a project's various timelines. With this checkbox enabled, importing clips whose timecode/file names/reel names line up with clips already in a timeline causes DaVinci Resolve to automatically reconform every matching missing clip, plus all the other timeline clips that have force conform switched off.
- Assist using reel names from the: With this checkbox enabled, DaVinci Resolve leans on reel numbers while conforming clips to align against any imported project. You also have to switch this setting on if you intend to pick distinct reel name extraction methods for individually chosen clips through the Clip Attributes window. Leaving this checkbox off compels DaVinci Resolve to recognize clips by file names while conforming XML and AAF projects. File names work for conforming only XML or AAF files, or when bringing in a DaVinci Resolve project. You get four choices: Source clip file pathname: Derives the reel number by pulling it out of each media file's path. This lets you draw a reel number out of all or some of the file name, or out of all or some of the name of any folder along the path that contains the file. You spell out the extraction in the Pattern field. Pattern: A code spelling out how a reel number ought to be pulled from the source clip path name.

To learn more on building patterns, refer to Chapter 56, "Conforming and Relinking Clips." within "Using the Pattern Field."

Media Pool folder name: The reel number comes from the name of the bin within the Media Pool that contains the clip. People often pick this for stereo projects, drawing the reel number out of directories named "Left" and "Right." It's handy as well for projects taking in fresh VFX clips day by day. Embedding in source clip file: Useful for file formats in which the reel number lives inside the media file itself. QuickTime files originating in Final Cut Pro, along with DPX frame files plus CinemaDNG files, all count as formats capable of carrying reel number header data. Source clip filename: Where no reel number is defined, it's frequently simplest to just fall back on the source clip filename. This is a safe pick in cases where you intend to manually choose distinct reel name extraction methods per clip through the Clip Attributes window.

- Limit reel name matching to X characters: For cases where the media files you were handed carry extra characters in the reel name that don't line up with the names used in the project file you received, "Limit reel name matching to X characters" lets you drop a set number of characters off the end of a reel name. It operates together with the setting that follows.
- Ignore the first X characters of the reel name: For cases where the media files you were handed carry extra characters in the reel name that don't line up with the names used in the project file you received, "Ignore the first X characters of the reel name" lets you drop a set number of characters off the front of the reel name. Paired with the prior setting, you can pare any reel name down to a conformable subset of characters.
- Extract reel names from EDL comments: Media file formats like R3D carry reel names, drawn from the file names, that run past the eight characters a standard EDL permits. This option lets DaVinci Resolve pull reel names out of suitably formatted EDL comments, like the ones produced by Final Cut Pro 7.
- Sort timeline using reel number and timecode: Lets you alter how C mode sorting behaves in the Timeline. With this checkbox on (the default), every clip in the Timeline gets sorted by reel number first and then by source timecode. That way, clips carrying similar timecode off the same reel land beside one another in C mode. Switch this checkbox off and reel number is disregarded, so every clip in the Timeline sorts purely by source timecode. The result can mix clips from several sources together, yet it proves useful in certain cases.
- Mixed frame rate format: (Available only before you import media into a project) From this drop-down menu you pick the method used to conform mixed frame rates for rendering and playback. The option you settle on governs how closely retimed clips inside DaVinci Resolve agree with the same clips after they were retimed in other editing applications, once you bring those timelines into DaVinci Resolve through XML or AAF. This same drop-down menu turns up in the Load AAF or XML dialogs as well.

If you're editing from scratch in DaVinci Resolve: Just leave this setting on "Resolve." When importing timelines via XML from Apple software: Pick either the "Final Cut Pro 7" or "Final Cut Pro X" conform methods. When bringing timelines in through XML or AAF originating in Premiere Pro, Media Composer, Smoke, or any other NLEs: Go with "Resolve." When none is selected: DaVinci Resolve conforms and processes every clip in the Timeline so they play at whichever frame rate is picked in the "Timeline frame rate" drop-down menu. As an example, 23.98, 29.97, 30, 50, 59.94 and 60 fps clips will every one play back at 24 fps when that's the value "Timeline frame rate" carries in the Master Project Settings, and clips run slower or faster to match. The way clips in mixed frame rate timelines render out hinges on whether the Render Settings are configured to render individual source clips or a single combined clip. Render the Timeline as individual source clips and each clip renders on its own at its native frame rate. Pick "single clip" and every clip converts to the "Timeline frame rate" frame rate and renders as one media file.
