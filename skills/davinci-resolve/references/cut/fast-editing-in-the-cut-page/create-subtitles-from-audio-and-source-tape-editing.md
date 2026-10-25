# Create subtitles from audio and source tape editing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](ripple-overwrite-and-close-up.md) / [Next section](camera-names-and-sync-clips-window.md)
<a id="source-all-clips-must-have-a-common-timecode"></a> <a id="source-an-unorganized-media-pool-in-the-cut-page"></a> <a id="source-create-subtitles-from-audio-studio-version-only"></a> <a id="source-limiting-the-source-tape-scope-by-folder-structure"></a> <a id="source-metadata-entry-using-the-file-inspector"></a> <a id="source-preparing-footage-for-sync-bin-editing"></a> <a id="source-source-tape-editing"></a> <a id="source-sync-bin-multicam-editing"></a> <a id="source-using-the-source-tape"></a>

### Create Subtitles from Audio (Studio Version Only)

Subtitles can be generated for you straight from your timeline’s audio tracks: the DaVinci Resolve Neural engine studies the speech and converts it into text subtitles on its own. For more on automatic subtitling, see Chapter 52, “Subtitles and Closed Captioning.”

To Automatically Detect and Create Captions from Timeline Audio:

- Open whichever timeline holds the video and audio clips that need captioning.
- Click the Timeline Actions icon, then pick Create Subtitles from Audio off the drop-down menu.

### Source Tape Editing

Though every Cut page feature works fine on its own, a handful are built to pair up and smooth your editing along. Bring the File Inspector, Source Tape, Metadata View, and the Navigable Folder Structure together, for instance, and you can turn one folder of jumbled clips into a tidy, well-organized project.

### Metadata Entry Using the File Inspector

Entering metadata is where organizing any project begins. Our starting project holds a great many clips, every one of them parked in a single Master Bin. Those clips need suitable metadata attached, and the File Inspector is what we will lean on to do it.

### An unorganized Media Pool in the Cut page

With the File Inspector open, tick the Auto Select Next Unsorted Clip box; from then on, pressing the return key jumps you to the very same metadata field on the next clip in the Media Pool. Fill in each clip’s Scene, Shot, and Take metadata, going by what the slate in that clip shows. Once every clip bears its scene, shot, and take values, highlight the whole Media Pool, then type the text string “%{Scene}_%{Shot}_%{Take}” into the File Inspector’s Name field. Those variables relabel each clip with its scene, shot, and take numbers strung together by underscores — “02A_CU_03”, to give one. Keying Scene, Shot, and Take values into the File Inspector and renaming every clip through variables. Next, create a pair of new bins in the Media Pool, Scene01 and Scene02, then drag every clip whose name begins with 01 into the Scene01 folder and every clip whose name begins with 02 into the Scene02 folder. With that, this project’s metadata entry is finished.

The Media Pool, its scene 1 clips now gathered in the Scene01 folder and its scene 2 clips in the Scene02 folder

### Using the Source Tape

Switch the Source Tape on by clicking its icon in the Viewer. From the Media Pool view options choose Metadata View, then in the Sort menu choose Sort By Scene, Shot. The clips in the Media Pool now group by scene, and the clips from both scenes lay out in scene order inside the Source Tape viewer. Click a particular clip in the Media Pool and the playhead leaps to that clip’s opening frame in the Source Tape. From here the shots’ progression is plain to see (take two trails take one, and so on), and you can keep editing without poking around and clicking in the Media Pool.

The Source Tape mirroring every clip in the Media Pool, with the Metadata View grouping those clips by Scene

### Limiting the Source Tape Scope by Folder Structure

Once a project swells, keeping a whole film’s worth of media in the

Source Tape at all times turns cumbersome. You can rein the Source Tape’s scope in at the bin level. While you move through the

Source Tape, the clip you are on is highlighted, and its hierarchy now shows along the top of the Media Pool

title bar. Click straight on the bins in that bin path and you widen or tighten the reach of

the Source Tape in a flash. Click Scene02 and the Source Tape narrows to display only the clips in

that folder. Click back on Master and the Source Tape widens out once more to show every folder’s clips.

The navigable folder structure; a click on any of these levels tightens or widens how far the Source Tape reaches.

The Source Tape pared down to just the clips in Scene02

The Source Tape narrowed to display only the Scene01 clips

The Source Tape opened up to reveal every clip within the Master folder

It comes in handy too when you work through bin structures that echo the original camera file system. Picture this:

a camera might write each memory card out as its own folder, and within that, every single

clip is stored as a separate folder of its own. Pull this file system into the Media Pool

by way of the Create Bins option and those nested levels carry over into the Media Pool bin structure. From then on,

clicking a card bin in the Source tape shows you every clip on that card directly, instead of

presenting a host of separate sub-bins. You can view this in Thumbnail, List, and Filmstrip layouts as well.

### Sync Bin Multicam Editing

A whole set of tools in DaVinci Resolve makes editing multi-camera productions feel more natural and run more efficiently. When clips shot at the same instant on different cameras carry common timecode, DaVinci Resolve can knit all those camera angles into sync for you as you cut. Think of the tools covered in this section as a kind of digital assistant editor, forever combing through your media and laying the right shots in front of you at just the right moment. Pair this with the DaVinci Resolve Speed Editor and the Cut page becomes a formidable multi-camera editor.

### Preparing Footage for Sync Bin Editing

For the Sync Bin to function correctly, each clip it holds has to meet the characteristics laid out below.

### All Clips Must Have a Common Timecode

As a rule, professional video cameras and audio recorders can “jam-sync” their timecodes to one another, so that every distinct video and audio source lays down the exact same timecode at the exact same instant. Jam-syncing timecode is the fastest, simplest, and most dependable way to make your footage line up flawlessly. Where your footage lacks a shared timecode, you will have to take a few extra steps to get all your material aligned at the right moment. For more, consult the Sync Clips Window section further down.
