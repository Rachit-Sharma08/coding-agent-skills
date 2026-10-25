# Canva affinity af file support and original layered affinity file

Version: DaVinci Resolve 21 New Features Guide. Context: Editing.
[Chapter index](INDEX.md) / [Next section](font-browser-toolbar-and-show-font-previews-preference.md)
<a id="source-canva-affinity-af-file-support"></a> <a id="source-cut-and-edit"></a> <a id="source-cut-and-edit-part-1"></a> <a id="source-enhanced-retime-keyframing-controls"></a> <a id="source-font-browser-for-choosing-text-and-subtitle-elements"></a> <a id="source-keyframe-and-add-curves-for-selected-clips"></a> <a id="source-keyframe-fusion-effects-generators-and-text-tools-in-the-keyframe-editor"></a> <a id="source-new-keyframing-ease-options"></a> <a id="source-subframe-support-for-audio-keyframing-and-markers"></a> <a id="source-support-for-ograf-html-graphics-and-lottie-animations"></a> <a id="source-the-affinity-file-in-a-timeline"></a> <a id="source-the-font-browser-in-thumbnail-view"></a> <a id="source-the-original-layered-affinity-file"></a>

### Cut and Edit

### Canva Affinity .af File Support

The DaVinci Resolve timeline can now read Canva Affinity .af files natively. Bring an Affinity file into the media pool and, by default, it arrives flattened and rasterized. From there the image behaves on a timeline exactly like any other still-image format. Yet once it sits on the timeline, you can break the Affinity file apart again into its separate layers, each one fanning out onto a fresh video track. Should the Affinity file hold several layer levels or groups, those start out composited onto one video track, though you can break them down further into separate layers whenever you need to. Here is how to split a Canva Affinity .af file on the timeline: 1 On the timeline, click the .af clip to select it. 2 Right-Click the clip, then choose “Split Layers in Place” As an illustration, this Affinity file consists of a group containing several layers, and those layers are in turn sub-grouped into head, body, and legs.

### The original layered Affinity file

Pulling the file into a Timeline rasterizes and flattens every one of the layers by default.

### The Affinity file in a Timeline

Right-click the image on the timeline and choose “Split Layers into Place” and the file fans out into its first tier of layer groupings on the timeline — here, Head, Body, and Legs.

The Affinity broken up into Head Body and Legs layers Should you want to, you can break the layers down into still more tracks by right-clicking one of the layers on the timeline and once more choosing “Split Layers in Place.” Below you can watch the Body group break apart into its separate layers.

The Body layer group expanded into its component layers At this point you can go on to adjust, animate, or edit each layer further inside DaVinci Resolve. Layers can also be folded back together by selecting them and turning them into a compound clip. Over in Affinity, you can keep altering and reshaping the image, and the moment you save those edits they will refresh automatically within DaVinci Resolve. That said, sweeping changes to the layer grouping and hierarchy in Affinity might not carry over cleanly into DaVinci Resolve, and when that occurs you should simply re-import the revised .af file into the media pool once more.

### Enhanced Retime Keyframing Controls

In the Keyframe Editor, the Retime parameter controls have been upgraded so they now share the same bezier easing tools the other parameters use. With these tools you can pull off intricate retime effects — easing into a freeze frame, say, or smoothing out non-linear speed ramps across a clip.

The Speed controls now lean on bezier easing so retime speed shifts come out smooth

### Keyframe and Add Curves for Selected Clips

Keyframe editing now handles multi-clip selection. No matter whether your clips run side by side or are stacked one above another, you can pick the clips you mean to work on, switch on Keyframe mode, and tweak their keyframes right away. The selected clips’ keyframes display at the same time when stacked, or one after another when side by side. That both saves you time when keyframing a run of clips and gives you a visual reference for how the various curves and keyframes stack up against one another between clips.

The Keyframe / Curves editor with multiple clips selected (sequentially).

### New Keyframing Ease Options

For advanced keyframing, fresh ease functions let you set behavior on a single keyframe or alter how interpolation is read between several keyframes. Step In/Out: Step in and out flip a keyframe’s state from one to the next instantly, with no interpolation. You might, for instance, want the second hand on a clock illustration to tick ahead rather than glide ahead. To step a run of keyframes, multi-select the keyframes you want to change and click either the Step In or Step Out icons up top in the Keyframe Editor.

Step In keeps the value of the keyframe before it, then leaps to the next keyframe. Here Step In is at work on a cluster of keyframes along a curve. Step Out leaps right at the keyframe and holds that value all the way to the next keyframe. Here Step Out is at work on a cluster of keyframes along a curve. Loop: Looping a run of keyframes makes it simple to build a repeating motion without slogging through the setup of each keyframe by hand. The motion of the originally selected keyframes is copied across the clip’s whole length. You might, for example, build a walking animation that carries on by itself once the first “step” is laid down. To Loop a run of keyframes, multi-select whichever keyframes you want repeated, then reach for Loop via the Option Menu > Loop Type inside the Keyframe Editor.

