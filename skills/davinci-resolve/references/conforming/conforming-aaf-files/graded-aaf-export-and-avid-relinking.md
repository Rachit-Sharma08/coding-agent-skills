# Graded aaf export and avid relinking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming aaf files.
[Chapter index](INDEX.md) / [Previous section](avid-aaf-roundtrip-project-setup.md)
<a id="source-audio-aaf-import-from-pro-tools"></a> <a id="source-import-aaf-edl-xml"></a> <a id="source-import-aaf-to-current-timeline"></a> <a id="source-relinking-transcoded-media-to-ama-media"></a> <a id="source-step-1relink-your-transcoded-media-to-ama-linked-source"></a> <a id="source-step-2export-an-aaf-file"></a> <a id="source-step-3import-the-aaf-grade-render-and-export"></a> <a id="source-step-4continue-editing-grading-and-finishing-the-project"></a> <a id="source-step-4reimport-the-aaf-into-media-composersymphony"></a> <a id="source-step-5render-graded-media-and-export-a-new-aaf"></a> <a id="source-step-6copy-the-graded-media-to-avid-mediafiles"></a> <a id="source-step-7import-the-graded-aaf"></a>

### Step 4–Continue Editing, Grading, and Finishing the Project

Cut the Timeline within the Edit page and grade every clip over in the Color page just as you would on any project. Be aware, though, that reaching for the Edit page tools to make any editorial tweaks to the timeline you brought in shifts the export options you’ll see down the road:

- If you don’t make editing changes: Then DaVinci Resolve can lean on the Avid AAF file you first imported to build a refreshed version of it. Doing so retains audio plus every other unsupported effect carried in the original AAF file, so they show up again once you export a fresh AAF over to Media Composer. Choosing this route means you must keep the original AAF file you import sitting in its same spot.
- If you do make editing changes: Then you’ll have to reach for the “Generate New AAF” command so an AAF of the re-edited Timeline gets exported out of DaVinci Resolve and back into Media Composer. The freshly built AAF file won’t carry along any effects that DaVinci Resolve doesn’t support.

### Step 5–Render Graded Media and Export a New AAF

1 Once you’re set to ship a graded project over to Media Composer, pick the Timeline you graded and bring up the Deliver page. 2 Pick “Avid AAF” out of the Presets sitting atop the Render Settings so its settings load.

Selecting the Avid AAF setup for round-trip 3 Within the Format section, pick whichever MXF codec you intend to render to.

4 Over in the File section, pick a suitable file destination path where the rendered media lands. Which spot you pick hinges on a single question: do Media Composer and DaVinci Resolve share one machine? If Media Composer and DaVinci Resolve are on the same computer: Build a fresh folder inside your Avid MediaFiles folder (Avid MediaFiles/MXF/) and name it with a number. Be certain the number you pick hasn’t been used before. If DaVinci Resolve is on a different computer using different storage: Pick any directory living on the portable hard drive you’ll rely on to ferry the media back to the very Media Composer workstation it came from. 5 Should you need handles on your rendered output, you can tack handles on within the Advanced Settings of the Video tab. Whenever you alter the File render settings, be sure to keep the “Render Clip with Unique Filename” checkbox switched on so every rendered clip carries a distinct file name, since several clips in the edited sequence can trace back to one source clip. 6 Over in the Timeline, hit Select Entire Timeline to mark the whole Timeline for delivery, then hit Add to Render Queue down at the foot of the Render Settings to drop the job you’ve assembled into the Render Queue. 7 Hit Start Render at the bottom of the Render Queue to kick off rendering. The project renders, and an AAF gets exported automatically into the very directory holding the media you rendered.

### Step 6–Copy the Graded Media to Avid MediaFiles

1 In setups where DaVinci Resolve and Media Composer live on separate workstations, track down the media directory holding the media files DaVinci Resolve rendered out, sitting on the portable hard drive carrying the project back to your Avid workstation, and copy it across into the Avid MediaFiles/MXF/ directory. 2 Give the directory a number as its name. Be certain the number you pick hasn’t been used.

### Step 7–Import the Graded AAF

