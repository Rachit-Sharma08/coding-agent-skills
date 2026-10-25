# About supported transitions and transition names

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing timelines for import and comparison.
[Chapter index](INDEX.md) / [Previous section](effect-import-format-support.md) / [Next section](about-supported-composite-modes-and-fcp-7-x-xml.md)
<a id="source-4-corners-effect-in-the-shape-wipe-category"></a> <a id="source-about-flip-and-flop-support"></a> <a id="source-about-ken-burns-effect-and-dynamic-zoom"></a> <a id="source-about-nested-sequences-and-compound-clips"></a> <a id="source-about-speed-effects"></a> <a id="source-about-supported-opacity-position-scale-and-rotation-settings"></a> <a id="source-about-supported-transitions"></a> <a id="source-circle-effect-in-the-shape-wipe-category"></a> <a id="source-clock-effect-in-the-shape-wipe-category"></a> <a id="source-clock-wipe"></a> <a id="source-diamond-effect-in-the-shape-wipe-category"></a> <a id="source-diamond-iris"></a> <a id="source-dip-to-color-dissolve-edge-wipe-center-wipe"></a> <a id="source-dip-to-color-effect-in-the-blend-category"></a> <a id="source-oval-iris"></a> <a id="source-pitch-and-yaw-1"></a> <a id="source-transition-names"></a>

### About Supported Transitions

When it comes to transition support in DaVinci Resolve, EDLs allow the least, since only Cross Dissolves get read. As an EDL imports into DaVinci Resolve, every other transition in it is turned automatically into a Cross Dissolve running the same length. By contrast, DaVinci Resolve will bring in ten distinct transitions from XML project files made by Final Cut Pro X and legacy Final Cut Pro 7, or nine distinct transitions from AAF files made by Avid Media Composer or Symphony.

| Transition | EDL | FCP XML | AAF |
| --- | --- | --- | --- |
| Clock Wipe | No | Yes | Yes |
| Center Wipe | No | Yes | Yes |
| Cross Dissolve | Yes | Yes | Yes |
| Additive Dissolve | No | Yes | No |
| Dip to Color Dissolve | No | Yes | Yes |
| Edge Wipe | No | Yes | Yes |
| Venetian Blind Wipe | No | Yes | Yes |
| Cross Iris | No | Yes | Yes |
| Diamond Iris | No | Yes | Yes |
| Oval Iris | No | Yes | Yes |

### Avid transition names

| Resolve transition | Media Composer or Symphony equivalent |
| --- | --- |
| Dip to Color Dissolve | Dip to Color in Blend |
| Edge Wipe | Horizontal, Vertical, and diagonal wipes in Edge Wipe |
| Center Wipe | Horizontal Open or Vertical Open in Edge Wipe |
| Clock Wipe | Clock in Shape Wipe |
| Venetian Blind Wipe | Vertical Blinds or Horizontal Blinds in Shape Wipe |
| Cross Iris | 4 Corners in Shape Wipe |
| Diamond Iris | Diamond in Shape Wipe |
| Oval Iris | Circle in Shape Wipe |

### About Supported Opacity, Position, Scale, and Rotation Settings

Bringing in XML project files made by Final Cut Pro X, by Premiere Pro, or by legacy Final Cut Pro 7, DaVinci Resolve will accept Opacity, Position, Scale, and Rotation settings. The imported Composite and Transform settings for any clip turn up either in the Edit page Inspector or in the Edit Sizing mode of the Color page’s Sizing palette. Where those settings carry keyframes, the animation comes through in DaVinci Resolve. As it brings in AAF files from Media Composer or Symphony, DaVinci Resolve accepts Opacity, Resize, and 3D Warp effects, turning them into Pan, Tilt, Zoom, and Rotate settings inside DaVinci Resolve, found in the Edit page Inspector or the Edit Sizing mode of the Color page’s Sizing palette.

### About Flip and Flop Support

As it brings in AAF project files from Media Composer or Symphony, DaVinci Resolve turns Flip, Flop, and Flip-Flop effects into the matching horizontal and vertical Flip toggles, found in the Edit page Inspector or the Edit Sizing mode of the Color page’s Sizing palette.

### Pitch and Yaw

As it brings in AAF files from Media Composer or Symphony, DaVinci Resolve accepts Pitch and Yaw 3D Warp effects and turns them into matching Pitch and Yaw settings inside DaVinci Resolve, found in the Edit page Inspector or the Edit Sizing mode of the Color page’s Sizing palette.

### About “Ken Burns Effect” and Dynamic Zoom

Bring in a Final Cut Pro X project whose clips lean on the Ken Burns effect to build pan and scan animation, and the Dynamic Zoom parameters (which sit in the Edit page Inspector once a clip is selected) for every affected clip get filled with a matching animated effect.

### About Speed Effects

Speed effects from various applications can come into DaVinci Resolve, though how much speed effect support you get changes with the project format.

- EDL: From EDLs, DaVinci Resolve takes in linear speed effects only.
- XML: Both linear and variable speed effects come into DaVinci Resolve when you

bring in XML project files authored by Premiere Pro, by Final Cut Pro 7, or by Final Cut Pro X. Starting with DaVinci Resolve version 11.1, XML from Final Cut Pro X can additionally report whether frame blending or optical flow is in use, along with detail on the Bezier curve transitions of speed effects.

- AAF: Both linear and variable speed effects come into DaVinci Resolve when you bring in AAF files from Media Composer or Symphony that rely on Timewarp effects.

DaVinci Resolve converts variable-speed speed effect data from other applications with high fidelity, laying down a single speed keyframe on every frame of each affected clip. You might still notice slight differences between the speed effect that results in DaVinci Resolve and an offline reference movie exported from the source NLE, should you have left the Retime Process setting on a speed interpolation type other than the one the source NLE used. Put another way, if you made a Timewarp speed effect in Media Composer that uses FluidMotion for smooth slow motion, you will want to switch either the project-wide or the clip-specific Retime Process setting to Optical Flow so DaVinci Resolve’s speed effects line up as closely as possible with those in Media Composer.

To read more about speed effects in DaVinci Resolve, see Chapter 51, “Speed Effects.”

### About Nested Sequences and Compound Clips

Compound clips from Final Cut Pro X and nested sequences from legacy Final Cut Pro 7 can both come into DaVinci Resolve, where each shows up as a compound clip across both the Timeline and the Media Pool. Compound clips holding mixed frame rates work in DaVinci Resolve, as do multicam and A/V synchronized clips out of Final Cut Pro X, all of which DaVinci Resolve represents as compound clips. For deeper coverage of building and working with compound clips inside DaVinci Resolve, turn to Chapter 43, “Take Selectors, Compound Clips, and Nested Timelines,” specifically its “Compound Clips” section.
