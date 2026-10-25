# Group menu on a mixer channel strip and audio effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio overview.
[Chapter index](INDEX.md) / [Previous section](group-management-via-mixer-channel-strips-overview.md) / [Next section](applying-plugins-and-editing-plugin-parameters.md)
<a id="source-about-audio-plugins"></a> <a id="source-audio-effects"></a> <a id="source-audio-effects-1"></a> <a id="source-audio-plugins-in-the-effects-library"></a> <a id="source-audio-units"></a> <a id="source-clearing-timing-points"></a> <a id="source-elastic-view"></a> <a id="source-elastic-wave-audio-retiming"></a> <a id="source-elastic-wave-disabled"></a> <a id="source-elastic-wave-options"></a> <a id="source-elastic-wave-time-points"></a> <a id="source-fairlight-fx"></a> <a id="source-group-menu-on-a-mixer-channel-strip"></a> <a id="source-using-audio-plugins"></a> <a id="source-vst-and-vsti"></a>

### Group menu on a Mixer channel strip

## Audio Effects

### Audio Effects

DaVinci Resolve ships with Fairlight FX audio plugins and supports compatible third-party VST and Audio Unit plugins for the Edit and Fairlight pages, letting you layer effects such as echo, reverb, noise reduction, and aural enhancement onto audio clips, tracks, and busses. This chapter walks through various ways of putting these effects on clips and tracks.

### Elastic Wave Audio Retiming

Elastic Wave retiming is a quick, simple, keyframe-based approach to dynamically retiming audio, squashing and stretching different stretches of a waveform to subtly retime audio playback for all sorts of reasons, all while pitch stays constant. For instance, if you're swapping in the audio of one take for the current take, but the performer's timing runs a touch different, Elastic Audio lets you make small tweaks to retime the second performance against the first. Putting Elastic Wave retiming to work on an audio clip: 1 Here, two tracks of foley effects have been laid down, and the lower one has to be retimed so it lines up with the upper one. 2 Right-click an audio clip, then pick Elastic Wave retiming off the contextual menu to bring up the Elastic Wave retiming controls. Switching Elastic Wave on 3 Command-click any point on the clip to drop speed keyframes onto the waveform sections you'd like retimed by stretching or squishing. Speed keyframes can also be placed to pin down waveform sections you'd rather leave untouched.

Dropping a speed keyframe while Elastic Wave retiming is on 4 Drag the speed keyframe to the left or the right and the audio speeds up on one side of the keyframe while it slows on the other, reaching from that keyframe out toward the adjacent keyframes on the clip. With an audio clip's waveform to guide you, several speed keyframes let you align one performance's waveform against another's so their timing matches. Alternatively, shift speed keyframes at will to warp performances or sounds for creative effect. In the same vein, dragging an audio clip's start or end retimes that stretch of the clip forward or back as far as the next speed keyframe you've placed.

Tuning a run of speed keyframes so one performance matches another

5 If you've made a handful of speed keyframe tweaks but find yourself wishing one you created sat somewhere else relative to the audio waveform being adjusted, hold down the Command key and drag any speed keyframe to move it toward or away from the part of the waveform it should retime. Doing so fine-tunes the audio retiming taking place at that point in the clip.

(Left) The state before a speed keyframe is Command-dragged nearer the original start of the retimed sound, (Right) the state afterward 6 Once finished, click the close button up in the top-left corner to hide the Elastic Wave retiming controls. To clear Elastic Wave retiming keyframes, take one of these routes:

- To clear one speed keyframe: Right-click a speed keyframe and pick Remove Speed Keyframe out of the contextual menu.
- To clear every speed keyframe and wipe out the Elastic Wave retiming effect: Right-click a clip and pick Reset Speed Curve.

NOTE: Every Elastic Wave retiming tweak you make on the Fairlight page surfaces on the Edit page as variable speed effects, reachable through the Retime controls. Bear in mind that although any Elastic Wave retiming effect can show up as an Edit page retime effect, the reverse isn't true—not every Edit page retime effect translates into an Elastic Wave retiming effect back on the Fairlight page.

