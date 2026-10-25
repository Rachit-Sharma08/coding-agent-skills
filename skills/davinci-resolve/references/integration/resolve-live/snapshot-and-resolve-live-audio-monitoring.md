# Snapshot and resolve live audio monitoring

Version: DaVinci Resolve 20.3 Reference Manual. Context: Resolve live.
[Chapter index](INDEX.md) / [Previous section](resolve-live-system-configuration.md)
<a id="source-resolve-live-audio-monitoring"></a> <a id="source-using-luts-in-resolve-live-workflows"></a> <a id="source-using-resolve-live-grades-later"></a> <a id="source-using-snapshot"></a>

### Using Snapshot

After you're satisfied with a grade, hitting the Snapshot button stores a snapshot of the still currently in the Viewer, the arriving timecode value, and your grade onto the Timeline. Snapshots are nothing more than single-frame clips. They carry grades and versions exactly like every other clip. Truthfully, in the end there's no real distinction between the timeline a Resolve Live session produces and any other timeline, apart from the fact that the Resolve Live timeline holds only a run of one-frame clips, which surface in the Edit page Timeline as a string of 1-frame stills. Storing a snapshot can be done either way below:

- Click the snapshot button (with a camera icon).
- Choose Color > Resolve Live Snapshot (Command-Option-R).

The snapshot button saves a frame and the grade for future use

As an illustration, you might kick off the work of crafting and polishing a grade for a given scene during an unrecorded rehearsal. Then, once cameras roll, you might grab snapshots of each shot's slate, followed by the meaningful takes that come after, adjusting as needed and in step with the DP's notes once momentum builds. Fresh camera setups might call for more adjustments, which you'll store as snapshots for those shots, and working this way you'll find a timeline of snapshots tied to that day's shoot steadily taking shape. While you work, bear in mind that you have to briefly switch Resolve Live off to open a grade from an earlier snapshot on the Timeline so you can reuse it as a starting point for a different shot. Grades can also be stored into the Gallery.

### Resolve Live Audio Monitoring

With Resolve Live in use, you're now able to hear the audio feed from the camera arriving at the Decklink or Ultrastudio device as you grade. Flip this behavior on or off by clicking the speaker icon below the Viewer.

Clicking the speaker icon switches the audio on and off throughout a Resolve Live session.

### Using Resolve Live Grades Later

Because every Snapshot you grab in a Resolve Live session carries timecode that came off the camera, grades from snapshots whose timecode lines up with recorded camera original media can be synced through ColorTrace once it's time to begin building dailies. Bear in mind that snapshot grades match the monitored camera output during the shoot. If your shoot used a raw format, you'll have to apply whatever in-camera debayering settings drove monitoring on set if you want your snapshot grades to land on the same result. To learn more about working with ColorTrace, see Chapter 149, “Copying and Importing Grades Using ColorTrace.”

### Using LUTs in Resolve Live Workflows

Plenty of on-set workflows lean on Lookup Tables (LUTs) for calibrating displays, normalizing log-encoded footage for monitoring, and previewing looks in the video village to gauge how the current lighting setup will pair with the planned grade. You can bring LUTs in by way of the Lookup Tables area within the Project Setting's Color Management panel, or fold them into a grade as a piece of a node tree. You can equally export LUTs, where monitor previewing calls for it, then apply them by loading them into some compatible LUT box wired between the camera's video output and a display, or via a display able to load LUTs on its own. When exporting LUTs through the Generate 3D LUT command on the Thumbnail timeline's contextual menu, hold yourself to only Primaries palette and Custom Curves palette controls inside a single node. Those are the lone grading controls that can be mathematically turned into a LUT. During LUT export, any node relying on Windows or OpenFX gets skipped, along with every correction performed inside such nodes. Every other node carrying Primaries palette and Custom Curves palette adjustments that convert into a LUT will have its combined result translated into a LUT. For any node mixing supported and unsupported adjustments where LUT export is concerned (sharpening or blur filtering operations, say), the unsupported adjustments are simply dropped. To learn more about exporting LUTs, under “Exporting Grades and LUTs” see Chapter 142, “Grade Management.”

NOTE: DaVinci Resolve writes LUTs out in the .cube format, a LUT format developed by DaVinci that bears no connection to the Adobe SpeedGrade.cube format.
