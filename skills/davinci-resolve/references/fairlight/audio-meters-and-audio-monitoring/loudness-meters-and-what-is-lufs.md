# Loudness meters and what is lufs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Audio meters and audio monitoring.
[Chapter index](INDEX.md) / [Previous section](meter-plugin-and-surround-analyzer.md) / [Next section](visualizing-loudness-monitoring-and-metering-options.md)
<a id="source-absolute-scales-and-dialog"></a> <a id="source-graphical-loudness-meters"></a> <a id="source-loudness-meter-options"></a> <a id="source-loudness-meters"></a> <a id="source-numeric-loudness-meters"></a> <a id="source-offline-loudness-analyzer"></a> <a id="source-support-for-multiple-loudness-standards"></a> <a id="source-using-the-loudness-meters"></a> <a id="source-what-is-lufs"></a>

### Loudness Meters

Furthest to the right lie the Loudness meters, a pairing of two graphical meters with a numerical readout. They let you stay on top of the overall mix’s “integrated loudness,” the very measure every present-day mixing specification cites when it lays out client deliverables. Where the RMS audio meters in the Timeline or Mixer gauge audio in dB, the Loudness meters carry out a different sort of analysis, expressed in LUFS (loudness units relative to full scale).

### What Is LUFS?

A LUFS measurement weighs sound levels averaged across time and pegged to full scale. Full scale marks the loudest point a digital audio system can take before it overloads (“clipping”). Because LUFS lets wildly different sorts of program material line up in how loud they seem to human ears, it has grown into the usual yardstick for measuring mixes when program material ships for final delivery. LUFS read out as negative figures, -23, -14, and the like, since the level is pegged to full scale (digital 0).

### Loudness Meter Options

Within the General Options of the Project Settings, a pair of options let you tailor the Loudness meters.

- Target Loudness level: Lets you fix the LUFS value that serves as the reference point for loudness metering. It defaults to –23 LUFS, which handily makes these meters scale much like the traditional audio meters you already know.
- Loudness Scale: Lets you settle on which scale the meters are read against. The choices at present are the default EBU +9 Scale (–18 to +9) and the EBU +18 Scale (–36 to +18).

### Support for Multiple Loudness Standards

You can flip the Loudness Meter between a range of international, industry-standard loudness monitoring standards. Whichever standard you settle on draws on the integrated loudness value (together with a tolerance that each chosen standard spells out) to signal whether the present mix level counts as acceptably loud, doing so by color-coding the Integrated Loudness value and within the Integrated Loudness graph laid out below. Blue marks loudness levels sitting under tolerance, yellow marks those that fall within tolerance, and red marks those running over tolerance.

The built-in standards open to you cover these: BS.1770-1: A somewhat dated loudness standard that DaVinci Resolve version 15 and earlier relied on. BS.1770-4: The freshest loudness standard once DaVinci Resolve 16 arrived; its specified algorithms underpin the rest of the standards further down this dropdown menu. ATSC A/85: America’s benchmark for permissible broadcast loudness. EBU R128: Europe’s benchmark for permissible broadcast loudness. OP-59: The New Zealand and Australian benchmark for permissible broadcast loudness. TR-B32: Japan’s benchmark for permissible broadcast loudness. AGCOM 219: Italy’s benchmark for permissible broadcast loudness. NETFLIX: Netflix’s own benchmark for permissible broadcast loudness. YouTube: YouTube’s own benchmark for permissible broadcast loudness. Disney 2.0: The Disney 2.0 benchmark for permissible broadcast loudness. Disney 5.1: The Disney 5.1 benchmark for permissible broadcast loudness. Every one of these loudness standards can be used for off-line readings too, by way of the Loudness Analyzer laid out in the section that follows.

NOTE: For gauging the maximum “true peak,” the target peak meter has switched to the BS.1770-4 standard, which means it can now register “inter-sample peaks” instead of catching only the peaks landing at each waveform sample.

### Graphical Loudness Meters

Two distinct meters hand you a live graphical read on the loudness of whichever bus you’re monitoring, judged against the loudness standard you’ve picked, which sets how the subjective loudness of a given audio mix is analyzed so it meets the broadcast quality control (QC) standards demanded of it.

