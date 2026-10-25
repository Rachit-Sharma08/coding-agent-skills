# Text and color

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](general-settings-overview.md) / [Next section](general-settings-and-automation.md)
<a id="source-color"></a> <a id="source-fairlight"></a> <a id="source-general-settings"></a> <a id="source-printer-light-step-calibration"></a> <a id="source-ripple-mode"></a> <a id="source-text"></a> <a id="source-video-io-offset"></a>

### Text

Tick the Display Only Specific Fonts box to deliberately pare down the font choices offered for your text elements. That builds a white list of fonts you’re approved to use and tucks every other system font out of sight. To assemble an allowed fonts list: 1 Tick the box at Preferences > User > Editing > Text > Display Only Specific Fonts. 2 Pick a font filter file. Such a file is any UTF-8 text document that blends explicit font names with entries using asterisk wildcards to catch several fonts, listed one per line. _Gothic_ (matches any font name containing Gothic) Arial Helvetica\* (matches any font name that starts with Helvetica) Open Sans Default Fades The curves of Fairlight’s default audio fades are laid out by these settings.

- Fade In/Out: Lay out the curve type used for fade ins and outs.
- Crossfades: Lay out the curve type used for the ins and outs of the crossfade.

Checkboxes for None, Equal Power, and Equal Gain for crossfade type.

### Color

This panel’s settings steer various behaviors over on the Color page.

### General Settings

Shape an assortment of behaviors as you work on the Color page.

- Master reset maintains RGB balance: Sets how the DaVinci control panel’s trackball/ring reset buttons clear primary color adjustments. With this option off (its default), a press of the ALL Reset button brings the primary correction values back to their defaults. Switch the checkbox on and a press of the ALL Reset button (a) clears the YRGB values such that the overall levels stay put and the YRGB-to-each-other ratio holds, while (b) a press of the RGB Reset button drops the three color channels to the average of their former settings.
- Wipe wraps when viewing reference stills: Switching this on (its default) lets stills carry over the screen edge as you drag the wipe with the mouse, instead of halting at that edge. Should the behavior feel clumsy when you’re trying to whip up full-frame still comparisons to toggle on and off, you can turn it off.
- High-Visibility Power Window Outlines: Switching this on draws Power Window outlines in green (the center shape) and yellow (the softness shapes) so the windows read more easily in certain situations, in place of the default white and gray.
- Mattes display high contrast black and white: When this is on, the HILITE command — which shows the current key — renders a black and white matte (that is, high contrast) rather than the usual gray one.

For more on this setting and on working with the HILITE command, see Chapter 135, “ColorSlice.”

- Next scene switches to visible track: While grading a multi-track project, this option reshapes the “next scene” command so it behaves better where multi-clip composites are involved. With it off, pressing NEXT SCENE on the DaVinci control panel, or hitting the Down Arrow shortcut, carries the playhead to the very next clip in the Thumbnail timeline whether that clip sits ahead of or behind another. Switch it on and the NEXT SCENE command instead lands the playhead on the clip in the topmost track whenever the next clip belongs to a multi-clip composite of clips piled over one another.
- Previous or Next node navigates only to correctors: Node navigation picks out corrector nodes alone, stepping past mixer, splitter, combiner nodes, and the like.
- Preserve node numbers when adding nodes: Tick this box and node numbering rises in the order nodes were made, no matter where each sits in the node tree. Leave it unticked and the numbering reflows on its own according to each node’s spot in the tree.
- Always perform copy and paste on selected nodes: Sidesteps the interface focus-driven choice between copying and pasting full grades versus single nodes. When ticked, DaVinci Resolve copies and pastes only among selected nodes, whatever the interface focus happens to be.
- Use Legacy Auto Color: Since DaVinci Resolve 16, two tools — the Color Wheels palette’s A button together with the Shot Match command found in the Thumbnail Timeline contextual menu — both lean on advanced algorithms built on the DaVinci Neural Engine, yielding better outcomes when color balance and contrast are adjusted automatically. This checkbox points the A button back at the older algorithm.
- Use Legacy Shot Match: Beginning with DaVinci Resolve 16, the Shot Match command in the Thumbnail Timeline contextual menu draws on an advanced algorithm built on the DaVinci Neural Engine, yielding better outcomes when color balance and contrast are adjusted automatically. This checkbox points the Shot Match command back at the older algorithm.
- Histogram Background on Grading Tools: Through this drop-down menu you set the histogram shown behind the Curves palette to Off, to On based on the node’s Input (where curve edits leave the background histogram untouched), or to On based on the node’s Output (where curve edits do reshape the background histogram).
- Automatically cue x frames into timeline clips: This setting bears on how the Color page’s NEXT SCENE and PREV SCENE commands behave. By default, moving from one clip to the next cues on each clip’s first frame. Type a value here, in frames, and the default cue point shifts to that many frames past the first frame of every clip the playhead lands on. It comes in handy when the source carries black or camera rollup flashes at the head of each clip while you grade dailies.
- Neighboring Clips in Split Screen: Lets you set how many clips adjacent to the current ones appear in a grid within the Color page Viewer once you switch on the Neighbor Clips option of the Split-Screen shot comparison control.
- Switching clips: (this setting is also changeable from the Node Editor’s Option menu) On switching clips, DaVinci Resolve can move to the same node or a different one in the node graph. The four options below decide which node ends up selected:

