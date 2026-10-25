# Introduction to the primaries palette and HDR grading with the primaries palette

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primaries palette.
[Chapter index](INDEX.md) / [Next section](top-adjustment-controls-and-bottom-adjustment-controls.md)
<a id="source-color-balance-controls"></a> <a id="source-hdr-grading-with-the-primaries-palette"></a> <a id="source-introduction-to-the-primaries-palette"></a> <a id="source-master-wheels"></a> <a id="source-numeric-parameters"></a> <a id="source-primaries-color-bars"></a> <a id="source-primaries-log-wheels"></a> <a id="source-primaries-log-wheels-1"></a> <a id="source-primaries-palette"></a> <a id="source-primaries-palette-part-1"></a> <a id="source-shared-adjustment-controls"></a> <a id="source-shared-controls-in-the-primaries-palette"></a> <a id="source-switching-between-primaries-tools"></a> <a id="source-which-do-i-start-with-the-primaries-or-hdr-palette"></a>

### Primaries Palette

This chapter centers on the fundamental color work behind “primary” corrections — the adjustments that shift an image’s overall color and contrast. It draws on the Lift/Gamma/Gain controls (found within the Wheels and Bars modes of the Primaries palette) together with Log mode’s Shadow/Midtone/Highlight/Offset controls, two control sets that have long been the bedrock of most grades.

### Introduction to the Primaries Palette

If you’ve ever touched color correction tools in any program, the Lift/Gamma/Gain controls inside the Primaries palette’s Wheels mode will feel familiar. They embody the most traditional, fundamental color correction available in DaVinci Resolve, built so that users without control panels can still reach color balance and YRGB contrast manipulation with a mouse, tablet, or trackpad.

Color Balance controls for primary grading, in Wheels mode True to its name, the Primaries palette is built for those broad “primary” color tweaks to the image that usually form the basis of any grade. By contrast, “Secondary” adjustments are the more targeted changes made to isolated subjects in the frame. It is a long-proven habit, though, to wring everything you can out of the overall image with one or more primary corrections before turning to more detailed work layered on top of those first moves. For one thing, it’s a tidier, more orderly way to operate. It is also the most efficient route to handling the image holistically — maximizing the gains while putting the least strain on the video signal. The Primaries palette runs in three separate modes:

- Wheels mode holds the classic DaVinci YRGB Lift/Gamma/Gain controls, whose adjustment regions are tonally specific yet broadly overlapping. It additionally exposes the RGB Offset/Printer Points color balance and master controls.
- Bars mode reaches the very YRGB Lift/Gamma/Gain and Offset controls that Primaries Wheels mode offers, yet its interface has you make vertical slider-driven moves on individual YRGB lift, YRGB gamma, and YRGB gain channels, and gives a slider-and-button interface for the RGB Offset/Printer Points controls.
- Log mode is where the RGB Offset/Printer Points color balance and master controls live, shaping the whole signal in a linear, film-style fashion. It supplies Shadow/Midtone/Highlight/Offset controls offering tighter yet adjustable regions of adjustment meant for working on log-encoded image data.

Which mode you reach for comes down entirely to how you like to work and the kind of adjustments you have to make.

### HDR Grading With the Primaries Palette

As of DaVinci Resolve 17, several of the Color page palettes used for color adjustment became “color space aware.” That means a palette behaves largely the same whatever Timeline Color Space you’re in, and whether you’re grading toward SDR or HDR output. Not every color palette gained this awareness, though, so when you push various Color page grading controls on wide-latitude images for HDR output and find them behaving roughly, it can help to switch on the HDR Mode of the node you’re on — right-click that node in the Node Editor and pick HDR Mode from the contextual menu (offered only in Resolve Studio). The setting forces that node’s controls to operate inside an expanded HDR range. In practice, that eases work on wide-latitude signals with controls that let you adjust separate tonal ranges, such as Lift/Gamma/Gain or the Log controls.

### Which Do I Start With, the Primaries or HDR Palette?

