# Timecode and Fairlight synchronization settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](switch-group-manager-and-dropdown-in-the-sw-group-column.md) / [Next section](fairlight-presets-and-undo-redo.md)
<a id="source-customizing-the-fairlight-page"></a> <a id="source-dual-monitor-layout"></a> <a id="source-external-sync-via-ltc-enabled"></a> <a id="source-external-sync-via-mtc-enabled"></a> <a id="source-fairlight-synchronization-settings"></a> <a id="source-generate-timecode-enabled"></a> <a id="source-generating-timecode"></a> <a id="source-ltc-and-mtc-chase-sync"></a> <a id="source-ltc-synchronization"></a> <a id="source-mtc-synchronization"></a> <a id="source-pro-tools-aaf-import"></a> <a id="source-status"></a> <a id="source-sync-status-pane"></a> <a id="source-the-fairlight-page-in-dual-screen-mode"></a> <a id="source-working-with-timecode"></a>

### Working with Timecode

Fairlight provides synchronization options letting you set up DaVinci Resolve to either chase and lock onto an outside device or separate application, or to create and send out timecode as an audio signal so an outside device can trail your Timeline. These settings are reached by clicking the Fairlight menu and picking Synchronization Settings.

### Fairlight Synchronization settings

### LTC and MTC Chase Sync

### LTC Synchronization

Suppose you wish to have Fairlight chase and lock onto an outside device or a computer system: 1 Turn on External Sync. 2 From the Source dropdown, pick the Timecode option. 3 From the Timecode Audio Input dropdown, pick a suitable audio input on your interface. 4 Set an SMPTE offset where one is called for; if not, keep it at +00:00:00:00. 5 Start the external device playing. Your Fairlight mix will then run in perfect step with that external device.

### External Sync via LTC enabled

### MTC Synchronization

To have Fairlight chase and lock onto either an app on your machine — a DAW, for instance — or an outside device that can send MIDI timecode: 1 Turn on External Sync. 2 From the Source dropdown, pick the MIDI Timecode option. 3 From the MIDI Timecode Port menu, pick the right MIDI port. As an example, to sync DaVinci Resolve with a DAW running on your computer, choose IAC Driver Bus 1. 4 Set an SMPTE offset where one is called for; if not, keep it at +00:00:00:00. 5 Get playback going on the external device or DAW, and Fairlight's audio will follow along in time.

### External Sync via MTC enabled

### Status

This portion of the Synchronized Settings dialog reports live details about how synchronization stands at the moment during playback.

- Incoming Timecode: While playback runs, this field keeps refreshing with the timecode currently being sent to DaVinci Resolve.
- Transport Status: This light goes green to signal that synchronization is holding steady during playback.
- Timecode Freewheel: With this checkbox ticked, Fairlight will produce its own timecode

briefly should trouble arise with the timecode coming in. That keeps synchronization steady and unbroken.

### Sync Status pane

### Generating Timecode

To create and send timecode as an audio signal out of your audio interface to an outside device or application: 1 Switch on Generate Timecode. 2 Pick from the Interface Output dropdown the audio-interface output through which you'd like the timecode audio sent. 3 Start playback of your Fairlight mix. DaVinci Resolve keeps feeding the timecode audio signal to its destination right up until you click the Stop button.

### Generate Timecode enabled

TIP: When a Fairlight SX36 audio interface is in play, that signal serves to synchronize a second DaVinci Resolve system, or indeed any system able to take timecode audio as a reference.

### Pro Tools AAF Import

AAF projects and media from Pro Tools can be brought into DaVinci Resolve, letting you carry an audio project across from a Pro Tools workstation to a Fairlight one. The AAF import handles embedded audio together with track automation. To run it, choose File > Import Timeline > Import AAF/EDL/XML.

### Dual-Monitor Layout

A dual-monitor layout on the Fairlight page hands the mixer and audio meters the full width of one screen while devoting the other to a full-screen timeline. Even with just a single ultra-wide display, the dual-monitor layout remains available, and DaVinci Resolve will scale the interface as though you were running two ordinary monitors side by side.

To enter dual screen mode: Choose Workspace > Dual Screen > On.

### The Fairlight page in dual screen mode

To flip which UI elements land on which screen: Choose Workspace > Primary Display > Display 1 or Display 2, an action that swaps what each of the two monitors shows while in dual screen mode.

### Customizing the Fairlight Page

For plenty of jobs on most screens, the default layout works well enough. Choosing Workspace > Reset UI Layout always brings you back to that default. That said, you're free to reshape the Fairlight page to open up extra room for particular parts of the interface as different tasks demand. To resize any area of the Fairlight page:

- Grab the vertical or horizontal divider separating a pair of panels and drag it to grow one panel while the neighboring one shrinks.

To resize the height of individual audio tracks:

- Bring the pointer down to the lower border of any audio track header, and once it turns into a resize cursor, drag the border up or down to set that track's height. With this method each track can carry its own independent size.

To resize any column of the Index:

- Hover the pointer over the divider sitting between any two columns and drag once the horizontal resize cursor shows up.

To rearrange Index columns:

- Drag any column's header left or right to relocate that column.

NOTE: To keep the track heights you've set even after a project is shut and reopened, right-click the track header and pick “Lock Track Height to.” For any height beyond the standard sizes, pick “Custom” to specify whatever value you want.

TIP: The option key likewise lets you resize the heights of every selected track at once, or use Commandoption to do the same across all selected tracks.
