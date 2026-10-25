# Tracking transport buttons and analysis parameters and tips for choosing a good pattern

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](tracker-inspector-controls-and-tracker-control-tab.md) / [Next section](best-match-tracking.md)
<a id="source-every-frame"></a> <a id="source-none"></a> <a id="source-selecting-patterns-for-stabilization"></a> <a id="source-selecting-the-patterns-image-channels"></a> <a id="source-the-adaptive-mode-options"></a> <a id="source-the-tracker-pattern-selection-and-flipbook-thumbnails"></a> <a id="source-the-tracking-transport-buttons-and-analysis-parameters"></a> <a id="source-tips-for-choosing-a-good-pattern"></a> <a id="source-using-adaptive-pattern-tracking"></a> <a id="source-using-the-pattern-flipbooks"></a>

### The tracking transport buttons and analysis parameters

To begin tracking, do one of the following:

- Click the Track Reverse button, which begins tracking at the render range's very end.
- Click the Track Backward from Current Frame button, which tracks backward starting at the playhead's present position.
- Click the Track Forward button, which begins tracking at the render range's very start.
- Click the Track Forward from Current Frame button, which tracks forward starting at the playhead's present position.

On its own, pattern tracking stops once it hits the render range's end (or its start when you're tracking backward), though you're free to cut in and halt tracking at any moment. To stop tracking, do one of the following:

- Click the Stop Tracking button in the tracker transports.
- Click Stop Render at the bottom of the Fusion window.
- Press the Escape key.

Once tracking finishes, the path attaches to the pattern. That pattern's path can now be wired into another node or put toward more advanced operations like stabilization and corner positioning. With the track complete and presumably good, you can apply the various techniques in this chapter to put the track to work in your composition.

### Tips for Choosing a Good Pattern

The Tracker operates by hunting each frame for the pixels held in the pattern. For a track to succeed, a reasonably high-contrast and distinctive region of the image has to be present in the footage. This step is known as pattern selection. The first part of pattern selection is to screen the footage you'll track several times over. Keep an eye out for candidate patterns that stay visible through the whole range of frames, where the contrast runs high and the pattern's shape holds steady over time. The more distinctive the pattern, the better the odds the track succeeds. Along with spotting high-contrast, well-defined patterns, watch for the frames where the pattern travels the most. Pinning down the full extent of a pattern's motion helps you settle on the right size for the pattern search area. It's not unusual for a scene to need several different patterns to build one path. Most often this happens because the pattern leaves the frame or is briefly hidden by another scene element. Merging patterns into a single pattern is covered later in the chapter.

### Selecting the Pattern's Image Channels

When a patch of pixels is selected as a pattern, the Tracker automatically picks the color channel used for tracking it, drawing on an analysis of each channel for contrast, clarity, and reliability. Within the node controls, the bars off to the right of the Pattern display window highlight whichever channels were chosen. To override that automatic channel choice, click the buttons beneath each channel's bar and thereby decide which channel does the tracking.

For tracking a pattern, you're free to pick any single color channel, either luminance channel, or the alpha channel.

Highlighted channel bars indicate which channel is selected for tracking When picking a channel, the aim is to choose the cleanest, highest-contrast channel for the track. Steer clear of channels carrying lots of grain or noise. Bright objects against dark backgrounds frequently track best on the luminance channel.

### Selecting Patterns for Stabilization

Picking patterns for stabilization can be a delicate affair. Where a pattern sits at the moment it's selected determines exactly how the image gets stabilized. Correcting for rotation needs at least two patterns; three patterns will correct for scaling, and more usually sharpens the solution. Resist the urge to grab just any seemingly valid pattern in the sequence, since some patterns degrade the solution rather than improve it. To steer your choices, lean on the following guidelines while selecting patterns for stabilization.

- Place patterns at the same relative depth within the image. Objects deeper in the background travel by greater amounts than objects in the foreground, thanks to perspective distortion. That can throw off the stabilization calculations, which don't account for depth.
- Place patterns whose positions are fixed relative to one another. Patterns shouldn't be able to move with respect to each other. A sign's four corners would make excellent candidates, whereas the faces of two different people in the scene would be terrible choices for patterns.

### Using the Pattern Flipbooks

Every pattern carries a pair of thumbnail windows shown in the Inspector. The left window displays the selected pattern, while the right window refreshes during the track to display the actual pattern acquired for each frame.

### The Tracker Pattern Selection and Flipbook thumbnails

Each stored pattern joins a Flipbook. After the render finishes, you can play this Pattern Flipbook to gauge how accurate the tracked path is. Spot any jumps between frames and you'll know something probably went wrong.

### Using Adaptive Pattern Tracking

Even the most ideal pattern usually goes through shifts in profile, lighting conditions, and other variables. Such changes can damage pattern recognition to the point where a pattern stops being usable. To help offset these conditions, the Tracker provides three pattern-acquisition modes you can apply while tracking. Those modes are set through the Adaptive Mode options in the Inspector.

### The Adaptive Mode options

### None

With the Adaptive mode set to None, the pattern inside the rectangle is acquired the moment the pattern is selected, and that becomes the lone pattern used throughout the track.

### Every Frame

With Every Frame chosen, the pattern inside the rectangle is acquired the moment the pattern is selected, then reacquired at each frame. The pattern found at frame 1 drives the search on frame 2, the pattern found on frame 2 drives the search on frame 3, and onward. This approach helps the Tracker keep pace with changing conditions in the pattern. Every Frame tracking is the slower route and can drift when the pattern undergoes sub-pixel shifts from one frame to the next. Its use is therefore not recommended unless other methods fail.
