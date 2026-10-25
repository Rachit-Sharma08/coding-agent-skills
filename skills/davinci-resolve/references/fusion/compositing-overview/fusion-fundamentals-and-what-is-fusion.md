# Fusion fundamentals and what is Fusion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing overview.
[Chapter index](INDEX.md)
<a id="source-3d-compositing"></a> <a id="source-fusion-fundamentals"></a> <a id="source-fusion-fundamentals-1"></a> <a id="source-how-hard-will-this-be-to-learn"></a> <a id="source-introduction-to-compositing-in-fusion"></a> <a id="source-introduction-to-compositing-in-fusion-1"></a> <a id="source-introduction-to-compositing-in-fusion-2"></a> <a id="source-overview"></a> <a id="source-rendering-out-your-final-result"></a> <a id="source-the-fusion-page-within-davinci-resolve"></a> <a id="source-the-fusion-studio-stand-alone-application"></a> <a id="source-what-is-fusion"></a> <a id="source-what-kinds-of-effects-does-fusion-offer"></a>

## Overview

Covers: Fusion Fundamentals; Introduction to Compositing in Fusion.

## Fusion Fundamentals

### Fusion Fundamentals

## Introduction to Compositing in Fusion

### Introduction to Compositing in Fusion

The purpose of this introduction is squarely to help anyone fresh to Fusion find their footing in this remarkably capable environment for building and reworking visual effects and motion graphics directly inside DaVinci Resolve or by way of the stand-alone Fusion Studio application. What follows applies both to the Fusion Page within DaVinci Resolve and to the stand-alone Fusion Studio application.

### What Is Fusion?

Blackmagic Design Fusion is a heavyweight 2D and 3D visual effects compositing package with more than three decades of refinement behind it in the motion picture and broadcast world, responsible for effects featured in a great many films and TV series. You can run it as a stand-alone application or reach for it as a page inside DaVinci Resolve. At its core, Fusion amounts to a set of image-processing engines known as nodes. Such nodes stand in for effects like blurs and color correctors, and equally for images, 3D models, and spline masks. Much like effects you’ve likely encountered, every node carries a group of parameters open to adjustment and animation across time. Wiring assorted nodes together inside a graphical user interface known as a node tree is what lets you assemble elaborate visual effects. Whatever nodes, node trees, and settings you build get stored in a document referred to as a Composition, or “comp” for short.

### The Fusion Page within DaVinci Resolve

Built straight into DaVinci Resolve, the Fusion page lets you leap instantly out of editing and into compositing, with nothing to export, no files to relink, and no second application to fire up before getting on with the job. These days everything you require sits right within DaVinci Resolve.

The Fusion page inside DaVinci Resolve, with its viewers, the Node Editor, and the Inspector on display How Do I Use the Fusion Page? The way the Edit page relates to the Fusion page mirrors how the Edit page relates to the Color page. Just as any clip can receive a grade over on the Color page, every clip can likewise carry a composition built on the Fusion page. The moment you use the Fusion page to construct any sort of effect or composite, a badge shows up on that clip in the Timeline marking it as having a composition.

Any clip carrying a Fusion page composition displays a Fusion badge just past its name on the right. Making an effect on the Fusion page of DaVinci Resolve takes nothing more than parking the playhead atop a clip in the Edit or Cut page and clicking the Fusion page button. That clip turns up right away as a MediaIn node on the Fusion page, set for you to layer on all kinds of stylistic effects. You might paint away an unwanted blemish or object, throw together a fast composite to drop in graphics or text, or pull off whatever other visual effect comes to mind, drawing on the Fusion page’s arsenal of effects. As another route inside DaVinci Resolve, you can first edit together every clip you intend to use — stacking and aligning each piece of media you’ll require with the right timing — before selecting them and producing a Fusion clip. Such a Fusion clip behaves as one item on the Edit or Cut page timeline, yet once you’re inside the Fusion page, every piece of media you gathered is laid out in a fully assembled Fusion composition, ready for you to begin adding nodes and tailoring it to whatever effect you’re chasing. However you prefer to work, all of it unfolds on the very same timeline as editing, grading, and audio post, giving you a seamless back and forth while you edit, refine, and finish your projects.

