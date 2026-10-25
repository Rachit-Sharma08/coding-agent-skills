# Duplicate frame detection and comparing timelines

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating and working with timelines.
[Chapter index](INDEX.md) / [Previous section](timeline-scrolling-and-wheel-controls.md)
<a id="source-comparing-timelines"></a> <a id="source-comparison-window-playhead-output"></a> <a id="source-duplicate-frame-detection"></a> <a id="source-highlighting-differences"></a> <a id="source-the-change-list"></a> <a id="source-the-change-list-of-the-timeline-comparison-window"></a> <a id="source-the-timeline-comparison-window"></a> <a id="source-the-timeline-comparison-window-1"></a>

### Duplicate Frame Detection

For clips in the Timeline, Duplicate Frame Detection (often shortened to Dupe Detection) is switched on by choosing View > Show Duplicate Frames. That places colored bars atop Timeline clips anywhere a range of frames has been reused.

Wherever a frame range gets used more than once in a timeline, Duplicate Frame Detection marks it with colored bars.

### Comparing Timelines

For cases where you're bringing in several versions of a timeline edited in another application, or where you and other editors are working on different versions of the same Timeline in collaborative mode or across separate DaVinci Resolve installations, DaVinci Resolve gives you a way to compare two timelines against each other. Through the Timeline Comparison window, you can both see a visual comparison of where two timelines diverge and assemble a more traditional change list by opening the Difference Index. To set two timelines side by side: 1 Bring up the first of the timelines you mean to compare. 2 Over in the Media Pool, right-click a second timeline and pick Compare With Current Timeline. Up comes a Timeline Comparison window, laying the currently open Timeline across the bottom and the Timeline you right-clicked across the top.

### The Timeline Comparison Window

The first time you open the Timeline Comparison window, the first thing in front of you is a pair of miniature timelines. The currently open Timeline sits at the bottom while the Timeline you right-clicked sits at the top.

### The Timeline Comparison window

### Comparison Window Playhead Output

Out of the box, the two playheads are ganged together, the top playhead appearing in the Source Viewer and the bottom playhead appearing in the Timeline Viewer. You can ungang these playheads to compare different parts of both timelines, simply by switching off Sync Playheads in the option menu.

### Highlighting Differences

Special highlights point out the sections of both timelines that differ. Individual changes aren't highlighted one by one, though they remain visible, on the assumption that you care more about a section-by-section read of what your collaborating editor has been up to, so you can decide whether to fold in changes or reversions based on this comparison.

Each section of differences between the two timelines are highlighted While using this tool, you can bring the bottom Timeline in line with the top Timeline, one section at a time: right-click a highlighted section, then pick Accept Change off the contextual menu. The moment you do, the currently open Timeline updates straight away to fold in the altered section from the Timeline you're comparing against. You can undo this if you have to.

### The Change List

Clicking the Diff Index button opens the change list, which gives you a more conventional item-by-item comparison of where the two timelines differ.

### The change list of the Timeline Comparison window