### Elastic Wave Options

The Elastic Wave context menu carries three processing options:

- Off: Elastic Wave is not enabled for the clip (Default).
- Voice: Geared toward human speech or singing. Bear in mind it's a poor fit for any other material.
- General Purpose: Ideal for music and effects.

### Elastic View

Elastic view reveals Elastic Wave “time points,” which resemble Resolve keyframes but aren't quite the same. Keyframes stand for a point in time together with a value, whereas Elastic Wave time points stand for only a point in time.

With Elastic View on, time points become visible on the selected clip.

### Elastic Wave time points

### Elastic Wave disabled

When it's off, the time points stay hidden, yet the info lane still flags that Elastic Wave is on with the Elastic Wave icon.

### Clearing Timing Points

“Timing points” are the movable Elastic Wave control points that stretch or squeeze a particular region of a clip. Choosing “Clear Timing Points” wipes out (deletes) every selected point inside a clip. Elastic Wave is able to operate in the Edit window, where video editors might want spoken word performances re-timed so that, as the audio shifts, the video follows that retiming to stay in sync. On the Fairlight page, by contrast, video re-timing is turned off so you retain independent control over the audio file.

### About Audio Plugins

When in FlexBus mode, there's no cap on how many single or multiple plugins you can apply to clips and tracks. There is, however, a ceiling of 480 under Fixed Bus Legacy. You reach plugins through each track's control strip, or through the Inspector, which opens the door to both clip and track plugins.

### Fairlight FX

Fairlight FX are proprietary DaVinci Resolve-specific plugins running natively on macOS, Windows, and Linux, delivering high-quality audio effects with professional features to every DaVinci Resolve user on every platform. Most Fairlight FX plugins—Channel Dynamics and EQ included, along with dynamics processors such as the Multiband Compressor, Limiter, Reverb, and Ambisonics Meter—run Ambisonics native and deliver multichannel processing.

### VST and VSTi

VST (Virtual Studio Technology) is an audio plugin standard that Steinberg created. The VST standard opens the door for third-party developers to build plugins usable inside VST host applications, or to build VST host applications themselves. The Fairlight page handles VST effects from Mono right up to 7.1 and beyond. You can insert these effects on mono channels or Link Groups, and compatible VST Ambisonic effects work on Ambisonic tracks or busses.

Drop a stereo VST effect onto an LCR, LCRS, or 5.1 Link Group, and the left plus right channels are routed on their own to the Link Group's left and right channels. DaVinci Resolve supports VST3. VST effects are at your disposal on macOS and Windows workstations, yet Linux misses out. VST Effects versus VST Instruments (VSTi) A VST effect is one type of VST plugin built to process audio. Such an effect might take the form of a Reverb, Compressor, or EQ. VST Instruments, on the other hand, typically generate sound or replay sampled audio. VSTs have quickly displaced hardware synthesizers and dedicated samplers thanks to their flexibility, repeatability, and low cost.

### Audio Units

Audio Units is an audio plugin API that Apple created for macOS workstations. As with VST, Audio Units (AU) can either process audio or operate as instruments. Compatible AU Ambisonic effects work on Ambisonic tracks or busses.

### Using Audio Plugins

Fairlight FX come pre-installed with every DaVinci Resolve installation. Install extra VST or Audio Unit effects on your workstation and they show up in the Audio FX panel of the Effects Library, sorted into separate categories.

### Audio plugins in the Effects Library

A click at the far right of any effect tags it with a star as a favorite effect. Do that and the favorited effects collect into their own Favorites area down at the foot of the Effects Library Bin list, while they also surface up top in the Effects button's menu on the Mixer whenever you click the “plus” button.

Stars mark a flagged favorite effect; right now every favorite is filtered Audio plugins let you drop effects onto single audio clips or an entire track's worth of audio—to layer on creative qualities like echo or reverb, or to tackle mastering tasks via noise reduction, compression, or EQ.
