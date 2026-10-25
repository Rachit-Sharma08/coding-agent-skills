# Track groups and editing with track groups

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio overview.
[Chapter index](INDEX.md) / [Next section](group-management-via-mixer-channel-strips-overview.md)
<a id="source-create-group---group-settings-dialog"></a> <a id="source-create-groups-icon"></a> <a id="source-creating-and-editing-track-groups"></a> <a id="source-editing-with-track-groups"></a> <a id="source-groups-list"></a> <a id="source-groups-list-controls"></a> <a id="source-mixing-with-track-groups"></a> <a id="source-overview"></a> <a id="source-showing-the-groups-list"></a> <a id="source-the-all-group"></a> <a id="source-the-mixer-and-track-groups"></a> <a id="source-the-selected-checkbox"></a> <a id="source-tools-icon-to-launch-modify-groups-dialog"></a> <a id="source-track-groups"></a> <a id="source-track-groups-1"></a> <a id="source-track-groups-audio-effects"></a>

## Overview

Covers: Track Groups; Audio Effects.

## Track Groups

### Track Groups

Track groups give you a way to apply adjustments and edits to your mix over several tracks all at once.

### Editing with Track Groups

Track groups let you shift your attention from single tracks onto bundles of tracks, anything from a handful of tracks up to a sizable multitrack sub-mix group. Once a group is on, an editing action carries across every track within it. Some actions that shift clip boundaries or trim, however, behave differently. As an example, tapping the Up and Down arrows to jump between clip boundaries respects the boundaries of each track inside the group, no matter where they stack vertically in the timeline. You can switch groups off to return your focus to the individual tracks they hold. Yet when smaller groups sit “nested” inside a bigger one, disabling the larger group leaves the smaller group untouched. Where an edit group holds clips of unequal lengths, the group behavior still holds, so that every edit—trim, cut, or paste—follows the group at whatever boundaries it currently has.

### Mixing with Track Groups

While mixing with track groups, an adjustment to one channel applies to all the others in the group at the same time. That spans fader moves, panning settings, send levels, automation, plus toggles of the mute, solo, and record-arm buttons.

NOTE: Plugin controls cannot be added to Mix groups.

### Showing the Groups List

Click the Groups button in the Interface Toolbar to open and close the Groups list. Should the Track Index or other Index tabs already be open, the Groups list shows up below them. Even after you shut the Track Index, or click any of the remaining Index tabs, this list keeps showing.

### Groups list

### Groups List Controls

Group Name: This column shows the group name or “ID.” Groups Switch: Flips all groups on or off, letting you move smoothly from working with groups to working with individual tracks.

Selected Checkbox: When ticked, every track belonging to the group is selected. If only part of them are selected, a hyphen appears instead. Action Icons on Hover: These icons surface only while you hover over the group row. The Tools icon opens the Modify Groups dialog, and the Trash icon removes the group.

### The All Group

The All Group holds every track's Mixer channels, which makes editing or mixing across all tracks at once simple. This group always lives at the top of the Groups list.

### The Selected Checkbox

Ticking the Selected Checkbox places a checkmark, which means every track inside the group is now selected. That makes it simple to build on a current group (shift-clicking to bring in more members and using Create Group) or to steer the routing of all selected tracks together by holding the Option (Alt Windows) keys while assigning or unassigning. Say, for instance, we've got Group 1 with six tracks and Group 2 with 10. Just click the Selected checkbox for Group 1, and every track in Group 1 gets selected. Then hold Shift and click the checkbox beside Group 2. Now both groups' members are selected, and you can build a new Group 3 containing all of them.

- A hyphen (“-“) is shown if only some tracks are selected.
- Clicking the checkbox to remove the checkmark or hyphen deactivates the group.

NOTE: Whether a group sits enabled or disabled has no bearing on the Selected checkbox; it stands as its own control, not bound directly to grouping.

Group Key Commands Switch Groups on or off with Command + num keypad 0 key (Control on Windows). Use Command (Control on Windows) + num keypad number 1-9 to switch the first nine groups on or off. Use Command (Control Win) + num keypad \* key to toggle the All Group.

### Creating and Editing Track Groups

To create a track group, do one of the following:

- Pick one or more tracks through their track headers in the Timeline. Right-click any track you'd like in the group and choose Create Group. The same works in the Mixer on a channel strip.
- Pick one or more tracks through their track headers in the Timeline. Then click the Create Group icon at the top-right corner of the Groups list.

### Create Groups icon

Inside the dialog that opens, proceed this way: 1 Give the group a name. To choose a group color, click the dropdown list sitting to the right of the Group Name field. 2 Decide which controls belong to the group (Editing, Fader, Solo, Mute, Arm, Sends, Panning, and Automation). Hit Set as Default and these choices stick for any groups you make later. 3 Highlight tracks within the Add Channels column at the left, then click the >> icon to move the highlighted tracks into the group. The same way, highlight tracks in the Channels Added column at the left and click the << icon to take those tracks out again. 4 Hit Save to store the group. 5 Up pops the new group in the Groups list.

### Create Group - Group Settings dialog

To activate or deactivate a group:

- In the Groups list, select or deselect the group. A selected group lights up, a sign that it's active.

To rename a group:

- Double-click the group name in the Groups list.
- Type the new name you want for the group.

To edit a group:

- Hover over the group you'd like to edit and click the Settings icon to bring up the Modify Groups (Group Settings) dialog.
- Make whatever changes you want, then pick Save.

### Tools icon to launch Modify Groups dialog

Removing a track group: 1 Open the Tracks Index. 2 Within the Groups list, hover over whichever group you want gone, click the Trash Can icon on the right, then hit the Delete button in the confirmation dialog.

### The Mixer and Track Groups

Temporary Override (“Clutch”) As you work the Mixer, hold Command‑Shift (Mac) or Control-Shift (Windows) while nudging one fader or several within a group, and you can move them independently of the group's other members (in other words, this acts like suspending the group just for whichever faders you've “clutched”).