Across the clip’s full span, the first three keyframes here are Looped Ping Pong: Much like loop, Ping Pong likewise spins up a run of keyframes automatically, but rather than repeating the sequence, Ping Pong runs it in reverse on reaching the end, then reverses once more when it returns to the start. The textbook example is a bouncing ball.

To Ping Pong a run of keyframes, multi-select whichever keyframes you want bouncing back and forth, then reach for Ping Pong via the Option Menu > Loop Type inside the Keyframe Editor.

Across the clip’s full span, the first two keyframes here are Ping Ponged back and forth Reverse: Reverse could not be plainer — it grabs your keyframe selection and plays it backward along that same keyframe path. To Reverse a run of keyframes, multi-select whichever keyframes you want flipped, then reach for Reverse Keyframes via the Option Menu inside the Keyframe Editor. Shape Box: The shape box lets you tune the interpolation across several keyframes in a steady, measured way by enclosing them in a box whose edges you can manipulate. Keyframes inside that box stretch and squeeze as you drag the box’s edges. Grab the shape box from the toolset up top in the Keyframe Editor, then draw the box around whichever keyframes you want to shift. Hold the Option key and drag the box’s corners to skew the keyframes in a particular direction.

With the Shape Box icon (circled red), you draw a bounding box around a run of keyframes so as to stretch or grow them.

Hold the Option key and drag a corner of the box to skew the keyframes.

### Keyframe Fusion Effects, Generators and Text Tools in the Keyframe Editor

Fusion Effects, Generators, and Text tools can be keyframed through their Fusion parameters in the Keyframe Editor. Just pick one or more Fusion titles, effects, or transitions to bring these properties up in the keyframe editor. Fusion-based clips may carry a great many associated parameters, so you’ll want to pare those down to only the ones you mean to keyframe. The tool for that, Display Selected Parameters, sits within the Keyframe Parameters 3-dot option menu. NOTE: This holds only for Fusion effects living in the Cut and Edit pages. Ordinary Fusion clips and compositions will still rely on Fusion’s expansive keyframe editor instead.

The Keyframe editor modifying a Fusion Title.

### Subframe Support for Audio Keyframing and Markers

The DaVinci Resolve 21 Edit timeline brings several quality-of-life upgrades for audio work. Getting precise subframe audio adjustments calls for you to be zoomed almost all the way in on the timeline.

- On the edit page you can place and shift audio keyframes with subframe, audio sample precision. To add keyframes more easily, hold alt, press the left mouse button to drop the keyframe, then drag it where you want and release to lock in the action.
- You can likewise add and move markers and duration markers so they begin and end between frames. This works for both clip and timeline markers.
- Zoomed in, you can scrub the edit timeline in sub-frame steps with full audio feedback.

### Support for OGraf HTML Graphics and Lottie Animations

On macOS and Windows alike, DaVinci Resolve 21 now handles HTML-based animation in the OGraf (.json) and Lottie (.lottie) formats. An animation — whether you turned it up online or built it yourself — can now drop straight onto your timeline. Once you’ve exported the .json or .lottie file, just drag and drop it into your Media Pool the same as any other media. You can also drop it right onto the timeline, where it gets recognized and handled like a fully rendered animation clip. The alpha background is recognized too, so transparency holds. Simply drop the clip over another layer and it composites properly, which makes it ideal as a stinger or transition. On top of that, Fusion now ships a new node called OGrafLoader. This handy tool lets you load your OGraf or Lottie files into your composition with ease.

### Font Browser for Choosing Text and Subtitle Elements

When picking a font for text-based elements, users can now opt to bring up an expanded Font Browser. The Font Browser opens out and puts the spotlight on the text faces, making the perfect font easier to land on. You can open the Font Browser by clicking its icon near the font selection box across various tools. Clicking that icon (circled red) is what opens the Font Browser. A thorough view of your installed fonts is what the Font Browser lays out. To settle on a font, just pick it in the Font Browser, then press the Select button. That font then loads into the font selection field of your tool.

### The Font Browser in Thumbnail View

Clicking a font actually picks the whole font family. When the family carries several styles in thumbnail mode, tiny circular forward and back icons turn up beneath the font, letting you cycle through each font iteration. In List view a disclosure triangle near the font name reveals them all. There’s also a star icon you can click at the upper right of the font face, which drops the chosen font into the Favorites tab. With the Font Family picked, you can move through each iteration by clicking the left and right arrows. Clicking the star at the upper right Favorites the font. The Font Browser can be resized, and it carries a tidy toolset to help you pin down the perfect font.
