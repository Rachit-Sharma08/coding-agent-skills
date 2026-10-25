# Ducking music voice and audio chain effects

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ducker, Music remixer studio version only, Voice isolation studio version only, Ambisonics meter, Chain FX.
[Chapter index](INDEX.md) / [Previous section](dialogue-leveler-and-dialogue-separator-and-ducker.md) / [Next section](chain-fx-and-chorus.md) / [Ducker](dialogue-leveler-and-dialogue-separator-and-ducker.md)
<a id="source-adding-ducker-input-sources-in-the-inspector"></a> <a id="source-adding-input-sources-via-the-inspector"></a> <a id="source-ambisonics-meter"></a> <a id="source-ambisonics-meter---power-map-view"></a> <a id="source-ambisonics-meter---sonar-view"></a> <a id="source-chain-fx"></a> <a id="source-ducker-controls"></a> <a id="source-ducker-graph-display"></a> <a id="source-insert-effects"></a> <a id="source-music-remixer-studio-version-only"></a> <a id="source-the-ducker-plugin"></a> <a id="source-the-music-remixer-plugin"></a> <a id="source-the-voice-isolation-plugin"></a> <a id="source-using-the-ducker"></a> <a id="source-voice-isolation-studio-version-only"></a>

### The Ducker plugin

### Using the Ducker

Picking up the examples above: 1 Pick the target track you mean to attenuate (the Freeway Traffic track) and open the Ducker. 2 Open the Source dropdown and set Dialogue 1 as the input source.

- For extra input sources, Command-click the remaining track names — here that means Dialogue2 and Dialogue3.
- Run a portion of your sequence and tune the duck level along with the other controls to taste.

### Adding Input Sources via the Inspector

Should you rather stay inside the Inspector: 1 Pick the Freeway Traffic track, confirm the Ducker is on, and open the Inspector’s Audio tab. 2 Hit the plus sign beside the Source 1 dropdown that holds Dialogue 1 to spawn a dropdown for Source 2, and pick Dialogue2 off the list. 3 Hit the plus sign beside the Source 2 dropdown to spawn a dropdown for Source 3, and pick Dialogue3 off the list.

### Adding Ducker input sources in the Inspector

### Ducker Controls

- Duck Amount: This sets how much the target track’s level drops, measured in dB, with a default value of 2.7 dB. As a rule, somewhere between 2.0 dB and 5.0 dB sounds best.
- Lookahead: Sets the lookahead time in milliseconds, defaulting to 15ms. Lookahead lets the Ducker begin pulling the destination track down before the source track even becomes audible. Raise the value and the Ducker “pre-anticipates” the source track more. If you want the sound to start dropping before a line of dialogue or VO arrives, try higher values, though the default usually does the trick.
- Rise Time: This fixes how many milliseconds the Ducker takes to hit the reduction set by the Duck Amount. By default it is 10 milliseconds, fine for most cases. Longer Rise Times can help when Duck Amount values run high and the source track has wider gaps.
- Hold: This parameter governs how long the target signal stays attenuated. Its default is 150ms.
- Recovery Time: This figure tells how fast the target signal climbs back to its prior level

once attenuation lifts. The default sits at 750ms, but a well-chosen Recovery time is key to ducking that sounds natural, so test a range of values to land on the best.

### Ducker Graph Display

In this area a gray line stands for the incoming signal, set against the Ducker’s action drawn in yellow. Wherever the yellow line dips, the target track is being attenuated according to the Duck Amount working together with the other parameters.

### Music Remixer (Studio Version Only)

Built on DaVinci Neural Engine AI, this plugin pulls music apart into separate stems — Vocals, Drums, Bass, Guitar, and “Other” (“everything else”) — so you can rebalance or remix the track to creative ends. The level controls let you set each stem’s volume, while the Mute buttons drop stems out or fold them back into your mix. You might, for instance, want to strip out or lower a vocal that fights with a featured piece of dialogue.

### The Music Remixer plugin

### Voice Isolation (Studio Version Only)

Powered by an AI model schooled on every sort of human voice — male or female, young or old — Voice Isolation lets you strip loud, unwanted sounds out of existing voice recordings entirely, and to striking effect.

### The Voice Isolation plugin

All manner of background noise can be cleared away — air conditioners and fans, jackhammers, the din of a restaurant, music sounding under a featured piece of dialogue, and beyond.

The Amount control balances the blend of the original source against the isolated voice. Set it to 50 and the two sit at roughly equal weight. Settings from 70 to 80 tend to give natural results while still isolating the source hard. Voice Isolation will run on an audio track in real time, but not on live audio input; it accepts any mono, stereo, or dual-mono audio track, though tracks of more than two channels lie outside what it supports.

### Insert Effects

### Ambisonics Meter

Drop this Fairlight FX plugin onto an Ambisonics track or bus and it paints a graphic picture of your Ambisonic sound field. A click on the three dots at the upper right opens an options menu where you choose your metering style — either “power” (Power Map) or “Sonar.” Whichever you pick, the meter conveys how intense the sound is and where it currently sits in the Viewer.

### Ambisonics meter - Power Map view

### Ambisonics meter - Sonar view

### Chain FX

With Fairlight Chain FX you can string together as many as six Fairlight FX, or compatible Audio Units or VST effects plugins, and steer the whole lot from one control.
