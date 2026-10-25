# Toolbar audio monitoring controls and monitoring controls in the edit page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](toolbar-selecting-the-timeline-view-options.md)
<a id="source-customizing-the-edit-page"></a> <a id="source-displaying-audio-meters"></a> <a id="source-dual-monitor-layout"></a> <a id="source-floating-timecode-window"></a> <a id="source-the-edit-page-in-dual-screen-mode"></a> <a id="source-the-floating-timecode-window"></a> <a id="source-the-mixer-and-meters"></a> <a id="source-the-monitoring-controls-in-the-edit-page"></a> <a id="source-toolbar-audio-monitoring-controls"></a> <a id="source-undo-and-redo-in-davinci-resolve"></a> <a id="source-using-video-scopes"></a> <a id="source-video-scopes-in-a-floating-window"></a>

### Toolbar Audio Monitoring Controls

Over at the far right of the toolbar sits a trio of monitoring controls that let you swiftly govern your mix’s output volume. An audio Enable/Disable button toggles audio playback on and off, a slider changes the volume, and a DIM button lets you briefly duck the monitored output volume so you can have a quick word with your client about sports or world events while still keeping half an ear on the mix.

### The monitoring controls in the Edit page

Whenever a project defines several audio Mains, an extra drop-down dialog joins the audio monitoring controls in the toolbar, letting you choose which Main you are hearing.

### The Mixer and Meters

The Audio Mixer hands you a set of graphical controls for setting track levels, panning stereo audio, and muting and soloing tracks, all without interrupting your editing. To open the Audio Mixer: On the Interface toolbar, click the Mixer button. A row of channel strips whose controls correspond to the Timeline’s tracks is what the Audio Mixer lays out, and every channel strip carries a number of audio meters that matches how many channels live inside that track. By default, a Main 1 channel strip sits all the way to the right, letting you set the overall level of the mix. That said, should you add subs and mains on the Fairlight page, those turn up at the right of the mixer too. To learn more about putting the Mixer to use on the Edit page, consult Chapter 45, “Working with Audio in the Edit Page.” To learn more about working the Mixer on the Fairlight page, consult Chapter 177, “Mixing in the Fairlight Page.”

The Audio Mixer, its four channel strips each mapping to one of the four Timeline tracks

### Displaying Audio Meters

When all you care to see is your program’s levels, you can instead switch over to the “Control Room” audio meters rather than the Mixer. How many audio meters appear comes down to whatever speaker configuration is currently set in the System Preferences’ Video and Audio I/O panel. To show the Audio Meters: On the Interface toolbar, click the Mixer button so the audio panel appears, then pick Meters from the option menu in the upper right-hand corner.

### Using Video Scopes

A set of four real-time video scopes ships with DaVinci Resolve for watching, as you work, the internal data levels of the clips in your project. A clear graphical breakdown of the video signal’s various traits is what each scope delivers, revealing the relative strength and range of individual color components, luma, chroma, saturation, hue, along with the red, green, and blue channels that jointly form the color and contrast of your program’s images. While on any of the Media, Cut, Edit, Color, or Deliver pages, you can open the video scopes by doing one of these:

- To bring the video scopes up inside a floating window, choose Workspace > Video Scopes > On/Off (Command-Shift-W).
- To bring the video scopes up as part of a dual screen layout, choose Workspace > Dual Screen > On.

### Video scopes in a floating window

The video scopes are not confined to the Color page. They turn up as well in the Media, Cut, Edit, and Deliver pages for any moment you need a more objective read on the video signal, such as when you are gearing up to capture from tape or scan from film, or while preparing for output. To learn more about working with the video scopes, see Chapter 126, “Using the Color Page.”

### Floating Timecode Window

A Timecode Window can be summoned from the Workspace menu on every page but Fusion. Picking this option puts up a floating timecode window displaying the timecode of whichever Viewer or Timeline currently holds focus. You can resize this window to make the timecode bigger or smaller.

### The floating timecode window

### Dual-Monitor Layout

A dual-monitor layout is on offer in the Edit page, handing the Timeline and Viewers the most room possible on the primary monitor, while the secondary monitor holds an enlarged Media Pool plus a Timelines browser, Edit Index, Effects Library, and Metadata Editor all shown at once. A dual-screen layout’s second screen will resize but cannot be rearranged. If a single ultra-wide monitor is all you have, the dual-monitor layout still works, and DaVinci Resolve scales the interface as if two regular monitors stood beside each other. To enter dual-screen mode: Choose Workspace > Dual Screen > On.

### The Edit page in dual-screen mode

