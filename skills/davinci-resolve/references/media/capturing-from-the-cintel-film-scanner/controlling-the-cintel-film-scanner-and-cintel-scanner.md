# Controlling the cintel film scanner and cintel scanner

Version: DaVinci Resolve 20.3 Reference Manual. Context: Capturing from the cintel film scanner.
[Chapter index](INDEX.md) / [Next section](scanner-light-status-and-stabilization.md)
<a id="source-adjusting-the-light-source"></a> <a id="source-calibration"></a> <a id="source-capturing-from-the-cintel-film-scanner"></a> <a id="source-capturing-from-the-cintel-film-scanner-part-1"></a> <a id="source-cintel-scanner-controls-in-the-media-page"></a> <a id="source-controlling-the-cintel-film-scanner"></a> <a id="source-correct-calibration-of-standard-8mm-film"></a> <a id="source-film-controls"></a> <a id="source-film-type"></a> <a id="source-film-type-controls-in-the-media-page"></a> <a id="source-incorrect"></a> <a id="source-incorrect-1"></a> <a id="source-standard-16mm-neg-correct"></a> <a id="source-super-16mm-poss-correct"></a> <a id="source-the-cintel-scanner"></a> <a id="source-the-cintel-scanner-interface"></a>

### Capturing From the Cintel Film Scanner

Walking through how to bring scanned film in, this chapter covers the DaVinci Resolve settings and workflows that drive the Cintel film scanner.

### Controlling the Cintel Film Scanner

The Blackmagic Cintel film scanner is a small, simple, real-time film scanner that turns 35mm, 16mm, and 8mm (the latter needing gates bought separately) positive and negative film formats into Cintel Raw Image (CRI) digital files. Those files can then be organized, edited, and graded in DaVinci Resolve, delivered to whatever format DaVinci Resolve is able to output, and stored away for later use.

### The Cintel scanner

Any Blackmagic Cintel film scanner hooked up to your computer over Thunderbolt or PCIe can be driven by DaVinci Resolve. With it connected, you can switch on the Film Scanner controls in the Media page, which let you pick the film type for scanning, line the film frames up with the sensor, tune the scanner’s light source for the best exposure and color, and decide whether the scanner’s hardware-based Automatic Perf Detection should handle image stabilization. NOTE: This chapter of the DaVinci Resolve manual covers running a Cintel film scanner connected to DaVinci Resolve so as to ingest scanned film. For other operational questions, consult the documentation shipped with the scanner itself, or head to the Blackmagic Design support page on the web to download it. This part of the manual walks you through using the settings and features in DaVinci Resolve’s film scanner panel to drive your scanner — for instance, calibrating it, dialing in the light source strength and color temperature, configuring image stabilization, and beyond. You can even dictate how gently your Cintel scanner treats film that may have grown fragile with age. TIP: DaVinci Resolve stores every scanner setting inside your current project.

### The Cintel Scanner Interface

Click the ‘capture’ button on the UI toolbar across the top of the DaVinci Resolve screen to point the media page at your Cintel scanner. Bring up DaVinci Resolve’s film scanner panel to configure, calibrate, and set options for logging or scanning a chosen stretch of the roll of film currently spooled. Should you want extra space to view the Cintel scanner controls, click the full height button sitting at the far right of the UI toolbar, then switch off the ‘metadata’ panel.

### Cintel scanner controls in the Media page

Transport Controls: Though the transport controls beneath the viewer look much like those you use in playback mode, here they instead drive the Cintel scanner. Extra controls show up for stepping forward or backward one frame at a time. In and Out Controls: Once Cintel Scanner mode is active, the transport controls have In and Out buttons sitting to their right that mark out a stretch of the film roll to capture from. The following clusters of settings turn up to the right of the Media page viewer once Cintel Scanner mode is engaged, so you can pull clips from film straight into the Media Pool.

### Film Controls

The film controls give you options to calibrate the scanner’s optics and pick the film type; you can also dial in frame alignment, set scan speed plus spool wind direction, settle on a reel type, and toggle the focus assist feature. You can lean on the calibration button to help clear dust or minor blemishes from your Cintel scanner’s optics.

### Calibration

This option lets you calibrate the scanner’s optics so as to wipe out optical blemishes or dust that won’t come off. Be aware that this feature does nothing about dust on the film itself. Although it’s wise to “spray dust” the optics before scanning fresh material, over time certain blemishes on the optics can prove impossible to remove, and that’s where hitting the calibrate button clears them from the scanned image. Run the calibration with the skid plate installed and lined up correctly, since that helps with image stabilization and yields the best image quality. To accommodate small gauge film types, the calibration button additionally examines the gate that’s fitted and shifts the captured image onto a datum reference. To allow this, run the calibration process on every gate swap with no film in the gate so performance stays optimal. Should you be working with the 8mm HDR gate or 16mm HDR Gate and have moved the aperture shutters to switch to a different film gauge, you’ll have to run the calibration process again to head off a ‘ghost image’ left from the previous calibration.

