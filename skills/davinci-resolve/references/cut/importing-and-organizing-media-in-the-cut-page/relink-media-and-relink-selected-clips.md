# Relink media and relink selected clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Importing and organizing media in the cut page.
[Chapter index](INDEX.md) / [Previous section](relinking-media.md) / [Next section](voiceover-settings-and-script-settings.md)
<a id="source-relink-media"></a> <a id="source-relink-selected-clips"></a> <a id="source-the-built-in-prompter-in-the-voiceover-tool"></a> <a id="source-the-voiceover-icon-red-opens-the-voiceover-toolset"></a> <a id="source-using-the-prompter"></a> <a id="source-using-voiceover-on-the-cut-page"></a> <a id="source-voiceover-settings"></a> <a id="source-voiceover-tool"></a>

### Relink Media

Whenever DaVinci Resolve can’t locate your media, a Relink Media icon turns orange within the Media Pools of both the Cut page and the Edit page.

The Relink Media icon that appears for unlinked media Click this icon and a dialog box opens listing the volumes the missing files first lived on. With that detail in hand, you can hunt the media down on your file system, locate the particular hard drive, or check with a client about whether they handed you the media off this volume. Hitting the Locate button reconnects the missing clips to whatever new file location you point it at. Should the quick search the Locate buttons kick off fail to turn up media you’re sure is present, you can launch a thorough deep disk search for it by clicking the Disk Search button.

The Relink Media dialog listing the volume names that the missing clips came from

### Relink Selected Clips

Aptly titled, the “Relink selected clips” command is the most adaptable way to relink your project’s clips against clips in any directory you pick, leaning on file name and timecode as the main means of reestablishing the tie between each clip and the media file matching it on disk. Here is how to relink selected clips, or the clips inside a selected bin: 1 Do one of the following:

- Within the Media Pool browser, pick one or more clips for relinking; then, right-clicking either one of those selected clips or the selected bin, choose “Relink Selected Clips” from the contextual menu.
- From the Media Pool bin drop-down menu, pick a bin whose clips you want relinked; then, right-clicking that selected bin, choose “Relink Clips for Selected Bin” from the contextual menu.

2 Once the Relink File dialog opens, pick a volume and directory to search for the files you’re relinking to, then click OK. DaVinci Resolve sets out to locate every clip whose file name matches inside the subdirectories of the directory you picked, and to keep this fast it relies on the original file paths of the clips being relinked. Because it checks the directories the clips first came from to begin with, relinking can go pretty quickly. 3 Should any clips not turn up via the approach in step 2, a second dialog gives you the chance to run a “deep search.” Click Yes and DaVinci Resolve hunts for each clip within every subdirectory of the directory you picked back in step 2. That can take a good deal longer, yet it ought to succeed completely as long as the media you need sits somewhere inside the chosen directory structure. 4 Should there still be other clips that couldn’t be found, you’re given the choice of pointing at a different directory to keep searching, or quitting.

### Voiceover Tool

Built into the Cut page of DaVinci Resolve is a purpose-made voiceover and teleprompter interface you reach right in the Viewer by clicking the Voiceover icon. With the Voiceover tool, laying down precisely timed scripts straight into the Cut page timeline is easy. You can even bring in Voice Isolation and the Dialog Leveler as you go for strong results, even when the microphones and recording surroundings are subpar.

### The Voiceover icon (red) opens the Voiceover toolset

Laying down a VO audio track straight onto the Cut Page timeline by way of the Voiceover tool

### Using Voiceover on the Cut Page

At the simplest level, a recording can be “punched in” with nothing more than a microphone and an In point, though the Voiceover tool carries plenty of features that make the whole thing more exact and repeatable, teleprompter support and AI-based audio tools among them. What follows is a sample setup that gets the most out of the Voiceover features on the Cut page. 1 Hook an external microphone and headphones up to your computer, then prepare a plain text (.txt) script for the VO. 2 Hit the Voiceover tool icon in the Viewer. 3 Within the Voiceover settings, choose your microphone interface. 4 Choose the Audio Track you’d like the voiceover clip recorded onto. The Cut page makes a fresh track named VO by default. 5 More options let you handle countdowns and choose which file folder holds your saved voice recordings.

6 Work out where along the timeline this voiceover belongs. In a basic setup, simply drop the playhead at the spot where you want the VO to begin. You can also place an In point on the timeline that acts as a cue point the Voiceover tool comes back to on later takes. 7 You may optionally switch on Voice Isolation and Dialog Leveler when recording in a poor audio environment (say, straight into your laptop microphone in an office) so your audio gets cleaned up as it’s captured. 8 Click the Record button to launch the teleprompter and start recording onto the chosen track. The interface goes red to signal you’re “on the air.” 9 Click Stop to finish the recording. The playhead snaps back to your start position on its own, so you can play your new voiceover right there. 10 To have another go, hit the Cue button to jump back automatically to the In point, then press Record once more for a new take. That new voiceover overwrites the previous take on the timeline automatically. Even so, every one of your earlier VO takes remains saved in the Media Pool if you’d like to return to them.

### Using the Prompter

CUT A Prompter toolset is built into the Voiceover tool, letting you bring in a text (.txt) script; as you record, the text rolls across the picture so your voiceover stays on cue and well placed.

### The built-in Prompter in the Voiceover tool

To use the Prompter while recording voice over: 1 Open and configure the Voice Over tool as laid out above. 2 Within the Script Settings, switch on the Prompter Overlay and load the Script File. Further settings cover how the script gets formatted in the Viewer. 3 You can drop In and Out points on the timeline to define the VO range for the teleprompter. From there the teleprompter sets its own speed, beginning its scroll at the In point and finishing at the Out point. Should no In or Out points be set, by default the script’s scroll length spans the whole timeline. 4 As you press record, the text rolls across the image while your voice over is captured.

### Voiceover Settings

A number of optional settings on the Voiceover tool let you fine-tune your VO session.

A click on the Voiceover icon (red) brings up the Voiceover toolset along the bottom of the Viewer
