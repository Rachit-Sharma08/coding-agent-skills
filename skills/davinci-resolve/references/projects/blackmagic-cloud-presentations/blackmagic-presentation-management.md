# Blackmagic presentations and creating and managing presentations

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blackmagic cloud presentations.
[Chapter index](INDEX.md) / [Next section](viewer-controls-and-markers.md)
<a id="source-blackmagic-cloud-presentations"></a> <a id="source-blackmagic-cloud-presentations-1"></a> <a id="source-blackmagic-presentations"></a> <a id="source-controlling-a-clip-in-the-viewer"></a> <a id="source-creating-a-new-presentation"></a> <a id="source-creating-and-managing-presentations"></a> <a id="source-deleting-a-presentation"></a> <a id="source-enabling-and-disabling-a-presentation"></a> <a id="source-leaving-a-presentation"></a> <a id="source-renaming-a-presentation"></a> <a id="source-selecting-a-clip"></a> <a id="source-sharing-a-presentation-with-another-user"></a> <a id="source-the-clips-column"></a> <a id="source-the-information-panel-of-a-presentation"></a> <a id="source-the-my-presentations-column"></a> <a id="source-using-presentations"></a> <a id="source-video-conferencing"></a> <a id="source-viewer-controls"></a>

### Blackmagic Cloud Presentations

This chapter walks through working with the Presentations application within the Blackmagic Cloud, which lets you run online review and collaboration sessions alongside people anywhere in the world.

### Blackmagic Presentations

Through nothing more than an internet browser, the Presentations application in Blackmagic Cloud enables real time collaboration on and review of DaVinci Resolve timelines. Its collaboration tools cover video conferencing for live communication, a chat interface that retains notes and comments, plus markers syncing straight to a DaVinci Resolve timeline. Using them, every user can watch a video with frame accurate sync while video conferencing simultaneously.

The Blackmagic Presentations application in a web browser Three parts make up the Presentations application. Along the left runs My Presentations, the column where your various presentations get created, kept, and arranged. The middle holds the Viewer, used to move through the clip, drop markers, and set the audio playback. Sitting above the Viewer is the Video Conferencing area, your space for collaborating live with fellow members. The right column breaks into three sections: Clips, Markers, and Chat. Clips lists every clip on hand to comment on and collaborate over. Markers presents a roster of markers and comments that sync with a DaVinci Resolve timeline. Chat brings up a plain chat interface so a record of your notes and comments exists. NOTE: At the time of writing, Presentations remains in beta. Being beta software, whatever features appear below could be altered, reworked, or dropped entirely before the final release.

### Creating and Managing Presentations

Two pieces make up online collaboration in Presentations: first the Presentation within the Blackmagic Cloud, and second a timeline coming from a DaVinci Resolve workstation (covered below). This section covers how Presentations get created and managed. NOTE: Presentations applies somewhat different terminology for clips than DaVinci Resolve does. Within Presentations, a “clip” means a DaVinci Resolve “timeline,” rather than a clip you'd come across in the Media Pool.

### Creating a New Presentation

Picture each presentation as akin to a project in DaVinci Resolve, only it centers on discussion instead of post production. Presentations hold several “clips” for review and carry an assortment of collaboration tools rather than editing/color/fx/audio tools. Spinning up a fresh presentation per project works fine, yet you may equally build presentations around other criteria, such as who's collaborating, a date, or a particular phase of post production. Here's how to build a Blackmagic Cloud Presentation: 1 Sign in to your Blackmagic Cloud account through a web browser at www.blackmagicdesign.com. 2 Click the Presentations icon at the upper center of the web page. 3 Within the My Presentations column, click the Add Presentation button down at the lower left. 4 Choose a Name for the presentation and click Add. 5 Click the Presentation inside the My Presentations column to open it.

### The My Presentations column

When you've amassed more presentations than the screen can hold, the My Presentations column sorts by name and date, ascending or descending, via the sort icon just off to the right. Searching the My Presentations column is possible too by clicking the magnifying glass on the right and typing your search terms. Only the presentations that match your terms appear. Up until you've uploaded a first clip from a DaVinci Resolve project, the Viewer reads “Upload clips from DaVinci Resolve to get started.” The “Sending a Timeline to Presentations” section further down covers that process.

### Sharing a Presentation with Another User

