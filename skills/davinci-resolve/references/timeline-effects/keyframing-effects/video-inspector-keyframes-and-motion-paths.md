# Basic keyframing in the video inspector and keyframing motion paths in the timeline viewer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing effects.
[Chapter index](INDEX.md) / [Next section](imeline-playback-keyframing-and-curve-editor.md)
<a id="source-basic-keyframing-in-the-video-inspector"></a> <a id="source-keyframing-effects"></a> <a id="source-keyframing-effects-part-1"></a> <a id="source-keyframing-in-the-edit-timeline-and-curve-editor"></a> <a id="source-keyframing-motion-paths-in-the-timeline-viewer"></a>

### Keyframing Effects

Both the Edit and Cut pages give you controls for keyframing the effects you place onto your timeline.

The Inspector lets you keyframe most of its parameters so you can build animated effects — for example zooming in through the Zoom parameter, fading out through the Opacity parameter, or sliding in from an edge to reveal the clip beneath through the Cropping parameters. On top of that, when you bring in a project from an NLE carrying keyframed sizing settings, DaVinci Resolve imports and surfaces those keyframes for you. You will find the core keyframing controls inside the Video Inspector. Each keyframeable parameter carries a gray keyframe button just right of its slider. When the playhead sits on a keyframe that button shifts to orange and tiny navigation arrows show up on either side; otherwise it remains gray.

Orange buttons throughout the Inspector signal how keyframes are being used. Zoom shows the playhead resting on the present keyframe while the gray navigation arrows reveal further keyframes both ahead of and behind it. Position shows the playhead resting on the lone keyframe placed (orange diamond, no arrows), and Rotation Angle shows that no keyframe exists (gray diamond). After you have keyframed a parameter or two inside some group of the Inspector, that clip picks up a Keyframe icon at the far left end of its name bar in the Timeline. This icon appears solely on keyframed clips.

Shown here on a keyframed clip in the Timeline: the Keyframe track button (circled)

### Basic Keyframing in the Video Inspector

You can handle most straightforward keyframing right in the Inspector with the three buttons that sit to the right of any keyframeable parameter. Creating an animated effect requires no fewer than two keyframes.

In the Inspector, reading left to right, the trio of keyframe controls is: Previous keyframe, Create/ Delete keyframe, Next keyframe Ways to keyframe parameters within the Inspector:

- To add a keyframe: Choose a clip, open the Inspector, then drag the Timeline playhead to the frame that should hold a keyframe, and press the Keyframe button beside whichever Inspector parameter you mean to animate. After you have set at least one keyframe on a parameter, every further tweak you make to Inspector parameters, or through the onscreen Transform/Crop controls in the Timeline Viewer, spawns fresh keyframes on its own whenever the playhead sits on a different frame.
- To move the playhead to the next or previous keyframe: Press the little left- or right-hand arrow flanking a parameter’s keyframe control to send the playhead to the next or previous keyframe. Alternatively, tap Right-Bracket ( [ ) and Left-Bracket ( ] ) to step between keyframes.
- To edit an existing keyframe of a parameter: Park the playhead directly over the keyframe you intend to change, then alter that parameter, either in the Inspector or with the onscreen controls of the Timeline Viewer.

Methods of changing keyframe interpolation in the Inspector:

- To change a keyframe to Ease In or Ease Out: Eased keyframes produce animated transitions that start gently and ramp up to full speed, or wind down gradually until they halt. This applies only when two or more keyframes are forming an animated effect. Using the next/previous keyframe controls, land the playhead on a keyframed frame; now right-click the orange keyframe button and select Ease In, Ease Out, or Ease In and Out, depending on the keyframe under edit and the result you are after.
- To change a keyframe to Linear: Drive the playhead onto a keyframed frame via the next/ previous keyframe controls; afterward, right-click the orange keyframe button and select Linear.

Methods of deleting keyframes and disabling keyframed effects:

- To delete a single keyframe: Open the Inspector, slide the Timeline playhead onto a frame carrying a keyframe, and press the orange Keyframe button in the Inspector to remove it.
- To delete all keyframes for one parameter: Press the reset button at the right of a parameter’s keyframe control in the Inspector.
- To delete all keyframes in a group of parameters in the Inspector: Press the reset button at the right of a parameter group’s title bar in the Inspector.
- To disable or enable a group of parameters in the Inspector: At the left end of a parameter group’s title bar within the Inspector, press the toggle control. Orange means the group is on; Gray means off.

### Keyframing Motion Paths in the Timeline Viewer

When you are keyframing a clip’s transform controls to generate motion, a motion path shows up once you switch on the Transform controls via the drop-down menu at the lower left of the transport controls.

A visible motion path resulting from animated Position X and Y parameters Every keyframed shift in the Position X and Y parameters lays a control point onto the surface of the motion path, which defaults to linear and so produces a sharp corner. Even so, you can right-click any control point and pick Smooth from the contextual menu to attach Bezier handles to it, turning that sharp corner into an adjustable curve.

Changing the linear control point into a Bezier curve You may drag the control points that form any motion path wherever you like to reroute the course the chosen clip follows. The dots running along the motion path’s surface convey how fast the motion is; dots packed close together signal slower motion, while dots spread apart signal faster motion. Pulling one motion path control point further from a neighbor accelerates the animation between the two, whereas pulling it nearer slows the animation, since you are making the chosen clip cover a greater or smaller distance over the same keyframed span of time.

Along the motion path the dots reveal slow motion across its left portion and quicker motion across its right You can likewise reshape any control point’s curve by clicking to select it, which reveals its Bezier handles, and then dragging those handles to tune the curve. After the handles are revealed, a range of approaches is available for adjusting them and shaping the motion path. Lastly, you can tune the motion’s acceleration via the Acceleration handle on the stem of any Bezier curve. Pulling an acceleration handle in toward a control point yields an eased keyframe, where motion eases to a halt or starts up from a halt. Pulling an acceleration handle out from a control point yields more linear motion, where the object passes steadily through that control point.

Sitting on a curve’s Bezier handle, an acceleration handle produces eased motion when you pull it inward toward the control point under adjustment Ways to adjust the Bezier handles on motion paths:

- Drag any control point to reshape the motion path.
- Drag any Bezier handle to change the shape of the curve.
- Command-drag any Bezier handle to sever the tangent linking it to the Bezier handle opposite. Once you let go of the Command key, the two Bezier handles lock back together at whatever angle you set.

To remove a motion path control point together with its keyframe:

- Right-click any control point and choose Delete Keyframe.

To switch a control point between sharp and curved angles:

- Right-click whichever control point you want and pick Linear to get a sharp angle, or Smooth to get a curve.

### Keyframing in the Edit Timeline and Curve Editor

You can work with keyframes straight in the the Timeline; or, when you need keyframe editing more involved than the fairly basic controls of the Inspector and Timeline permit, turn to the Keyframe tracks and Curve Editor that live in the Edit Timeline. Once one or more clip parameters carry keyframes, the far-right edge of that clip’s Timeline name bar gains two tiny buttons: a Curve button and a Keyframe button. Through these buttons you reach dedicated keyframe editors built for different jobs.
