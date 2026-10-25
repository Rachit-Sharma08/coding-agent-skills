# Manually syncing clips in the sync clips window and your newly synced clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](camera-names-and-sync-clips-window.md) / [Next section](multicam-viewer-selection-and-make-the-source-overwrite-edit.md)
<a id="source-manually-syncing-clips-in-the-sync-clips-window"></a> <a id="source-media-pool-in-the-sync-bin"></a> <a id="source-select-your-camera"></a> <a id="source-sync-bin-editing"></a> <a id="source-the-sync-bin-icon"></a> <a id="source-using-your-newly-synced-clips"></a> <a id="source-viewer-in-the-sync-bin"></a>

### Manually Syncing Clips in the Sync Clips Window

Should none of the Sync By tools suit the clips sitting in your bin, you're free to sync them by hand

by dragging each clip into the right spot along the Sync Clips Window timeline. For greater precision,

highlight the clip you mean to sync and tap the Comma (,) or Period (.) keys, which shift the clip

one frame at a time, either back or ahead. Holding Shift-Comma (,) or Shift-Period (.) moves the clip by 5 frames

(the default), or by however many frames the “Default fast nudge length” setting specifies, found under the General

Settings portion of the Editing panel within the User settings of the Resolve Preferences. Every clip occupies its

own track, and turning on sync lock in the right-hand Viewer keeps things from slipping by accident.

After every clip in the window has been synced properly, click the Save Sync button down in the lower-right corner of the window.

### Using Your Newly Synced Clips

Once you've saved the sync across your clips, a fresh Multicam clip turns up in the Media Pool. Switch to the Thumbnail View and a Sync icon shows on each clip you altered. Wanting to adjust the sync, right-click a thumbnail and pick Open Sync Group to bring your clips back up in the Sync Clips window. As soon as you drop your first clip onto the Timeline to serve as a reference, you're set to edit with the Sync Bin.

Sync icons (upper left arrows) identifying synced media clips

### Sync Bin Editing

What the Sync Bin layout is really about is that, rather than separately scrubbing your timeline and clips the old way, you need only scrub the timeline itself. Over in the Media Pool, every clip sharing that same timecode value scrubs along in lockstep with the playhead. That keeps the precise clips destined to slot neatly into your timeline ready and within reach at all times. Choosing this mode reshapes the Media Pool and Viewer layout on its own to better suit multi camera editing on the Cut page.

Edit in Your First Clip from the Media Pool Pick a clip to act as your base layer and drop it onto Track 1. Every other clip in the Sync Bin treats this one as its reference. After that, click the Sync Bin icon.

### The Sync Bin icon

### Media Pool in the Sync Bin

Every clip held in the bin, along with those in its subfolders, shows up in filmstrip mode. These clips get ganged together by timecode automatically and arranged in camera-number order. A further playhead sits at wherever the timeline currently is, and shifting any one of the Cut page's three playheads scrubs through all the Sync Bin clips together.

### Viewer in the Sync Bin

The Viewer changes over to a live Multi Viewer handling as many as nine cameras. Every camera carries a label and number,

while the one currently active in the Timeline gets marked in red. Any camera that wasn't active at the present

playhead time is blacked out.

You can throw the Sync Bin camera selection up full screen in the Cinema Viewer by tapping “P” on the keyboard, which gives you a bigger, more detailed look at each individual camera. Within this fullscreen mode, the Sync Bin view controls behave exactly as they do back in the normal Viewer.

The Sync Bin view as shown across the Media Pool and Viewer Select Your Timeline In Point Set the In point on your timeline by dragging the timeline playhead to wherever you'd like your media to begin. While you do, every clip in the Sync Bin scrubs right along with the playhead's position. Locating and picking edit points in the Sync Bin becomes far easier, since all the synced media options open to you sit there ready in an instant. Turn on the “Video Only” mode on the Cut page and the audio coming from the Sync Bin sources falls silent, leaving audio playback to come solely from the Timeline clips.

### Select Your Camera

Within the Multicam Viewer, choose the camera angle you intend to draw on as source material in one of these ways:

- Clicking the camera you want inside the Multicam Viewer
- Clicking that camera's number icon over in the Filmstrip Viewer
- Hitting that camera's number key on the keyboard

At that point the Viewer drops into Single Clip mode and displays the camera you picked. Heading back to the Multi Viewer takes either a click on the circled X close icon or a simple press of the Escape key. The clip lays down an In point on its own at your present timeline position, running a default duration of five seconds. From there you're free to place the clip's Out point by hand wherever you like.