How Do Fusion Effects Differ from Edit Page Effects? While working in DaVinci Resolve, plenty of effects can be built right on the Edit page. Lower third titles, time remapping, over-the-shoulder picture-in-picture setups, superimpositions, fades, and transitions all sit among the effects you can throw together more quickly and efficiently right on the Edit or Cut page timeline. The node-based interface of the Fusion page, by contrast, lets you burrow into the fine detail of a composition to craft sophisticated 2D and 3D effects with exacting control and limitless customization. Effects layering more than two or three elements grow far more manageable inside Fusion. Green or blue screen composites, sky replacements, and object removal all sit better with Fusion’s deeper toolset. How Do Fusion Effects Differ from Color Page Effects? Some visual effects work can also be tackled on the Color page in DaVinci Resolve. Effects that straddle the boundary between color grading and finishing can prove quick and intuitive on the Color Page, particularly for folks already at home with the Color page toolset. Beauty work and minor image repairs can lean efficiently on the Color page’s no-nonsense Tracking tool, Face Refinement, and Patch Replacer effects. That said, once you reach the trickier blue/green screen compositing, the tools assembled around Fusion’s formidable Delta keyer handle such shots more ably. Dropping 3D objects into live-action footage, split-screen effects, motion graphics, and precise keyframing all belong more naturally on the Fusion page.

### The Fusion Studio Stand-Alone Application

Making visual effects in the stand-alone Fusion Studio software starts by launching Fusion, spinning up a new composition, pulling in a few clips through Loader nodes, and fleshing out your composite with effects. Exactly as with the Fusion Page in DaVinci Resolve, effects get added through the various nodes in the Effects Library, and several layers of imagery are combined by means of Merge nodes. After you’ve arrived at the look you’re after, cap off the tree of nodes you’ve built with a Saver node to render your finished result.

### Rendering Out Your Final Result

In contrast to the Fusion Page in DaVinci Resolve — which renders straight back into the Edit or Cut page timeline — the closing move in Fusion Studio is to write the finished effect out to disk as a movie file or image sequence. Every node tree ends with a Saver node. A Saver node sets the output file format and writes the file out to disk. Feel free to drop as many Saver nodes into a composite as the work calls for. You might, for example, lean on several Saver nodes to render out intermediate portions of a composite or to deliver one composite across multiple formats.

### What Kinds of Effects Does Fusion Offer?

On top of the robust compositing, paint, rotoscoping, and keying effects you’d count on from any full-featured 2D compositing environment, Fusion brings considerably more to the table.

### 3D Compositing

Fusion comes with capable 3D nodes covering extruded 3D text, basic geometry, and the means to bring in 3D models. With a 3D scene assembled, you can layer in cameras, lighting, and material shaders, then render the outcome with depth-of-field effects and auxiliary channels so it slots in alongside more traditional layers of 2D compositing — a refined marriage of 3D and 2D operations inside the very same node tree.

A textured 3D text scene, built start to finish inside Fusion Particles Fusion further packs a deep collection of nodes for building particle systems that have appeared in major motion pictures, with particle generators able to spawn further generators, 3D particle generation, intricate simulation behaviors that play off 3D objects, and no end of room for experimentation and customization. Whether you want particle-driven simulations aimed at VFX or looser, more abstract particle work for motion graphics, you can build either.

A 3D particle system, also created entirely within Fusion Text Fusion’s Text tools are first-rate, handing you layout and animation choices in both 2D and 3D. What’s more, inside DaVinci Resolve those Text tools have been folded into the Edit and Cut pages as Fusion Titles. Such title templates are compositions saved out of Fusion as macros carrying published controls that surface in the Edit or Cut page Inspector for painless customization, even when you’re collaborating with people who have no Fusion experience.

A layered text composite that blends video clips together with elements generated in Fusion And Lots More The list runs on and on. What with Warping effects, formidable Masking and Rotoscoping nodes, Deep Pixel nodes that re‑composite rendered 3D scenes off Auxiliary Channel data, Planar Tracking, and Stereo and VR adjustment nodes, Fusion stands as a stunningly well-equipped environment for conjuring worlds, mending problems, and soaring multi-layered motion graphics animations through your programs.

### How Hard Will This Be to Learn?

The answer hinges on your goals, but frankly it’s not too rough with this PDF kept close, lending a hand along the way. It bears restating that this Fusion documentation was crafted expressly to take users who’ve never touched Fusion and ground them in the core ideas they need to handle the basics, setting them up to pick up the remainder of the application on their own. Fusion is a deep, production-tested product carrying decades of development, which makes its feature set deep and far-reaching. An hour won’t crack it, yet much of what awaits you won’t stray all that far from other compositing applications you may already know. And should you have gotten comfortable with the node-based grading workflow on the DaVinci Resolve Color page, you’re already partway toward grasping the central operating idea behind compositing in Fusion.