A presentation can be shared with as many as 10 other users. The single prerequisite is that every one of them holds a Blackmagic Cloud account of their own. Here's how to share a Blackmagic Cloud Presentation: 1 Click the information icon (the circled letter i) beside the presentation name. That opens a Members pane listing all the current users the presentation is shared with. Whoever holds the crown icon is the presentation administrator, and they alone can add or remove users. 2 Click the Share button at the foot of the Members pane. 3 Type the email address (the one used to set up the Blackmagic Cloud account) of the user you'd like to share the presentation with. 4 Click the Share button.

### The information panel of a presentation

That user's name then shows in the Members pane, and the presentation surfaces in their own My Presentations column once they sign in to the Blackmagic Cloud. From there they're free to watch any clips, video conference, or leave comments inside that presentation. On top of that, an email goes out to the user's email address, telling them about the presentation and giving a direct link to reach it. Removing a user from a presentation is simply a matter of clicking the “x” beside their name in the Members panel. Only the administrator may add or remove members.

### Enabling and Disabling a Presentation

The administrator may opt to disable a presentation for a while. This temporarily locks down access to it without erasing anything. Every clip, user, and comment stays put, and the only effect is that the presentation can't be viewed or changed until it's enabled once more. To Enable or Disable a Blackmagic Cloud Presentation 1 Click the Information icon (the circled letter i) beside the presentation name. 2 Click the Presentation enabled switch right under the presentation name to flip between enabling and disabling the presentation.

### Renaming a Presentation

The administrator can readily rename a presentation so it better captures its purpose or contents. To Rename a Blackmagic Cloud Presentation 1 Click the Information icon (the circled letter i) beside the presentation name. 2 Click the Settings icon (the small gear) beside the presentation name. 3 Choose Rename out of the drop-down menu. 4 Enter the presentation's new name. 5 Click the Save button. The presentation's name is then refreshed in the My Presentations column for every user.

### Deleting a Presentation

Once you're done with a presentation, the administrator may remove it from the Blackmagic Cloud. Deleting a presentation wipes out all of its clips and comments for good and can't be undone, so be certain you're entirely finished before deleting. To Delete a Blackmagic Cloud Presentation 1 Click the Information icon (the circled letter i) beside the presentation name. 2 Click the Settings icon (the small gear) beside the presentation name. 3 Choose Delete out of the drop-down menu. 4 Click the Delete button in the warning dialog box.

### Leaving a Presentation

You as a user may step away from a Presentation whenever you like. Doing so strips your permission to view and edit the presentation and clears it from your My Presentations column. Should you want back into a presentation after leaving, its administrator will need to re-share it with you. Here's how to leave a Blackmagic Cloud Presentation: 1 Click the Information icon (the circled letter i) beside the presentation name. 2 Click the Settings icon (the small gear) beside the presentation name. 3 Choose Leave out of the drop-down menu. 4 Click the Leave button in the warning dialog box.

### Using Presentations

At the core of Presentations sits the Viewer; from here you can both video conference and steer a clip's playback. The Viewer delivers a low latency, streaming video that you can mark and comment on precisely, with those comments appearing live for other users and on the DaVinci Resolve timeline.

### Video Conferencing

Across the top of the Viewer runs a simple video conferencing interface, where every user's video stream shows up in a live thumbnail. The camera and microphone start off switched off, so you'll have to enable them yourself.

The video conferencing interface; spot the Camera and Microphone on/off controls over in the upper right. Here's how to switch the Camera and Microphone on and off for a Blackmagic Cloud Presentation: 1 Click the Camera and/or Microphone icons up at the right of the Viewer. 2 Grant your OS and browser the permissions they need to use the devices. 3 To switch the Camera and Microphone back off, click their respective icons once more. With your camera and microphone running, every other connected user sees and hears you over their web browsers, so stay generous and discreet with your comments.

### Controlling a Clip in the Viewer

Every user can watch and comment on any clip (the same one included) in real time. Each user's Viewer runs independently of the rest, though the administrator may sync everyone's Viewer to theirs so the same clip plays for all at once.

### Selecting a Clip

Choosing a clip to watch is as simple as clicking its thumbnail in the Clips column. Clips can be sorted by date, duration, and name in ascending or descending order. Searching the Clips column is possible too by clicking the magnifying glass on the right and typing your search terms. Only the clips that match your terms appear. Hovering your pointer across a clip thumbnail also lets you scrub the video. Administrators may rename and remove clips from the presentation by hovering over the thumbnail and clicking the matching icons (pencil and trashcan) up at the right.

### The Clips column

### Viewer Controls

Along the bottom of the browser the Presentations Viewer carries a row of playback controls for placing your playhead exactly.
