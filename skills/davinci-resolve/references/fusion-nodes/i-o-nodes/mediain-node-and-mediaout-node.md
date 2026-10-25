# Mediain node and mediaout node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mediain node, Mediaout node.
[Chapter index](INDEX.md) / [Previous section](mediain-node-image-tab.md) / [Next section](mediaout-node-and-saver-node.md) / [MediaIn Node MI](mediain-node-image-tab.md)
<a id="source-audio-tab"></a> <a id="source-audio-with-media-pool-clips"></a> <a id="source-basic-node-setup"></a> <a id="source-color-effects"></a> <a id="source-edit-page-plugins"></a> <a id="source-fusion-effects"></a> <a id="source-inputs"></a> <a id="source-mediaout-node-introduction"></a> <a id="source-mediaout-node-mo"></a> <a id="source-purging-the-audio-cache"></a> <a id="source-the-mediaout-node"></a>

### Audio Tab

An Audio tab lives in the Inspector for the MediaIn node, where you can opt to solo the clip’s audio or listen to every audio track on the Timeline.

What the Audio tab on the MediaIn node does is let you pick the track to play back, slip the audio timing, and reset the audio cache.

Should the audio drift out of sync while playing back in Fusion, the Sound Offset wheel on the Audio tab lets you slip the audio in subframe frame increments. That slipped audio changes only on the Fusion page. Every other page keeps the original audio placement.

### Audio with Media Pool Clips

By default, audio from a clip pulled in via the Media Pool stays muted. Getting that Media Pool clip’s audio to play takes two steps. To listen to audio from a clip pulled in via the Media Pool, go through the following: 1 Pick the clip in the Node Editor. 2 Within the Inspector, open the Audio tab and pick the clip name off the Audio Track drop-down menu. With more than one MediaIn node in the comp, what plays is the audio most recently picked in the Inspector. The Speaker icon in the toolbar lets you flip among the MediaIn node audio files. 3 Right-click that Speaker icon in the toolbar, then pick the MediaIn for whichever clip you want to listen to.

### Purging the Audio Cache

For quicker performance, the audio and its settings get cached. Change which audio tracks you want playing back in Fusion, or reach for the Sound Offset wheel to slip the audio tracks, and you’ll need to purge the audio cache. Likewise, head back to the Edit, Cut, or Fairlight page and tweak the audio levels, and the audio cache needs purging. To purge the audio cache following any audio playback change:

- Hit the Purge Audio Cache button in the Inspector.

Next time you play the composition back, the audio will be brought up to date.

### MediaOut Node [MO]

### The MediaOut node

NOTE: Only in DaVinci Resolve is the MediaOut node available.

### MediaOut Node Introduction

A MediaOut node has to be part of every composition you build on DaVinci Resolve’s Fusion page. What the MediaOut node does is send the finished output, on DaVinci Resolve’s Edit or Cut page, back to your Timeline. Most of the time it stands in for the Saver node that Fusion Studio uses when exporting clips.

Whatever the Fusion page’s MediaOut node outputs gets carried through by way of the Color page’s source inputs — the one exception being that, if you’ve applied transforms or plugins to that clip on the Edit or Cut page, the handoff running from the Fusion page over to the Color page goes like this:

### Fusion Effects

### Edit Page Plugins

### Color Effects

Where Resolve Color Management or ACES is in play, each MediaOut node turns the output image back into the Timeline color space before the handoff to the Color page.

NOTE: From the Effects Library, extra MediaOut nodes can be dropped into the Node Editor. Those extra MediaOut nodes serve to pass mattes over to the Color page.

### Inputs

The MediaOut node’s lone input is where you wire up the finished composite image you’d like rendered back to the Edit page. Input: That orange input is a required one. Any 2D image you want rendered back to the Edit page is what it accepts.

### Basic Node Setup

A single comp can hold several MediaOut nodes. It’s always the first MediaOut node that renders the image back to the Edit page Timeline. To pass mattes over to the Color page, you can put extra MediaOut nodes to work.

Here the MediaOut1 node renders to the Edit page while MediaOut2 passes mattes over to the Color page
