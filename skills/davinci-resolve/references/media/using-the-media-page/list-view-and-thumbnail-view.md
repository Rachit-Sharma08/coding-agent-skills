# List view and thumbnail view

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the media page.
[Chapter index](INDEX.md) / [Previous section](understanding-the-media-page-user-interface-and-media-page.md) / [Next section](media-viewer-and-current-frame-export.md)
<a id="source-list-view"></a> <a id="source-revealing-a-finder-location-in-the-media-browser"></a> <a id="source-thumbnail-view"></a> <a id="source-viewer"></a>

### List View

Within List view, these columns are on offer for sorting media before you bring it into the Media Pool:

- File name: The name of a file.
- Reel name: The reel name as it is presently derived per the Conform Options that are

currently chosen in the General Options panel of the Project Settings.

- Start TC: The first timecode value in the source media.
- Start: The first frame number in the source media.
- End: The last frame number in the source media.
- Frames: The duration of each clip in frames.
- Resolution: The frame size of the source media.
- Bit Depth: The bit depth of the source media.
- Video Codec: The codec used for the video track of supported media.
- Audio Codec: The codec used for the audio tracks of supported media.
- FPS: The frame rate of the source media.
- Audio Ch: The number of audio channels within the source media.
- Date Created: When the media file was created.
- Date Modified: When the media file was last altered and then saved.
- Shot: Additional metadata from media formats that support it.
- Scene: Additional metadata from media formats that support it.
- Take: Additional metadata from media formats that support it.
- Angle: Additional metadata from media formats that support it.
- Good Take: Additional metadata from media formats that support it.

Working in List view hands you extra organizational control by revealing columns that display the metadata each clip carries, before any media reaches your timeline. These columns help you arrange your media. Ways to tailor metadata columns within List view:

- To show or hide columns: Right-click atop any column in the Media Storage browser and pick an entry from the contextual menu list to tick or untick a given column. Unticked columns stay out of sight.
- To rearrange column order: Drag any column header left or right to reorder the columns.
- To resize any column: Drag the boundary between two columns rightward or leftward to make that column narrower or wider.
- To sort by any column: Click whichever column header you want to sort on. Every further click on that same header flips the column between ascending and descending sort order.

You can likewise tailor column layouts within the Media Storage area. After you have built a column layout suited to your particular purpose, you can store it for later recall. Ways to save and apply a custom column layout:

- To create a column layout: Reveal, hide, resize, and reorder the columns a given task calls for, then right-click any column header in the Media Pool and pick Create Column Layout. Type a name into the Create Column Layout dialog, and click OK.
- To recall a column layout: Within the Media Pool, right-click on a column header and choose the name of whichever column layout you wish to apply. Every custom column layout sits at the top of the list.
- To delete a column layout: Within the Media Pool, right-click on a column header, then from the Delete Column Layout submenu choose the name of whichever column layout you wish to discard.

### Thumbnail View

While in Thumbnail view, scrubbing across a clip's icon reveals its contents; you can additionally click the Clip Info drop-down menu tucked into the lower right corner of any clip's thumbnail for a quick rundown of that clip's key information, such as:

- File name: The name of that file.
- In timecode: The first frame in the source media.
- Out timecode: The last frame in the source media.
- Duration: The total duration of the source media.
- Resolution: The frame size of the source media.
- Frame Rate: The frame rate, in fps, of the source media.
- Pixel Aspect Ratio: The aspect ratio of the source media.
- Codec: Which codec is used by the source media.
- Date Created: The date created metadata from the source media file.
- Flags: Flag metadata applied either by the camera that shot the media,

in the Metadata Editor, or in the Color page Timeline.

Also while in Thumbnail view, the Thumbnail Sort drop-down menu (sitting between the Search and Option menu) lets you pick a criteria for arranging the thumbnails. A broad assortment of metadata options turns up, among them: File Name, Reel Name, Start TC, FPS, Audio Ch, etc. You can sort in ascending or descending order too.

### Revealing a Finder Location in the Media Browser

Should you drag a folder out of the macOS Finder and into the Media Storage browser, the Media Storage browser refreshes at once to display that folder's location.

### Viewer

Whatever clips you pick across any region of the Media page display their contents in the Viewer. Where the playhead currently sits shows up in the timecode field at the Viewer's upper right-hand corner.