- A steel-blue meter marked M (for momentary) carries as many channels as the bus you’re monitoring, leaving out the LFE channel(s) of surround formats, which loudness metering doesn’t reckon with. It gauges LEQ (equivalent sound level) inside a 400ms window trailing the playhead, sampled every 100ms. That lets you read the mix’s LUFS (Loudness Units Full Scale) level at the current frame as it plays. This per-channel analysis feeds the calculation of every other value the loudness metering system reports.
- A second steel-blue mono meter on the right shows the combined level of all channels in the M meter, given in LU (loudness units). The figure at the top of this meter is the highest LU value caught across any span of timeline playback. It stays put until reset, which happens either by halting and starting playback again while Link to Playhead is on, or by clicking the Reset button down at the foot of the loudness meter area.

### Numeric Loudness Meters

Off to the right of the meters, a group of values keep up a running account of your mix’s audio level. Handy as the graphical meters are for studying your mix while you work, these numeric readouts earn their keep by supplying the exact figures you need to meet written QC standards. Here’s what each one means:

- Short: Gauges the average LU level across a 30-second window trailing the playhead.
- Short Max: Reports the peak level over that same 30-second window. EBU R128 calls

for this analysis.

- Range: Gauges the dynamic range of your mix’s Loudness (in LU, or loudness units), namely

the gap between the average soft and average loud portions of your mix. It weighs the overall loudness across a played stretch of the mix, sets aside the bottom 10% and top 5%, then puts out a standardized figure for the gap between the soft and loud levels that remain. Its window of analysis runs for however long you’ve been playing. Most QC specifications call for this analysis.

- Integrated: Gauges the LUFS value across the slice of the mix you’ve played through. This integrated figure builds up as playback continues. Most QC specifications call for this analysis.

### Absolute Scales and Dialog

Some people like to read their levels against a relative scale anchored at “0,” the way a VU meter’s needle rides above the “0,” while others would rather see the amplitude’s absolute figure in LUFS and true peak. The Loudness meter starts out on relative scale, yet you can now toggle the Loudness meter between relative scale and absolute scale. Relative scale in the Loudness menu is reckoned against the chosen scale, so a loudness unit of 0 lines up with the target of whatever measure type you’ve selected. Take EBU R128, whose target measure is -23dB LUFS: there the “0” LU (Loudness Unit) equals -23dB. Choose ATSC A/85 instead — its target is -24dB — and that value becomes the equivalent of the relative LU of 0. Switch to absolute scale and the Loudness meter lays out its increments to mirror the chosen measure type. On absolute scale, the EBU R128 meter reads -23 in place of the 0 you’d see on relative scale.

The option over in the Loudness panel surfaces the assorted measure types along with the choice for absolute scale.

### Using the Loudness Meters

When you put the Loudness meters to work on a structured analysis of your mix to check QC adherence, a cluster of controls lets you mark out where the analysis starts and stops.

- Lock Metering to Transport: You’ll find this setting in the compound meter option menu. With it on, every loudness metering analysis resets on its own each time you carry the playhead somewhere else on the Timeline. It comes in handy while you’re spot-checking various parts of your mix, or focused on one scene. Leave this option off when you’d rather the measurement of playback up to that point on the Timeline stayed in place.
- Absolute Scale: An absolute reading of the chosen scale type.
- Pause and Reset buttons: During a formal analysis of your mix, the Reset button

clears out all the analyses gathered so far, while the Start button kicks off the build-up of loudness values. Need to halt playback for a moment to handle something else? Click Pause, then click Resume once you’re set to pick the analysis back up.

### Offline Loudness Analyzer

You can also examine an audio file’s loudness offline. It’s a quick route to measuring loudness within imported audio files or bounced mixes. To kick off offline loudness analysis:

- Right-click the file on the Timeline and pick Analyze Audio Level from the contextual menu. A dialog box then lays out the measurement options on offer.

Every measurement the real-time loudness meter offers is reachable through the dropdown menu inside the Analyze Audio Level panel. Pick an analyzer mode and that mode’s target measurements appear beside the reading in parentheses. Click the analyze button and the results land in the panel next to the chosen mode’s target measurement values.

Pick the audio file, choose the analyzer mode you want, EBU R128 in this instance, and click analyze.