The HDR palette, which arrived in DaVinci Resolve 17, was likewise built to serve as a strong way to make the primary adjustments your grade is founded on. Although the HDR palette’s Global and Zones controls come from a different philosophy of signal adjustment, they aim to tackle the same problems, so beginning with the HDR palette rather than the Primaries palette is an entirely legitimate choice. So which should you use? In the end it hinges on how comfortable you are with the HDR palette and how experienced you are with the Primaries palette. If your muscle memory for the Primaries palette still makes it the quickest way to dial in adjustments, there’s no need to abandon it now. The Offset/Printer Points controls in the HDR palette, in fact, remain adjustments quite distinct from the rest of the HDR palette’s functionality. Even so, give the HDR palette a go, because it has powerful primary grading abilities the Primaries palette modes can’t match. Even if it’s unfamiliar, stick with it a week and you’ll uncover countless advantages to the HDR palette’s approach, though it asks for some fresh ways of thinking about the process. The bottom line, though, is that you’ll likely keep using both palettes. If you do, bear in mind that inside every Corrector node’s sequence of image-processing steps, the HDR palette controls are handled ahead of those in the Primaries palette — mostly because the HDR palette’s more “photographic” grading approach was purpose-built for primary color work in today’s landscape of wide-gamut HDR mastering and delivery, and so was placed into the processing pipeline as the new base under all adjustments.

### Shared Controls in the Primaries Palette

This section sets out, in general terms, how to use the common control-interface conventions shared by the Wheels, Bars, and Log modes when making adjustments. It also describes how to use the parameters common to all three modes.

### Switching Between Primaries Tools

The icons at the top right of the Primaries palette let you jump between the Primaries tools with a single click.

### Primaries: Log Wheels

### Primaries: Color Bars

### Primaries: Log Wheels

### Color Balance Controls

Whether you’re working in the Wheels or Log controls, the Color Balance controls let you shift all three color channels of a given tonal range of the image at once with a single move of the pointer, depending on the active mode. A range of keyboard modifiers also lets you make specific adjustments through the GUI. These controls likewise map to the trackballs on any DaVinci or third-party control panel you might have hooked up. Methods of making adjustments using the Color Balance controls:

- Click and drag anywhere within the color ring: Shifts the Color Balance indicator relative to where it was, rebalancing the three color channels across whichever tonal range that control governs. There’s no need to grab the Color Balance indicator itself. This mimics the relative control you get steering these parameters with a trackball. As the Color Balance indicator moves, the RGB parameters beneath it change independently to mirror the separate adjustment being made to each channel.
- Shift-click and drag within the color ring: Snaps the Color Balance indicator straight to the pointer’s absolute position, letting you push faster, more extreme moves to the color balance that control governs.
- Double-click within the color ring: Clears the color adjustment while leaving that control’s matching contrast adjustment in place.
- Command-click and drag within the color ring: Moves YRGB contrast just as if you were dragging that control’s master ring.
- Click the reset control at the upper-right of a color ring: Clears both the Color Balance control and the master ring that goes with it.

### Master Wheels

Sitting below the Color Balance controls, the Master Wheels let you move the YRGB channels for a given tonal range of the image together. The practical upshot is that you can adjust the image’s lightness and contrast.

Lift, Gamma, Gain — or Shadow, Midtone, Highlight — together with the Offset master wheels, all serving to adjust contrast Each Master Wheel maps to a ring around the trackballs on every DaVinci control panel, which alter image contrast through YRGB adjustment (not through Y-only adjustment, which comes up later in this chapter). To work a Master Wheel: drag it leftward and the matching tonal region of the image darkens; drag it rightward and that region lightens. The exact effect depends on the mode you’re in. As you adjust, the YRGB parameters underneath all move together to reflect the simultaneous change you’re making across every channel.

### Numeric Parameters

Each Color Balance Control and Master Wheel pair also carries a set of four YRGB number fields beneath them that display the YRGB adjustment both controls are making. These four values cover every color and master adjustment these controls can produce, and they map directly onto the Bars interface that mirrors the Wheels controls. Editing these fields works the same as editing any other Color page parameter. Even though space constraints in the interface show only two decimal places, each field really keeps three, because these are floating point operations — the third one is simply hidden from view. To edit YRGB values directly:

- You can double-click a field to type its value in numerically.
- You can place the text cursor beside a value in the field and tap the Up and Down Arrow keys to step the value one digit at a time.
- You can cut, copy, and paste values between fields.
- You can click a field and drag it left or right to set its value with a virtual slider.

Every Color Balance Control and Master Wheel offers editable number fields.

### Shared Adjustment Controls

All three Primaries palette modes additionally share two strips of controls for finer work on assorted aspects of the image — Contrast, Saturation, Hue, Highlight retrieval, Color boost, and the like. Much like most DaVinci Resolve parameters, dragging a parameter’s name or value sideways raises or lowers it with a virtual slider, double-clicking its number opens numeric editing, and double-clicking its name returns the parameter to its default.
