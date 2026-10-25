# Creating DCTL luts and about DCTL

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](advanced-workflows-and-workflow-integrations.md) / [Next section](dctl-function-signatures.md)
<a id="source-about-dctl"></a> <a id="source-creating-dctl-luts"></a> <a id="source-creating-dctl-luts-1"></a>

## Creating DCTL LUTs

### Creating DCTL LUTs

How you build DCTL LUTs to run your own bespoke mathematical transforms inside DaVinci Resolve is the subject of this chapter.

### About DCTL

A DCTL file is in fact a color transformation script that DaVinci Resolve recognizes and applies the same way it would any LUT. Whereas other LUTs are 1D or 3D lookup tables whose values approximate image transforms by interpolation, a DCTL file instead consists of actual computer code that transforms images directly through whatever combination of math functions you assemble. On top of that, because a DCTL file executes natively on your workstation’s GPU, it can run quickly. Making and installing a DCTL is open to anyone who has the math background for it. You just type your transformation code in a syntax resembling C (more detail follows below) into any text editor that can save a plain ASCII text file, then make certain the filename ends in “.dctl” (DaVinci Color Transform Language). With that finished, relocate the file into your workstation’s LUT directory. Its location varies according to your OS: On Mac OS X: `Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/` On Windows: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT` On Linux: `/home/resolve/LUT` Provided your .dctl syntax is valid, the entries show up the moment DaVinci Resolve launches, inside the Color page Node contextual menu under the DaVinci CTL submenu.
