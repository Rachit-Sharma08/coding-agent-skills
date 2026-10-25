# Rendering versions and copying grades

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grade management.
[Chapter index](INDEX.md) / [Previous section](deleting-unused-versions.md) / [Next section](copy-forward-commands-and-copying-using-memories.md)
<a id="source-applying-saved-grades-from-the-gallery"></a> <a id="source-choosing-how-to-copy-keyframes"></a> <a id="source-copy-and-paste-from-one-clip-to-another"></a> <a id="source-copy-and-paste-specific-parameters-using-paste-value"></a> <a id="source-copying-grades"></a> <a id="source-copying-grades-using-the-pointer"></a> <a id="source-node-editor-clip-and-track-selector"></a> <a id="source-preparing-to-copy-or-apply-grades"></a> <a id="source-protecting-adjustments-with-the-copy-grade-options"></a> <a id="source-rendering-versions"></a>

### Rendering Versions

Once you reach the Deliver page to render clips, whatever version each clip currently has selected is the one rendered. To render a different version for some clip, either confirm it's the selected one in the Color Page timeline before opening the Deliver page, or reach for the Versions submenu within the Color mode of the Deliver page Thumbnail timeline. That contextual menu likewise reaches the Stereo 3D commands, plus the Edit PAR (Pixel Aspect Ratio) command, along with one for refreshing the Render Window Timeline thumbnails so your recent changes show, in case they didn't refresh on their own. On top of that, the Deliver page's Commercial Workflow output option offers a way to render several versions per clip when your project goes out in Source Order (as individual media files). Two further options sit in the Version submenus of each Thumbnail timeline clip's contextual menu, governing which versions render under Commercial Workflow. Render Disabled: Switch this on and that version is left out of the render while Commercial Workflow is active. Enable Flat Pass: Switch this on and the chosen version renders with its grade off, so essentially the original media is what comes out. To read more about rendering versions through the Commercial Workflow option, consult “Rendering Media” at Chapter 187.

### Copying Grades

Several techniques exist for copying grades between clips, and the right one for you comes down to how you like to work in DaVinci Resolve.

### Protecting Adjustments with the Copy Grade Options

Ahead of the many ways grades travel from clip to clip, it helps to know about a set of options reached from the Gallery's contextual menu (right-click anywhere in the Gallery's gray area) that let you spell out exactly which grading, sizing, and stereo data survive when you overwrite grades on the clips you copy to. Three options exist: Copy Grade: Preserve number of nodes: Lets you set 0–10 nodes to shield while a grade is applied. At 1, the copied grade's first node is skipped while the rest carry over. At 5, the first five nodes of the copied grade are skipped, provided the clip you're copying to already holds at least five nodes. The option suits colorists who habitually devote the opening nodes to shot matching and scene balancing, leaving later nodes for individual or stylistic touches.

Copy Grade: Preserve Camera Raw Settings: Switch this on and the current clip's camera raw Source settings hold firm, so you can borrow stylistic grades from unrelated clips without trampling clip-specific source settings. Copy Grade: Preserve Input Sizing: Switch this on to keep Input Sizing adjustments safe from the copied grade's own. Copy Grade: Preserve Convergence: Switch this on so the Stereo 3D palette's Convergence adjustments stay put rather than yielding to the copied grade's. Copy Grade: Preserve Floating Windows: Switch this on so the Stereo 3D palette's Floating Windows adjustments aren't replaced by the copied grade's. Copy Grade: Preserve Auto Align: Switch this on so the Stereo 3D palette's Auto Alignment adjustments survive the copied grade. Copy Grade: Preserve Dolby Vision™ Analysis Metadata: Switch this on to keep the Dolby Vision Analysis Metadata clear of the copied grade's. It's only there once you're configured for Dolby Vision grading. The relevant background sits in “Data Levels, Color Management, and ACES,” which is Chapter 9. Copy Grade: Preserve Dolby Vision™ Trim Metadata: Switch this on to keep the Dolby Vision palette's Dolby Vision Trim Metadata clear of the copied grade's. It too only appears when you're configured for Dolby Vision grading. Again, Chapter 9 — “Data Levels, Color Management, and ACES” — has the fuller picture.

### Copy and Paste From One Clip to Another

Reaching for the very same Edit > Copy and Paste commands found in nearly every application ever built is the easiest route to lifting color adjustments off one clip and dropping them onto another. That plain functionality works one of two ways, though, depending on where the interface focus sits.

- Click the clip over in the Thumbnail Timeline and you carry the whole grade from one clip to the next.
- Click inside the Node Editor and only the selected node moves across to another selected node.

You can override this focus-driven behavior so that, no matter where the interface focus lands, copying defaults to node-to-node rather than whole grades. To do so, tick the “Always perform copy and paste on selected nodes” box found in the Color section of the User panel in Preferences.

Methods of copying and pasting grades and node adjustments.