To switch which UI elements appear on which monitors: Pick Workspace > Primary Display > (Monitor Name); in dual screen mode this swaps what each of the two monitors holds. To view only the timeline in a monitor: Pick Workspace > Full Screen Timeline.

### Customizing the Edit Page

For a good many tasks on most displays, the default layout works quite efficiently. You can always come back to the default arrangement by choosing Workspace > Reset UI Layout. Even so, you can reshape the Edit page to free up extra room for particular interface areas as different tasks demand. To resize any area of the Edit page: Between any two panels, drag the vertical or horizontal border so that one grows while the other shrinks. To expand the width of the Timeline: Hit the Media Pool/Effects Library/Edit Index height button, which shrinks the space used by the Media Pool, Effects Library, and/or Edit Index down to half height. At that point the Media Pool/Effects Library/Edit Index cling to the top of the UI (only one shows at any time), while the Timeline runs across your display’s entire width. Tucking away the Edit Index and the Effects Library lets the Timeline reach across your screen entirely. To adjust the height of an individual video or audio track: Move the pointer onto the upper edge of any video track header, or onto the lower edge of any audio track header, and as soon as it becomes a resize cursor, drag that edge upward or downward to resize that track. Worked this way, each track can hold a size of its own.

To switch on a full-screen timeline while in Dual Screen mode: Choose Workspace > Dual Screen > Full Screen Timeline; that hands the entire primary display over to the Timeline and shifts the Browser, Viewers, Audio Mixer, Edit Index, and Effects Library onto the secondary display. Customizing the columns in the Edit Index: For showing or hiding columns within the Edit Index: On any column header, right-click, then from the contextual menu choose the column you wish shown or hidden. A checked column shows; an unchecked one stays out of sight. To resize any column of the Edit Index: Hover your pointer over the divider separating two columns, then drag the moment the horizontal resize cursor turns up. To sort the Edit Index by any column: Up at the top right, click the Option button to display all active tracks, only the video, or only the audio tracks. To rearrange Edit Index columns: Take any column’s header and drag it sideways to relocate that column. For toggling the visibility of the Audio Meters or Audio Mixer: In the UI toolbar, click the Mixer button. To switch between the Audio Meters and the Audio Mixer: From the Option menu in the Mixer’s top right corner, pick Meters or Mixer.

### Undo and Redo in DaVinci Resolve

Wherever you happen to be in DaVinci Resolve, the Undo and Redo commands let you reverse steps you have taken or commands you have run and reapply them should you change your mind. DaVinci Resolve can undo the whole history of what you have done since you created or opened a given project. Close a project and its entire undo history is wiped. The next time you take up a project, its undo history begins fresh. Since DaVinci Resolve packs so much capability into one application, it keeps three distinct sets of undo “stacks” to help you manage your work.

- A single multiple-undo stack is shared by the Media, Edit and Fairlight pages, letting you reverse changes you made within the Media Pool, the Timeline, the Metadata Editor, and the Viewers.
- Every clip in the Fusion page keeps its own undo stack, so you can undo changes to each clip’s composition on its own.
- Every clip in the Color page keeps its own undo stack, so you can undo changes to each clip’s grades on its own.

In every case, the number of steps you can undo has no real ceiling (though what you can remember might). To take advantage of that, there are three routes for undoing work and dropping back to an earlier state of your project, no matter the page you occupy. For plainly undoing or redoing your changes a single one at a time:

- Choose Edit > Undo (Command-Z) to undo the previous change.
- Choose Edit > Redo (Shift-Command-Z) to redo to the next change.

You can also walk back several steps at once through the History submenu and window. At this writing, only the Media, Cut, Edit, and Fairlight pages support multiple undo steps that way. For undoing and redoing by way of the History submenu: 1 Open the Edit > History submenu, where (up to) the twenty most recent things you did are listed. 2 Choose any entry on the list and you undo back to that moment. Whatever you did most recently sits atop this list, and the change you just performed appears bearing a check alongside it. Steps that have been undone but can still be redone stay in this menu, so you can see what remains possible. That said, should you undo several changes at once and then make a new change, no further undo is possible and those steps drop off the menu. After you settle on a step to undo to, the menu shuts and the project updates to show where it now stands. The History submenu, your means of undoing a number of steps in one go For undoing and redoing by way of the Undo window: 1 Choose Edit > History > Open History Window. 2 Once the History dialog appears, click any entry on the list to roll back to that moment. Here, contrary to the menu, the thing you did most recently lands at the bottom of this list. Picking a change in this spot grays out whatever can still be redone, as the project updates to show where it now stands.

The Undo history window, through which you can page through the whole undo stack available for the current page 3 Once finished, shut the History window.
