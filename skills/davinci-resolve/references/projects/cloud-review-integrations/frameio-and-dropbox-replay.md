# Frameio and dropbox replay

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cloud review integrations.
[Chapter index](INDEX.md) / [Previous section](../../delivery/metadata-burn-in/metadata-burn-in-prefixes.md)
<a id="source-choosing-the-frameio-preset"></a> <a id="source-deliver-and-upload-to-dropbox-replay"></a> <a id="source-deliver-and-upload-to-frameio"></a> <a id="source-dropbox-replay-comments-sync-with-timeline-markers"></a> <a id="source-enabling-dropbox-replay-integration-in-preferences"></a> <a id="source-enabling-frameio-integration-in-preferences"></a> <a id="source-frameio-and-dropbox-replay-integration"></a> <a id="source-frameio-and-dropbox-replay-integration-1"></a> <a id="source-frameio-comments-sync-with-timeline-markers"></a> <a id="source-frameio-marker-navigation"></a> <a id="source-importing-media-from-frameio"></a> <a id="source-linking-media-pool-clips-and-timelines-with-frameio-clips"></a> <a id="source-unlinking-a-timeline-from-dropbox-replay"></a> <a id="source-upload-new-versions-to-dropbox-replay"></a> <a id="source-working-with-dropbox-markers"></a>

## Frame.io and Dropbox Replay Integration

### Frame.io and Dropbox Replay Integration

Built specifically for the postproduction trade, advanced integrations tie DaVinci Resolve into the Frame.io and Dropbox Replay video review and collaboration services.

### Enabling Frame.io Integration in Preferences

Under the System tab of the DaVinci Resolve Preferences, an Internet Accounts panel lets you log in to your Frame.io account and name a local cache location where media syncing with Frame.io lands. Activating Frame.io integration calls for your login name and password, yet after they’re entered, DaVinci Resolve logs in on its own each time DaVinci Resolve launches.

Within the DaVinci Resolve Preferences window, the System tab’s Internet Accounts panel (its login deliberately obscured) That local cache location holds the clips you bring into a DaVinci Resolve project off the Frame.io volume found in the Media Storage panel of the Media page.

### Deliver and Upload to Frame.io

Sitting at the top of the Deliver page’s Render Settings panel, a Frame.io preset lets you render a program and push it up for review. Every option across the Render Settings panel refreshes to show controls fit for this purpose. Pick the Frame.io preset and the Location field becomes an Upload To field, while the Browse button lets you select the project and folder path that the exported result uploads to.

### Choosing the Frame.io preset

Choosing a Frame.io account to deliver a program to

Exporting to Frame.io trims the selectable entries in the Resolution, Format, Video Codec, and Type pop-up menus down to those best matched for Frame.io file sharing. Set the export options you want, then press the Add to Render Queue button to drop this job into the Render Queue just as you would for any other export. After that job renders, it moves on by itself to upload to Frame. io, and the job listing shows an upload percentage indicator marking how far the upload has gotten. Upon completion, the job reads “Upload completed.”

Inside the Render Queue, the job reports what percentage of the file has gone up so far Because this upload runs in the background, you can keep busy with other tasks in DaVinci Resolve as the file goes up. To check how long the upload needs from any other page, choose Workspace > Background Activity and open the Background Activity window.

### Frame.io Comments Sync with Timeline Markers

Render a timeline straight to Frame.io and that timeline links automatically to the movie pushed up to Frame.io, so every comment, “Like,” and graphical annotation (drawings and arrows) that reviewers add online through the Frame.io interface syncs automatically to Frame.io markers on your timeline (provided your computer holds an active internet connection). Frame.io markers stand apart from all the other markers and may be shown, hidden, or deleted on their own. Drawings and arrows out of Frame.io get translated into their matching DaVinci Resolve annotation graphics so they’re visible in DaVinci Resolve.

On your DaVinci Resolve Timeline, comments and graphical annotations out of Frame.io show up as markers carrying their matching overlays Working With Frame.io Markers Double-click any Frame.io marker on the Timeline to open a dialog where you can fire back replies to the comments living on Frame.io, letting editors answer commenters straight away. You may likewise drop Frame.io markers onto the Timeline so they sync automatically back to Frame. io, granting you the means to return your own comments to commenters (be kind). Delete one or more Frame.io markers on the DaVinci Resolve timeline and those same markers vanish in Frame.io too. The Mark > Delete All Markers > Frame.io command falls under this. There’s no undoing it.

An editor holding a one-sided conversation through the Frame.io comment dialog surfaced upon opening a Frame.io marker

### Frame.io Marker Navigation

While inside the comment dialog of a Frame.io marker, you can step through only the markers born in Frame.io, leaning on the Previous Marker (Shift-UpArrow) and Next Marker (Shift-DownArrow) commands. That lets you leap straight from one Frame.io comment to the next without trudging through every in-between marker or double-clicking each Frame.io marker on its own to reply. Frame.io interoperability is a Studio Only feature.

### Importing Media from Frame.io

Within the Media Storage panel of the Media page, a Frame.io volume turns up that opens access to the media your Frame.io account holds. Inside that Frame.io volume, a top-level directory stands for your account directory, and beneath it every project you’ve built in Frame.io shows up as a sub-directory.

