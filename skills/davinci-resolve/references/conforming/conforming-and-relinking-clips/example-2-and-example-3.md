# Example 2 and example 3

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming and relinking clips.
[Chapter index](INDEX.md) / [Previous section](media-pool-metadata-and-reel-names.md) / [Next section](reconform-from-bins-criteria.md)
<a id="source-conform-missing-clips-by-importing-their-source-media"></a> <a id="source-conformed-timeline-showing-missing-clips"></a> <a id="source-conforming-and-relinking-clips-part-3"></a> <a id="source-example-2"></a> <a id="source-example-3"></a> <a id="source-example-4"></a> <a id="source-relinking-clips-to-media-files-on-disk"></a> <a id="source-using-change-source-folder-to-relink-clips"></a> <a id="source-using-conform-lock-as-a-command"></a> <a id="source-using-the-import-additional-clips-command"></a> <a id="source-using-the-reconform-from-bins-command"></a>

### Example 2

This time the reel name sits inside the clip’s parent folder name and carries the reel name as a prefix.

- Pattern: _/????%R/%D or alternatively _/Reel%R/%D
- File path: /vol0/MyMovie/Scans/Reel1234/Frame[1000-2000].dpx
- Reel name: 1234

Both of these extraction patterns yield an identical result, and both echo the first example. The reel name still rests in the parent directory name, but here the fixed characters “Reel” precede it. That first pattern, with its ????, would in fact match any 4 characters ahead of the reel name. The second pattern is tighter, matching only the word “Reel” within the directory name.

### Example 3

Here the reel name resides in the parent folder name found two directory levels above.

- Pattern: \*/%R/%D/%D
- File path: /vol0/MyMovie/Scans/004B/134500-135000/Frame[1000-2000].dpx
- Reel name: 004B

Once more this mirrors Example 1; what sets Example 3 apart is that here the reel name is the directory name standing two levels up from the clip, where in Example 1 it sat just one level up in the directory name.

### Example 4

Last of all, the reel name turns up buried within the material’s clip name.

- Pattern: \_/Reel%R\_\_
- File path: /vol0/MyMovie/Scans/Reel004B\_[1000-2000].dpx
- Reel name: 004B

This case demonstrates one way to pull the reel name from the clip’s file name. Once again reading from the right, the two pattern characters “_\*” catch any string of characters running up to the first underscore. Here that sweeps in the file extension (.dpx) along with the frame number slice of the file name. After that, the “/Reel%R” characters mark the reel name as whatever falls between the “/Reel” and the _ character. The \* heading the pattern will match a file path nested any number of directories deep ahead of the file name.

### Conform Missing Clips by Importing Their Source Media

A timeline holding one or more missing clips means the tie between that timeline clip and the Media Pool has snapped, because no matching clip exists in the Media Pool. Should you choose to import clips by hand into the Media Pool to stand in for missing ones, the outcome rests on one checkbox — “Automatically conform missing clips added to Media Pool” — located in the General Options panel of the Project Settings. Do bear in mind that the “Auto conform clips with media added into Media Pool” setting has to be off if you work collaboratively. While that “Auto conform clips with media added into Media Pool” setting stays on in the General Options panel of the Project Settings, DaVinci Resolve refreshes the conformed tie between the clips you drop into the Media Pool and the missing clips across your project’s timelines on its own. At the same moment, DaVinci Resolve also refreshes the conform tie of every other timeline clip whose Conform Lock Enabled is off. The whole of this happens the instant you import the clips. If, however, “Auto conform clips with media added into Media Pool” is off as you import extra clips into the Media Pool, DaVinci Resolve will make no automatic reconform attempt, leaning on you instead to reconform offline or missing clips by hand through one of the many manual reconforming methods on offer — Reconform From Bins or Conform Lock With Media Pool Clip among them. For more on adding clips to the Media Pool by hand, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.”

### Using the Import Additional Clips Command

When a timeline turns out to be riddled with missing clips that have no matching Media Pool clips, a simple remedy exists that automates compiling the list of what is absent so every missing clip can be imported and conformed in one stroke. It applies to missing clips alone, never to unlinked clips (for those, reach for the Media Pool’s Relink command).

### Conformed Timeline showing missing clips

To bring in missing clips and reconform them to the Timeline: 1 On the Edit page, right-click a timeline in the Media Pool that carries missing clips, and from the Timelines > Import submenu pick one of these: Timelines > Import > Additional Clips With Loose Filename Match: Sweeps the Timeline for every missing clip and asks you to name a media directory to try conforming them against, pulling only the needed media into the Media Pool. The “Loose Filename Match” command turns a blind eye to file extensions, so you can swap offline media for online media in another format. Timelines > Import > Additional Clips With Tight Filename Match: Sweeps the Timeline for every missing clip and asks you to name a media directory to try conforming them against, pulling only the needed media into the Media Pool. The “Tight Filename Match” command hunts solely for media whose file extensions match exactly. 2 In the dialog that opens, pick the directory holding the remaining media to be conformed and click OK. Provided the media files in your chosen directory satisfy the conditions for matching the current Timeline’s missing clips, the required clips drop into the Media Pool and conform to the timeline automatically.

### Using Conform Lock As a Command

