# Introduction to the HDR palette and controls panel of the HDR palette

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR palette.
[Chapter index](INDEX.md) / [Next section](zone-bank-controls-and-making-global-adjustments.md)
<a id="source-color-space-aware-controls-when-using-color-management"></a> <a id="source-customizable-zones"></a> <a id="source-hdr-palette"></a> <a id="source-hdr-palette-part-1"></a> <a id="source-introduction-to-the-hdr-palette"></a> <a id="source-navigating-multiple-zones-in-the-controls-panel"></a> <a id="source-perceptually-uniform-adjustments"></a> <a id="source-superior-temp-and-tint-controls"></a> <a id="source-the-controls-panel-of-the-hdr-palette"></a> <a id="source-the-hdr-palette"></a> <a id="source-the-hdr-palette-interface"></a> <a id="source-using-the-hdr-palette-without-color-management"></a> <a id="source-what-makes-the-hdr-palette-special"></a>

### HDR Palette

The subject here is the overall and zone-driven tweaks available through the HDR palette, DaVinci’s most recent primary grading tool. Its name notwithstanding, you can rely on this palette — much as you would the Lift/Gamma/Gain mode of the Primaries palette — to build the base adjustment underneath any grade, whether SDR or HDR. That said, because it operates by zones, it carries the reach and precision associated with curve-based work, which leaves the HDR palette well-suited to a wide range of both creative and corrective jobs. On top of that, the palette’s awareness of color space, combined with the perceptually uniform space where its adjustments take place, positions it especially well for governing the saturation and highlights of images mastered in HDR.

### Introduction to the HDR Palette

Purpose-built for quick, adaptable primary grading of wide-latitude footage bound for either SDR or HDR delivery, the HDR palette is what it is. Being “color space aware” means it cooperates with Resolve Color Management, mapping the source image data into the palette’s own perceptually uniform operational color space according to that known transform. Sophisticated color processing under the hood then yields more economical color and contrast moves, plus perceptually uniform controls that let you treat every color across the spectrum evenly while keeping a tight grip on the image’s saturation.

### The HDR palette

On the right side of the palette sits a group of global controls for base adjustments to the whole image, joined at the bottom by Hue, Midtone Detail, Contrast/Pivot, and Black Offset controls. Beyond that, an overlapping bank of zone-specific controls handles color and contrast tweaks aimed at particular bands of image tonality. Taken together, the HDR palette supports primary grading work that stays photographically natural while reaching as broadly or as narrowly across the tonal range as you want, all with few unwanted artifacts. For all its depth, the palette relies on color balance and slider controls any colorist or editor who knows the more traditional Lift/Gamma/Gain controls will recognize. Seasoned grader or color newcomer alike, you’ll get strong results with less effort from the HDR palette once you’ve learned to wield it.

### The controls panel of the HDR palette

TIP: As HDR-capable media and HDR streaming delivery pipelines keep spreading, both the node HDR mode and the HDR palette ship with no restrictions in the free downloadable build of DaVinci Resolve.

### What Makes the HDR Palette Special?

Ahead of working through the specifics of the palette’s controls, it pays to grasp a little more about the way the HDR palette handles image data, since that context clarifies the benefits this tool brings to the table.

### Using the HDR Palette Without Color Management

Although the HDR palette was built to operate alongside color management, nothing stops you from using it in workflows that aren’t color managed, provided you configure it properly. Inside the HDR palette option menu you’ll find Color Space and Gamma submenus where you declare how you intend to work. Out of the box, each submenu defaults to “Timeline,” mirroring the color space you’ve elected to work in for display-referred workflows.

### Color Space Aware Controls When Using Color Management

Where the HDR palette truly excels is with Resolve Color Management or ACES turned on, since as a color space aware palette it exploits color management for all it’s worth. What color space awareness amounts to is this: the palette’s color and contrast controls adapt themselves to the span of each clip’s image data, mapped from the Input Color Space assigned to the source clip over to the Timeline Color Space in which your program lives. In day-to-day terms, that yields two advantages:

- Regardless of which kind of source clip you’re tweaking, and regardless of the timeline color space you’ve picked to work in, the HDR palette’s controls behave and feel essentially the same.
- Tweaks you apply through the HDR palette on one media type carry over to other media types with comparable results when copied. As a consequence, lining up shots and porting looks across media types becomes simpler than it was with earlier tools.

NOTE: Since the HDR palette is color space aware, you don’t have to switch on the HDR setting on nodes for the controls to behave intuitively when you’re working in a wide gamut Timeline Color Space, or outputting to an HDR format such as ST.2084. The palette handles all of that on your behalf, automatically.

### Perceptually Uniform Adjustments

