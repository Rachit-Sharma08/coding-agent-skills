# Resolve FX and open FX

Version: DaVinci Resolve 20.3 Reference Manual. Context: Color page effects.
[Chapter index](INDEX.md) / [Next section](plugin-corrector-and-legacy-fx-nodes.md)
<a id="source-a-node-with-an-open-fx-plugin-mapplied"></a> <a id="source-adding-a-plugin-to-an-existing-corrector-node"></a> <a id="source-applying-resolve-fx-and-open-fx-plugins"></a> <a id="source-browsing-the-effects-library"></a> <a id="source-color-page-effects"></a> <a id="source-color-page-effects-1"></a> <a id="source-effects-library-favorites"></a> <a id="source-open-fx"></a> <a id="source-open-fx-plugins-can-be-processor-intensive"></a> <a id="source-overview"></a> <a id="source-resolve-fx"></a> <a id="source-stars-indicate-a-flagged-favorite-effect"></a> <a id="source-using-open-fx-and-resolve-fx"></a> <a id="source-using-open-fx-and-resolve-fx-1"></a> <a id="source-using-open-fx-and-resolve-fx-2"></a> <a id="source-using-resolve-fx-and-open-fx-in-the-color-page"></a> <a id="source-where-are-ofx-installed"></a>

## Overview

Covers: Color Page Effects; Using Open FX and Resolve FX.

## Color Page Effects

### Color Page Effects

## Using Open FX and Resolve FX

### Using Open FX and Resolve FX

This chapter walks through working with Resolve FX and Open FX plugins. With them you can reach for the filters bundled into DaVinci Resolve, plus filters sold by outside vendors, to build elaborate looks and corrections that the standard palette tools of the Color page simply can't produce on their own.

### Resolve FX

Resolve FX are the plugins bundled directly inside DaVinci Resolve. Their range is broad: everything from blurs and intricate color work, through stylized treatments and lighting looks, to sharpening and repair tasks that would be far too involved to pull off with the Color page's palette controls alone.

An image before/after using the Abstraction Resolve FX filter The majority of Resolve FX plugins are tuned for real-time playback. That tuning lets you drop in demanding effects like Lens Flares, Light Rays, Film Grain, or Warping and tweak them with instant, high-quality feedback, so you can preview each version of a look while you build it rather than sitting through a render or cache pass first. Naturally, performance can drop off if your footage is very high-resolution or raw, if your machine is aging, or if you stack many Resolve FX together at once, which is when you'll want to lean on either the Smart Cache or User Cache.

### Open FX

Open FX (OFX) is an open plugin specification whose purpose is to make it simpler to author cross-platform visual effects plugins that run inside many different host applications. Widely used packages in this space include BorisFX Sapphire and Continuum Complete, Red Giant Universe, and NewBlue TotalFX, each a staple across feature and broadcast pipelines. The catalog of Open FX packages keeps expanding year over year as more developers adopt the standard. Because DaVinci Resolve supports Open FX, plugins let you achieve plenty of stylized results that its native toolset would struggle or fail to deliver. With the appropriate plugin set in hand you can tackle lens flares, optical blurs and prism looks, lens warp correction, film and video grain and damage effects, dead-pixel fixes, and a good deal more.

One of the many Sapphire OFX plugins from GenArts

Each vendor supplies its own installer that takes care of setting up and licensing its Open FX plugins. After that's done, those plugins show up inside the Library of the Open FX panel, which you reveal by clicking the FX button near the upper-right of the Color page or Edit page Interface toolbar.

### Where are OFX Installed?

The OFX specification dictates that every OFX plugin on a given machine lands in one agreed-upon directory, which is what keeps the plugins usable across more than one host application. The directories differ by platform. Under macOS the path is /Library/OFX/Plugins; for a Windows host it becomes C:/Program Files/Common Files/OFX/Plugins; and on a Linux box it resolves to /usr/OFX/Plugins instead.

### Open FX Plugins Can Be Processor Intensive

Given the enormous span of looks they produce, certain third-party Open FX plugins demand a great deal of processing power, and that demand only grows when you pile several of them onto one grade. Should playback start to stutter under an especially costly effect, the Smart Cache can step in and automatically cache the nodes and clips carrying Open FX plugins. After they're fully cached, those clips will replay at full speed, right up until you alter that clip's grade again. To dig deeper into caching and into boosting DaVinci Resolve's overall responsiveness, see Chapter 8, “Improving Performance, Proxies, and the Render Cache.”

