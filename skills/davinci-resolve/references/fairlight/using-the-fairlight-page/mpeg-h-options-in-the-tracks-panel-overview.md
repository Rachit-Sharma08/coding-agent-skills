# Mpeg h options in the tracks panel overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](preview-and-audition-controls-and-sound-effect-list.md) / [Next section](switch-group-manager-and-dropdown-in-the-sw-group-column.md)
<a id="source-mpeg-h-options-in-the-tracks-panel"></a> <a id="source-using-the-fairlight-page-part-4"></a>

### MPEG-H Options in the Tracks Panel

When MPEG-H is switched on for immersive audio authoring in the Video and Audio I/O preference pane, extra columns appear in this panel. Among those columns are:

- Track Type: Lets you define either a static component or a dynamic object. Choose dynamic and that track's dynamic track-level pan automation gets exported as well. Only a track can be set to dynamic.
- Kind: A content type label — Mixed content, Music, Dialogue, Effect, and so on. Once Kind is set for a bus (instead of the default Undefined state), that bus is bounced automatically through the export process.

With MPEG-H switched on, the Tracks panel surfaces extra columns of metadata for defining each track in the Timeline.

- Language: Sets the language tied to that particular track's content. Switch Group: Lets a track be placed into a switch group that you define. Such a group bundles a track together with others within the finished content, producing one selectable option once it's rendered. As an illustration, a dialogue switch group holding both an English and a Chinese language track might let the viewer pick a language during playback. To set up a switch group, click the relevant cell in that track's Switch Group column and pick “Sw Groups…” to bring up the Switch Groups Manager window, where new switch groups get created.
