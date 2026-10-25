# Multiple compositing artists working together and editors and colorists working together

Version: DaVinci Resolve 20.3 Reference Manual. Context: Collaborative workflow.
[Chapter index](INDEX.md) / [Previous section](editor-and-assistant-editor-collaboration.md)
<a id="source-collaboration-chat"></a> <a id="source-editors-and-colorists-working-together"></a> <a id="source-managing-notes-among-collaborators"></a> <a id="source-multiple-colorists-working-together"></a> <a id="source-multiple-compositing-artists-working-together"></a>

### Multiple Compositing Artists Working Together

So that no versioning conflicts arise, a given clip in the Fusion page can only be open to a single compositing artist at any moment, and whoever selects a clip first locks it. Anyone else viewing the Thumbnail timeline in the Fusion page sees a tiny icon marking it as locked, signaling that they cannot touch it until the person editing that composition switches to a different clip.

That tiny icon tells you a fellow compositing artist has the clip open and you are shut out, which means no two compositing artists can edit the same composition simultaneously. That said, an assisting compositing artist is free to handle setup chores on one composition — things like rotoscoping, paint, particle system design, or other tasks that eat up time — while a lead compositing artist tackles a separate shot at the same moment. After the assisting compositor wraps up, they pick a new clip and message the other compositor over collaborative chat to report that the work is finished and the clip is open for further effort. To keep incomplete work from spreading to the rest of the team, a clip currently being worked on in the Fusion page stays unrefreshed for everyone else on that same timeline until the compositing artist handling it moves to a different clip. The instant it is deselected, every edit is checked in automatically and pushed out to all the other collaborators, who get notification badges in the Fusion page and the Edit page warning them that updates exist and that they can reload their timeline to pull them in.

### Editors and Colorists Working Together

In DaVinci Resolve, colorists and editors are able to collaborate tightly, because a colorist can grade the shots in a timeline that an editor still has open, even when that timeline and its bin are locked against other editors. Seen from the colorist's side, each time the editor changes the Timeline a badge shows up at the top-right corner of the Color page Viewer to flag that the timeline under grade has shifted. Clicking that badge brings the colorist's timeline up to date. To stop unfinished work from leaking to the editor — or, worse yet, being shown to the client — clips being graded stay unrefreshed for other collaborators viewing that timeline until the colorist handling them "checks in" by jumping to a different clip. So, from where the editor sits, the moment a colorist wraps up a grade on one clip and picks another to grade, a set of badges turns up in the Edit page — one marks the graded clip, another marks the Timeline Viewer, and a third marks whichever bin in the Bin List houses the Timeline. Clicking any of them refreshes the Timeline with the newest grades.

### Multiple Colorists Working Together

A particular clip can only be open to one colorist at a time, and the colorist who selects it first locks it. Everyone else looking at the Thumbnail timeline in the Color page sees a small icon marking it as locked, telling them they cannot alter it until whoever is grading that clip switches to a different one.

That small icon means a different colorist has the clip and you are locked out. To prevent half-done work from reaching other colorists or editors, a clip in mid-grade is not refreshed for the other collaborators viewing that timeline until the colorist working it picks another clip. Those edits are then handed automatically to every other collaborator in the Color page, who watch badges show up across the Edit and Color pages flagging which clips have updates waiting. That arrangement lets several colorists cooperate smoothly. As an example, an assistant colorist might get a Collaborative Chat message asking them to draw a custom window a senior colorist requires for a grade. The assistant brings up that timeline in a separate suite, picks the right clip, and draws the window. Done with that, the assistant just selects a different clip, and the edits they made surface immediately for the senior colorist, who sees a badge on the clip in the Thumbnail timeline and can click it to refresh.

### Managing Notes Among Collaborators

When an editor needs to pass a note to colorists or compositing artists, any of these options work:

- They can attach a marker carrying note text to the Timeline ruler (the marker turns up in the marker submenu of the Color page Viewer option menu)
- They can attach a marker carrying note text to a clip (the marker then surfaces in the mini-timeline of the Color page)
- They can apply different color codes to clips to flag them for the colorist (the clip color coding shows up as a dot in the Thumbnail timeline).
- And naturally, the editor and colorist can always talk through the collaborative chat window too.

### Collaboration Chat

So that collaborators can talk to one another, DaVinci Resolve ships with built-in text chat, named Collaboration Chat. Just click the Collaboration Chat button to bring up the chat window, and start typing.

The Collaboration Chat window lets collaborators talk to each other; the Collaboration Chat button along the bottom of the DaVinci Resolve interface glows orange any time someone writes while the window is shut, so you know messages are sitting there for you. The Collaboration Chat button lights up to signal that a message has arrived.
