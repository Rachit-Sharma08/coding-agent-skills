# Viewer controls and markers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Blackmagic cloud presentations.
[Chapter index](INDEX.md) / [Previous section](blackmagic-presentation-management.md)
<a id="source-presentations-in-davinci-resolve"></a> <a id="source-sending-a-timeline-to-presentations"></a> <a id="source-the-chat-column"></a> <a id="source-the-markers-column"></a> <a id="source-the-viewer-controls"></a> <a id="source-using-chat"></a> <a id="source-using-markers"></a> <a id="source-using-markers-between-presentations-and-davinci-resolve"></a>

### The Viewer controls

Jog Bar: The long line spanning the bottom of the browser marks your present playhead position as a rectangle along with any markers already placed. Click and drag the playhead to scrub forward and back through the clip. Timecode: The current clip's timecode, which points back to the original DaVinci Resolve timeline. Previous Clip: (Up Arrow) Pulls into the Viewer whichever clip sits above the current one within the Clips column. Should the current clip already sit at the top of the stack, it wraps round to the clip at the bottom. Stop: Halts the clip's playback inside the Viewer. Play: Runs the clip forward inside the Viewer at 1x speed. Next Clip: (Down Arrow) Pulls into the Viewer whichever clip sits below the current one within the Clips column. Should the current clip already sit at the bottom of the stack, it wraps round to the clip at the top. Loop: Cycles among no looping (the default), Loop One which repeats the current clip endlessly, and Loop All which runs through every clip in the Clips column and loops back to the start of the stack. Volume: A click on this icon mutes the audio. The slider beside the icon, when dragged, sets the clip's volume. Start Sync: (Administrator only), a click on this icon makes your Viewer's contents appear for every member. The administrator's view takes over the Viewers of all the other users, so everyone watches the same thing together. Add Marker: A click on this icon drops a marker at the playhead position. Editing and commenting on that marker happens in the Markers column covered below. Full Screen: This grows the Viewer to fill the whole screen.

NOTE: The left and right arrow keys move the playhead one frame back and forward respectively.

### Using Markers

You have three avenues for voicing your view on a clip in Presentations. The first is talking straight through video conferencing as covered above; the second and third run through markers and chat. Markers let you pin written comments to a specific frame of video. That way your targeted notes land exactly where they belong. The chief upside of markers is that they likewise carry over at once to the DaVinci Resolve timeline the clip was built from. That guarantees your comments reach the editor/colorist/audio engineer while they work the project.

### The Markers column

To drop a marker onto a clip at wherever the playhead sits, take one of these routes:

- Click on the Add Marker icon in the Viewer.
- Tap the letter M on your keyboard.
- In the Markers column, write your comment in the text

box down at the bottom and click the Add Marker button. A marker shows up as a triangle sharing the tint of the colored dot linked to that user's thumbnail over in the Video Conferencing pane. Here's how to revise a marker's text: 1 Float over the marker within the Markers column and tap the Pencil icon. 2 Enter your comment into the text box. 3 Click save. Here's how to remove a marker from a clip: 1 Float over the marker within the Markers column and tap the Trashcan icon. 2 Click Delete in the warning dialog.

### Using Chat

The Chat column hands you a plain text-based conversation tool that's kept around permanently. With it you can drop notes and comments and look back at earlier sessions when needed. Rather than belonging to any one clip, the Chat column belongs to the presentation overall. To Leave a Chat Comment: 1 Type your message in the text box at the foot of the Chat column. 2 Press the Send icon. Your message lands in the chat window in chronological order. The chat messages you've sent show up unattributed and right justified. Messages from other members show up left justified, carrying their names and User icon. For now the chat is visible to every member of the presentation, and a chat message can't be deleted once sent, so be kind.

### The Chat column

### Presentations in DaVinci Resolve

The Presentations application is built to operate hand in hand with DaVinci Resolve. Every “clip” in Presentations ties to a DaVinci Resolve timeline. Whatever markers members add inside Presentations get pushed to the timeline in DaVinci Resolve automatically, and the reverse holds as well.

### Sending a Timeline to Presentations

Every “clip” in Presentations is a DaVinci Resolve timeline. To fill the Clips column with footage to work on, you first have to export your timeline out of DaVinci Resolve into Presentations.

The Presentations Render Preset sitting on the Deliver page. Here's how to push a DaVinci Resolve Timeline over to Presentations: 1 Confirm you're signed in to your Blackmagic Cloud account within the Internet Accounts section of the DaVinci Resolve Preferences. 2 Confirm you belong to the presentation you intend to send the timeline to. 3 Open the timeline you intend to send. 4 On the Deliver page, choose the Presentations render preset. 5 In the File Name field, type the name your timeline should carry inside Presentations. 6 In the Upload to field, choose the presentation you'd like the timeline uploaded to. Should the presentation be missing from the list, revisit steps 1 and 2. 7 Click the Add to Render Queue button at the foot of the Render Settings. 8 Click the Render All button beneath the Render Queue.

No video or audio codec parameters need setting, and DaVinci Resolve goes ahead to render your timeline and upload it automatically to the chosen presentation. Uploading a timeline to a presentation is open to any member, not the administrator alone. Your timeline now turns up as a “clip” within the presentation's Clips column.

### Using Markers Between Presentations and DaVinci Resolve

A major plus of Presentations is markers that persist between a presentation and a DaVinci Resolve timeline. After a timeline has been uploaded to a presentation, it's linked behind the scenes automatically, and whatever markers get added, whether inside the Presentations app or in DaVinci Resolve, sync to one another. On the DaVinci Resolve end, that sync happens whenever a timeline is open and the user is signed in to the Blackmagic Cloud. As an example, members might add markers overnight, and they'll then sync once the editor opens the timeline come morning. Live collaboration with a presentation is also possible when the members are online and the editor is working the timeline, updating markers in real time.

Presentations markers carry a circular shape and stay synced between the timeline and its paired Presentations clip. Markers tied to Presentations render as circular on the DaVinci Resolve timeline, setting them apart from ordinary markers, which are triangular. Presentations Markers also take on the color of the member who created the marker. The flow of markers isn't only one way from Presentations into DaVinci Resolve. While working a timeline in DaVinci Resolve, the user can drop special Presentations markers that sync and appear inside the Presentations application for every member to see. Here's how to place a Presentations marker on a DaVinci Resolve Timeline: 1 A timeline must already have gone up to Presentations per the steps above. 2 Park the playhead at the Timeline spot where the Presentations marker belongs. 3 Choose Mark > Add Marker > Presentations. Here's how to clear a Presentations marker from a DaVinci Resolve Timeline: 1 Pick the circular Presentations marker sitting on the Timeline. 2 Hit the Delete key. 3 Click the Delete button in the warning dialog. Removing a Presentations marker takes it off both the Timeline and the presentation itself. This action can't be undone. The timeline user may delete a Presentations marker belonging to any member, not just their own.
