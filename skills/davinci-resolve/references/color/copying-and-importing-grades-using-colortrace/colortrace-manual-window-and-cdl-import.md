# Colortrace manual window and importing cdl data using colortrace

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copying and importing grades using colortrace.
[Chapter index](INDEX.md) / [Previous section](colortrace-timeline-selection-and-grade-copying.md)
<a id="source-calculating-cdl-functions"></a> <a id="source-colortrace-manual-window"></a> <a id="source-example-cmx-edl-file"></a> <a id="source-importing-cdl-data-using-colortrace"></a> <a id="source-using-cdl-adjustments"></a>

### ColorTrace Manual window

Manual mode has the following controls:

- Source timeline: Presents every clip in the Source timeline you chose — the clips you're pulling grades from. Click a single clip thumbnail to select it, or click one thumbnail and then Shift-click another to grab an unbroken range of clips. A noncontiguous range of clips can't be selected.
- Copy Range controls: A pair of fields shows the range of clips in the present selection you'll be copying from, named by their numeric place in the Source timeline. You can reset the range by the numbers, either keying fresh values into the fields or nudging the value by one with the up/down arrow buttons. The First button automatically folds in every clip from the Timeline's first one into the present selection. The Last button automatically folds in every clip out to the Timeline's last one into the present selection.
- Target timeline: Presents every clip in the Target timeline you chose — the clips you're pushing grades to. Selecting clips here behaves exactly as it does on the Source timeline.
- Paste Range controls: A pair of fields shows the range of clips in the present selection you'll be pasting to, named by their numeric place in the Source timeline. Every control behaves exactly like the Copy Range controls.
- Attributes and options checkboxes: Clear the checkboxes of any clip characteristics you'd rather leave out of the ColorTrace operation. A fuller rundown of these options sits in the section covering the Automatic ColorTrace mode.
- Paste button: After you've chosen one or more source clips plus a matching count of target clips, clicking Paste carries over the grades, PTZR settings, and marks (subject to the matching checkboxes).
- Undo Last: Lets you undo the most recent paste action.
- Undo All: Lets you undo all paste actions in Manual mode.
- Done: Finishes the operation and closes the ColorTrace window.

Whenever you're cherry-picking lone grades off one timeline to drop onto shots elsewhere, the copying can go one grade at a stretch. To move a single source grade onto a single target clip:

- Pick a thumbnail up in the Source timeline (the top one) as your source, next pick a thumbnail down in the Target timeline (the bottom one), then hit Paste.

You can equally carry the grades of whole scenes' worth of clips from one timeline onto another in one move. As an example, when you're bringing grades over from an originally graded timeline onto a re-edited cut of that same program, you can carry every grade off a 10-clip scene in the Source timeline onto those same 10 clips in the Target timeline that have been shoved later in the Timeline.

To move a batch of source grades onto a batch of target clips: 1 Settle on an unbroken run of source clips through one of these routes:

- Select the range's first clip, after which you Shift-click the range's last clip.
- Type the clip number of that first clip into the left “Copy Range” field, then type the clip

number of the last one into the field on the right.

- Select a clip, then hit First so every clip from there back to the Timeline's first one comes in.
- Select a clip, then hit Last so every clip from there out to the Timeline's last one comes in. 2 Settle on an unbroken run of Target clips following the identical steps from before, except this time on the “Paste Range” controls.

IMPORTANT: The Paste button only switches on once your tally of target clips equals the tally of source clips you picked.

Group copy and paste of grades 3 With your selections made, click Paste. The grade settings off the source clips land on the destination clips in order. Put differently, if you copy from clips 5 through 9 onto clips 11 through 15, then grade 5 lands on shot 11, grade 6 lands on shot 12, grade 7 lands on shot 13, and so forth.

### Importing CDL Data Using ColorTrace

By way of the ColorTrace CDL command you can pull ASC CDL file formats out of other applications and into DaVinci Resolve. DaVinci Resolve is likewise able to read DRX filenames out of CDL files, which lets a CDL load exported DaVinci Resolve grades. Three file formats are supported: CMX EDL: An EDL whose comments point at CCC/CDL XML files, or even Slope, Offset, and Power (SOP) data tucked inside the comment area. CCC and CDL XML: A file format holding assorted color correction looks, plus references too.

Pulling CDL data into DaVinci Resolve goes like this: 1 Where what you're bringing in is CCC/CDL XML correction looks:

- Open the Gallery page, right-click somewhere inside the Stills tab, and pick Import off the contextual menu.
- Once the Import Stills dialog shows up, open the CDL/CCC files. As they finish coming into the Gallery, an ASC logo turns up next to them.

2 Open the Edit page and pick, in the Timeline list, the Timeline you mean to run ColorTrace against. 3 Right-click somewhere inside the Timeline, and pick ColorTrace from CDL. 4 Pick an EDL through the Select EDL dialog, and click Open. 5 Pick its matching CDL and CCC files through the Select CDL Files dialog. Where no CDL or CCC files exist (which holds when there are inline SOP comments inside the EDL), you ought to click Cancel. 6 Through the ColorTrace With CDL window, carry the source grades off the CMX EDL/CCC & CDL XML files onto the Target timeline. From here on, the ColorTrace window behaves exactly as laid out earlier.

As a formatting guide, below are a few sample CMX, CCC, and CDL files.

### Example CMX EDL File

TITLE: Final EDL FCM: NON-DROP FRAME 010 001 V C 01:19:28:16 01:19:28:16 01:00:41:18 01:00:42:18 *ASC_CC_XML test_cc.102 011 001 V C 00:00:00:00 01:19:28:16 01:00:42:18 01:00:43:18 *ASC_SOP (0.9 1.2 0.5)(0.4 -0.5 0.6) (1.0 0.8 1.5) Example CCC File <ColorCorrectionCollection xmlns:”urn:ASC:CDL:v0.5” > &lt;InputDescription&gt; test corrections for ref_input_image.1920 &lt;/InputDescription&gt; &lt;ViewingDescription&gt; for mathematical analysis only &lt;/ViewingDescription&gt; &lt;ColorCorrection id=”test_cc.100”&gt; &lt;SOPNode&gt; &lt;Description&gt; for ref_output_image.0100 &lt;/Description&gt; &lt;Slope&gt; 1.0 1.0 1.0 &lt;/Slope&gt; &lt;Offset&gt; 0.0 0.0 0.0 &lt;/Offset&gt; &lt;Power&gt; 1.0 1.0 1.0 &lt;/Power&gt; &lt;/SOPNode&gt; &lt;/ColorCorrection&gt; &lt;ColorCorrection id=”test_cc.101”&gt; &lt;SOPNode&gt; &lt;Description&gt; for ref_output_image.0101 &lt;/Description&gt; &lt;Slope&gt; 1.0 1.5 0.6 &lt;/Slope&gt; &lt;Offset&gt; 0.0 -0.1 0.01 &lt;/Offset&gt; &lt;Power&gt; 1.0 1.5 0.5 &lt;/Power&gt; &lt;/SOPNode&gt; &lt;/ColorCorrection&gt; </ColorCorrectionCollection>

Example CDL File <ColorDecisionList xmlns=<94>urn:ASC:CDL:v0.5<94> > &lt;InputDescription&gt; GeneralProducts M1 std thru GP M1 LUT4 </ InputDescription> &lt;ViewingDescription&gt; GP P1, DCI P3, Pathe color emul </ ViewingDescription> &lt;ColorDecision&gt; <MediaRef ref=<94>/some/Project/frame%250900-0954%5B.dpx<94>/> &lt;ColorCorrection id=”cc03340”&gt; &lt;SOPNode&gt; &lt;Description&gt;change +1 red, contrast boost&lt;/Description&gt; &lt;Slope&gt;1.2 1.3 1.4&lt;/Slope&gt; &lt;Offset&gt;0.3 0.0 0.0&lt;/Offset&gt; &lt;Power&gt;1.0 1.0 1.0&lt;/Power&gt; &lt;/SOPNode&gt; &lt;/ColorCorrection&gt; &lt;/ColorDecision&gt; </ColorDecisionList>

### Using CDL Adjustments

After you've imported a CDL (Color Decision List), the CDL adjustment for each clip becomes reachable through a contextual menu command in the Thumbnail timeline of the Color page.

### Calculating CDL Functions

To convert the SOP values into a primary correction, DaVinci Resolve runs the following math: Output = (Input \* Slope + Offset)Power Output stands for the finished grade. Input is each pixel's value within each color channel (on a 0–1 scale). Slope rests at a detent of 1 while Offset rests at a detent of 0 and Power again at a detent of 1.
