# Saver node saver export tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Saver node.
[Chapter index](INDEX.md) / [Previous section](mediaout-node-and-saver-node.md) / [Next section](saver-node-and-common-controls.md) / [Saver Node SV](mediaout-node-and-saver-node.md)
<a id="source-audio-tab-1"></a> <a id="source-export-tab"></a> <a id="source-format-tab"></a> <a id="source-legal-tab"></a> <a id="source-saver-audio-tab"></a> <a id="source-saver-export-tab"></a> <a id="source-saver-format-tab"></a> <a id="source-saver-legal-tab"></a>

### Saver Export tab

### Export Tab

Process Mode Reach for this menu to pick which Fields Processing mode Fusion uses while saving the images or movie file to disk. Both the default option and the default height come from the Has Fields checkbox control in the Frame Format preferences. The options on offer take in:

- Full frames
- NTSC fields
- PAL/HD fields
- PAL/HD fields (reversed)
- NTSC fields (reversed).

Those two reversed options write fields in the reverse order, so the fields wind up spatially swapped both in time order and in vertical order. Export Mode Use this menu either to render the file out normally or to put a SMPTE standard 3:2 pulldown on the footage, taking the footage from 24 fps up to 30 fps.

Clipping Mode This menu — sometimes thought of as source image clipping — lays out how the image’s edges ought to be handled.

- Frame: By default, the Frame setting clips to whichever parts of the image fall inside its visible dimensions. Any infinite-workspace behavior gets broken. Where the upstream DoD is smaller than the frame, whatever area is left in the frame counts as black/transparent.
- None: No source image clipping at all happens with this setting. So any data ordinarily called for beyond the upstream DoD counts as black/transparent. Mind that this may spawn humongous images able to eat up a considerate amount of disk space. So reach for this option only where it’s truly needed.

To learn more about ROI, DoD, and Infinite Workspace, turn to Chapter 69, "Using Viewers." within the DaVinci Resolve Reference Manual, or to Chapter 7 within the Fusion Reference Manual. Save Alpha to Color Switch this control on and the Alpha channel gets written into the color channels as a grayscale image. Doing so wipes out any color information already there. Color Space Type Setting the output file’s Color Space is what this menu does, so that you could, say, color space convert images from linear to Rec709, and the like, thereby putting out linear EXRs, 709 Quicktimes, and so on from one source. Nothing gets converted within the Comp; only the images written to disk get converted.

- Auto: Carries along whatever metadata might sit in the rendered image.
- Space: Lets the user fix the color space according to the output format.

Curve Type Picking a Gamma curve for the rendered file is the job of this menu. Having set the gamma curve type, you may opt to apply the curve for output.

- Auto: Carries along whatever metadata might sit in the incoming image.
- Space: Lets the user fix the gamma curve according to the chosen file format.
- Log: Brings up the Log/Lin settings, much like the Cineon Log node.

For fuller detail on the Log settings, turn to Chapter 99, “Film Nodes,” within the DaVinci Resolve Reference Manual, or to Chapter 39 within the Fusion Reference Manual. Apply Curve Depending on which Curve Type you chose, or on the Gamma Space turned up in Auto mode, the matching Gamma Curve gets applied, which in effect converts away from a linear working space.

### Audio Tab

NOTE: This tab shows up only in Fusion Studio’s Saver node.

### Saver Audio tab

The audio capability ships in Fusion Studio purely for scratch track use (lining up effects with audio and clip timing). Final renders ought, almost every time, to run without audio. Keep your audio files as small as they can be, since Fusion pulls the whole audio file into memory so it can show the waveform efficiently in the Timeline. Pick a Quicktime file format and the audio track gets folded into the saved image. As things stand, Fusion can play back WAV audio. Source Filename Into the Source Filename field you can type, for whatever audio clip you intend to use, both its file path and its name. You can equally click the Browse button to open a file browser window and track down the audio scratch track. Pick the WAV file you want, then over in the keyframes panel expand the Saver bar to bring up the audio waveform. Drag the pointer across the audio wave within the Timeline layout, and you’ll hear the track. Sound Offset Drag this control either way, left or right, to shift the audio clip’s Timeline position relative to the Node Editor’s other nodes.

### Legal Tab

For producing “broadcast safe” saturation and video range files to output, the Legal tab holds the relevant settings.

### Saver Legal tab

Video Type Reach for this menu to pick which standard gets used for broadcast legal color correction. The choices are NTSC, NHK, or PAL/SECAM. Action Reach for this menu to decide how Fusion handles illegal colors in the image.

- Adjust to Legal: This has the images saved with legal colors suited to the chosen Video Type.
- Indicate as Black: This has the illegal colors shown as black in the views.
- Indicate as White: This has the illegal colors shown as white in the views.
- No Changes: This has the images saved untouched.

Adjust Based On Reach for this menu to decide whether Fusion makes the image legal to 75% or 100% amplitude. Hardly any broadcast markets allow 100% amplitude, so for the most part leave this at 75%. Soft Clip What the Soft Clip control does is pull out-of-range values back into the image. It manages that by easing the conversion curve at its top and bottom, so more values can be represented.

### Format Tab

Information, options, and settings tied to whichever image format is being saved fill the Format tab. The controls for an EXR sequence look nothing like the ones shown when a MOV file is saved.

### Saver Format tab

EXR is displayed above for reference.

Once the Saver node is set to DPX, it pays to grasp why the Bypass Conversion > Data is Linear option exists. When you’re writing log data into a DPX without leaning on the Saver node’s own lin-log conversion (that is, with Bypass Conversion ticked), the Data Is Linear option ought to be off. This signals whether Bypass Conversion got ticked because the data is linear, or because it’s already log. Switch Data Is Linear on and the DPX gets flagged in its header as holding linear data. That in turn means that when the DPX gets loaded back into Fusion, or into other apps that read the header, those apps take the data for linear and skip any log‑lin conversion.
