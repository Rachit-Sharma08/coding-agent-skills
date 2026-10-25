# Image output scaling settings and color management

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](blackmagic-ursa-cine-immersive-and-apple-vision-pro.md) / [Next section](apple-immersive-motion-data-and-select-the-axis-to-view.md)
<a id="source-about-davinci-wide-gamut"></a> <a id="source-apple-immersive-processing"></a> <a id="source-assembly"></a> <a id="source-backdrops"></a> <a id="source-color-management"></a> <a id="source-dip-to-color-dissolve-effect"></a> <a id="source-editing"></a> <a id="source-image-output-scaling-settings"></a> <a id="source-ingesting"></a> <a id="source-transitions"></a> <a id="source-trim-controls"></a> <a id="source-using-the-viewer"></a>

### Image Output Scaling Settings

### Color Management

Because you need fine command over the peak output nit luminance, the recommended approach to color management leans on Color Space Transform (CST) nodes on the color page. What the color management settings in the Project Settings aim to do is pin down the color page’s timeline (or ‘working’) color space and define the color space metadata that travels with the rendered file. 1 Pick Color Management from the Project Settings sidebar. 2 Keep ‘Color science’ at DaVinci YRGB. 3 Set the ‘Timeline color space’ to DaVinciWG/Intermediate. As a future-proof wide gamut color space built for HDR workflows, it suits Blackmagic URSA Cine Immersive media and Apple Vision Pro deliverables perfectly. 4 Set the ‘Output color space’ to ‘P3-D65 ST2084 1000 nit.’ That color space supplies a fitting gamut when you monitor the DaVinci Resolve viewers via a Mac Studio Desktop, whose display is typically Display P3. Working on a grading monitor or under a different Apple ICC profile means changing the output color space to align with your display’s color standard. You’ll also have to alter the gamma (transfer function) so it maps onto the ICC profile correctly. 5 Just above the color space settings, click ‘Use separate color space and gamma’. That action breaks the color space and gamma dropdown fields into two. 6 Set the output gamma (over in the right column) to ‘Rec.2100 ST2084.’ 7 Tick ‘HDR mastering is for 1000 nits.’

Apply these Color Management settings. So that your next Apple Immersive project takes less time to set up, you can store the present settings as a preset. 8 Open the three-dot options menu at the upper right of the Project Settings window and pick ‘Save Current Settings as Preset’. 9 Give the preset a name and click Ok. Next time you handle Immersive media, configure the project settings in a snap: open the Project Settings window, click the options menu, and pick the listed preset. 10 Click Save to dismiss the Project Settings.

### About DaVinci Wide Gamut

Developed for DaVinci Resolve, DaVinci Wide Gamut is Blackmagic Design’s sophisticated internal color space, furnishing an unusually wide and accurate arena for color grading and image processing. Coupled with the DaVinci Intermediate gamma, it yields one cohesive working space that eases color management across a mix of camera formats and holds tone and saturation mapping consistent from input through output. Well suited to HDR and Immersive media, this wide gamut lets colorists make subtle tweaks without courting banding or tonal clipping while mastering for high-fidelity delivery formats.

### Apple Immersive Processing

Within the Project Settings sidebar, the Apple Immersive section lets you supply custom ILPD (Immersive Lens Profile Data) to change how the immersive content gets calibrated and projected. 1 Pick Apple Immersive from the Project Settings sidebar. 2 Click Open Calibration Folder. 3 Drop in or refresh a custom ILPD file. 4 Click Update Lists so the ILPD content reachable in the Media Pool is refreshed. 5 Click Save to dismiss the Project Settings. 6 Over in the Media Pool, right-click an immersive clip. 7 From the contextual menu, head to Apple Immersive Calibration; here your choices are the source ILPD (‘No Apple Immersive Calibration File Selected’), a custom ILPD, or the gap ILPD. TIP: Out of the box, the folder holding the custom ILPD Calibration lives within ProIM, right beside the default LUT folder.

### Ingesting

As you import raw immersive content, both eyes plus every bit of associated immersive metadata come along inside the imported .braw clip. 1 Head to the media page. 2 In the Media Storage panel, browse to where the immersive video content lives. 3 Drag the media down into the Media Pool below. TIP: To preserve the original folder layout, drag folders out of the Media Storage panel onto the Media Pool sidebar. Dropped into the Master bin (or any bin you’ve made), the folders and their subfolders stay intact.

Select an Apple Immersive video clip and the codec parameter atop the Metadata panel labels it an Immersive Video, right next to its native frame rate and resolution. On top of that, a 3D icon down in the lower left of the video thumbnail likewise verifies it as a 3D clip.

The Metadata Panel displaying an immersive video The icon at lower left marking a 3D stereo clip

