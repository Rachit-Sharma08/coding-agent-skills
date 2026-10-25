# Voice isolation speed effects controls in the viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Voice isolation studio version only.
[Chapter index](INDEX.md) / [Previous section](speed.md) / [Next section](voice-dialogue-and-music-processing.md)
<a id="source-audio"></a> <a id="source-audio-controls-in-the-viewer"></a> <a id="source-color"></a> <a id="source-color-controls-in-the-viewer"></a> <a id="source-effects-overlay"></a> <a id="source-lens-correction"></a> <a id="source-lens-correction-controls-in-the-viewer"></a> <a id="source-ripple-delete-silence-for-selected-clip"></a> <a id="source-smart-reframe-studio-version-only"></a> <a id="source-speed-effects-controls-in-the-viewer"></a> <a id="source-stabilization"></a> <a id="source-stabilization-controls-in-the-viewer"></a> <a id="source-the-ripple-delete-silence-dialog"></a> <a id="source-voice-isolation-studio-version-only"></a>

### Speed Effects controls in the Viewer

Add Speed Point: Drops a speed-change point at the playhead's location so you can build speed-ramping effects. Speed: Adjusting this figure lets you accelerate or decelerate playback using a straightforward numeric multiplier. A negative value is also an option, which produces reverse speeds. Duration: While you retime a clip, the Duration field shows you how the change you're making affects the new duration relative to the clip's original duration with no speed effect applied.

### Stabilization

By applying warping and/or translation, the Image Stabilization controls let you smooth away—or even fully lock down—unwanted camera motion inside a clip. The analysis runs in a way that holds onto the motion of individual subjects within the frame, along with the overall direction of any intended camera motion, all while ironing out the unsteadiness.

### Stabilization controls in the Viewer

Stabilizing an image takes only a couple of steps: pick a Stabilization Method from the drop-down (more on those below), then click the Stabilize button. DaVinci Resolve studies the current clip and applies a stabilization effect. The remaining stabilization controls are there to fine-tune the outcome. Any time you change one of these parameters, you have to click the Stabilize button once more for the effect to refresh.

Stabilization Method: This drop-down menu offers three separate options governing how the chosen clip gets analyzed and reshaped while being stabilized. Settle on an option before you click the Stabilize button, since the option you select alters the way the image analysis runs. Switch to a different option and you click the Stabilize button again to reanalyze the clip.

- Perspective: Switches on perspective, pan, tilt, zoom, plus rotation analysis and stabilization.
- Similarity: Switches on pan, tilt, zoom, plus rotation analysis and stabilization, for cases

where running perspective analysis introduces motion artifacts you don't want.

- Translation: Switches on pan plus tilt analysis and stabilization alone, for cases where nothing more than

X and Y stabilization yields results you can live with. Stabilize: Click this button on a clip not yet stabilized and it studies that clip's motion before laying down an initial smoothing effect. Click it on a clip already analyzed and you can recompute a tweaked stabilization effect. TIP: These controls match the ones in the Video Inspector and the Color page Tracker palette, and they feed the same image processing data. So you can run the Stabilization on the Cut page, then turn to the stabilization graph and controls on the Color page to refine the outcome whenever that's needed.

### Lens Correction

Lens Correction supplies two controls that let you either fix lens distortion in the picture or introduce lens distortion of your own as an effect. You can also edit these controls in the Video Inspector and the Color page Edit Sizing palette.

### Lens Correction controls in the Viewer

Analyze: Automatically inspects the frame sitting at the playhead in the Timeline for edges that a wide-angle lens has distorted. Clicking the Analyze button shifts the Distortion slider to deliver an automatic correction. On an especially tough clip, a progress bar shows up to let you know how long it'll take. Distortion: Dragging this slider rightward lets you manually warp the image so that areas bent by wide-angle lenses are straightened out. Should clicking the Analyze button leave you with an overcorrection, dragging the slider leftward backs off the automatic adjustment until the picture looks right.

### Color

Inside the Tools, the Color section holds a single option: Auto Color. The Auto Color command offers a fast way to automatically balance a clip's blacks and whites using the current frame sitting at the playhead. Driven by advanced algorithms built on the DaVinci Neural Engine, it gives you superior results when automatically tuning color balance and contrast.

### Color controls in the Viewer

To dig deeper into working with Auto Color, turn to Chapter 127, “Automated Grading Commands and Imported Grades.”

### Audio