- To copy and paste an entire grade: Pick a clip whose grade you want and press Command-C. Then, in the Thumbnail Timeline, select the destination clip and hit Command-V to drop the full grade in.
- To copy and paste a single node: Pick a clip whose node you want and press Command-C. Then select the destination clip in the Thumbnail Timeline, click anywhere within the Node Editor, and hit Command-V to paste the node you had selected at copy time onto the node currently selected in the node tree.

### Copy and Paste Specific Parameters Using Paste Value

With the Edit > Paste Value (Shift-Option-V) command you can drop only one parameter's value into another clip's node. To paste just a single value: 1 Select a Corrector node carrying the parameter you want and press Command-C to copy. The whole grade is what you actually copy, but that's fine. 2 Move to any other node in any grade and open the palette that holds the parameter you'll paste into. 3 Double-click the number field of the exact parameter that should receive the copied value. 4 Pick Edit > Paste Value (Shift-Option-V) to drop that value in. NOTE: Paste Value applies only to parameters inside palettes; it has no effect on OFX or Resolve FX over in the Inspector.

### Applying Saved Grades From the Gallery

Each still you stash in the Gallery or a memory carries both the Clip grade and, where one exists, the Timeline grade. Which of those a still applies through the Apply Grade or Append Node Graph commands hinges on the Node Editor's current mode, picked from the drop-down at the Node Editor's top-right corner.

### Node Editor Clip and Track selector

In Clip mode you pick up only the saved clip grade; in Timeline mode you pick up only the saved timeline grade. NOTE: The same mechanism covers saving and applying grades for clips that belong to Groups. Whichever group grade is active in the Node Editor decides which grade a still stores, and whichever mode is active in the Node Editor decides where a saved grade lands.

### Preparing to Copy or Apply Grades

For every other way of copying or applying grades laid out in this chapter, a handful of shared controls dictate how the adjustments from your source clip or still reach the destination clip. Picking the part of a grade that applies through All/Color/Sizing No matter which technique in this section you use to apply grades, the All/ Color/Sizing setting is on hand through the Mark > Keyframe Timeline Mode submenu — the dropdown over at the Keyframes Editor's upper-right. Copy a grade alongside this menu's settings and these rules hold:

- All: Pick All and both the grade and the sizing come across.
- Color: Only the grade transfers; the target clip keeps its own Input Sizing settings.
- Sizing: Only the Input Sizing transfers; the target clip keeps its own grade.

### Choosing How to Copy Keyframes

When the grades you copy or apply carry keyframes, you decide how those keyframes travel via a setting in the Gallery contextual menu — right-click anywhere in the Gallery's gray background and pick one of the choices in the Apply Grades Using submenu. Three choices await:

- No Keyframes: Nothing is copied keyframe-wise. The grade's state at the frame where the still was saved is what reaches the target clip or clips.
- Keyframes Aligning Source Timecode: The keyframes come across with the saved grade's source timecode matched up against the target clip's source timecode. It's the setting you want when returning a grade to the clip it first came from, or to a duplicate of that clip elsewhere on the Timeline, so the keyframes sit on the same frames as before. Where no source timecode overlaps, the keyframes paste against the edit's start frame instead, just like the third choice below.
- Keyframes Aligning Start Frame: The keyframes come across with the start frame of the clip the still was saved from matched against the target clip's start frame. It's the setting you want when carrying a keyframed grade from one clip onto an entirely different clip whose timecode differs.

From there on, any keyframes that exist get copied or applied by the chosen method whenever you copy a grade through any of the techniques described earlier.

### Copying Grades Using the Pointer

A remarkably quick route for moving a grade between clips — or from a Gallery still or memory onto a clip — is your mouse's third button, typically the “middle‑click” of the scroll wheel. To copy a grade from a clip or still onto one or more clips with the pointer: 1 In the Timeline, select the clip thumbnail meant to receive the grade; a lone selected clip glows orange. To target several clips, Command‑click various non-adjacent ones or Shift-click an unbroken run of them, and those multiple selected clips glow red. 2 Middle-click the clip thumbnail, Gallery still, or memory whose grade you want to lift.

Whatever clip you middle-clicked has its grade copied onto the clip or clips you'd selected beforehand. TIP: On a trackpad, third-party software might let you set up a “three‑fingerclick” acting as mouse button 3. Pen-and-tablet or trackball users may likewise assign a stylus or other button to the same button-3 action. Lacking a middle-click on your pointing device, a contextual menu command offers another way through. To copy a grade from a clip or still onto one or more clips via the Apply Grade command: 1 In the Timeline, select the clip thumbnail meant to receive the grade; a lone selected clip glows orange. To target several clips, Command-click various non-adjacent ones or Shift-click an unbroken run of them, and those multiple selected clips glow red. 2 Right-click the clip thumbnail, Gallery still, or memory whose grade you want, then pick Apply Grade from the contextual menu. Whatever clip you middle-clicked has its grade copied onto the clip or clips you'd selected beforehand.
