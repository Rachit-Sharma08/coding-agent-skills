# Color and goals of color correction

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grading overview.
[Chapter index](INDEX.md) / [Next section](originally-graded-scene-and-hsl-qualification-of-the-sky.md)
<a id="source-audience-expectations"></a> <a id="source-balanced-and-gain-corrected"></a> <a id="source-color"></a> <a id="source-color-1"></a> <a id="source-cool-look-warm-look"></a> <a id="source-emphasizing-whats-important"></a> <a id="source-high-contrast"></a> <a id="source-high-saturation"></a> <a id="source-hsl-qualification-on-the-skin"></a> <a id="source-introduction-to-color-grading"></a> <a id="source-introduction-to-color-grading-1"></a> <a id="source-introduction-to-color-grading-2"></a> <a id="source-log-encoded-source"></a> <a id="source-low-contrast"></a> <a id="source-low-saturation"></a> <a id="source-maximizing-the-look-of-your-media"></a> <a id="source-normalized-and-corrected"></a> <a id="source-overview"></a> <a id="source-primary-correction-wheels-primary-correction-bars"></a> <a id="source-skin-now-has-warmer-grade"></a> <a id="source-source-image"></a> <a id="source-the-goals-of-color-correction"></a> <a id="source-underexposed-source"></a>

## Overview

Covers: Color; Introduction to Color Grading.

## Color

### Color

## Introduction to Color Grading

### Introduction to Color Grading

Across more than three decades, DaVinci has led the way in creating color correction hardware and software meant to improve the visuals captured from film and video. The tools shipping in this release of DaVinci Resolve are the most advanced and refined professional color correction tools we have ever offered. Yet, however technically sophisticated it may be, DaVinci Resolve remains nothing more than an instrument that needs a skilled artist’s hand to reach its full promise. Later chapters of this user manual go into the DaVinci Resolve grading tools on the Color page at length, but ahead of digging into the particulars of color balancing and contrast adjustment, Power Windows, and Custom Curves, it pays to pause and think about the purpose of these tools and why you are bothering to learn this application at all. What follows is meant for anyone fresh to the practice we refer to as color correction, or color grading. A seasoned colorist may wish to jump ahead, but for newcomers the sections below set out to lay out the numerous aims of color correction, along with the way the DaVinci Resolve toolset was built to meet them, turning images quickly and efficiently in countless directions as we raise raw footage into cinematic art.

### The Goals of Color Correction

Picture reality as a fire hose of visual information; digital cinema and broadcast, by comparison, would be the garden hose. Seen that way, color correction amounts to deciding which portions of that fire hose of raw image data get squeezed into the garden hose of our displays so the viewer ends up with a pleasing picture.

### Maximizing the Look of Your Media

Plainly, the bedrock of the color correction process is getting every clip to look as good as it can. The cinematographer’s task is to light and expose the picture with an artistic aim; yours is to deliver that aim by tweaking the color and contrast of the picture until the end result sits as near to the director’s and cinematographer’s vision as is humanly achievable. Along the way, you get a chance to iron out exposure and white balance inconsistencies that, for one reason or another, could not be helped. On top of that, you can apply gentle tweaks that introduce warmth or contrast the shoot never allowed but the cinematographer would have welcomed. More and more, color correction is regarded as a pivotal phase of the post-production process. Take the latest crop of digital cinema cameras, which can shoot raw colorspace image data, or RGB image data carrying a log exposure, so as to hold onto as much image data as possible for reworking during the color correction process. Acquire image data in that fashion, though, and it has to be turned into a viewable image through color correction, much the way film negative must first be developed and printed onto positive film.

### Log encoded source

### Normalized and corrected

Source footage courtesy of Gianluca Bertone DP, www.bertonevisuals.com

