# Sticky note and underlay

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sticky note, Underlay.
[Chapter index](INDEX.md) / [Next section](underlay-flow-organizational-nodes.md)
<a id="source-flow-nodes"></a> <a id="source-flow-nodes-1"></a> <a id="source-flow-nodes-flow-organizational-nodes-fuses"></a> <a id="source-overview"></a> <a id="source-sticky-note-introduction"></a> <a id="source-sticky-note-nte"></a> <a id="source-the-sticky-note"></a> <a id="source-the-underlay"></a> <a id="source-underlay-introduction"></a> <a id="source-underlay-node-structure"></a> <a id="source-underlay-und"></a> <a id="source-usage"></a> <a id="source-usage-1"></a>

## Overview

Covers: Flow Nodes; Flow Organizational Nodes; Fuses.

## Flow Nodes

### Flow Nodes

This chapter walks through the Sticky Note and Underlay capabilities that Fusion offers.

The short code shown beside each feature's name works in the Select Tool dialog while you hunt for tools, and within scripting references as well. Throughout this document, you can read node trees that display MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a note says otherwise.

### Sticky Note [NTE]

### The Sticky Note

### Sticky Note Introduction

A Sticky Note isn't really a node. Rather, it offers a handy way to pin notes, comments, and history onto a particular region of a comp. Adjusting their dimensions and color lets them serve as either understated remarks or prominent warnings, whatever you need. Sticky Notes pair nicely with the Comments tab over in the Inspector.

### Usage

Dropping a Sticky Note into a node tree lets you leave an explanation for collaborators or a note to your future self. To make a Sticky Note, click an open spot in the Node Editor at the place you'd like it to show up. After that, head to the Effects Library and click the Sticky Note effect found under the Tools > Flow category, or press Shift-Spacebar and look up Sticky Note inside the Select Tool window. As with Groups, a fresh Sticky Note arrives compact and collapsed. A double-click opens it up. Once open, you can drag any edge or corner to resize it, or move it about by grabbing the name header. Clicking the icon at the top-left corner collapses the Sticky Note once more. Right-clicking the note brings up a contextual menu from which you can rename it, delete it, copy it, or recolor it. That same menu also lets you lock the note so it can't be changed. Editing the words inside a Sticky Note means first opening it with a double-click anywhere on it, then clicking just under its title bar. As long as the note stays unlocked, its text is yours to edit.

### Underlay [UND]

### The Underlay

### Underlay Introduction

Underlays give you a handy way to lay out regions of a composition visually. Much like Groups, Underlays can make a comp easier to read by carving it into labeled, purpose-driven blocks. Where Groups tidy a comp's appearance by folding intricate layers into single nodes, Underlays draw attention to areas instead of concealing them, and they place no limits on connections reaching in from outside.

### Usage

### Underlay node structure

Just like Sticky Notes, you bring an Underlay into a comp either by picking it out of the Flow category within the Effects Library or by looking it up in the Select Tool window. The Underlay lands in the Node Editor with its title bar centered over wherever you last clicked. You can resize Underlays by dragging any edge or corner, and doing so leaves the nodes untouched. Underlays can double as straightforward selection groups too. Clicking an Underlay's title activates it and grabs every tool sitting entirely inside it, so the whole bunch can be moved, duplicated, routed through, and the like. Renaming an Underlay starts with making sure none of the nodes inside it are selected. After that, Option-click the Underlay title to grab the Underlay on its own without grabbing the nodes it holds. With it selected, right-click the title and pick Rename. The very same right-click contextual menu lets you give an Underlay a color.
