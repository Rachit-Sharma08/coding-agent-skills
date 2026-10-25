# Assigning a clip or timeline for offline comparison

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing timelines for import and comparison.
[Chapter index](INDEX.md) / [Previous section](about-supported-composite-modes-and-fcp-7-x-xml.md) / [Next section](offline-reference-timeline-comparison.md)
<a id="source-assigning-a-clip-or-timeline-for-offline-comparison"></a> <a id="source-preparing-timelines-for-import-and-comparison-part-2"></a>

### Assigning a Clip or Timeline for Offline Comparison


You have two methods available for attaching an Offline Reference Clip or Timeline to a given timeline so it can be compared. The simplest and most adaptable approach is to first open a timeline, then drag a clip or timeline whose timecode matches what you want to check against out of the Media Pool and drop it onto the Source Viewer while it is in Offline mode. To attach any clip or timeline to a chosen timeline for comparison: 1 In the Edit page, open the timeline you intend to attach to. 2 Switch the Source Viewer into Offline mode. 3 Drag the clip or timeline whose timecode matches onto the Source Viewer to assign it. Whatever you dragged is instantly attached to the open timeline as an Offline Reference Clip and kept in sync by timecode. 4 Within the Media Pool, right-click the Timeline you intend to compare against the Offline Reference Clip, then pick the reference clip or timeline you attached from that timeline’s contextual menu under the Timelines > Link Offline Reference Clip submenu. Alternatively, you may bring a clip into the Media Pool directly as an Offline Reference Clip, which makes pairing it with a specific timeline simple: right-click that timeline in the Media Pool and select it from the Link Offline Video submenu. The concept here is that whenever you or your client outputs a flattened rendering of their cut sequence alongside the EDL, AAF, or XML project file that needs grading, you are then able to check the project information loaded into DaVinci Resolve against the real video of the offline cut. To attach an imported Offline Reference Clip to a chosen timeline for comparison: 1 Go to the Media page and browse with the Media Storage browser until you locate the flattened Offline Reference Clip you wish to use for comparison. 2 Right-click that Offline Reference Clip file and pick Add as Offline Reference Clip. 3 The clip then shows up in the Media Pool carrying a tiny checkerboard badge on its icon.

Checkerboard indicating an offline video 4 Switch to the Edit page, right-click the timeline you intend to compare against the Offline Reference Clip, then select the offline clip you brought in from the Timelines > Link Offline Reference Clip submenu.

Selecting the offline video to link to the current Timeline.
