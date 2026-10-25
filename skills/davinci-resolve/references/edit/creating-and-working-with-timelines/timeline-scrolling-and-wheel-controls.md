# Scrolling through the timeline and scroll wheel controls on timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating and working with timelines.
[Chapter index](INDEX.md) / [Previous section](naming-timeline-tracks-and-the-tracks-index.md) / [Next section](duplicate-frame-detection-and-comparing-timelines.md)
<a id="source-move-playhead-to-mouse-pointer-using-the-c-key"></a> <a id="source-resizing-the-timelines-video-and-audio-track-regions"></a> <a id="source-scroll-wheel-controls-on-timeline"></a> <a id="source-scrolling-through-the-timeline"></a> <a id="source-stacked-timelines"></a> <a id="source-stacked-timelines-1"></a> <a id="source-tabbed-and-stacked-timelines"></a> <a id="source-tabbed-timelines"></a> <a id="source-the-button-for-adding-a-stacked-timeline"></a> <a id="source-the-button-for-closing-a-stacked-timeline"></a> <a id="source-view-and-edit-dual-timelines-using-the-source-viewer"></a>

### Scrolling Through the Timeline

Once you're zoomed into the Timeline, several approaches let you scroll around as you work.

- Dragging the Timeline's horizontal and vertical scroll bars lets you move left and right, or up and down.
- Moving left and right through the Timeline one “page” at a step at the present zoom level is done by choosing Playback > Next/Previous > Timeline Page. Where you call on these often, assigning them a keyboard shortcut helps.
- Moving up and down the Timeline's tracks is also possible with the scroll wheel, scroll ball, or scroll gestures of whatever mouse, trackball, trackpad, or other pointing device you use.
- You can also scroll within the Timeline by middle-clicking and dragging any direction, which behaves the same as panning around a viewer you've zoomed into. That spares you from relying on the scroll bars as you move among your edited clips. Should you scroll past where the playhead sits, a small playhead indicator shows up in the bottom scroll bar to tell you where it is relative to the full length of your edited sequence.

Should the playhead fall beyond the Timeline's visible area, a small indicator marks where it sits.

### Scroll Wheel Controls on Timeline

Extra scroll wheel and key-press combinations let you manipulate the Timeline on the Edit page. To work the Timeline, spin the scroll wheel while holding down: Shift: Grows or shrinks all the Video or Audio track heights, depending on which section the pointer sits over as you scroll. Option: Zooms the Timeline view in and out. Command: Moves forward and backward through the Timeline.

### Move Playhead to Mouse Pointer Using the C key

On the Edit page, you can snap the playhead instantly to wherever your pointer rests on the timeline by pressing the “C” key on the keyboard. That lets you move around the timeline fast without having to steer the mouse up to click on the upper timeline ruler. A menu action works too: Playback > Go To > Mouse Pointer.

### Resizing the Timeline’s Video and Audio Track Regions

When you want to see more of the video or audio tracks within the Timeline's available area, drag the horizontal divider separating the audio and video tracks up or down so room opens where it's needed. Drag the Timeline's center divider to free up additional space for either audio or video tracks

### Tabbed and Stacked Timelines

The Timeline now offers the choice of having tabs that let you browse multiple timelines in a hurry. With tabbed timeline browsing on, a second option lets you bring up stacked timelines so two (or more) timelines appear at once, one above another.

### Tabbed Timelines

The Timeline View Options menu in the toolbar holds a button that switches on tabbed browsing and the stacking of timelines.

A button in the Timeline View Options enables tabbed timelines.

The first time you turn this on, a Timeline tab bar shows up above the Timeline, presenting a tab for the currently open timeline that holds a Close button and a Timeline drop-down menu. After Tab mode is on, opening another timeline from the Media Pool brings it up in a new tab. Beyond whatever tabs already exist, an Add Tab button lets you spin up more tabs, each one starting out at “Select Timeline.” Click any tab's drop-down menu to pick the timeline that tab shows.

