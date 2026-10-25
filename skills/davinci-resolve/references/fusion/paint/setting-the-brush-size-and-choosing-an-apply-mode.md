# Setting the brush size and choosing an apply mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint.
[Chapter index](INDEX.md) / [Previous section](paint-overview-and-types-of-paint-nodes.md) / [Next section](tracking-a-paint-stroke-and-tracking-a-group-of-paint-strokes.md)
<a id="source-animating-and-tracking-paint-strokes"></a> <a id="source-animating-with-write-on-controls"></a> <a id="source-choosing-an-apply-mode"></a> <a id="source-cloning-from-the-frame"></a> <a id="source-deleting-strokes"></a> <a id="source-editing-paint-strokes"></a> <a id="source-editing-paint-strokes-in-the-modifiers-tab"></a> <a id="source-setting-the-brush-size"></a> <a id="source-stroke-animation-drop-down-menu"></a> <a id="source-write-on-start-and-end-parameters"></a>

### Setting the Brush Size

Once the Stroke type is chosen, you can set the Brush size in the Inspector or, more naturally, within the viewer itself. Select the Paint node over in the Node Editor and rest the pointer above the viewer, and an outline of the current brush size becomes visible. To resize the brush, keep the Command key pressed and drag. The circle grows or shrinks, letting you gauge it against other objects you might be painting over.

The brush size can be adjusted interactively right in the viewer

### Choosing an Apply Mode

What the paintbrush actually does is governed by the Apply Mode buttons. Eight Apply modes are available, each tasking the brush with things like painting a color, cloning from a source, smudging an area, or taking out thin wires.

The Apply Mode buttons govern what the paint brush does Picking a Paint Color A colored brush stroke’s paint color and opacity can be chosen in several ways. Reach for the Fill button in the row of Apply modes when your goal is to paint a solid color.

The Color swatch displays the present color A click on it brings up the OS Color Picker window

To pick a color for the paint brush, do one of these:

- Click the color swatch to summon a standard OS Color Picker window.
- Drag the Eyedropper out into the viewer.
- Drag within the color chooser to set a saturation and luminance. Drag along the sidebars to shift the hue and transparency.

As you paint, every stroke comes out unpremultiplied, which means nudging the Alpha slider in the Inspector leaves what you put on the RGB channels alone. Altering opacity, by contrast, reaches all four channels.

### Cloning from the Frame

Picking the Clone Apply Mode lets you paint one area of an image over another. This is the Paint tool’s most frequent application. It lets you strip objects or artifacts from a clip by masking them with a different part of the frame. Whether you clone on a single frame or across the clip’s whole duration depends on the Stroke type you’ve chosen. The Clone Apply Mode lets you sample one area and put it to work as a source for painting over another Clone Apply Mode can draw either from the very image plugged into the Paint node’s background input or from a different source within the node tree. To clone from another region of the same frame: 1 Choose a Stroke type via the Paint toolbar overhead. 2 With the size slider in the Inspector’s Brush controls section, set the brush size. 3 Among the Apply Mode buttons, pick the Clone mode. 4 Option-click over the spot in the viewer you want as the source. A dot turns up marking the center of whatever you’re sampling.

The Clone source’s starting area marked by the X, with the circle standing for the paint brush size 5 Paint across the area you want hidden, drawing on the source pixels.

The Clone finished, once the source area was chosen and the flag pole painted over While erasing objects or artifacts from a clip with the Clone Apply Mode, you’ll sometimes find it simpler to sample from a different frame on the same clip. That approach pays off when the object you’re cloning out shifts during the clip and lays bare the area behind it. By offsetting the source frame, sampling from a different frame can draw on that exposed background. To clone from a different frame of the same clip: 1 Choose a Stroke type using the Paint toolbar that sits over the viewer. 2 Dial in the brush size. 3 Among the Apply Mode buttons, pick the Clone mode. 4 From the Node Editor, drag the clip (MediaIn or Loader) over into the Inspector’s Source Tool field.

The Paint Inspector after MediaIn1 was dragged from the Node Editor into the Source Tool field

5 Tick the Overlay checkbox to view the current frame and the offset frame laid on top of each other. 6 Drag the Time Offset slider to settle on the source frame you want. 7 Option-click over the spot in the viewer you’ll use as the source, or to shift the source frame’s position.

Overlay layers two frames together via Time Offset, so you can clone from one frame onto another 8 Paint across the area you want hidden, drawing on the source pixels.