Selects last adjusted node: The default, under which every Timeline clip keeps its own separate node selection that’s recalled each time you return to that clip. Selects first node: The first node is always chosen as you move to a different clip. Selects last node: The last node is always chosen as you move to a different clip. Selects same node: Should the clip you’ve jumped to hold as many nodes as the previous clip or more, the node bearing the matching number is chosen. Should it hold fewer nodes than the previous clip, the next highest node is chosen.

- Color picker: Alters how colors get chosen while you use the Secondary color correction controls. DaVinci Resolve is the standard, current mode, though some colorists at home with the legacy 2K lean toward the DaVinci 2K mode.

### Ripple Mode

This setting fixes how the Ripple command launched from the Color page behaves.

- Target clips are set to: The Ripple mode applied when you trigger a Ripple command on the Color page, whether through the RIPPLE button on the Advanced Panel or by choosing it from the Color menu.

For more on putting this function to use, see Chapter 142, “Grade Management.” Exact values changed: Edits to the current clip ripple out to the named clips using the very parameters you altered. Say the current clip’s Master Gain level is moved to 0.75 of its range — then every clip you ripple ends up with a Master Gain level of 0.75. Only the parameters you touch ripple. Percent value changed: Edits to the current clip ripple out to the named clips by the percentage shift you applied to the altered parameters. If, for instance, the current clip’s Master Gain level sits at 1.00 and you drop it to 0.90 units, the Master Gain level of each rippled clip falls 10% relative to its earlier value. Unit values changed: Edits to the current clip ripple out to the named clips by the same change delta, in whatever units suit the affected parameter. For example, if the current clip’s Master Gain ran 0.80 and you raised it to 0.90, each rippled scene’s Master Gain level climbs by 0.10. All values are copied: The current clip’s grade ripples to the named clips in full. No check is made against the original clip’s parameters, and every memory parameter ripples.

### Printer Light Step Calibration

On film projects where you’re closely tied to a film lab, the printer light calibration sets can be tuned to suit the lab you work with. Partner with your lab technician to dial in the Lab Aim settings, the Steps adjustments — an incremental value — and the Density Increment adjustment, which is how much correction each step applies. The Step and Density values usually match, but that rests with your lab and what you prefer.

### Fairlight

### Video I/O Offset

This section’s two preferences let you push overall video playback as much as 7 frames ahead of your audio playback, covering cases where image processing on your video output introduces delays that knock the video out of step with the audio. Picture your video output passing through a converter that tacks on a 1 frame delay and then reaching a projector that adds another 1 frame. Setting your Video Monitor Offset to 2 frames cancels that out and keeps audio/video sync rock solid.

- Video Monitor Offset: From this drop-down menu, pick an offset anywhere from 0 to 7 frames.
- Apply Offset during Jog and Shuttle: Switch this checkbox on and the offset you

picked applies as well when you use Jog and Shuttle to travel through your program.
