# Navigating using the color page timeline and color page timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page timeline and lightbox.
[Chapter index](INDEX.md) / [Next section](thumbnail-information-and-representative-image.md)
<a id="source-color-page-timeline-and-lightbox"></a> <a id="source-color-page-timeline-and-lightbox-part-1"></a> <a id="source-enablingdisabling-tracks"></a> <a id="source-mini-timeline"></a> <a id="source-navigating-to-clips-using-clip-number"></a> <a id="source-navigating-using-the-color-page-timeline"></a> <a id="source-scrolling-zooming-and-navigation"></a> <a id="source-setting-inout-points-for-looping"></a> <a id="source-show-current-clip-with-handles"></a> <a id="source-the-color-page-mini-timeline"></a> <a id="source-the-color-page-thumbnail-timeline"></a> <a id="source-the-color-page-timeline"></a> <a id="source-thumbnail-timeline"></a> <a id="source-using-multiple-timeline-playheads"></a>

### Color Page Timeline and Lightbox

Made up of the Thumbnail Timeline together with the Mini‑Timeline, the Timeline found in the Color page mainly helps you move through how clips are currently laid out, and keep tabs on per-clip attributes — for instance whether a shot is graded or ungraded, whether tracking is in play, the version that's active, and the like. Beyond that, it speeds up duplicating grades between clips, building groups, and lining shots up side by side in the Viewer. Acting as the Thumbnail Timeline's counterpart, the Lightbox offers a picture-driven way to weigh clips against each other, handle grades, and carry out many kinds of sorting jobs. The pages ahead describe how both the Timeline and the Lightbox are used.

### Navigating Using the Color Page Timeline

Two cooperating components make up the Color page Timeline: the Thumbnail Timeline plus the Mini Timeline. In tandem they give you several distinct ways to inspect and travel through your program's Timeline.

### The Color page Timeline

Each of the two scroll bars — one for the Mini-Timeline and one for the Thumbnail Timeline — operates separately, so each may be configured to reveal a different span of clips. Rolling your pointing device's scroll control adjusts the Mini-Timeline's zoom level inward or outward. At its fullest zoom-out, the Mini-Timeline fits the whole timeline inside whatever screen width is on hand, giving you a quick route from the program's start clear through to its finish. Even so, you're free to zoom in on a given stretch whenever you require more detail about how a dense stack of layered clips is laid out as you grade.

### Thumbnail Timeline

Gives you a compact picture of the project in which every clip shows up as one numbered thumbnail no matter how long it runs. A click on any thumbnail jumps the playhead onto that clip's opening frame, whereas the Up/Down Arrow keys shift the selection back to the prior clip or ahead to the following one. The clip sitting under the playhead's present location is shown with an orange border around its thumbnail. Both middle‑click-and-drag and your pointing device's scroll wheel let you roll back and forth across the Thumbnail timeline.

### The Color page Thumbnail Timeline

Above and beneath every thumbnail sits assorted data — among it a rainbow border encircling the count of graded clips, the text under each thumbnail showing clip format, file name, or grading version, badges for tracking or stabilization, flag badges, plus link badges that signal clip groups or automatic remote grade linking wherever it applies.

### Mini-Timeline

Presents a scaled-down version of the Edit page's Timeline, with the width of each clip matching how long it lasts and any layered clips stacked over each other. No more than six video tracks fit in the Mini‑Timeline at once; should your edit carry additional ones, a scroll bar lets you swap which tracks show. A click on any clip within the Mini-Timeline picks that clip and parks the playhead on its opening frame.

### The Color page Mini-Timeline

### Scrolling, Zooming, and Navigation

Housing the playhead's top handle, a Timeline Ruler shows the record timecode for the present edit and works as a scrubber bar that normally covers a wider stretch of the Timeline. Your mouse's scroll wheel zooms your edit both ways, and zooming fully out lets you pack every clip of the Mini-Timeline within the ruler's available width, so you can scrub through the Timeline's entire run of clips fast. A click on any spot inside the ruler snaps the playhead straight to that frame.

### Enabling/Disabling Tracks

Track numbers for each track sit at the Mini-Timeline's far left, and floating the pointer above any track's number in the Color page's Mini-Timeline surfaces a tooltip with that track's name. A click on a track number toggles that track on or off together with every clip riding it, much as the Timeline > Enable/Disable Video Tracks submenu commands do (Shift-Command-1 through 9). Clips sitting on switched-off tracks neither render in the Viewer nor in video output, and they vanish from the Thumbnail Timeline. Should a track already be disabled back in the Edit page, it shows up dimmed within the Mini-Timeline. Option-clicking a Mini-Timeline track number tints that track number red, which lets you conceal clips from the Thumbnail Timeline while leaving the video in your program enabled. That comes in handy when you'd rather keep clips on one track (say, titles or motion graphics rendered by a separate program) from catching the playhead as you run the next/previous clip commands.

### Setting In/Out Points for Looping

The I and O keyboard shortcuts let you place your own In and Out points across the Timeline. After they're set, switching on Loop within the Viewer transport controls makes that span loopable, be it a piece of a single clip or a stretch covering several clips at once.

### Navigating to Clips Using Clip Number

Within the Color page you can leap straight to any particular clip by referencing its clip number in the Color timeline. To reach a clip, pick Playback Go To > Clip Number, then key a clip number into the timecode entry field and hit Enter. Doing so selects that clip and parks the playhead at its start. As an alternative, you may key in the clip number first and then choose the menu command in place of pressing Enter, yielding the same outcome. To work faster, you can also bind this operation to a keyboard shortcut named "Clip Number" if it's something you reach for regularly.

Shown in red, the timecode entry area is where a clip number gets typed to leap there during a Go To Clip Number operation

### Using Multiple Timeline Playheads

Within the Mini-Timeline, DaVinci Resolve lets you make as many as four independent playheads, handy for hopping between separate spots in your timeline. At any moment just one playhead may be active, and whichever is active marks the current clip, shown in orange. Every Mini-Timeline playhead carries a label running from the letter A through D.

Several Mini-Timeline playheads serving multi-region navigation How you place a fresh playhead into the Mini-Timeline:

- Pick a playhead out of the Color > Active Playheads submenu. It lands wherever the original playhead sits, yet it's now the active one, so dragging the fresh playhead somewhere else in the Mini-Timeline will uncover the original playhead you had been on.

To select another playhead to view:

- Click the top handle of whichever playhead you want to make it the active one driven by the transport controls. Out of the box none of the four available playheads carry keyboard shortcuts, but you can build a custom keyboard mapping to flip between them in a hurry.
- With the DaVinci Advanced control panel, the A, B, C, and D buttons on the jog/ shuttle panel let you jump to whichever playhead you wish to drive.

To eliminate all additional playheads from the Mini-Timeline:

- Choose Color > Active Playheads > Reset Playheads.

### Show Current Clip With Handles

When your project sits inside a round-trip workflow and you're aware you'll render handles per clip, briefly revealing those handles for the clip you're grading can help, since it lets you readily lay tracking or keyframing effects across each clip's full frame span. To toggle clip handles on or off within the Color page's Mini-Timeline:

- Choose View > Show Current Clip With Handles.

(Left) The Mini-Timeline's current clip, (Right) That very clip displayed once Show Current Clip With Handles is switched on As long as this mode stays on, Unmix is forced on and can't be switched off, so that you can clearly see each clip's overlapping handles. How long the revealed handles run is governed by the Default Handles Length parameter found in the Editing panel of the User Preferences. You can reveal or conceal Clip Handles whenever you like.