### Browsing the Effects Library

Every one of these bundled plugins is sorted into categories near the top of the Effects Library.

Click the Effects button to open the Effects Library Clicking the Effects button slides the Effects panel out from the right edge of the Node Editor to display the Library, shrinking the Viewer, Gallery, and Node Editor to free up space. The arrangement of the Effects Library is hierarchical. A given vendor's plugins sit beneath a header carrying that collection's name, perhaps further split into categories, with Open or Close arrows to the right of each category name that toggle its contents in and out of view so you can keep the tree tight or expanded however you prefer.

To open and close Effects categories, do one of the following:

- Hover the pointer over whichever header you'd like to expand or collapse, then click the Close or Open arrow sitting to the right of the category name.
- Option-click an Open or Close arrow to expand or collapse every header in one go. Because a number of Open FX collections run quite large, you can also reveal an optional Search field at the top of the Library to locate plugins fast by full or partial name.

To locate an Effects filter by name: 1 Click the magnifying-glass button up in the top right corner of the Effects panel. 2 Enter your search text into the Search field that pops up. Just a handful of characters is usually plenty to narrow the list down to only the plugins whose names contain that string.

The Library in the Effects panel showing available effects

### Stars indicate a flagged favorite effect

### Effects Library Favorites

Clicking the far-right edge of any Resolve FX or OFX filter marks it with a star, tagging it as a favorite. Once tagged, picking Favorites from the Effects Library option menu hides everything that isn't a favorite, so the only effects on display are the ones you reach for most. Clicking a star again removes its highlight to “de-favorite” that effect.

### Using Resolve FX and Open FX in the Color Page

What follows is a high-level look at the procedures for handling Open FX plugins inside the Color page. Methods of working with Open FX:

- To add an Open FX plugin to a node: Drag any plugin out of the Open FX Library and drop it on a node. Dropping it on a node that already carries a plugin replaces whatever was there before.
- To remove an Open FX plugin from a node: Two approaches exist for stripping an Open FX plugin off of a node.

Right-click a node that's showing the FX badge and pick Remove OFX Plugin from the menu that appears. Or click the trashcan icon beside the effect's name over in the Effects Inspector.

- To edit the parameters of an Open FX plugin: Pick any node carrying an FX badge, then open the Open FX Panel so the Settings list is displayed. A click on the Library button switches you back to the Library.
- To sample a color parameter within an Open FX plugin: Certain OFX plugins include a color swatch parameter, which surfaces an eyedropper button within the Settings. Click that eyedropper and the pointer becomes an eyedropper you drag to sample whatever is shown in the Viewer.
- To use Open FX onscreen controls in the Viewer: Choose any node bearing an FX badge, and its onscreen controls, assuming it has any, ought to show up in the Viewer. If they don't, confirm the Viewer mode drop-down is set to FX.

### Applying Resolve FX and Open FX Plugins

After locating an Open FX plugin in the Library that you'd like to put to work, two routes are open for bringing it into the Node Editor of the Color page. Your choice between them hinges on the role you intend the plugin to play.

### Adding a Plugin to an Existing Corrector Node

When your goal is to merge an Open FX plugin and a grade inside one node, just drag it and release it onto a fresh corrector node so the plugin's effect attaches there. Any node that has an Open FX plugin on it carries an FX badge down in its lower-left corner.

### A node with an Open FX plugin mapplied

A single node holds only one Open FX plugin at any given moment, yet by chaining several nodes together you can fold as many Open FX plugins into a grade as the shot calls for. Inside a corrector node, Open FX run after Motion Blur and Noise Reduction but ahead of everything else. So you're free to let Motion Blur and Noise Reduction condition the image first, then pass it along to the Open FX plugin. It also follows that whatever other tweaks you perform in that node act on the Open FX plugin's result. That said, the chief payoff of dropping plugins into corrector nodes is that secondary tools, a window, a qualifier, or a key, can confine the plugin's reach in just the same way they'd rein in any other correction made within a corrector node.
