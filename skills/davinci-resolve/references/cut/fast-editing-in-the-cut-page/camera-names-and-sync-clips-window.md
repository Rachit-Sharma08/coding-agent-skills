# All clips must have a unique camera name and sync clips window

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](create-subtitles-from-audio-and-source-tape-editing.md) / [Next section](manual-clip-sync.md)
<a id="source-all-clips-must-have-a-unique-camera-name"></a> <a id="source-fast-editing-in-the-cut-page-part-3"></a> <a id="source-sync-by-tools"></a> <a id="source-sync-clips-window"></a> <a id="source-the-media-pool-sync-clips-window"></a> <a id="source-the-media-pool-sync-clips-window-icon"></a>

### All Clips Must Have a Unique Camera Name

Nearly every professional video camera provides some means of naming the camera within its internal menu system. That camera name then rides along as metadata in each captured clip, where DaVinci Resolve can read it automatically. Name your cameras either with letters (A, B, C, etc.) or with numbers (1, 2, 3, etc.), running in sequence up to however many cameras you are shooting with. Should your camera fail to log this on its own (or log it wrong), you can set the camera’s name by hand through the Camera # field of the Metadata Editor in the Media Pool.

### Sync Clips Window

When your footage carries no shared timecode, or the timecode it has needs changing for whatever reason, the Cut page’s Media Pool puts forward a Sync Clips window where you can adjust the sync of every clip in a bin. You reach it by clicking the Sync Clips Window icon atop the Media Pool.

### The Media Pool Sync Clips window icon

When the Sync Clips window opens, a live multi-camera sync Viewer sits on its left and an ordinary clip Viewer on its right. A timeline runs along the bottom too, charting how all the bin’s clips relate in time.

### The Media Pool Sync Clips window

### Sync By Tools

Several tools within DaVinci Resolve will bring your shots into flawless sync on their own.

- Timecode: Pressing this button attempts to line up every clip in the Sync Clips window according to timecode, and it's the option selected by default.
- Audio: Pressing this button attempts to line up every clip in the Sync Clips window by examining each one's audio tracks. For it to succeed, each clip needs at least some stretch of the same audio track captured cleanly enough to be analyzed. Any tracks that couldn't be synced this way are reported back to you through an error message.
- In Point: Pressing this button attempts to line up every clip in the Sync Clips window using the In point each user has set. It comes in handy when a shared mark was filmed across all cameras, say a slate clapping shut or a camera flash.
- Out Point: Pressing this button attempts to line up every clip in the Sync Clips window using the Out point each user has set. It comes in handy whenever there was a shared tail slate.
- Sync: Pressing this button runs the Sync By method you chose above.

After every clip in the window has been synced properly, press the Save Sync button over at the lower-right of the window.

The Sync By icons within the Media Pool, running left to right: Timecode, Audio, In point, Out point
