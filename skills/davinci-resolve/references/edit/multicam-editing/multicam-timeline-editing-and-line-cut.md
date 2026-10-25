# Editing multicam clips in the timeline and referencing a line cut

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multicam editing.
[Chapter index](INDEX.md) / [Previous section](multicam-clip-adjustment-and-editing.md)
<a id="source-editing-multicam-clips-in-the-timeline"></a> <a id="source-grading-multicam-clips"></a> <a id="source-multicam-editing-part-2"></a> <a id="source-multicam-smartswitch-analyzing-the-multicam-clip"></a> <a id="source-multicam-smartswitch-finished-cut-on-the-timeline"></a> <a id="source-multicam-smartswitch-settings"></a> <a id="source-multicam-smartswitch-studio-version-only"></a> <a id="source-referencing-a-line-cut"></a> <a id="source-the-multicam-smartswitch-tool"></a>

### Editing Multicam Clips in the Timeline

For editing and trimming, there is no practical difference between multicam clips and clips of any other type. Since what you really add are through edits within one clip, any edit can be discarded by selecting it and tapping Delete. What sets multicam clips apart is that angle switching is always on the table, whether from the Multicam Viewer or right inside the Timeline through each clip’s contextual menu. To swap the angle of any multicam clip in the Timeline:

- Right-click any clip and pick a fresh angle from the “Switch Multicam Clip Angle” submenu. That also lets you change angles without resorting to the Multicam Viewer. Should you want to strip all unused angles from a multicam clip and “flatten” it down to a single Timeline clip, there is a command for the job.

To flatten a multicam clip in the Timeline:

- Right-click any clip and pick Flatten Multicam Clip from the contextual menu. Choose either Copying Multicam Grades, which applies the current color grade across the flattened angles, or Retaining Grades from Angles, which holds onto whatever color grades each individual angle received. All unused angles drop away, the clip shortens if it held black tails left by another unused angle, and what remains is a single plain clip in the Timeline.

To Match Frame to the angle of any clip set up for multicam in the Timeline:

- Set the playhead over the frame in the Timeline you wish to match and press F. The exact frame from the referenced mulitcam clip shows up in the Source Viewer, with its correct angle already selected.

To Match Frame to the multicam clip in the Source Viewer:

- Load the multicam clip into the Source Viewer. Use the jog bar to reach the frame you want and press F. The Timeline playhead moves to that exact frame within the referenced mulitcam clip shown in the Source Viewer. Should the frame you chose not exist in the Timeline, pressing F simply has no effect.

To cut an angle of any multicam clip straight out of the Source Viewer:

- You can drag any multicam angle straight from the Source Viewer onto the Timeline. The clip’s length is set by the In and Out point selection of the clip.

### Referencing a Line Cut

On occasion a production hands you what is termed a “line cut.” This is a pre-edited rendition of the program, cut live on the switcher and recorded during the performance or event, intended as a reference for your own work. Should that line cut reach you in movie form, bring it in as an Offline Reference Movie, then hold it up against the Timeline by way of the Source Viewer’s Offline Reference Movie mode on the Edit page. For more about checking an Offline video against a timeline within the Edit page, refer to Chapter 55, “Preparing Timelines for Import and Comparison.”

### Multicam SmartSwitch (Studio Version Only)

DaVinci Resolve 20 introduces a new AI-powered multicam feature named Multicam SmartSwitch, which examines every multicam camera angle and cuts automatically to the angle it judges best, going by who is currently speaking. Multicam SmartSwitch relies on more than the audio track to settle on the strongest angle; it also factors in further video signals — for instance lip motion inside the frame and whether a shot reads as wide or as a close up. Having learned from thousands of hours of multicam footage, Multicam SmartSwitch shines at handing you a strong first pass while you refine what is left.

