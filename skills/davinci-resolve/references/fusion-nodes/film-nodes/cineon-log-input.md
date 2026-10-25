# Cineon log input

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cineon log.
[Chapter index](INDEX.md) / [Next section](film-grain-and-grain.md)
<a id="source-basic-node-setup"></a> <a id="source-black-rolloff"></a> <a id="source-cineon-log-controls"></a> <a id="source-cineon-log-log"></a> <a id="source-cineon-log-node-introduction"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-depth"></a> <a id="source-falloff-comparison"></a> <a id="source-film-nodes"></a> <a id="source-film-nodes-part-1"></a> <a id="source-input"></a> <a id="source-inspector"></a> <a id="source-log-type"></a> <a id="source-mode"></a> <a id="source-the-black-falloff-from-the-native-fusion-process"></a> <a id="source-the-cineon-log-node"></a>

### Film Nodes

This portion of the manual covers Fusion's Film nodes.

Each node's shortened abbreviation, shown beside its name, works in the Select Tool dialog while hunting for a tool and also turns up in scripting references. Throughout these pages, treat any node tree that depicts MediaIn nodes inside DaVinci Resolve as equivalent to Loader nodes within Fusion Studio, except where a note says differently.

### Cineon Log [Log]

### The Cineon Log node

### Cineon Log Node Introduction

Use the Cineon Log node to translate a variety of log camera encodings into linear gamma, as well as the reverse trip. Despite a name that suggests Cineon material, this tool also copes with “log” gamma sourced from numerous digital cinema cameras, including those made by Blackmagic Design, Arri, and Red.

### Input

The Cineon Log node carries a pair of Inputs: one accepts the log image, the other receives the effects mask. Input: Feed the primary 2D image that receives the highlight into the orange input. Effect Mask: Into the blue input goes a mask shape, which may come from polylines, simple primitive shapes, paint strokes, or bitmaps produced elsewhere. Wiring a mask here keeps the log conversion confined to whatever pixels the mask covers. The tool runs its own processing first, after which the effects mask takes effect.

### Basic Node Setup

Position the Cineon Log node immediately downstream of a MediaIn node when in DaVinci Resolve, or of a Loader node when in Fusion Studio. A frequent second use is ahead of a MediaOut or Saver node, where it reverses the conversion to yield a Logencoded image.

### Inspector

A Cineon Log node sitting downstream of a Fusion Studio Loader node

### Cineon Log controls

### Controls Tab

Within the Controls tab live the options that move log gamma toward linear, or run the trip the other way from linear into log. Begin by picking the Mode, followed by the Log Type. As an example, pick Log to Lin in the Mode menu, then set the Log Type to BMD Film when your composite uses a RAW clip captured on a Blackmagic Design camera. That combination yields a linear image that is ready to composite.

### Depth

Through the Depth menu you choose which color depth governs how the incoming image is processed. Its factory setting is Auto, which reads the loaded file format and picks a depth accordingly. JPEG files, for instance, default to 8 bit, since that format will not hold color depths beyond 8. By contrast, Blackmagic RAW files arrive at Float, and so on. Whenever a format's depth cannot be worked out, Fusion falls back on the depth set in the Frame Format preferences.

### Mode

Two choices sit in the Mode menu: one path turns log images into linear, while the other takes linear images into logarithmic.

### Log Type

Use the Log Type menu to indicate where the file originated. Most of the time that means naming the camera that shot the image, though the Josh Pines entry exists for film scan pipelines. The camera log types offered by this menu are listed below:

- Cineon
- Arri Log C
- BMD Film
- Canon Log
- Nikon N Log
- Panalog
- Panasonic V-Log
- Red Log Film
- Sony S-Log
- Viper Film Stream
- ACESlog

Lock RGB With this turned on, whatever you set in the tab is applied identically to every color channel. Switch it off when you want to treat the image's red, green, and blue channels separately, each with its own settings. Level This range control lets you fix where the black level and the white level fall in the log image ahead of conversion. Drag the left handle to move the black level and the right handle to move the white level. After conversion, any pixel whose log-space value lies under the black level drops into out-of-range territory below 0.0, while any pixel above the white level climbs to out-of-range values past 1.0. A floating-point color space keeps both the negative and the elevated out-of-range values intact; switch to 16-bit or 8-bit mode and those out-of-range values get clipped instead. Soft Clip (Knee) Reach for the Soft Clip control when you want to pull out-of-range values back into the picture. It works by easing the conversion curve at its upper and lower ends, which makes room for additional values to be expressed. Set the soft clip to anything besides 1 and the node switches to 16-bit integer processing, discarding every out-of-range value that won't sit inside the soft clip.

Film Stock Gamma, Conversion Gamma, and Conversion Table Together these controls shape the response curves applied to the logarithmic data as it converts. Beyond the controls already covered, you may build a custom ASCII file Lookup Table (LUT) holding your own conversion values, then bring that ASCII LUT file in by clicking the Browse button.

### Common Controls

Settings Tab Because every Film node shares the same Settings tab controls, you will find them documented together under the “The Common Controls” heading that closes this chapter.

### Black Rolloff

A mathematical log() applied to zero or a negative number yields garbage, so to stay correct Fusion snaps anything under 1e-38 (a 0 trailed by 38 zeros) down to 0. In practice this rarely matters, because numbers that minuscule leave no mark on a picture. Glimpsing values that faint would require stacking three Brightness Contrast nodes, each one gained up to 1,000,000, and even that would leave them barely off zero. Some pipelines, rather than discarding these tiny numbers, choose to rescale them: values sitting between 0.0 and 1e-16 get remapped into the 1e-18 to 1e-16 band. The goal is to compress nearly the whole visible range of a float image down toward zero and then stretch it back out, producing a soft ramp through the deepest blacks. If you ever inherit a color pipeline built on this trick, you can reproduce it with a Custom node as follows. First convert the log image to linear using a tiny gamma along with an unusually broad black-to-white spread (for instance, conversion gamma of 0.6, black of 10, white of 1010), which squeezes most of the image’s range into very small numbers. Next comes a Custom node (covered just below), and after that a linear-to-log conversion that undoes the earlier step while applying a marginally higher black level. That gap between the two black levels sets the falloff range. Because this raises the blacks, you normally finish by converting once more to linear with the usual figures (i.e., 95-685) to re-establish the black point. Inside the Custom node, enter this equation into each of the red, green, and blue expressions: if (c1< 1e-16, 1e-18 + (c1/1e-16)\*(1e-16 - 1e-18), c1)

### Falloff Comparison

### The black falloff from the native Fusion process

A nearly indistinguishable black falloff produced by the ramped clipping technique