Naturally, there will also be times when you have to try repairing source media plagued by much weightier color and exposure troubles. For those occasions, the tools are on hand to apply far more elaborate adjustments to the image; the caliber of what you get, however, leans heavily on the data quality and “latitude” of your source media. Cameras like the Blackmagic URSA, ARRI ALEXA, and RED DRAGON, for instance, capture a good deal of image data, which makes drastic corrections far more feasible than they are with more heavily compressed camera formats such as the Canon 5D. Either way, though, DaVinci Resolve supplies the tools to work images in numerous fashions and nudge them toward a better look.

### Underexposed source

### Balanced and gain corrected

No matter whether a clip calls for big shifts or tiny ones, the primary DaVinci Resolve toolset tunes the qualities of hue, saturation, and contrast through several methods. Within the Color Wheels palette, the Color balance wheels let you move all three color channels together, shifting the scene’s color temperature across particular tonal-detail ranges known as lift, gamma, and gain. As an alternative, the slider‑based Primaries Bars mode delivers those same kinds of controls by way of separately adjustable red, green, and blue lift, gamma, and gain controls.

### Primary correction wheels, Primary correction bars

Every one of these controls lets you set the color tone of the shadows, midtones, and highlights apart from one another.

### Cool look Warm look

The Master Lift, Gamma, and Gain wheels, for their part, act in concert so you can reshape image contrast various ways: driving shadows deeper, lifting highlights, and pushing the in-between midtones brighter or darker to land on whatever image tonality suits a particular scene.

### High contrast

### Low contrast

Source footage courtesy of Gianluca Bertone DP, www.bertonevisuals.com

Dedicated saturation controls let you raise or lower color intensity across the whole scene, whereas the Lum vs. Sat and Sat vs. Sat curves hand you the means to fine-tune saturation in a very targeted way.

### High Saturation

### Low Saturation

To read more about these controls, which are indispensable to the color correction process, see Chapter 131, “Primaries Palette.”

### Emphasizing What’s Important

A further key facet of the color correction process is being able to adjust the image so as to play up or play down particular elements inside the frame. The idea parallels equalization in audio mixing, since you are deciding which color values to lift or hold back through an assortment of techniques. You might do this to steer where the viewer looks, say by ringing a chosen portion of the image with a window, which confines specific adjustments to the inside and the outside of that window’s shape.

Drawing a window to isolate a region of the picture to highlight Targeted alterations are equally useful for keeping the audience from being distracted. A low-saturation monochromatic tint, for instance, might read well as an overall look, yet within that gentle wash of color the viewer could lose sight of the watch that consumes the protagonist. Tools like the Hue curves and HSL Qualifier let you, with little effort and in short order, recolor both the woman’s hands and the watch itself, steering the viewer’s eye and lending the scene some welcome depth.

Source image Curves and HSL qualification put to work setting the hands apart and drawing attention to the watch To read more about Power Windows, see Chapter 138, “Secondary Windows.” To read more about Hue curves, see Chapter 134, “Curves.”

### Audience Expectations

A separate group of tools, the HSL, RGB, and Luma Qualifiers, grants still finer control, and it comes in handy for tuning color ranges so they either reinforce or push against what the audience expects of color in a scene. A good deal of research into the so-called “memory color” reveals that people hold precisely calibrated expectations for the hues of certain subjects, flesh tone, foliage greens, and sky blues among them. Straying from those expectations can stir a feeling that something is slightly off, which may work for you or against you depending on what you intend for a given scene. In practice, HSL Qualification behaves as a chroma keyer, letting you sample the image to build a key that marks out where a particular correction lands. Suppose, for example, that the rest of the image pleases you but the actor’s skin tone has taken on an unhealthy green cast; you can single out the color of that actor’s skin and shift it toward a healthier hue.

### Source Image

### HSL qualification on the skin

### Skin now has warmer grade

Skies are another frequent case for adjustment. When you are after a glorious summer day, a washed out sky in the source media can be something of a letdown. Lean on qualification, though, and singling out that slice of blue becomes simple, after which you can nudge it back and forth until it carries just the right dose of summertime joy.