Selecting a multicam clip to be used with Multicam SmartSwitch To set Multicam SmartSwitch loose on your multicam clip so it cuts on its own: 1 Assemble a multicam clip in the Media Pool out of every separate camera angle clip, in the manner described earlier here. 2 Cut that multicam clip onto the timeline. 3 Right-click the clip and choose Multicam SmartSwitch from its context menu. 4 Dial in the appropriate settings and parameters within the Multicam SmartSwitch tool. 5 Click Analyze.

### Multicam SmartSwitch analyzing the multicam clip

Now Multicam SmartSwitch will study every video angle and audio track and select the angle it considers strongest for the situation. This may take a while, depending on how long the multicam shoot runs and how many camera angles were used.

### Multicam SmartSwitch finished cut on the timeline

Once it is done, a fully cut version of your multicam clip waits for you in the timeline. If a choice Multicam SmartSwitch made isn’t to your liking, swapping the camera angle is easy: rightclick it and pick a different one from the Switch Multicam Clip Angle context menu, or use the standard trim tools to shift the edit point.

### The Multicam SmartSwitch tool

### Multicam SmartSwitch Settings

You can configure parameters on the Multicam SmartSwitch tool that change how it reaches its cut decisions.

- Angle Switching: Tunes the timing of the edits. Minimum Edit Duration: Sets the shortest an edit can run. No matter what unfolds in the cut, Multicam SmartSwitch will not switch angles until this duration ends. Edit Change Delay: This lets you specify the lag between someone speaking and the edit changing.
- Wide Angle Setup: Much like a technical director, Multicam SmartSwitch tends to lean on wide angles to cover situations such as people talking over one another and silences. You can fine-tune those behaviors here. Automatically detect wide angles: Tick this box to let Multicam SmartSwitch pick what it regards as wide shots on its own. Wide Angle: When you have a particular wide shot in mind for coverage, you can select it manually here. Wide Angle Frequency: How often Multicam SmartSwitch should return to the wide shot. The options are Low, Medium, and High. Use wide angle for intro and outro: Tick this box to begin and end the multicam clip on a wide shot. Use wide angle for silence: Tick this box to revert to the wide shot whenever nobody is speaking.
- SmartSwitch Setup: Establishes which kinds of media the analysis draws on. Switch: The cuts can be set to Video Only, or you can have them join Video and Audio tracks at the same time. Use Audio Only Fast Analysis: Tick this box so the pass leans solely on the audio rather than examining the picture too. It is much quicker and shows up only under certain modes.

### Grading Multicam Clips

In the Color page, multicam clips look like any other clip. Each angle inside a multicam clip, however, carries its own grade (unlike the Take Selector covered later, where all takes share one grade). When you grade a multicam clip, you are in fact editing the grade of whichever angle is currently exposed in that clip. To reach every angle within a multicam clip for grading, right-click it and pick “Open in Timeline” to lay out each angle in a superimposed stack. Then you can open the Color page and grade whichever angles you like, whether or not they are visible back in the Edit page. You might do this to bring the various angles into closer agreement, or to pre-grade all of them with the look you want ahead of multicam editing. You also have to use “Open in Timeline” to reach and adjust the camera RAW settings when your footage was captured in a RAW format.

A multicam clip opened on the Color page lays bare every one of its angles for grading one by one. Since opening such clips in the Timeline yields a vertical stack of superimposed clips, you will want Unmix switched on in the Color page viewer so the angle you have selected is actually visible in the Thumbnail Timeline while you work.

With the Unmix control you can isolate a single clip out of a stacked, superimposed set. As you flatten a multicam clip, there's a choice between grading each angle on its own or grading the multicam clip together as one. On the Edit page, pick Flatten Multicam Clip, then either Copying Multicam Grades, which pushes the current color grade onto the flattened multicam angles, or Retaining Grades from Angles, which preserves whatever color grades were already applied to the separate angles. Once your grading is finished, head back to the Edit page and click the path control over in the bottom left-hand corner of the Timeline to step back up to your edited Multicam timeline.