Incorrect calibration shows Super 8mm film with a Standard 8mm calibration

Incorrect calibration shows Standard 8mm film with a Super 8mm calibration

### Correct calibration of Standard 8mm film

### Incorrect

### Incorrect

### Super 16mm poss correct

### Standard 16mm neg correct

### Film Type

Lets you pick which type of film you’re scanning. Whether the film is color or black and white, your choices are positive, negative, interpositive, and internegative. HDR scanning brings a step up for every one of these film types. Choose the film type you’re scanning from 35mm 2, 3, and 4 perf, 16mm, Super 8mm, and 8mm. On its own, the scanner figures out the gauge — 35mm, 16mm, or 8mm. Where 8mm scanning is concerned, Super 8mm is the default. When you scan regular 8mm, you’ll need to set your scanner to that particular film type by hand. When you scan interpositive and internegative film on Cintel Scanner and Cintel Scanner G2, the film’s heavier density calls for slightly longer pulse durations out of the light source. Usually this leaves the scan untouched; however, a small drop in resolution can show up when scanning above 12 frames per second. Should you spot a resolution difference, just drop your scanning speed to 12 frames per second or below.

### Film Type controls in the Media page

- Enable 2 Pass HDR Scan: Turns on high dynamic range multi pass capture. Running an ‘auto black’ or ‘auto white’ on a frame holding a wide dynamic range matters here, since it works out the high and normal exposure levels from the frame you chose.
- Perf nudge: Serves for making fine tweaks to where the perf sits relative to the scanner gate aperture. To nudge upward, press Command-J; to nudge downward, press Command-L.
- Frame: These buttons activate on a push and hold. While held, the film advances slowly to shift the frame up or down, and on release the film halts where it is. This comes in handy for lining the film frame up with the scanner’s sensor. Using the ‘perf nudge’ and ‘frame’ buttons, line the visible film frame up such that the previous frame’s bottom and the following frame’s top barely show at the viewer’s top and bottom, while the current frame sits centered vertically. Make a point of confirming that the image in the viewer isn’t zoomed in while you do this. On your keyboard, Command‑Left Arrow shifts the frame up, whereas Command-Right Arrow shifts it down.
- Scan Speed: Given enough disk performance, you ought to be able to scan at 30 fps. That said, if you’re scanning to a slow hard drive, you can lower the scanning speed to a frame rate your workstation can keep up with and not drop frames.
- Supply: Sets the wind direction of the left-hand side feed spool. Auto-detection will block incorrect operation, but you should still set the reel winding direction by hand to match how each film roll is wound.
- Take up: Establishes which way the right-hand side take up spool winds. Auto-detection will block incorrect operation, but you should still set the reel winding direction by hand to match how each film roll is wound.
- Use Film Reel: Small film reels carry a different weight and inertia than large film spools, and that can throw off the transport system. Tick this box to switch over to settings that give small film reels better stability.
- Focus Assist: Switches on luminance peaking on your scanner’s HDMI monitor output, along with the viewer in DaVinci Resolve’s film scanner panel, which makes nailing optimum focus adjustments straightforward.

### Adjusting the Light Source

These controls let you tune your Cintel Scanner’s light source so the optimal Dmin density minimum can be calibrated. That value — the Dmin density minimum — represents the lowest scanned value, together with the color temperature of the scanned material. Setting the light source correctly will deliver the best quality scans and keep you from clipping image data during the scanning process. Checking your light source settings whenever you change film is a smart move to safeguard your capture quality. Lean on the built-in software scopes inside DaVinci Resolve to help you set your light source to its best level settings. You can open the scopes in the Media page by choosing Workspace > Video Scopes > On.

The Media page Light Source controls, with the light source in its default uncalibrated state (left) and in its state once calibration succeeds (right)

- Light Source master wheel: The vertical light source master wheel sits beside the color wheel and sets the intensity of the light source that illuminates the film, lifting or dropping the RGB channels all together. For typical negative film, this lets you set the black point of the film image, which is the image’s darkest part. With negative film, that actually maps to the film image’s highlights. Nudge the light intensity so it rests just over the typical Dmin value of 95, as read on the histogram of the video scopes, which makes sure the highlights aren’t clipped by a Cineon‑style LOG conversion. For positive film, simply set the master wheel so no part of the signal gets clipped.
- Auto Black and Auto White button: Reads whatever frame is showing in the Viewer and, for negative and internegative, automatically fixes the black point off the framing bar area. With print and interpositive film, it instead leans on the image area’s brightest highlight when fixing the white point, which makes your choice of frame a key one. There’s another route for positive film types: a punch hole frame can serve as your maximum white, keeping every later frame consistent. With positive film types, what reads as the ‘auto black’ button instead becomes ‘auto white’.