Sitting above the Timeline Editor, tabs let you jump among several timelines fast Right-clicking a tab brings up a contextual menu that hands you several frequently used Timeline functions. Tabbed timeline contextual menu options: Close Timeline: Shuts the current tab's timeline and clears the tab. Same as clicking the “x” inside the tab. Close All Other Timelines: Shuts every open timeline and tab apart from the one on which you right-clicked and picked this option. Rename Timeline: Brings up the tab's text editing field so the name of the timeline inside the tab can be changed. That changes the timeline's name throughout the project in the Media Pool too. Find Timeline in Media Pool: Opens the bin where the timeline lives in the Media Pool and highlights the timeline in orange. Duplicate TImeline: Makes a duplicate of the chosen timeline in the same bin, with the word “copy” tacked onto the timeline name. It also opens the copied timeline in a new tab on its own.

A right-click on a tab surfaces the timeline options. Methods of working with tabbed timelines:

- Click any tab to switch to that timeline.
- Use the drop-down menu inside any tab to switch that tab over to a different timeline from the Media Pool. Every tab's drop-down menu lists all the project's timelines alphabetically, though a given timeline can only be open in one tab or stack at any moment.
- Drag any tab left or right to reorder the timeline tabs.
- Click any tab's Close button to close that timeline and take the tab away.
- Middle-click any tab to close that timeline and take the tab away.

### Stacked Timelines

While tabbed browsing is on, an Add Timeline button shows up at the far right of the tab bar, letting you stack two (or more) timelines one above another. That lets you keep two (or more) timelines open simultaneously, which makes editing clips from one timeline into another easy. A solid example of where this helps is when you've built a timeline that holds a stringout of selects drawn from one particular interview. Two Timeline Editors can be stacked, one over the other, with the Selects Timeline brought up on top and the Timeline you're cutting into placed on the bottom. With that layout, it's simple to play through the top timeline to spot clips you want, then drag and drop them into the bottom timeline to cut into your program.

### The button for closing a stacked timeline

Switching stacked timelines on or off: Click the Add Timeline button sitting at the right end of the Timeline tab bar.

### The button for adding a stacked timeline

After you've switched stacked timelines on, every timeline gets its own tab bar, and the selected one is flagged by an orange underline. Over at the right end of each tab bar, beside the Add Timeline button, sits a Close Timeline button that lets you close any timeline and lift that timeline browsing area off the stack.

### Stacked Timelines

### View and Edit Dual Timelines Using the Source Viewer

You can now operate on two timelines at the same time in the Edit page, with one loaded into the Source Viewer and one in the Timeline Viewer. This makes it easy to compare two timelines or shift content from one timeline to another.

Switch on Display Stacked Timelines within the Timeline View options before working with dual timelines To squeeze the most from this feature, begin by enabling Display Stacked Timelines through the Timeline View Options icon at the upper left of the timeline. With that view turned on, each timeline gets its own tab, and the Viewer redirects focus by itself according to which tab is active. Next, loading a timeline into the Source Viewer means right-clicking a clip's timeline over in the Media Pool and picking “Open in Timeline with Source Viewer.” That timeline shows up in the Source Viewer as a fresh tab, its name and playhead turning blue so you can keep straight which timeline lives in which Viewer. The timeline in the Source Viewer is read only. You move between the timelines by clicking the tabs, pressing Q, or clicking in the relevant Viewer.

A dual-timeline editing layout: one timeline loaded in the Source Viewer (blue) alongside a second one in the Timeline Viewer. Each tab switch hands focus to whichever viewer is relevant.

You can change which timeline shows up in the Source Viewer either by right-clicking a different timeline in the Media Pool and picking the “Open in Timeline with Source Viewer” option, or by picking one of the timelines from the dropdown menu atop the Source Viewer. Ordinary cut and copy moves carry content from the read-only source timeline into the actual timeline, and dragging out of the Source Timeline viewer (left) and into the Timeline viewer (right) also makes an edit. TIP: For playback purposes, a particular track in the Source Timeline Viewer timeline can be soloed. As one case, you might simply wish to hear the boom mix track, or a single specific ISO of a character's wireless mic, as you cut from the Source Timeline. Just click the “S” solo button on whichever audio track you want soloed. Shortcuts exist as well that make shifting focus between viewers that much faster:

- To toggle between the Source and Timeline viewers, press Q.
- To turn on and off the Source Timeline view, press Option-Q.
- To bring a particular timeline into the source viewer, right-click its tab and pick Load Timeline to Source Viewer.

TIP: You can likewise right-click an ordinary media clip and pick Open in Timeline with Source Viewer to bring that clip into the Viewer as a timeline. Such “timelines” will be read only, yet will still permit the same timeline-to-timeline editing operations available now. This mode comes in handy for very long clips such as interviews.