NOTE: The first time you drag immersive media into the Media Pool, a dialogue window may ask whether you want to Keep Settings or Change Settings. Picking Change Settings makes the Project Settings take on the source media’s frame rate and resolution on their own.

### Editing

While handling immersive content, the editing tools and actions stay largely identical to those you’d use on ordinary 2D video formats. The instructions that follow cover edit features and actions found only in immersive video workflows.

### Assembly

As you preview clips while assembling the timeline, you can switch which eye (left or right) the source viewer shows. Apart from that, building a cut on the timeline works just as it does in standard NLE workflows. 1 Head to the edit page. 2 Double-click a clip so it loads into the source viewer on the left. A label across the top of the viewer tells you which eye is on display.

The label up top tells you the left eye is what you’re viewing

3 To swap the eye shown in the viewer, right-click the source clip over in the Media Pool and pick Stereoscopic 3D > Stereoscopic 3D Mode > Left Eye/Right Eye/Both Eyes.

TIP: Hovering over the thumbnails in the Media Pool also scrubs clips in the source viewer, provided Live Media Preview is switched on in the source viewer options. 4 Lean on the I and O shortcuts to mark out a range in the source viewer. 5 Hit Insert Clip on the toolbar (or the F9 shortcut) to drop clips onto the timeline.

TIP: Dragging clips out of the Media Pool onto the timeline panel works as well. 6 Trim clips on the timeline with your mouse (while in Selection or Trim Edit mode).

### Backdrops

Tick ‘Enable Apple Immersive workflow’ in the Project Settings and a Backdrops track (‘BD’) shows up on its own beneath the Video 1 track. The term backdrops describes whatever the viewer sees once they look past the edge of the immersive video content, an edge usually capped at a 180–210 degree field of vision. That zone is black by default, yet you can drop custom background imagery (in the .usdz format) onto the backdrops track.

Pull a .usdz backdrop file onto the Backdrops track to place it on the timeline. A backdrop image’s duration has to line up with the clip boundaries over in the video tracks. One backdrop file may cover a single clip, several clips, or the whole timeline, but it can’t break partway through an immersive .braw clip (the so-called ‘L-cut’). Reach for the usual trimming controls to set the backdrop file’s length. Drag the .usdz file’s edge (while in Selection or Trim Edit mode) to change its length.

### Trim Controls

The , (comma) and . (period) commands are another option for inching the trim edge along a single frame per press. TIP: So that backdrops stay locked to the Immersive Video edits, switch on Snap mode from the edit page toolbar.

### Using the Viewer

As a default, the DaVinci Resolve page viewers present immersive clips inside the circular ‘lens space’. The visual lens calibration that projects the image comes from the camera and differs for each individual clip.

The DaVinci Resolve page viewers presenting an immersive clip inside the circular ‘lens space’ You can also flip the view mode over to LatLong or Viewport. 1 Down at the lower left of the timeline viewer, click the drop-down arrow beside the onscreen controls button. 2 Pick Immersive.

Pick Immersive from the timeline viewer’s drop-down menu to switch your view mode A fresh toolbar shows up over the viewer carrying further view options.

3 Click LatLong for an equirectangular projection of the image. This mode bends the image so it sits closer to the proportions of traditional 2D media, which smooths certain post-production tasks like tracking and compositing.

The LatLong option presents an equirectangular projection of an image 4 Click Viewport for a center cutout of the immersive scene framed as a square. This mode lets you read the scene’s correctly-proportioned details plainly on a standard monitor, though you’ll want to stay alert so no off-frame action slips by. Up top, the transform controls in the immersive toolbar let you tilt and pan the stereoscopic image within the frame and dial in the horizontal and vertical fields of view.

Picking Viewport gives you a center cutout of the immersive scene framed as a square

### Transitions

Moving from one immersive video clip to the next, you can make a straight cut, drag the handles flanking the clip to fade in or out, or apply a Dip To Color Dissolve effect. Transitions ought not be baked into the footage; instead the Apple Vision Pro renders them itself at playback. 1 Open the Effects panel. 2 In the sidebar, work your way to Toolbox > Video Transitions. 3 Pull Dip To Color Dissolve onto a cut point sitting between two clips.

### Dip To Color Dissolve effect

NOTE: Applying a transition demands sufficient trim data past the cut points of both clips. Without enough trim data (the ‘handles’), the transition won’t take. 4 Within the Inspector panel, open the Transition tab and tick Render Bypass. That guarantees the Apple Vision Pro renders the dissolve correctly. 5 From there, the rest of the parameters in the Dip To Color Dissolve Inspector let you change the transition’s duration, alignment, animation speed, and color.

Further parameters within the Dip To Color Dissolve Inspector panel