The plane is halfway painted out by way of the Overlay with Time Offset 9 Untick the Overlay checkbox.

The Clone Apply Mode can pull from a different frame of the same clip

TIP: With a Clone Apply Mode active, keep the O key pressed rather than ticking the Overlay checkbox in the Inspector to see the Overlay. Let go of the O key and you’re back to normal viewing without the Overlay.

### Editing Paint Strokes

After you’ve painted with the Stroke or Polyline stroke type, you can reshape the stroke’s look by selecting it and revising the parameters in the Inspector. Selecting it means switching to the selection tool on the Paint toolbar above the viewer. With the Paint node’s selection tool, either click once on a stroke or draw a bounding box around it to mark it for editing. TIP: To grab several strokes, Shift-click or Command-click to add and drop particular strokes from the selection, or drag a selection box around every stroke you mean to take. While changes can be made in the Inspector’s Tools tab, the Paint node draws on both the Tools tab and the Modifiers tab. Under the Tools tab you make new brush strokes and pick a stroke in the viewer to edit. The Modifiers tab lays out a list of every stroke on the selected Paint node, making it simple to rework any paint stroke you made earlier. NOTE: Multistroke and Clone Multistroke each show as a single item in the Modifiers tab regardless of how many strokes you draw with them. Those two tools can’t be edited once made. The very controls you used in the Tools tab to create strokes live in the Modifier’s tab for changing them. Each individual stroke can be animated as well.

You edit the Stroke or Polyline Stroke type by picking the stroke within the viewer

### Editing Paint Strokes in the Modifiers Tab

Paint a stroke and that stroke’s settings turn up in the Inspector’s Modifiers tab. From there you can adjust the Tools tab settings for the next stroke you’re about to paint. Every time you click, drag, and let go of the pointer button, a new stroke is born. The Modifiers tab numbers each stroke, where it can be selected and edited. Once you finish painting a stroke, it joins the Modifiers tab alongside an extra Stroke modifier standing in for the next stroke. As an example, paint your first stroke and the Modifiers tab lists it as Stroke1 plus a stroke 2, the latter representing the next stroke you’ll make. The Modifiers tab always carries one stroke more than the viewer does. Every stroke shows up in the Modifiers tab ready for editing

### Deleting Strokes

Paint strokes can be removed in two ways. To remove a single stroke, proceed like so: 1 Select the Paint node. 2 Open the Modifiers tab. 3 On the Stroke header you mean to remove, right-click and pick Delete from the menu. To wipe out every paint stroke you’ve made across all frames, do one of these:

- Click the reset button in the Inspector’s top-right corner.
- Delete the Paint node from the Node Editor.

### Animating and Tracking Paint Strokes

In certain respects, animating paint strokes is the same as animating any other effect in the Inspector. Every parameter open to animation carries a gray diamond Keyframe button down its right edge. A click on that Keyframe button drops a keyframe on the current frame and turns on auto-keyframe mode for the parameter. More often, though, the paint stroke gets tracked with one of Fusion’s trackers, or, for motion graphics, animated through the Write-On Start and End sliders.

### Animating with Write-On Controls

Both the Stroke and Polyline stroke types carry Write-On controls, found in the Inspector’s Stroke controls section. Those Write-On controls animate how a stroke emerges along the path. You can drive the Write-On controls either from the Stroke Animation drop-down menu or with the Start and End sliders.

### Stroke Animation Drop-Down Menu

Six options for auto-animating a paint stroke sit in the Stroke Animation drop-down menu. The opening two don’t so much animate the stroke as define a duration. The Limited Duration option leans on the Duration slider to set how many frames the stroke stays onscreen. For genuine auto-animation, choose one of the three Write options or the Trail option. Pick Write On and a write-on animation is built for you automatically. Its duration is pinned by two keyframes that appear the moment you choose Write On from the menu. The Start keyframe lands on the frame where you first drew the stroke. The End keyframe is dropped on the current frame as you choose Write On from the menu. The menu’s other options place their Start and End keyframes much the same way but flip the animation’s direction according to which one you select.

### Write-On Start and End Parameters

The Write-On Start and End parameters let you set the start point and end point along any stroke’s path by hand and keyframe each one on its own. The Start parameter fixes where the stroke begins, given as a percentage offset from the start of the stroke’s path. A Start value of 50, for instance, slides the stroke’s starting point to the middle of its path. The End parameter behaves identically but reckons from the stroke’s far end. By keyframing the End parameter from 0 to 100 across several frames, you can animate a stroke onscreen for a handwriting effect.