1 Reopen the original project inside Media Composer. Should the media in the Avid MediaFiles folder’s new directory be in a compatible format, it joins the internal database of media on its own. 2 Build a fresh bin to hold the graded sequence you’re set to import. 3 Open that new bin, then go to File > Input > Import Media, pick the graded AAF file you exported out of DaVinci Resolve, and click Open. 4 So long as the media sits in the Avid MediaFiles directory, the new bin you built ought to populate on its own with the clips DaVinci Resolve rendered out, and a fresh sequence ought to turn up. 5 Double click the sequence you imported so it opens into the Record monitor and Timeline, fully conformed alongside the color corrected clips out of DaVinci Resolve. That sequence is now set for finishing within Media Composer.

### Relinking Transcoded Media to AMA Media

This upcoming workflow comes in handy whenever you’ve been cutting transcoded, offline copies of processor- or bandwidth-heavy media, yet you’d like to hand the original high-quality source media (think ALEXA or RED raw files) to DaVinci Resolve for grading. Under some circumstances, you’re better off reconforming your sequence onto the original AMA-linked media files inside Media Composer ahead of round tripping from Media Composer to DaVinci Resolve.

### Step 1–Relink Your Transcoded Media to AMA-Linked Source

1 Cut a sequence relying on media you’ve transcoded inside Media Composer. 2 Once you’re done, open the bin holding your project’s camera original media, and pick the AMA-linked clips matching the transcoded clips you’ve been cutting. 3 Right-click the edited sequence within its bin, and pick Relink off the contextual menu. 4 As the Relink dialog comes up, switch on “Select items in ALL open bins.” Pick “Tape Name or Source File Name” beneath the Source Name settings, and keep the “Create new sequence” checkbox switched on. A fresh sequence gets built that now ties to the AMA-linked camera originals.

### Step 2–Export an AAF File

1 Pick the freshly built sequence, and go to File > Output > Export to File. 2 Enter a fresh name, settle on a location for the file, and click Options. 3 Pick AAF off the Export As pop-up menu, and pick “Link to (Don’t Export) Media” off the Export Method pop-up menu. 4 Click Audio Details, and pick “Link to (Don’t Export) Media” off the Export Method pop-up menu. 5 Click Save to leave the Export Settings dialog, then click Save once more to export the file.

### Step 3–Import the AAF, Grade, Render, and Export

1 Launch DaVinci Resolve, and bring the AAF file you exported into the Edit page. A second dialog will require you to hand-pick the media. 2 Grade the project just as you would any other. 3 After grading wraps up, reach for the AAF Round Trip option over in the Deliver page so the graded media renders into a fresh (numbered) directory within the Avid MediaFiles directory. 4 Bring up the Edit page, pick the original AAF timeline you imported, right-click it, and pick Export AAF/XML. Settle on a location for the file and click Save.

### Step 4–Reimport the AAF into Media Composer/Symphony

Launch Media Composer, and bring in the AAF you exported out of DaVinci Resolve. Your graded sequence stands ready for finishing.

### Audio AAF Import from Pro Tools

Bringing audio AAF timelines in from Pro Tools (or whatever DAW software can export AAF) plays out much like the workflow for pulling a video AAF in from Media Composer that this chapter covered earlier. There are, however, a pair of methods at your disposal.

### Import AAF, EDL, XML

Reach for File > Import Timeline > Import AAF, EDL, XML — its keyboard shortcut is (Command-Shift-I) — and you get to pick a Pro Tools AAF. The same import options a Media Composer AAF gives you show up, yet what lands in front of you is an audio-only timeline, onto which you can layer a reference video should the need arise.

### Import AAF to Current Timeline

The File > Import Timeline > Import AAF to Current Timeline command lets you bring an audio AAF into whatever timeline you currently have open. Run this command and the import dialog lays out comparable import options, except this time a pair of extra options also appear.

Extra choices that surface once you run the “Import AAF to current timeline” command Here the “Import AAF to current timeline” checkbox sits switched on, surfacing a pair of options:

- Insert Additional Tracks: Brings the audio tracks in beginning at the front of the current timeline, dropping them beneath the lowest track that already carries audio in the Timeline.
- Insert with offset: Brings the audio tracks in using a chosen offset measured from the front of the Timeline.