Reaching a Frame.io account’s directories by way of the Media Storage browser Whatever media files Media Storage can reach may be brought into the Media Pool through the usual means. After it joins the Media Pool, that media file downloads quietly in the background to the named local cache location, yet it’s ready at once over your internet link before the download wraps, letting you dive in right away. To check how long the download needs, choose Workspace > Background Activity and open the Background Activity window.

Through the Background Activity window you can watch whatever the background is doing as you keep working

### Linking Media Pool Clips and Timelines with Frame.io Clips

Frame.io reach within the Media Storage panel of the Media page can also be used to tie clips or timelines to media you’ve already pushed up to your Frame.io account. Simply find and select a Frame. io clip inside Media Storage, then right-click the clip or timeline in the Media Pool you’d like it tied to and pick Link to Frame.io Media off the contextual menu. Once you’ve tied a Frame.io clip to a timeline, comments left on that Frame.io clip surface on the linked timeline as Frame.io markers, exactly as though you had exported that timeline straight to Frame.io.

### Enabling Dropbox Replay Integration in Preferences

Under the System tab of the DaVinci Resolve Preferences, an Internet Accounts panel lets you log in to your Dropbox account. Activating Dropbox integration calls for your login name and password, yet after they’re entered, DaVinci Resolve logs in on its own each time DaVinci Resolve launches.

The Dropbox Login window, sitting inside the Internet Accounts panel under the System tab within the DaVinci Resolve Preferences window.

### Deliver and Upload to Dropbox Replay

Sitting at the top of the Deliver page’s Render Settings panel, a Dropbox Replay preset lets you render a program and push it up for review. Every option across the Render Settings panel refreshes to show controls fit for this purpose. NOTE: The Dropbox Replay Render settings stand apart from the ordinary Dropbox Render settings, and this particular set of presets is the one you must use to hook into Dropbox Replay.

The Dropbox Replay Render settings (highlighted); bear in mind they aren’t the same as the ordinary Dropbox Render settings sitting over to the left. Exporting to Dropbox Replay trims the selectable entries in the Resolution, Format, Video Codec, and Audio pop-up menus down to those best matched for Dropbox Replay. Set the export options you want, then press the Add to Render Queue button to drop this job into the Render Queue just as you would for any other export. After that job renders, it moves on by itself to upload to Dropbox Replay, and the job listing shows an upload percentage indicator marking how far the upload has gotten. Upon completion, the job reads “Upload completed.” Within the Render Queue, the listing reports the file’s upload percentage and signals you once it has wrapped. Because this upload runs in the background, you can keep busy with other tasks in DaVinci Resolve as the file goes up. To check how long the upload needs from any other page, choose Workspace > Background Activity and open the Background Activity window.

### Unlinking a Timeline from Dropbox Replay

Should you want a particular timeline to stop using Dropbox Relay integration, just right-click on the Timeline and pick Unlink from Dropbox Media off the contextual menu.

### Upload New Versions to Dropbox Replay

The versioning features within Dropbox Replay are supported by DaVinci Resolve. This makes it simple for the Replay user to comment on and flip between the various versions of one clip. After the original timeline is rendered and pushed up to Dropbox via the Replay preset on the Deliver page, an extra checkbox surfaces within the preset, named “Upload as new version.” With that box ticked, every later render of this timeline lands automatically on the clip’s version stack inside Dropbox Replay. Within the Replay interface, the newest version stays the clip’s default every time.

### Dropbox Replay Comments Sync with Timeline Markers

Render a timeline straight to Dropbox Replay and that timeline links automatically to the movie pushed up to Dropbox Replay, so every comment and graphical annotation (drawings and arrows) that reviewers add online through the Dropbox Replay interface syncs automatically to Dropbox markers on your timeline (provided your computer holds an active internet connection). Dropbox markers stand apart from all the other markers and may be shown, hidden, or deleted on their own. Drawings and arrows out of Dropbox Replay get translated into their matching DaVinci Resolve annotation graphics so they’re visible in DaVinci Resolve.

On your DaVinci Resolve timeline, comments and graphical annotations out of Dropbox Replay surface as markers bearing their matching overlays.

### Working With Dropbox Markers

Double-click any Dropbox marker on the Timeline to open a dialog where you can fire back replies to the comments living on Dropbox Replay, letting editors answer commenters straight away. The Dropbox Replay comment dialog surfaced upon opening a Dropbox marker You may likewise drop Dropbox markers onto the Timeline so they sync automatically back to Dropbox Replay, granting you the means to return your own comments to commenters (be kind). Delete one or more Dropbox markers on the DaVinci Resolve timeline and those same markers vanish in Dropbox Replay too. The Mark > Delete All Markers > Dropbox command falls under this. There’s no undoing it Dropbox Marker Navigation While inside the comment dialog of a Dropbox marker, you can step through only the markers born in Dropbox Replay, leaning on the Previous Marker (Shift-UpArrow) and Next Marker (Shift-DownArrow) commands. That lets you leap straight from one Dropbox Replay comment to the next without trudging through every in-between marker or double-clicking each Dropbox marker on its own to reply.
