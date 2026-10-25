# Burn away transition and adjust timing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using transitions.
[Chapter index](INDEX.md) / [Previous section](wipe-and-user-transitions.md)
<a id="source-adjust-timing"></a> <a id="source-appearance"></a> <a id="source-audio-transitions"></a> <a id="source-burn-away-transition"></a> <a id="source-dctl-transition"></a> <a id="source-edge"></a> <a id="source-openfx-transitions"></a> <a id="source-openfx-transitions-in-the-effects-library"></a>

### Burn Away Transition

This transition mimics the look of a film print catching fire inside the projector. Reach for it when you want a vintage retro feel, or simply to put dread into projectionists the world over.

The Burn Away transition, with two pirates fretting over what’s become of their release print The Burn Away effect carries these parameters: Progression This cluster of controls shapes the kind of movement the burn makes on its way across the frame.

- Motion: Lets you choose a flavor of burning effect, each choice opening up its own parameters. Directional: The burn travels in a straight line from one frame edge to the opposite one. This setting mimics film being dragged off and burned by the take-up reel. Under this mode, the Viewer’s OFX overlay lets you set the direction. Hotspots: The burn bursts out from one or several central points. This setting mimics film stalling before a projector bulb and melting away. Under this mode, the Viewer’s OFX overlay lets you drag the burn points around right in the Viewer. Path: Lays out a curved track the burn keeps to. This setting lets you pin down the burn direction exactly, so you can decide which elements in the frame burn first. Under this mode, the Viewer’s OFX overlay lets you drop points onto a spline to draw whatever curved motion path you’d like the effect to take.
- Angle: (Directional Only) The line the burn travels along. This can also be reset straight in the Viewer while in Open FX Overlay mode.
- Number of Hotspots: (Hotspots Only) How many points the burn bursts out from. Its possible values run from 1 to 8.
- Randomize Hotspots: (Hotspots Only) Scatters the hotspots randomly across the frame.
- Number of Points: (Path Only) How many points the onscreen curve control carries. The range runs

from 2 to 5. These points can be handled straight in the Viewer while in Open FX Overlay mode.

### Adjust Timing

This group of parameters hands you control over where the burn’s progression begins and ends.

- Adjust Start: Sets at what point in the transition the effect kicks in. Values are from -1.000 to 1.000.
- Adjust End: Sets at what point in the transition the effect wraps up. Values are from 0.000 to 2.000.

### Edge

These controls let you shape what the film’s burning edge looks like.

- Raggedness: How jagged the burn’s edge turns out. Values are from 0.000 (perfectly flat) to 1.000 (extremely rough).
- Scale: How large that raggedness is scaled. Values are from 1.00 to 10.00.

### Appearance

These controls tune the burn’s look and color as it works its way through the transition.

- Melt: Drives how much the image distorts while it burns away. Values are from 0.000 to 1.000.
- Char: Drives how much darkened charring forms along the edge. Values are from 0.000 to 1.000.
- Char Color: Lets you pick what color the Char effect takes.
- Burn: Lets you dial in how thick the burn effect runs. Values are from 0.000 (no burn)

to 1.000 (maximum thickness).

- Burn Hue: Lets you pick the hue the Burn effect takes.
- Burn Sat: Lets you pick how intense the Burn effect’s color is.
- Burn Brightness: Lets you dial in the Burn effect’s brightness. At the low end, the burning edge

takes on a mottled, uneven look. Values are from 0.000 to 1.000.

- Glow Brightness: Lets you drive how strong a glow effect radiates off the Burn effect.

Values are from 0.000 to 2.000.

- Glow Spread: Lets you drive how wide the glow effect reaches. Values are from 0.000 to 2.000.
- Ash: Drives how much ash drags along behind the burn as it crosses the frame.

Values are from 0.000 to 1.000.

- Ash Color: What color the Ash parameter takes.

### DCTL Transition

Transitions built on DCTL (DaVinci Color Transform Language) now work in DaVinci Resolve. For the finer points, consult the DaVinci Resolve Developer Documentation reachable from the help menu.

### Audio Transitions

One lone audio transition covers every crossfade you’ll need. Cross Fade +3/–3/0 dB: An audio-only transition for fading between two audio clips. Its three separate crossfades let you pick how forceful the actual move from one level to the next is.

### OpenFX Transitions

Once one or more OpenFX plugin sets are installed on your DaVinci Resolve workstation, whatever transitions those sets carry show up in the Effects Library’s OpenFX panel.

### OpenFX transitions in the Effects Library