On top of that, every clip’s image data gets translated out of the Timeline Color Space into an operational color space that the HDR palette employs; the image is adjusted there, then translated back into the Timeline Color Space, set for whatever operation comes next. That operational color space the HDR palette draws on is perceptually uniform, so the band of values tied to each visible hue spreads itself evenly across the whole space. The HDR palette grades standard dynamic range (SDR) material perfectly well, yet the color science beneath it also tackles problems that have long vexed colorists grading high dynamic range programs with conventional controls. Among those benefits:

- Because this palette computes all of its color transformations inside a perceptually uniform color space, your color adjustments gain finer, more photographically intuitive control. You might notice, for instance, that yellow hues grade more readily here, owing to a more balanced spread of hues around the rim of the color wheels.
- With the HDR palette you can change contrast and leave image saturation untouched; in contrast to the master wheels on the Lift, Gamma, and Gain panel, the HDR palette lets you push contrast up without driving saturation up, and pull contrast down without pulling saturation down. This proves especially handy when you’re lifting highlights

within HDR grades, because you can do it now without triggering runaway saturation in those highlights. In truth, any contrast move you make with these controls reshapes the image while holding saturation rock-steady (perceptually, that is; the Vectorscope will indeed reveal slight saturation shifts). Naturally, the saturation controls are the exception to this.

- Thanks to how tightly the HDR palette is woven into Resolve Color Management, matching shots and porting looks from one media type to another is also easier than with earlier tools. Pro or color beginner, you’ll see better outcomes with less hassle from the HDR palette.

### Superior Temp and Tint Controls

Owing to the HDR palette’s color space awareness, the Temperature and Tint moves in it rely on the very same XYZ to LMS color space transform that drives the Chromatic Adaptation Resolve FX plugin. What follows is that Temp adjustments come out photometrically accurate, producing visuals that resemble how human vision registers a scene shifting as the color temperature of the lighting changes.

### Customizable Zones

A further distinctive trait of the HDR palette is the degree to which you can tailor it to a broad spread of working styles, particular jobs, and individual colorist tastes. Flipping over to the Zones panel exposes an interface for tuning the Range and Falloff of every zone you’ve defined, via graphical controls laid over a histogram of the present image, while a curve illustrates to you how the contrast and color moves you’ve made mathematically influence the image’s RGB channels inside each zone. The default zones preset gives an efficient launching point for many scene types, yet because the tonal range of image data differs from scene to scene — daytime, nighttime, interior, or exterior — you’ll frequently need to customize these zones to wring the best out of adjustments made with these controls.

Through the Zones panel you can tailor the tonal ranges that each group of zone controls governs. On top of that, the sidebar to the left supplies controls for adding and deleting zones, letting users mold the palette to behave precisely as they prefer. You can save any custom preset for quick recall later. In this fashion, users get the latitude to work however suits them best. Meanwhile, the Option menu offers rapid access to other ways of customizing the palette’s behavior — picking and managing presets, choosing among methods for editing Color Balance adjustments numerically, and a setting that decides whether the Global controls stay permanently exposed or get banked to alongside the other zone controls.

### The HDR Palette Interface

Two panels make up the HDR palette. The first holds Color Balance controls and custom sliders and exists for color and contrast moves. The second holds the Zones sidebar and Zones graph and exists for tailoring the range and falloff of each zone tied to a given group of controls over on the controls panel. Those zones are precisely what you use to apply detailed image adjustments to tonally-specific regions of the picture. By default the two panels share the same palette area, and a pair of buttons at the upper right of the palette toggles between them. That comes in handy when screen space is tight, or your adjustments are straightforward. Otherwise, a single button click reveals both panels side-by-side, filling the left and middle palette areas of the Color page at once.

Going across from the left: the Side-by-side view button, then the Controls panel, the Zones panel, the Reset control, plus the Option menu. This Side-by-side mode makes it straightforward to view and tailor how each zone maps onto the source image data while you adjust simultaneously.

The HDR palette in Side-by-side mode; on the left, the Color/Exposure/ Saturation controls; on the right, the Zone Customization controls. An Option menu sitting at the far right of the title bar (rendered as three dots) brings up this palette’s preset manager, plus assorted GUI options for tailoring how you’d like to work with the palette.

### Navigating Multiple Zones in the Controls Panel

A strip of buttons directly beneath the HDR palette’s title bar indicates, out of all the zones on offer, which ones you can currently adjust with the controls visible below. The default HDR palette preset carries six zone-specific Zone controls along with the Global controls, but most users will find the GUI has room for only four sets of controls on screen at any moment. Grading control panel users, for their part, will be limited by however many trackballs their specific control panel offers.
