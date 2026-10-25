# Conforming adl files and more about conforming adl files

Version: DaVinci Resolve 20.3 Reference Manual. Context: Conforming overview.
[Chapter index](INDEX.md) / [Previous section](conforming-otio-files-and-more-about-conforming-otio-files.md)
<a id="source-conforming-adl-files"></a> <a id="source-conforming-adl-files-1"></a> <a id="source-importing-adl-project-files"></a> <a id="source-more-about-conforming-adl-files"></a>

## Conforming ADL Files

### Conforming ADL Files

Every workflow for bringing in and conforming timelines by way of the AES31 Audio Decision List format (.adl) is what this chapter walks through.

### More About Conforming ADL Files

On the import side, DaVinci Resolve handles the AES31 Audio Decision List (.adl) format. ADL is a timeline interchange format, the work of the Audio Engineering Society. Built to stay neutral toward any application or platform, it carries your timeline and its media assets from one digital audio workstation to another. At the time of writing, DaVinici Resolve has no ADL export.

### Importing ADL Project Files

How to import ADL files through one straightforward procedure is what this section lays out.

The AES31 Audio Decision List (.adl) import progress dialog Here’s how to bring an Audio Decision List (.adl) file in and have it link itself to the media it references: 1 Take either of these routes:

- From any page, choose File > Import Timeline (Shift-Command-I).
- Head into the Edit page, right-click somewhere within the Media Pool, then go to Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO. 2 In the file system dialog that comes up, locate the .adl project file you mean to import, highlight it, and click the Open button. 3 DaVinci Resolve goes on to bring in the timeline along with all the .wav files that accompany the ADL. An Import AES31 File dialog box keeps you posted on how the import is progressing. In contrast to every other Timeline Import format, importing an ADL file offers no extra controls. The timeline and the media that goes with it land straight in the open bin within the Media Pool.
