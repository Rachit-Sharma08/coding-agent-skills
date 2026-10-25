# Light source status indicators and image stabilization controls in the media page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Capturing from the cintel film scanner.
[Chapter index](INDEX.md) / [Previous section](controlling-the-cintel-film-scanner-and-cintel-scanner.md) / [Next section](editing-capture-info-metadata-and-film-scanning-workflows.md)
<a id="source-audio-and-synchronization"></a> <a id="source-film-protection"></a> <a id="source-image-stabilization-controls-in-the-media-page"></a> <a id="source-light-source-status-indicators"></a>

### Light Source Status Indicators

These indicators beneath the ‘auto’ button let you know whether the auto black or auto white light source calibration came off successfully or whether there are things to deal with. They also serve as a handy nudge to recalibrate the LED light source so your scans stay at the highest quality.

Light source calibration has not yet been performed.

Light source calibration has performed successfully.

Light source calibration failed. Double-check that the right film type is chosen, that nothing blocks the light path, and that a fitting reference frame is picked. Should it be needed, try winding the film forward and choosing a different reference frame.

Light source calibration balanced the colours fine, yet not at the levels you wanted. To work around this, either accept the balanced scan and refine the image over on DaVinci Resolve’s color page, or pick a different reference frame — one with a broader dynamic range — for calibration.

- RGB controls: By default, a color balance control lets you shift all three color channels by differing amounts to change the color temperature of the light source that illuminates the film, while the adjusted R, G, and B values show in three fields beneath. If you like, you can flip this control into ‘color bars’ mode using the mode pop-up that sits just right of the ‘light source’ title bar; doing so turns the control into three vertical red, green, and blue color channel sliders.Image Stabilization

NOTE: The light source calibration is held when you swap rolls. That means one light source calibration can cover several rolls across both SDR and HDR modes alike. Whatever the most recent light source calibration was, it stays held until a fresh calibration runs, or until your Cintel scanner is power cycled. These controls let you switch image stabilization on and off as well as steer it to wipe out vertical film hop and horizontal weave

### Image Stabilization controls in the Media page

- Image Stabilization enable/disable control: Sitting just left of the ‘image stabilization’ title bar, a dot lets you switch your scanner’s hardware-based image stabilization on or off entirely. Hardware stabilization is usually what you want when your perforations are high quality, yet you might switch this option off when the perforations are in poor shape and you opt for DaVinci’s software based stabilization instead. With image stabilization switched on, a horizontal X axis detection overlay shows in the viewer, marking the edge of the film perforation that will serve as the reference for stabilization. This overlay hides itself automatically during recording. Image stabilization is switched on by default.
- Enable X and Y checkboxes: Enable X and enable Y let you decide whether hardware image stabilization should fix horizontal gate weave and vertical gate hop respectively. Should the results fall short with both axes switched on, you can switch off whichever axis is causing the stabilization trouble and reach for DaVinci Resolve’s software-based stabilization tools instead.
- Horizontal Position slider: Your Cintel scanner tries on its own to drop the stabilization detection overlay in the best spot, going by the perforation shown on the frame currently loaded, for the best stabilization result.

You’ll spot a thin transparent line within the blue alignment overlay. For the best stabilization, that line should sit right on the edge of the perforation. When the automatic positioning falls short, you can shift the overlay to a better spot by hand — drag it across the viewer with your mouse, or work the horizontal slider. The best placement of the stabilization overlay puts the clear line in the alignment overlay on the perforation’s edge, as the example image shows. With the overlay placed correctly, this switches on hardware stabilization of gate weave along the X axis. Image stabilization takes care of vertical gate hop on its own once you tick the ‘enable y’ checkbox. No further tweaking is needed, and it works hand in hand with horizontal stabilization.

Incorrect 35mm setup. Here the stabilization overlay’s horizontal position is being adjusted; it has not yet settled onto the perforation’s edge.

Correct 35mm setup. In the viewer, the hardware stabilization control rests squarely over a perforation, its transparent stripe meeting that perforation’s edge.

Incorrect 16mm perf setup. The overlay has missed the perforation’s edge. Fit the 16mm HDR skid plate and the stabilizer snaps to the perforation’s far side on its own, steering clear of the film image and tightening horizontal stability. A ‘non-HDR’ 16mm skid plate behaves just like the 35mm one.

Correct 16mm perf setup. Because the perforation’s left edge stays free of image content, that edge is where the overlay defaults to; its transparent stripe lands on the perforation’s edge as it should.

Incorrect 16mm film edge setup. Here the overlay has not landed on the film reference edge.

Correct 16mm film edge setup. Here the overlay sits on the film reference edge, its transparent band meeting the film ref edge cleanly.

Incorrect 8mm setup. Here the overlay has not landed on the film’s edge.

Correct 8mm setup. Within the film base area, the overlay’s transparent stripe is correctly contained.

Incorrect 8mm perf setup. Here the overlay has missed the perforation’s edge.

Correct 8mm perf setup. Because the perforation’s left edge stays free of image content, that edge is the overlay’s default position; its transparent stripe lands on the perforation’s edge as it should.

Incorrect 8mm film edge setup. Here the overlay has not landed on the film reference edge; it sits off the film reference edge.

Correct 8mm film edge setup. Here the overlay sits on the film reference edge, its transparent band meeting the film ref edge cleanly.

To look over how your stabilization settings turned out before you capture, switch the Viewer to full resolution and zoom right in on the perforation area so you can fine-tune. Just click the options settings at the Viewer’s top right corner and pick ‘full resolution preview’ from the menu, then click the zoom scalar at the Viewer’s top left-hand corner and pick ‘100%’. This setting leaves the stabilization feature alone but gives you the best possible preview so you can watch how well it’s doing. Full resolution preview leans hard on the GPU and may bring some frame lag. For the best performance, switch full resolution off once you’ve checked stabilization. Worth noting is that the overlay position is stored within the project settings rather than the clip settings, so it may need to be set individually for several rolls. To reset the detection overlay to its default position for a given film type, use the Stabilization pane Reset button.

### Audio and Synchronization

The Audio and Synchronization palette holds settings for the optional Cintel Audio and KeyKode Reader. For more, consult the Blackmagic Cintel manual under its ‘optional Audio and KeyKode Reader’ section.

### Film Protection

These controls exist so that delicate film can be treated gently by the Cintel Scanner. Quick acceleration and shuttle speeds can be rough on archival footage, so it’s wise to bring both of these sliders down from their defaults any time you’re scanning older film.

When you scan older, delicate archival film, bring down the ‘Acceleration’ and ‘Shuttle Speed’ sliders. NOTE: A ‘Film Tension Adjust’ slider shows up on Cintel scanners fitted with sprockets.

- Max Acceleration: Sets the largest change in speed, to climb or fall by 5-30 fps per second.
- Max Shuttle Speed: Governs the pace of shuttling between film sections — ranging 1–100 frames per second on 35mm film, and ranging 1–200 frames per second on 16mm film.
- Film Tension Adjust: When your Cintel Scanner carries sprocket wheels, this setting lets you tune how much tension is put on 35mm film — say, when loading delicate archival film or making up for film shrinkage. There’s no way at all to harm the film with the ‘film tension adjust’ setting. The adjustment values are tiny, and only gentle changes are ever needed to stop sprocket picking. When your Cintel Scanner carries capstans, sprocket picking can’t happen, so this setting is disabled or absent.
