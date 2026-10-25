# Step 2 generate 3D stereo clips and step 3 optional create optimized media

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](media-326-and-hardware-requirements-for-working-in-stereo-3d.md) / [Next section](grading-windows-and-a-convergence-adjusted-window-in-stereo.md)
<a id="source-attaching-mattes-to-stereo-3d-clips"></a> <a id="source-controls-for-aligning-the-left--and-right-eye-media"></a> <a id="source-converting-clips-between-stereo-and-mono"></a> <a id="source-converting-mono-clips-or-an-entire-timeline-to-stereo"></a> <a id="source-converting-stereo-clips-back-to-mono"></a> <a id="source-monitoring-stereoscopic-3d-in-the-edit-page"></a> <a id="source-organizing-and-grading-stereo-3d-dailies"></a> <a id="source-step-1--create-3d-stereo-clips"></a> <a id="source-step-2--edit-the-new-stereo-clips-into-one-or-more-timelines-for-grading"></a> <a id="source-step-2--generate-3d-stereo-clips"></a> <a id="source-step-3--align-your-media"></a> <a id="source-step-3--optional-create-optimized-media"></a> <a id="source-step-4--grading-stereo-media"></a>

### Step 2 – Generate 3D Stereo Clips

With your media properly arranged, you’re ready to line up the left- and right-eye clips by timecode. 1 Add a new bin in the Media Pool and call it “Stereo Clips.” This bin will hold the linked stereo clips you’re about to generate.

How to organize media for working in stereo 3D

2 Right-click anywhere inside the Media Pool and pick Stereo 3D Sync. Up comes the Stereo 3D Sync dialog, offering buttons to select the left-eye folder, the right-eye folder, and the output folder, checkboxes to say whether reel names and file names should match, and extra fields for typing the characters that mark left- and right-eye clips.

The Stereo Media Sync window 3 Press the Browse button next to “Choose left eye folder,” then use the nested list of bins that opens to select the bin you called “Left.” Repeat the same steps for the right-eye media. 4 Press the Browse button next to “Output folder,” then use the nested list of bins that opens to select the bin you called “Stereo Clips.” 5 Decide which matching criteria to apply. Ideally you’ll use only whichever one of the three fits. The three choices are: Match Reel Name: switch this checkbox on if the reel names of the left- and right-eye media agree. Match File Name checkbox: switch this checkbox on if the file names of the left- and right-eye media agree. Left Identifiers and Right Identifiers fields: when a particular subset of characters inside the file name distinguishes the left- and right-eye clips (say, “3D_R” and “3D_L”), type each one into its field and those characters will pair the left and right eyes. 6 Press Sync. The starting clips in the Left and Right bins vanish, and a complete set of Stereo 3D clips shows up in the output bin you picked back in step four.

Final stereo clips, ready to be edited and graded

### Step 3 – (Optional) Create Optimized Media

Should your stereo media be unusually large, optimized media is an option. 1 Pick the stereo clips you’ve made. 2 Right-click one of the chosen clips and select Generate Optimized Media from the contextual menu. A window opens telling you how long the optimized media will take to finish.

### Monitoring Stereoscopic 3D in the Edit Page

A Stereoscopic 3D signal can now be viewed straight from the Edit page. In the past, the Edit page limited video output monitoring to the left eye only. The Edit Page Viewer still presents just one eye, yet it now sends Stereoscopic 3D video out through the Decklink or Ultrastudio video outputs. Over in the Color page, the 3D palette holds the stereoscopic controls for picking the stereo viewing options (Side by Side, Anaglyph, Line by Line, and so on) and for tuning convergence along with the other stereoscopic parameters.

### Converting Clips Between Stereo and Mono

A pair of Media Pool commands also gives you the choice of switching clips between mono and stereo 3D.

### Converting Stereo Clips Back to Mono

When the need arises, a single command splits one or more stereo clips back into mono clips. To turn stereo clips into mono clips: 1 In the Media Pool, highlight at least one stereo clip. 2 Right-click any of the highlighted clips and select Split Stereo 3D Clips from the contextual menu. Two fresh bins named Left and Right then appear, each holding the separate left- and right-eye clips you’ve pulled apart.

