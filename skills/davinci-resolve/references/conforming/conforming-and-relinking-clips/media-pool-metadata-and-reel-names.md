# Defining clip metadata when adding media to the media pool and how reel names are identified

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming and relinking clips.
[Chapter index](INDEX.md) / [Previous section](xml-aaf-conforming-and-extension-matching.md) / [Next section](example-2-and-example-3.md)
<a id="source-automatically-defining-reel-names"></a> <a id="source-defining-clip-metadata-when-adding-media-to-the-media-pool"></a> <a id="source-example-1"></a> <a id="source-examples-of-reel-name-extraction-patterns"></a> <a id="source-extraction-pattern-operators"></a> <a id="source-how-reel-names-are-identified"></a> <a id="source-using-the-pattern-field"></a>

### Defining Clip Metadata When Adding Media to the Media Pool

For pipelines in which you add media files to the Media Pool by hand — whether you are cutting from scratch in DaVinci Resolve, gearing up to process dailies, or taking a separate step ahead of importing EDL, XML, or AAF project files and reconforming them onto a higher-quality set of media than was first used to edit — the rules governing how clip metadata is set in readiness for conforming differ somewhat.

- Timecode: Worked out from the “Timeline Frame Rate” value, which lives in the Master Project Settings panel of the Project Settings.
- Reel Names: Settled by two things — whether the “Assist using Reel Names from the” checkbox sits on or off (you will find it in the General Options panel of the Project Settings), and which option you picked. Reel names may be pulled dynamically — so each time you alter this setting, the Media Pool’s reel names refresh to match — or they may be set by hand, in which case different clips can lean on different reel name extraction methods.
- Clip Names: Read and held; drawn on for AAF and XML imports, yet skipped for imported EDLs.

### How Reel Names Are Identified

Of the settings governing how conform behaves, the “Assist using Reel Names” checkbox — over in the General Options panel of the Project Settings — ranks among the weightiest. Out of the box it is off, with reel names blank. That suffices for conform workflows where the file path or file name plus source timecode is all it takes to pin each media file to its clip. Yet when reconforming your project’s clips demands more, ticking the “Assist using Reel Names” checkbox lets DaVinci Resolve fall back on one of four methods to set reel names automatically across every Media Pool clip.

### Automatically Defining Reel Names

Lean on the “Assist using Reel Names” options — these sit in the General Options panel of the Project Settings — and reel names are pulled dynamically. What that means is that whenever you switch the reel name extraction method in the Project Settings, the reel names across every Media Pool clip refresh on their own to match. You can watch this play out in the Reel Name column, which shows once the Media Pool is put into List view. Flip the “Assist using reel names” options from “Source clip file pathname” over to “Mediapool folder name,” for instance, and the Reel Name column’s contents visibly shift. It comes in handy when you import a project whose clips all settle their reel name the same way. Manually Choosing Reel Name Definitions for Individual Clips Through the Clip Attributes dialog you also get to choose by hand the criteria by which one or more selected Media Pool clips have their reel names set. That helps where particular clips in a project must lean on a different reel name extraction method, or on reel names typed in by hand.

To set reel names by hand for one or more clips: 1 In the Media Pool, pick one or more clips. 2 Right-click one of the chosen clips and pick Clip Attributes off the contextual menu. 3 Open the Reel Name panel within the Clip Attributes dialog, pick a fresh option, and click OK. After you have used Clip Attributes to rewrite a clip’s reel names, those clips cease refreshing automatically whenever you adjust the “Assist using Reel Names” options back in the General Options panel of the Project Settings. For more on wielding Clip Attributes, turn to Chapter 19, “Using Clip Metadata.” Methods of Defining Reel Names Five options exist for working out automatically how reel names are pulled from the source media while “Assist using Reel Names” is on, plus a single option in the Clip Attributes Reel Name panel for setting them by hand. Reel names matter a great deal in EDL and AAF workflows, though they carry less weight in XML‑centric ones.