If, for any reason, an unlinked timeline clip flatly refuses to conform to a Media Pool clip even when you are sure it is there, the “Conform Lock with Media Pool Clip” command lets you force a Timeline clip to conform to a Media Pool clip of your choosing. This command quietly sets aside a target clip’s Conform Lock Enabled setting and disregards file names and reel names, conforming the target clip instead to another clip you handpicked, while timecode still serves to align the clip being conformed with the one originally in the Timeline. To conform lock a Timeline clip to another clip in the Media Pool: 1 Pick a clip in the Media Pool. For Force Reconform to work, the Media Pool clip you pick must run as long as — or longer than — the Timeline clip you pick. 2 Right-click an unconformed Timeline clip and pick “Conform Lock with Media Pool Clip” off the contextual menu. The chosen Timeline clip then conforms to your chosen Media Pool clip one of two ways: Where the chosen Media Pool clip’s timecode matches the chosen Timeline clip’s: the new clip conforms flawlessly to the original. Where it does not match: the new clip conforms so that the Media Pool clip’s first frame lines up with the first frame of the reconformed Timeline clip and fills the same duration. 3 Right-click that clip once more and you will find Conform Lock Enabled switched on, a sign the clip has been conform locked to media it did not originally match.

### Relinking Clips to Media Files on Disk

The simplest and most familiar way to relink project clips that have either dropped offline or bonded to the wrong set of media files on disk is the aptly titled “Relink Media” or “Relink selected clips” command. Mind you, the Relink command serves only clips that are unlinked; it does nothing for missing clips, which have no matching clips in the Media Pool at all. The Relink command is the most pliable route to tying your project’s Media Pool clips back to clips in a file system directory you nominate, leaning on file name and timecode as the chief criteria for rebuilding the link between each clip and its media file on disk. It is a strong choice for relinking media that has been shifted elsewhere or rearranged under a different file structure on disk. To relink all unlinked media: 1 Click the orange Relink icon in the page’s Media Pool. 2 Click the Locate button beside whichever volume(s) are missing, and point to a directory where the absent files now live 3 Should the quick search the Locate buttons kick off fail to turn up media you know is present, you can launch a thorough deep disk search by clicking the Disk Search button. 4 If still other clips elude the search, you are asked either to nominate a wholly different directory and press on, or to quit. To relink selected clips: 1 Highlight one or more offline clips to relink, or highlight a bin in the Media Pool bin list holding clips you want relinked, then right-click one of the chosen clips or the chosen bin and pick “Relink Selected Clips” off the contextual menu. 2 Once the Relink File dialog opens, point to a directory in which to hunt for the files you mean to relink to, and click OK. DaVinci Resolve sets out to find every clip bearing a matching file name within the subdirectories of the directory you named, using the relinked clips’ original file paths to do so as swiftly as it can. Because it first checks the directories the clips originally lived in, relinking can move quite quickly. 3 Where any clips slip past the step-2 method, a second dialog offers you a “deep search.” Click Yes and DaVinci Resolve combs every subdirectory of the directory you picked in step 2 for each clip. That can run a good deal longer, yet it ought to succeed outright so long as the needed media lies somewhere inside the chosen directory structure. 4 If yet more clips still cannot be located, you are asked either to nominate a wholly different directory and carry on, or to quit.

### Using “Change Source Folder” to Relink Clips

When you have used your file system to relocate media belonging to a DaVinci Resolve project yet left the directory structure organizing it untouched, the “Change Source Folder” command will swiftly relink selected Media Pool clips to the media’s new file path on disk, taking the original file paths as its guide. Where possible, it is a sound relinking method for projects living on a SAN, where you would rather not court the painfully long search times the Relink command’s more flexible trawl through a nested folder hierarchy can invite. To relink your Media Pool clips to a fresh location: 1 Highlight one or more Media Pool clips, then right-click one of them and pick “Change Source Folder” off the contextual menu. The Relink Media window opens, showing the material’s original path together with controls that let you name a fresh directory. 2 To the right of the “Change To” field, click the “Browse” button, then use the file navigation dialog to track down the media file’s new location, select it, and click Open. 3 Having found the right media file, click Change; otherwise click Cancel.

### Using the “Reconform From Bins” Command

The “Reconform From Bins” command offers a way to reconform several timeline clips in one go to a particular bin (or bins) of clips whose metadata matches. Using it begins with selecting the timeline clips you want reconformed (all of them, or merely a subset) and switching off Conform Lock Enabled; then, via the Reconform From Bin command, you handpick another bin of Media Pool clips to reconform against. A key trait of the Reconform From Bins command is that DaVinci Resolve reconforms only the timeline clips it can match to source clips in the selected Media Pool bins. Every timeline clip it cannot match is left untouched. That makes Reconform From Bins the perfect command when you have imported a subset of clips to the Media Pool that needs reconforming to clips scattered through an existing timeline. You could, for example, turn to this method to:

- Swap transcoded versions of a timeline’s clips for the original camera raw clips.
- Swap a timeline’s earlier VFX clip versions for newer ones.
- Swap the offline-quality media you have worked with thus far for online‑quality media.
- Swap the temp clips you were first handed for rescanned or recaptured

stock footage. When you turn to Reconform From Bins, it pays to arrange the clips you're bringing into the Media Pool with care, keeping them in a self-contained bin or bins apart from whatever other media that timeline draws on. A sub-bin works fine, provided it stays separate. Take a straightforward case. Say the media you cut or first brought in lives in Bin 1, and you then bring the refreshed versions of every clip needing reconforming into Bin 2. With Reconform From Bins, you can next pick whether your timeline's clips conform to Bin 1, or to Bin 2 where feasible, since only the timeline clips that have a valid match get reconformed, and every other timeline clip is left untouched.

You can have DaVinci Resolve apply custom conform options that govern which metadata gets used to pair timeline clips with source clips in the Media Pool. So you aren't held to just Timecode, Reel Name, and File Name; you may also reach, in whatever mix you like, for Resolution, Frame Rate, Bit Depth, File Format, Total Duration, Media UMID/UID, and/or Codec, steering how clips conform to suit your needs and whatever problem you're solving.
