# Effects library and edit index

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Previous section](effects-library-browsing.md) / [Next section](work-area-and-viewers.md)
<a id="source-a-new-floating-timecode-window-is-available"></a> <a id="source-an-edited-timeline"></a> <a id="source-buttons-in-the-toolbar"></a> <a id="source-edit-index"></a> <a id="source-edit-index-list-shown-open"></a> <a id="source-floating-timecode-window"></a> <a id="source-inspector"></a> <a id="source-motion-graphics-and-visual-effects-in-davinci-resolve"></a> <a id="source-single-viewer-mode"></a> <a id="source-source-and-timeline-viewers"></a> <a id="source-sourceoffline-and-timeline-viewers"></a> <a id="source-the-effects-library"></a> <a id="source-the-fusion-page"></a> <a id="source-the-inspector-opened-and-showing-a-clips-parameters"></a> <a id="source-the-new-vfx-connect-clip-dialo"></a> <a id="source-timeline"></a> <a id="source-toolbar"></a> <a id="source-vfx-connect"></a>

### The Effects Library

### Edit Index

Pressing the Index button brings up the Edit Index, which by default presents an EDL-style list of every edit event in the timeline you're working on. The events shown belong to whichever timeline is highlighted in the Timeline list; every clip and every transition appears as its own event, and each event carries several columns of detail. Should you re-edit a timeline, the list updates on its own to mirror what you changed.

### Edit Index List shown open

### Source/Offline and Timeline Viewers

Use the Source Viewer to look at individual clips drawn from the Media Pool and ready them for editing. The Timeline Viewer, by contrast, displays the frame sitting under the playhead in the Timeline. A click selects either viewer, and whichever one holds focus has its name rendered in orange. Typically the Source Viewer's color matches the original source media, whereas the Timeline Viewer reflects any grade you applied over in the Color page.

### Source and Timeline Viewers

Should you wish to reconfigure the Edit page so the Source Viewer is concealed, pick Workspace > Single Viewer Mode; this hides the Source Viewer and leaves a single viewer that contextually presents either a chosen Source Clip or the Timeline's current frame.

### Single Viewer mode

While Single Viewer mode is active, your selection in the Media Pool or Timeline governs which controls show up in the Viewer, which lets you accomplish nearly anything you could with two viewers open simultaneously. Either the Source or Timeline Viewer can likewise be switched into Cinema Viewer mode through Workspace > Viewer Mode > Cinema Viewer (Command-F), which makes the currently selected viewer expand to cover the whole screen. Issuing this command again toggles Cinema Viewer mode off.

### Inspector

Open the Inspector to fine-tune compositing, transform, and cropping parameters on clips, along with clip-specific retime and scaling choices. On top of that, the Inspector lets you tweak the parameters of transitions, titles, and generators placed in the Timeline so you can tailor their look. Normally the Inspector appears next to the Source and Timeline Viewers, yet on smaller screens opening it flips the Edit page into single-viewer mode, presenting the Timeline item under inspection beside the Inspector loaded with that clip's parameters.

### The Inspector, opened and showing a clip’s parameters

### Toolbar

A row of eleven buttons, beginning at the left and stretching across the top of the Timeline, gives you a choice of tools for carrying out the various editing tasks.

### Buttons in the toolbar

### Timeline

The Timeline presents whatever timeline you double-clicked over in the Timelines browser. It is the space where you assemble programs from the ground up, or bring in sequences authored elsewhere to refine inside Resolve. No more than one Timeline may be open at any moment. It splits into audio and video tracks, and every track carries header controls along its left edge that let you pick destination tracks for editing, label tracks, and switch tracks on or off, among other functions. You can tailor how the Timeline looks via the Timeline View Options drop-down found in the toolbar.

### An edited timeline

### Floating Timecode Window

Every page, the Edit page included, offers a timecode window through the Workspace menu. Selecting it brings up a floating timecode window reporting the timecode of whichever Viewer or Timeline currently holds focus. Because the window is resizable, you can scale the timecode up or down.

### A new floating timecode window is available

### Motion Graphics and Visual Effects in DaVinci Resolve

For starters, DaVinci Resolve packs an abundance of effects across both the Edit and Color pages for building titles, transforming and animating clips, compositing and producing transparency effects, pulling mattes, running filters, stabilizing footage, dewarping lenses, and more. On top of that there's the Fusion page, which contributes far more potent VFX and motion graphics power through its node-based interface and rich toolset of effects nodes, keyframing and curve editing controls, plus 2D and 3D compositing features. Getting the most out of DaVinci Resolve means learning to regard the Edit, Fusion, and Color pages as complementary banks of controls.

- To an editor, the Fusion and Color pages amount to a pair of oversized inspectors; one stocked with

each compositing tool you might ever want, the other stocked with each color and visual adjustment control you might wish for, and both of them sit just a single click away.

- For compositing artists, the Edit page can be regarded as a capable shot management surface and also a chance to do VFX work that's tightly woven into the edit of the program at hand.
- For colorists, the Edit page offers a polished space for handling conform problems and knocking out countless finishing chores swiftly and effortlessly, and it sits a single click away.

If you want more detail on the effects DaVinci Resolve makes available, consult the chapters in Part 6, “Editing Effects and Transitions” and Part 11, “Color Page Effects”.

### VFX Connect

However capable DaVinci Resolve's native compositing has become, there are times when the features across the Edit, Fusion, and Color pages still fall short of the effect you're after; in those cases you can turn to DaVinci Resolve's VFX Connect features to dispatch one or several clips from the Edit page Timeline over to Blackmagic Fusion, Blackmagic Design's potent node-based compositing application, and carry out heavier compositing and effects work there. Beyond that, the VFX Connect feature can also round-trip media out to, and bring rendered results back from, external programs like Nuke from The Foundry, Autodesk Flame, or Blender. It's a straightforward round-trip step: it dispatches clips off the DaVinci Resolve timeline into Fusion or some other application, where you layer on effects and wrap up whatever needs doing before rendering a finished effect file that, provided it's named properly, comes back to your timeline on its own. With Blackmagic Fusion, VFX Connect creates a project file for you automatically and names the render path automatically so it links back from the DaVinci Resolve timeline on its own. When you use the feature with third-party applications, you'll have to set up the naming of your rendered effect file by hand. For more on this, refer to Chapter 63, “Introduction to Compositing in Fusion.”

### The New VFX Connect Clip dialo

### The Fusion Page

The aim for the Fusion page is that it will in time grow into a fully featured embedding of Blackmagic Design Fusion, a capable application for 2D and 3D compositing that boasts more than thirty years of refinement in service of the film and broadcast world, responsible for effects featured in countless films and television series. Folded straight into DaVinci Resolve with a freshly revised user interface, the Fusion page lets you leap right from editing into compositing, with no requirement to export media, relink files, or fire up a separate application to finish the job. Everything you require now sits inside DaVinci Resolve.

The Fusion page with its Viewers, Node Editor, and Inspector on display To dig deeper into working on the Fusion page, refer to Chapter 63, “Introduction to Compositing in Fusion.”
