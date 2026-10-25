# Checking and fixing your results and clean up video tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Modifying clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](audio-channel-pasting-and-auto-alignment.md)
<a id="source-checking-and-fixing-your-results"></a> <a id="source-clean-up-video-tracks"></a>

### Checking and Fixing Your Results

Should the Neural Engine get something wrong, you’re able to correct it by hand: move to the cut with the Up and Down Arrow keys to step through the Timeline, then do one of these:

- To remove a Cut: Select the through edit by clicking it, then hit the “Delete” key.
- To make a New Cut: Set the timeline indicator on the cut point, then choose Timeline >

Split Clips (Command-\).

One clip of a completed edit, made up of several cuts, shown prior to the Detect Scene Cuts command

Several separate clips pulled out of the edited clip with Detect Scene Cut; the In and Out points kept the operation bounded, and one of the through edits that resulted shows up highlighted in green.

### Clean Up Video Tracks

Being able to cut overlapping clips across several video tracks to test slipping clips around, or to stack a few takes or versions of a VFX clip, is handy — yet eventually all those surplus clips wear on the visual order of your timeline, and on your colorist’s sanity. That’s why a trio of commands for tidying your timeline now sits in the Timeline> Video> Clean Up Video Tracks menu. They are:

- Flatten Unused Clips: Every superimposed clip whose In and Out points line up with the clips beneath it drops down to track V1, provided no opacity, composite mode, transition, or fade effect on it turns it into a compositing effect.
- Disable Unused Clips: Every clip sitting under superimposed clips that bear no opacity, composite mode, transition, or fade effect gets disabled.
- Change Unused Clips Color: Every clip sitting under superimposed clips that bear no opacity, composite mode, transition, or fade effect has its color switched to whatever you pick.

(Top) The starting timeline, (Bottom) The Flatten Unused Clips command at work, dropping superimposed clips whose In and Out points match the clips beneath them down to track V1 so the Timeline is tidier for later work