- Source clip file pathname: Derives the reel name by pulling it from each media file’s path. With this you can draw a reel name out of the whole file name or part of it, or out of the whole — or part — of any folder name along the path that wraps the file. You spell out that extraction through the Pattern field.
- Pattern: A code setting out how a reel name ought to be pulled from the source clip pathname. Fuller notes on building patterns come later in this chapter.
- Media Pool folder name: Here the reel name is taken from whichever bin in the Media Pool holds the clip. In a stereoscopic workflow, say, you might export offline stereo media using the “Left” and “Right” bin names — the bins they live in — as reel names. Another instance: VFX undergoing incremental processing, filed into individually named bins like “VFX_Tuesday_10-12.”
- Embedding in Source clip file: Handy with file formats that bury the reel name inside the media file. Among the formats able to carry reel name header data are Blackmagic RAW (and other digital cinema cameras), QuickTime files born of Final Cut Pro, and DPX frame files.
- Source clip filename: Where no reel number is defined, it is frequently simplest just to fall back on the Source clip filename.
- User Defined: This choice surfaces solely when you hand-edit the Reel Name for one or more selected Media Pool clips by way of the Clip Attributes dialog. Picking User Defined lets you type whatever text string you wish to serve as the reel name.

One more checkbox is on hand, “Extract reel names from EDL comments,” which chiefly serves legacy workflows where you conform an EDL exported out of Final Cut Pro 7 against camera original R3D media. Extract reel names from EDL comments: Certain media file formats — R3D among them — carry reel names, taken from the file names, that run longer than the eight characters a standard EDL permits. This option lets DaVinci Resolve lift reel names out of suitably formatted EDL comments, like those Final Cut Pro 7 produces.

### Using the Pattern Field

When the Pattern option is your route to pulling the reel name out of a clip’s source file pathname, you are free to craft your own search pattern, letting DaVinci Resolve lift the reel name in very precise ways that suit more unusual workflows. A pattern is read from right to left, working through a clip’s file path piece by piece — beginning at the file name, then weighing each enclosing directory’s name to its left. Every pattern is a string of text characters and “wild card” operators in distinctive combinations that mirror the length and the names along the file path. Below are the search characters at your disposal.

### Extraction Pattern Operators

Hunts for any single character. Drop in one question mark for every ? character you mean to catch. ?? catches two characters, 02 for instance; ???? catches four, such as 0002.

- A wildcard matching any run of zero or more characters.

%R

Marks where the reel name truly sits. A reel name may hold any character, yet it must not include a directory separator (forward slash).

%\_R

Pulls the reel name while stripping away the R3D file name underscores seen in EDLs from Final Cut Pro 7 or older.

%D

Catches any directory name or file name. Where it stands as a pattern’s final operator, leave off the forward slash.

/ Serves to part any two operators

Should you be building a fresh extraction pattern for some one-off workflow, a test dialog lets you trial different patterns before turning them loose on your project. To test the extraction path: 1 Switch on “Assist using reel names from the” and click the Test button beside the current Pattern in the General Options panel of the Project Settings. Up opens the “Specify Reel Extraction Pattern” dialog. 2 Key the extraction patten you wish to trial into the Pattern field. 3 By whatever means you favor, locate the file path of the media file the pattern is to be trialed against, then paste or type that path into the Sample Path field. 4 Click Test. 5 Where the reel name shown beneath proves correct, click Apply, which drops the pattern into the Pattern field over in the Project Settings’ General Options panel. Where it proves wrong, tweak the pattern and have another go.

### Examples of Reel Name Extraction Patterns

For a clearer grasp of how this works, the examples below lay out the assorted ways reel names get extracted. Between control parameters, the / acts as the separator.

### Example 1

In this example the reel name lives inside the clip’s parent folder name.

- Pattern: \*/%R/%D
- File path: vol0/MyMovie/Scans/004B/Frame[1000-2000].dpx
- Reel name: 004B

Since parsing runs right to left, begin your read of this pattern at its right end. Here the %D lands on the file name “FrameNNNN.dpx,” where NNNN is the frame number carried by each file of the clip. Step left past the file name and the /%R/ chunk of the string comes next. It declares that the reel name will be the full name of the parent directory sitting immediately above the file. Then the \* leading the string tells it to match any pathname ahead of the directory name holding the reel name. Such a string would locate the parent directory no matter how many levels deep it lies along the directory path.
