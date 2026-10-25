# Render several frames at once and simultaneous branching

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering using saver nodes.
[Chapter index](INDEX.md) / [Previous section](render-nodes-and-relative-paths.md) / [Next section](checking-the-render-log.md)
<a id="source-limitations-of-render-nodes"></a> <a id="source-linear-tools"></a> <a id="source-render-several-frames-at-once"></a> <a id="source-saving-to-multi-frame-formats"></a> <a id="source-simultaneous-branching"></a> <a id="source-time-stretching"></a> <a id="source-troubleshooting"></a>

### Render Several Frames at Once

Fusion can process several frames in parallel to boost render throughput. This slider sets how many frames render at the same time. Whatever value shows multiplies memory consumption (a setting of 3 eats three times the memory of a setting of 1). Typical values run 2 or 3, though well-equipped machines may gain from higher numbers, while memory-starved machines might need the value held at 1.

### Simultaneous Branching

Turn this option on to have all layers render in parallel. The throughput payoff can be considerable, yet it may also consume far more memory, particularly when a composition stacks up many layers. On memory-constrained machines you may have to switch Simultaneous Branching off while rendering compositions that carry lots of layers.

### Limitations of Render Nodes

Keep in mind a handful of significant constraints as you build compositions and render them across a network.

### Time Stretching

Compositions leaning on the Time Stretcher and Time Speed tools can run into trouble during a network render. Accelerating or decelerating compositions and clips means pulling several frames both ahead of and behind the frame currently rendering, which drives up I/O against the file server. That can deepen network bottlenecks and make rendering inefficient. When a composition employs the Time Stretcher or Time Speed tools, confirm the network can handle the load, or pre-render that portion of the composition ahead of network rendering.

### Linear Tools

Some tools simply won’t network render correctly. Third-party particle systems like Genarts’s Smoke and Rain, along with the Fusion Trails node, can’t be rendered properly across the network. Such tools typically retain the result from the prior render and feed it into the next frame’s render, making each frame reliant on the one rendered just before. Because that data stays local to the tool, these tools fail to render correctly over a network.

### Saving to Multi-Frame Formats

A single QuickTime file can’t be rendered by several machines together. Render instead to discrete sequential file formats such as EXR, DPX, JPEG, and the like. After the render finishes, one workstation can pull in the image sequence in order and export it to whatever compiled format you want. NOTE: None of this pertains to network rendered previews, which are previews built over the network using spooling so that multi-frame formats render successfully. This limitation touches final renders alone.

### Troubleshooting

A few recurring traps show up when rendering across a network. Nearly every network rendering issue traces back to either path names or plugins. Revisit this chapter’s “Preparing Compositions for Network Rendering” section to go over the key setup requirements again. Make sure each Render node can load both the compositions and the media, and that every Render node has the plugins the composition relies on installed. Should trouble linger, get in touch with Blackmagic Design’s technical support through the support area on the Blackmagic Design website. Keep a copy of the render.log file to forward to technical support.