A slider lets you tune the current clip's audio levels right in the Viewer, making that audio clip's volume quieter or louder. This matches each clip's volume setting over in the Edit and Fairlight pages.

### Audio controls in the Viewer

### Effects Overlay

Switching on either the Open FX or Fusion overlays lets you work with the onscreen viewer controls for whichever effects make use of them. The Effects overlay turns on the onscreen viewer controls for effects.

### Smart Reframe (Studio Version Only)

The Smart Reframe feature inside DaVinci Resolve takes the pain out of quickly reframing footage across big aspect ratio shifts. It proves handy in cases where you shot a 16:9 horizontal video and now require a vertically-oriented 9:16 cut for mobile phones plus social media deliverables, or where you're fitting 4:3 archival footage inside a 2.39:1 widescreen movie. Smart Reframe runs either by hand or automatically; the automatic path is driven by the Neural Engine inside DaVinci Resolve. Smart Reframe in action with the Reference Point bounding box active (right) Within the Inspector's Video tab you'll find the Smart Reframe tool, on hand across both the Cut and Edit pages. Here is how you put the Smart Reframe tool to work: 1 Make a copy of your Timeline, then right-click it and pick Timelines > Timeline Settings; click Use Custom Settings so you can set the Timeline Resolution to whatever aspect ratio your delivery calls for. Confirm that “Mismatched resolution files” reads “Scale full frame with crop,” then click OK. 2 Pick one or more clips you'd like to reframe, then open the Inspector to its Video tab. 3 Bring up the Smart Reframe controls, keep the Object of Interest drop-down menu on Auto (where you've picked more than a single clip, Auto is your only choice), and click “Reframe.” DaVinci Resolve studies your footage and ought to shift each clip's position on its own to a framing that looks more pleasing. 4 (Optional) Should the “Auto” setting fall short on a given clip, you can pick the main subject by hand through these steps: a) To mark the subject area yourself, set the Object of Interest drop-down menu to “Reference Point,” then click the Target icon located just to the right of it. Doing so flips the Viewer mode over to Smart Reframe and reveals the onscreen controls for picking a reference. b) Drag the Reference Point bounding box so it encloses the frame's main subject of interest. Where your subject sits beyond the current framing, the Transform controls right above in the Inspector let you reposition the source clip. 5 (Optional) To pen the AI in to reframing along just one axis, pick either Pan Only or Tilt Only over in the Mode selector. 6 Click Reframe.

The Inspector’s Smart Reframe controls showing the manual reference point selected Using the reference you've picked, DaVinci Resolve fixes onto your subject—and tracks it where needed—automatically panning and scanning the original clip so the reference stays inside the new aspect ratio. Even with a little manual adjustment required, this function still cuts dramatically into the time it takes to pan and scan footage by hand-adjusting and keyframing the sizing controls.

### Ripple Delete Silence for Selected Clip

You can analyze and strip silences out of a selected clip on the Edit or Cut page timeline, leaning on the comparable tool over in Fairlight. Select a clip, then choose Clip > Audio Operations > Ripple Delete Silence to bring up the Ripple Delete Silence dialog. Threshold: Sets the highest signal level of your audio (in dB) that counts as silence. Audio signals beneath the threshold are regarded as silence and removed. Raising the threshold removes more audio. Pre Head: Sets how much silence, or pre-roll, sits ahead of each audible section. Post Tail: Sets how much silence, or post-roll, sits after each audible section. Minimum to Trip: This parameter sets the smallest stretch of silence (in frames) to be pulled from the selected timeline clips. Larger values leave more silent sections in the audio. Smaller values produce more strips, but you might notice that some leftover audio sounds “chopped up” where it cuts off abruptly. Crossfade audio: Runs a basic crossfade across the remaining audio clips to smooth out the sound, provided your head and tail settings allow enough length.

### The Ripple Delete Silence dialog

Here's how you strip silences out of a timeline clip: 1 On a track, pick a clip. 2 Head to Clip > Audio Operations > Ripple Delete Silence. 3 The look of the selected audio shifts to add vertical red stripes that mark where and how long the resulting silences run, drawn from the parameter values set in the Remove Silence dialog. 4 Click Remove. Every bit of audio beneath the red stripes is cut and removed, and the clip's leftover sections are ripple deleted together along the timeline.

### Voice Isolation (Studio Version Only)

Voice Isolation draws on an AI model trained for every kind of human voice—male or female, young or old—

which lets you fully strip loud, unwanted sounds out of existing voice recordings with

remarkable results.