### Converting Mono Clips or an Entire Timeline to Stereo

Clips that aren’t stereo (those lacking separate left- and right-eye media files) can be turned into stereo clips one at a time or across a whole timeline, for either of two reasons:

- You might convert non-stereo clips to stereo so they fit into a stereo project and output correctly with the rest of a stereo timeline, though without adjustable convergence or depth effects.
- When you’d like to grade both an HDR and a non-HDR version of your program simultaneously, converting non-stereo clips to stereo lets you a) keep two distinct SDR and HDR grades per clip in a timeline by way of the left- and right-eye channels, and b) route the SDR and HDR signals out independently over your compatible Blackmagic Design interface’s left- and right-eye SDI outputs, provided you’ve enabled “Use dual outputs on SDI” — that checkbox lives in the Video Monitoring section, under the Master Settings panel within the Project Settings.

To turn mono clips into stereo clips: 1 In the Media Pool, highlight at least one non-stereo clip. 2 Right-click any of the highlighted clips and select Convert to Stereo from the contextual menu. That clip then shows up in the Media Pool as a Stereo 3D clip, and once it’s edited into a timeline it can reveal its controls in the 3D Stereo palette in the Color page. When a whole timeline is filled with clips you’ve just converted to stereo using the steps above, you must also set the Timeline itself to stereo before you can build stereo grades for each clip. To give a timeline stereo grades for simultaneous HDR/SDR output during grading:

- Right-click a timeline in the Media Pool and pick Timelines > Set Timeline to Stereo.

For more on running stereo timeline workflows for simultaneous HDR and SDR grading, consult Chapter 9, “Data Levels, Color Management, and ACES.”

### Attaching Mattes to Stereo 3D Clips

When you’ve got left- and right-eye mattes to attach to stereo clips, the steps mirror those for importing mattes onto ordinary clips, the difference being that selecting a stereo 3D clip in the Media Pool surfaces a pair of dedicated commands: “Add As Left Eye Matte,” along with “Add As Right Eye Matte.”

### Organizing and Grading Stereo 3D Dailies

One frequent workflow is producing digital dailies inside DaVinci Resolve ahead of editing in an NLE. This gives editors, the director, and producers nicer-looking media to work with that’s also easier on the eyes, provided you run the automatic geometry and colormatching functions that pair the media of each shot together for a first-pass left- and right-eye balance. The Timelines that come out of this can then be exported to whatever media format proves most convenient.

### Step 1 – Create 3D Stereo Clips

When making dailies, the opening step is to bring every left-eye and right-eye media file into its own organized bin and then link them up into stereo 3D clips, exactly as the previous section laid out.

### Step 2 – Edit the New Stereo Clips Into One or More Timelines for Grading

With a set of Stereo 3D clips now in hand, you can cut them into one or more Timelines for grading. The simplest route is to make a new Timeline while leaving the Empty Timeline checkbox deselected. A new Timeline then appears already populated with the stereo 3D clips you built.

### Step 3 – Align Your Media

If the stereoscopic effect is to work without giving viewers headaches, keeping both eyes aligned is essential. Dialing this in by hand can be fiddly, but it’s something the software can analyze on its own. You can run stereo 3D alignment on one clip via the Stereo 3D Palette controls, or you can pick a span of clips and align them all automatically in a single pass. Two alignment methods exist, and the better fit depends on the kind of geometry problems you’re facing.

- Transform Alignment: Examines the image and applies vertical and rotational tweaks to bring the left- and right-eye images into the closest possible match.
- Vertical Skew: Examines the images and applies a vertical-only tweak to bring the left- and right-eye images into line.

### Controls for aligning the left- and right-eye media

### Step 4 – Grading Stereo Media

Grade the Timeline’s clips just as you would any other digital dailies, the one extra task being to use the Stereo 3D palette controls to govern monitoring and handle whatever per-eye adjustments are called for. Whichever eye is currently selected is the one the video scopes show. Exactly as with any other dailies, you’re free to apply LUTs, the Timeline Grade, and clip-by-clip grading to make whatever changes are needed to yield media that’s useful for editing.
