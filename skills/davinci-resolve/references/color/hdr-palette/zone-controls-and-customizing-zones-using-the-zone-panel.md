# Zone controls and customizing zones using the zone panel

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR palette.
[Chapter index](INDEX.md) / [Previous section](ansel-adams-zones-and-color-adjustments.md) / [Next section](resetting-color-and-zone-adjustments.md)
<a id="source-customizing-zones-using-the-zone-panel"></a> <a id="source-the-create-zone-dialog"></a> <a id="source-the-zone-graph"></a> <a id="source-the-zone-panel-of-the-hdr-palette"></a> <a id="source-the-zone-sidebar"></a> <a id="source-zone-controls"></a> <a id="source-zone-controls-1"></a> <a id="source-zones-graph"></a>

### Zone Controls

Every single zone additionally carries Color Balance and Saturation controls, letting you make pinpoint changes confined to particular bands of image tonality with no qualifier needed. Working all these zones in concert, you can apply quick, precise, smooth changes to the image that come across as remarkably natural. The palette's name notwithstanding, this supports careful work on SDR images as readily as creative shaping of the dramatic highlight range that HDR opens up. Flanking each control cluster on the left and right are Range and Falloff controls that let you redraw each zone's area of influence even while the Zone graph stays hidden.

The Shadow and Light zone controls sitting side by side; the Min and Max indicators are visible, as is the Range value (in stops) up at the top left of each control group.

- Range indicator: Up in the top-right corner of each zone control cluster, an icon and a value report that zone's range. The numeric value is the range value — the Luminance level of image tonality where that zone's adjustment kicks in. It is given in stops, and the icon tells you whether this is a maximum range (working the shadows) or a minimum range (working the highlights).

Click the icon to pop a brief preview into the Viewer of which image areas that zone's controls will touch. The affected areas show up in full color while everything else turns black.

- Zone-specific Color Balance: A color balance control lets you rebalance the comparative strength of the red, green, and blue channels inside the current band of image tonality.
- Zone-specific Exposure: These controls operate alongside a movable pivot that fixes the Luminance level from which each exposure change departs. So both shadow and highlight work are covered, there are two pivot varieties, labeled Maximum and Minimum range and flagged by an icon. Max Range controls — the Shadow control among them — begin at a maximum value, their exposure changes pulling image contrast downward toward the shadows. Min Range controls, Light being one, begin at a minimum value, their exposure changes pulling contrast upward toward the highlights. Every zone additionally has a falloff dictating how far that zone laps over its neighbors (measured from the pivot level) so overlapping changes blend gently enough to keep contouring at bay.
- Zone-specific Saturation: Tunes how intense the color is within the current band of image tonality.
- Min/Max Range: Sets the level of image tonality where that zone's adjustment begins. It is given in stops. The same as the Min or Max Range slider over in the Zone panel. Handy for nudging Range while the Zones graph is out of view.
- Zone Falloff: Sets how gently this zone melts into every overlapping zone. The same as the Falloff slider over in the Zone panel, with its value shown in the virtual slider beneath. Handy for nudging Falloff while the Zones graph is out of view.
- Zone-specific Color Balance Values: A pair of values puts the current color balance operation into numbers. Via the option menu you can have these shown either as X and Y or as Angle and Strength.

### Customizing Zones Using the Zone Panel

Much as with the Log palette's controls, the way these zones overlap is adjustable, letting you tune each zone's controls to suit the tonal spread of whatever scene you are on. That overlap is steered by separate Range and Falloff control pairs, so precise adjustment is possible regardless of how tonality is distributed in the image you are grading. You organize and customize all the zones through the Zone panel, which splits into the Zones sidebar on the left and the Zone graph on the right.

### The Zone panel of the HDR palette

### The Zone Sidebar

The Zone sidebar presents a list of every zone in the current preset. The list is ordered by range value, putting minimum range zones (working the shadows) up top and maximum range zones (working the highlights) further down. Clicking any entry in the list selects that zone and at the same time picks out its boundary handle over in the Zone graph on the right. The Zone sidebar offers these controls:

- Enable Zone toggle: These toggles flip each zone on or off. A disabled zone is left out of the render.
- Max/Min button: Decides whether a given zone's adjustment works the image from its current range value on down (Max) or from its current range value on up (Min). You normally set this while building a custom preset, to declare which zones reach down toward the shadows and which reach up toward the highlights.
- Show/Hide Zone button: This button tucks away sets of zone controls you have no further interest in adjusting, which frees room within the UI, and on your control surface, for whichever zones still matter to you. Say you decide the default Black and Specular zones are unnecessary; hide them and only the Dark, Shadow, Light, and Highlight zones remain to switch between. Any zone controls that already carry adjustments keep affecting the image even once hidden.
- Delete Zone button: Removes that zone. This mostly comes up while you are crafting your own zone preset. As of this writing, none of the default zones in the default Zone preset can be deleted. On top of that, you can add zones and save zone presets to invent your own custom approaches to adjusting the image.

To create a new zone: 1 Open the Zones panel. 2 Hit Create Zone at the foot of the Zones sidebar. 3 Once the Create Zone dialog opens, pick the Zone type you want for it (Dark/Min Zone or Light/Max Zone), type in a Name, and set the Range and Falloff values. Range, Falloff, and Zone type all stay editable afterward, so there is no harm in not nailing them on the first pass. 4 Hit Create. The zone shows up appended to the list, which orders itself by how Range is defined — Dark Zones up top, Light Zones at the bottom.

### The Create Zone dialog

### Zones Graph

The Zone graph is central to how you work the HDR palette. Across the bottom runs a stops scale marking the range the HDR palette covers. Up top sit handles for adjusting the editable range boundaries that delimit each zone's tonal range, all laid over a histogram of the current image as it feeds into the current node. Down the middle of the Zone graph runs a curve depicting every Global and Tonal color and contrast change the HDR palette is applying in the current grade. How those range boundaries line up against the source image histogram in this graph matters enormously. A given zone's range boundary has to cross the slice of the source histogram you mean to adjust before that zone's controls do anything at all. Should any zone boundary sit beyond the histogram, that zone's controls accomplish nothing. In the screenshot above, every one of the zone's range boundaries falls inside the visible histogram, so each zone's controls deliver a predictable adjustment to the image data in that stretch of the histogram.

### The Zone graph

In the screenshot below, the Zone graph reveals that the Specular zone boundary sits beyond the image's source histogram, so anything you do with the Specular controls produces no effect. That is why it pays to confirm the zone boundaries cross the image areas you intend to adjust before you start moving controls; and if you spot a particular zone's controls doing less to the image than you would like, you can always shift the zone boundary afterward to widen the image range that zone reaches.

. With the Specular zone boundary sitting beyond the source histogram, the Specular controls are shut out from touching the image. Tailoring zone boundaries like this ranks among the HDR palette's most potent capabilities, yet do not fear you will be forever dragging boundaries to and fro on every shot. As a rule, most well-shot scenes carry comparable tonal ranges from shot to shot, so boundaries you have customized for one shot in a scene will probably serve most of that scene's clips well. Even so, reworking zone boundaries is yet another strong way to tune a grade specifically for a clip whose contrast range is unusual.

### Zone Controls

- (Min/Max) Range: Sets the level of image tonality where that zone's adjustment begins. The value is given in stops.
- Falloff: Governs how gently that zone's adjustment merges into the image. At a value of 0 the change in the current zone arrives instantly, making the color adjustment a sharper effect. Larger values ease the current zone's adjustment into the image more softly, for a gentler, more seamless transition into the effect.
- Customizing and Saving Presets

When you have shaped the Zone graph in a way that might serve other grading situations too, you can store the Zone settings as a preset to reuse later. Saving, recalling, and managing those presets is straightforward. Ways to manage presets:

- To save a preset: Shape the Zone graph however you need, then pick Save As New Preset from the HDR palette Option menu.
- To load a preset: From the HDR palette Option menu, follow Presets > Name of Preset > Load Preset. Doing so saves a fresh preset.
- To update a preset: Load a preset, apply whatever Zone graph changes you need, then pick Presets > Name of Preset > Update Preset from the HDR palette Option menu.
- To delete a preset: Pick Presets > Name of Preset > Delete Preset from the HDR palette Option menu.
- To select the default preset: Pick Default Preset > Name of Preset from the HDR palette Option menu. That preset becomes the one the HDR palette loads at startup from then on.
