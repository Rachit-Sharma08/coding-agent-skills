# Stereo fixer and stereo width and surround analyzer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereo fixer, Stereo width, Surround analyzer.
[Chapter index](INDEX.md) / [Previous section](noise-phase-pitch-reverb-and-soft-clip-effects.md) / [Next section](vocal-channel.md)
<a id="source-stereo-fixer"></a> <a id="source-stereo-width"></a> <a id="source-surround-analyzer"></a> <a id="source-the-stereo-fixer-fairlight-fx"></a> <a id="source-the-stereo-width-fairlight-fx-in-action"></a>

### Stereo Fixer

A straightforward plugin meant to repair stereo source material — for cases where only one side of a stereo signal got recorded, where the two sides of a stereo recording sit at different levels, or where the Left/Right channels were mistakenly swapped. It can double as a “Mid/Side” decoder for material captured with that microphone technique. This plugin works on stereo clips only.

### The Stereo Fixer Fairlight FX

- Format: Which input processing mode you’ll use to repair the stereo output. Stereo: (Default) Leaves the format untouched, with no conversion. Reverse Stereo: Trades the Left and Right sides. Mono: The plugin puts out a mono blend of its two inputs. Left Only: The left input feeds both the left and right outputs. Right Only: The right input feeds both the left and right outputs. M/S: The left output equals the left (Mid) input minus the right (Side) input; the right output equals the left (Mid) input plus the right (Side) input.
- Left/Right Gain: Lets you set gain separately on the left and right outputs. It is applied after (post) the input processing mode.

TIP: To build a full M/S decoder, just chain a pair of Stereo Fixer plugins. The first unit governs the Side signal level, which in turn governs the width of the second unit (set to M/S).

### Stereo Width

This is an enhancement plugin that broadens or narrows a stereo signal’s spread to widen or tighten the separation between channels. Placed on a Mono channel it switches off, since there is no stereo width there to spread or rein in. A graph renders the chosen width of stereo spread as a purple arc, and within that graph a stereo meter charts the Left and Right spread of the signal. Two audio meters track levels — an Input meter on the left and an Output meter on the right.

### The Stereo Width Fairlight FX in action

Stereo Width has the following controls:

- Width: Governs how wide the stereo output spreads. Values run from 0 (Mono) through 1 (Stereo) to 2 (extra wide stereo).
- Diffusion: Adds more complexity to the output.
- Sparkle: Adds more high frequencies to the spread.

### Surround Analyzer

Rather than the usual bar-graph display, the Surround Analyzer is a graphical meter that paints a spatial picture of the audio it measures. Because its outline keeps shifting with whatever is playing, people sometimes call it the “jellyfish meter.” This style of metering is genuinely helpful: instead of leaning on bars to show where the audio is heading, you get a clear view of how every channel relates to the others.

Here the signal leans toward the right, which reflects how the audio is panned.
