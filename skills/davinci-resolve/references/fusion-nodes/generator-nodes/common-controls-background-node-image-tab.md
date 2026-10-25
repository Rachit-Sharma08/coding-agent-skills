# Common controls background node image tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](text-follower-timing-tab.md) / [Next section](common-controls-motion-blur.md)
<a id="source-background-node-image-tab"></a> <a id="source-common-generator-settings"></a> <a id="source-fast-noise-image-tab-options"></a> <a id="source-generator-nodes-part-4"></a> <a id="source-image-tab"></a> <a id="source-inspector-5"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a>

### The Common Controls

Image-generating nodes share several identical controls in the Inspector. This section covers the controls held in common across Generator nodes.

### Inspector

### Background node Image tab

### Image Tab

This tab's controls serve to fix the resolution, color depth, and pixel aspect of the image the node turns out. Process Mode This menu control picks the Fields Processing mode Fusion uses to render changes to the image. The default choice is governed by the Has Fields checkbox control over in the Frame Format preferences. Global In and Out This control fixes where this node sits inside the project. Use Global In to fix which frame starts the clip and Global Out to fix which frame ends the clip (inclusive) inside the project's Global Range. The node turns out no image on frames beyond this range. Use Frame Format Settings Tick this checkbox and the width, height, and pixel aspect of the image the node builds get locked to the values set in the composition's Frame Format preferences. Should the Frame Format preferences shift, the resolution of the node's image shifts to match. Switching this option off can help when you build a composition at a resolution other than the eventual target resolution for the final render.

Width/Height This pair of controls fixes the Width and Height dimensions of the image the node will build. Pixel Aspect This control fixes the Pixel Aspect ratio of the built images. A ratio of 1:1 yields a square pixel matching on every side (like a computer display monitor), while an aspect of 0.9:1 yields a slightly rectangular pixel (like an NTSC monitor). NOTE: Right-click the Width, Height, or Pixel Aspect controls to bring up a menu listing the file formats set in the preferences Frame Format tab. Pick any listed option and the width, height, and pixel aspect snap to that format's values accordingly. Depth The Depth drop-down menu fixes the pixel color depth of the image the Creator node builds. 32-bit pixels eat 4X the memory of 8-bit pixels yet carry far greater color accuracy. Float pixels permit high dynamic range values outside the usual 0…1 range, for showing colors brighter than white or darker than black. Source Color Space The Source Color Space menu lets you set the footage's Color Space to help reach a linear workflow. Unlike the Gamut tool, this performs no actual color space conversion; rather it folds the source space data into the metadata if that metadata is missing. Further down the chain, a Gamut tool set to the From Image option can lean on that metadata, as can a Saver where explicit output spaces have been defined. There are two options to pick from:

- Auto: On its own, reads any metadata the image carries and passes it along.
- Space: Brings up a Color Space Type menu from which you can pick the image's right color

space. Source Gamma Space Through the Curve type menu, you can fix the footage's Gamma Space and choose to strip it via the Remove Curve checkbox while working in a linear workflow. The Curve type menu holds three choices:

- Auto: By itself, reads whatever metadata sits in the image and hands it onward.
- Space: Brings up a Gamma Space Type menu from which you can pick the image's right gamma

curve.

- Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For a fuller account, turn to the DaVinci Resolve Reference Manual's Chapter 99, "Film Nodes," or to the Fusion Reference Manual's Chapter 39. Remove Curve Hinging on the chosen Gamma Space or on whatever Gamma Space Auto mode turns up, the Gamma Curve gets stripped from the material, or a log-lin conversion runs on it, effectively turning it into a linear output space.

### Fast Noise Image Tab Options

The controls below belong to the Image tab in the Fast Noise Node. Mask Map Inputs These outside connections let you use masks to steer the value of the Noise Detail and Brightness controls separately for each pixel. That can open the door to some intriguing, creative effects. Noise Detail Map Wire a soft-edged mask into the Noise Detail Map and you get a flat noise map (zero detail) wherever the mask is black, full detail wherever it's white, and in-between values that smoothly ease off in detail. It takes effect ahead of any gradient color mapping. That can really help when you want maximum noise detail in one spot while it falls off smoothly elsewhere. Noise Brightness Map A mask wired into this input can steer the noise map outright—boosting it in certain spots, blending it with other textures, or, where Detail sits at 0, standing in for the Perlin Noise map entirely.

### Common Generator settings

### Settings Tab

You'll find the Inspector's Settings Tab on every tool in the Color category. The Settings controls even turn up on third-party Color-type plugin tools. They stay consistent and behave the same across each tool, though some tools do throw in one or two individual options, covered here as well. Blend What the Blend control does is mix the tool's starting image input with the tool's finished, altered output image. With a blend value of 0.0, the outgoing image matches the incoming one exactly. As a rule this makes the tool skip processing altogether, copying the input straight across to the output. Process When Blend Is 0.0 The tool gets processed even when the input value is zero. That can help if this node's processing is scripted to set off another task while the node's value is parked at 0.0.

Red/Green/Blue/Alpha Channel Selector This quartet of buttons serves to confine the tool’s effect to the color channels you name. The filtering it performs usually happens once the tool itself has finished processing. To illustrate, when the red button on a Blur tool is switched off, the blur is applied to the image first, after which the red channel taken from the original input is laid back over the result’s red channel. Certain tools are exceptions: switching these channels off makes the tool bypass processing of that channel altogether. Such tools normally carry a matching set of RGBA buttons over on the Controls tab within the tool. Here, the buttons on the Settings and on the Controls tabs match one another. Apply Mask Inverted Turning on the Apply Mask Inverted option flips the entire mask channel belonging to the tool. That mask channel is the merged outcome of every mask that is wired into or built within a node. Multiply by Mask Choosing this option multiplies the RGB values of the masked image by the values held in the mask channel. The effect is that every image pixel lying outside the mask (that is, set to 0) turns black/ transparent. Use Object/Use Material (Checkboxes) Certain 3D software is able to render into file formats carrying extra channels. The EXR file format in particular handles Object ID and Material ID channels, and those can serve as a mask for the effect. Whether or not such channels get used when present is governed by these checkboxes. Exactly which Material ID or Object ID is targeted gets picked through the following group of controls. Correct Edges You only see this checkbox once the Use Object or Use Material checkboxes are turned on. It switches between methods for handling the overlapping edges of objects inside a multi-object image. With it enabled, the Coverage and Background Color channels go to work separating and refining the effect around the object’s edge. Should this option be disabled (or should no Coverage or Background Color channels exist), the mask edge may show aliasing. Further detail lives in Chapter 78, "Understanding Image Channels," found within the DaVinci Resolve Reference Manual, and additionally within Chapter 18 over inside the Fusion Reference Manual. Object ID/Material ID (Sliders) These sliders let you pick which ID becomes the basis for a mask drawn from the object or material channels of an image. The Sample button works just like the Color Picker does: it lifts IDs straight from the image shown in the view. Whatever image or sequence you use has to have been rendered out of a 3D software package that included those channels.
