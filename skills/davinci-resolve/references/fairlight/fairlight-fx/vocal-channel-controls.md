# Vocal channel controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vocal channel.
[Chapter index](INDEX.md) / [Previous section](vocal-channel.md) / [Vocal Channel](vocal-channel.md)
<a id="source-the-vocal-channel-fairlight-fx"></a>

### The Vocal Channel Fairlight FX

Vocal Channel has the following controls:

- High Pass: A toggle switches it on, and it stays off until you do so. A lone frequency knob marks the cutoff under which frequencies get rolled off to tame rumble or boominess.
- EQ: A toggle-activated, three-band EQ that tunes the assorted frequencies of a voice, spanning the Low, Mid, and High bands, each one carrying its own Mode plus Frequency and Gain controls Low/Mid/Hi Mode: Hands you a choice of filtering shapes for zeroing in on the frequency span you mean to tweak. Each band offers its own set of choices. Low/Mid/Hi Freq (Hz): Picks the center frequency you want to act on. Low/Mid/Hi Gain (dB): Raises or lowers the chosen frequencies.
- Compressor: Threshold (dB): Marks the signal level beneath which no compression kicks in. Defaults to -25dB. The range is from -40 to 0dB. Reaction: Governs how rapidly compression takes hold once a signal climbs past the threshold. The default is 0.10. Ratio: Tunes the compression ratio. It fixes the input-to-output gain reduction ratio imposed on whatever signal climbs past that threshold level. By default it sits at 1.5:1. Its span runs from 1.1 to 7.0. Gain (dB): Use this to nudge the output gain upward and make up for any level lost while compressing, should that be needed.
