# Media and media pool tabbed layouts

Version: DaVinci Resolve 21 New Features Guide. Context: Color and keyframing.
[Chapter index](INDEX.md) / [Next section](color-and-multimaster-trim-manager.md)
<a id="source-a-pdf-export-of-a-media-pool-bin"></a> <a id="source-automatic-smart-bin-and-clip-filter-for-offline-clips"></a> <a id="source-customize-project-poster-frames"></a> <a id="source-cut-page-supports-smart-bin-views"></a> <a id="source-export-media-bin-thumbnails-as-a-pdf"></a> <a id="source-keyboard-shortcuts-to-set-thumbnail-list-or-metadata-views"></a> <a id="source-media"></a> <a id="source-media-1"></a> <a id="source-media-color-resolve-fx-immersive"></a> <a id="source-media-pool-tabbed-layouts"></a> <a id="source-media-pool-tabs-showing-the-right-click-context-menu"></a> <a id="source-overview"></a> <a id="source-reset-audio-clip-attributes"></a> <a id="source-star-ratings-for-clips"></a> <a id="source-thumbnail-list-and-metadata-views-can-be-set-per-bin"></a> <a id="source-transcription-column-in-list-view"></a> <a id="source-use-custom-metadata-in-smart-bins-clip-filters-data-burn-in-and-naming-tags"></a>

## Overview

Covers: Media; Color; Resolve FX; Immersive.

## Media

### Media

### Media Pool Tabbed Layouts

You can now pin tabs in the Media Pool that act as shortcuts straight to particular bins. Each tab sits in a dedicated tab bar along the top of the Media Pool, and the same bar appears in Media Pool windows on other pages. The feature works for ordinary bins along with smart and power bins. Spin up a new bin tab by right-clicking a bin and picking “Open as New Tab” from the contextual menu; clicking a tab's name jumps that bin open in the Media Pool right away. If you keep browsing inside an already-open tab, the active bin gets swapped for whichever bin you most recently selected.

### Media Pool Tabs, showing the right-click context menu

Right-click a tab and these choices appear:

- New Tab: Creates a new tab (Command T).
- Previous / Next Tab: Jumps to the tab before or after the current one along the tab bar.
- Close Tab: Shuts whichever tab is current (Command-W) (CTL-W on Windows and Linux).
- Close All Other Tabs: Shuts every tab apart from the one you're on.

Clicking the dropdown icon on the tab bar's right-hand side opens a tab search

Once a lot of tabs pile up, the dropdown on the tab bar's right edge lets you hunt down a particular one. Clicking that icon brings up both a roster of your open tabs and a search field. Keep in mind the search field looks only at tab names and won't surface any media pool clips.

### Thumbnail, List and Metadata Views Can Be Set Per Bin

You can now lock a bin into a chosen layout view (Thumbnail, Metadata, and List) so it always opens that way, no matter the prevailing bin view settings. That means, for instance, a bin packed with audio clips can always come up in List view, where thumbnails add little. Here's how to assign a layout view to a bin: 1 Pick the view you'd like the bin to always launch in. 2 Right-click the bin you want this view applied to. 3 Choose Always Open in XXX View, with XXX standing in for the view you selected. The choice persists across sessions in DaVinci Resolve, yet it leaves other users and machines on the same project unaffected.

### Star Ratings For Clips

Media Pool clips can now carry a rating of one to five stars assigned in the Shot & Scene Metadata Panel, and the same goes for still photos via several Photo Page controls.

Giving a clip a four star rating in the Shot & Scene metadata.

Set a rating by clicking the stars, and click an already-rated clip again to change it. To wipe a rating, click once more on its current level. Rating can serve to sort the media pool's List View, act as a Smart Bin criterion, and order an album within the Photo page.

### Cut Page Supports Smart Bin Views

In its Media Pool view, the Cut Page now supports both viewing and building Smart Bins. Reach any Smart Bin in a project through the Media Bin dropdown at the media pool's upper left, and make new smart bins by clicking the + sign within that same dropdown.

On the Cut Page, reach Smart Bins through the Media Bin dropdown menu over at the top left.

### Export Media Bin Thumbnails as a PDF

A Media Pool bin's thumbnails can now be written out to a PDF file. What you get is effectively a digital “contact sheet,” a fast way to glance at which clips a given bin holds. The PDF honors whatever thumbnail image size the Media Pool is using. By default it tries to pack the thumbnails onto a single-page PDF; for very large or custom-sorted bins, though, the export comes out as one tall, expanded document instead of being split into pages. To produce a PDF of a Media Pool bin's thumbnails: open the bin in question, open the Media Pool 3-dot option menu, choose Export as PDF from the context menu, and then pick a save location.

### A PDF export of a Media Pool bin

Choosing Export as PDF from the Media Pool option menu

### Automatic Smart Bin and Clip Filter for Offline Clips

A Smart Bin or Clip Filter (on the Color Page) can now be configured to round up every offline clip on its own. The result is a single bin you can use to relink media no matter where it sits across your project. To create an Automatic Smart Bin for Offline Clips: tick “Automatic smart bin for offline clips” under DaVinci Resolve > Preferences > User > Editing > Automatic Smart Bins.

### Use Custom Metadata in Smart Bins, Clip Filters, Data Burn-in and Naming Tags

Any Custom Metadata fields you built earlier in the Metadata Editor can now feed into Smart Bins, Clip Filters, Data Burn-ins and Tags as criteria.

### Customize Project Poster Frames

Straight from the Media Pool, you can now assign a custom Poster Frame to the Project thumbnail shown in the Project Manager. That makes it easy to tell your projects apart visually at a glance. To assign a Project Poster Frame: 1 In the Media Pool, choose the clip you want the new poster frame drawn from. 2 Scrub through that clip until the frame you're after appears in the thumbnail. 3 Right-click the clip and choose Clip Operations > Set Project Poster Frame.

### Transcription Column in List View

The Media Pool list view now includes a Transcription Column, present mainly as a visual cue. For a transcribed clip, only the opening few words show up in the Transcription column, yet searches against the transcription still match its full text.

### Keyboard Shortcuts to Set Thumbnail List or Metadata Views

Keyboard shortcuts can now be bound to flip the Media Pool view into Thumbnail or Metadata views. Look for these entries within the Keyboard Customization panel, under Panels > Media Pool > View Type.

### Reset Audio Clip Attributes

Clip Attributes now carries a simple icon for returning the Audio Clip Attributes to how they started. Click that red reset icon and the audio clip attributes snap back to their original state.
