# Photo page panels and albums

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Next section](photo-album-filtering-icons-and-photo-album-thumbnail-icons.md)
<a id="source-a-photo-album-in-the-media-pool"></a> <a id="source-bins-and-smart-bins"></a> <a id="source-effects-library"></a> <a id="source-photo"></a> <a id="source-photo-page"></a> <a id="source-photo-page-1"></a> <a id="source-photo-part-1"></a> <a id="source-searching-the-media-pool"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-media-pool"></a> <a id="source-the-media-pool-in-the-photo-page"></a> <a id="source-the-photo-album-interface"></a> <a id="source-the-photo-effects-library"></a> <a id="source-using-the-photo-page"></a>

### Photo

Photo Image Editing Now Fully Integrated Within DaVinci Resolve.

### Photo Page

A capable new Photo page arrives with DaVinci Resolve 21. The page exists so users can organize, sort, and grade their photo projects through every powerful grading and color management tool that ships natively in Resolve. It stands as the very first image editor woven completely into a video editing pipeline, and so far the only one.

### Photo Page

At its core the Photo page is a photo editing app, yet its deep ties into the remainder of DaVinci Resolve's effects and toolset unlock creative options that still image editing usually can't reach. Photo Albums let you hand off full resolution stills to the Cut, Edit, Color, and Fusion pages for further work. A complete image management pipeline lives in the Photo page, covering tagging, favorites, ratings, and photo album collections. On top of that, you can tether a camera to the Photo page to grab images and adjust the camera's settings on the fly. The fresh IntelliSearch feature has the AI examine your images so you can then find them by content, objects, people, colors, and more. Built into the Photo page is a sizeable effects library, packing several of the strongest Resolve FX and Fusion FX ready for use. Bringing the Photo page into DaVinci Resolve means you can glide effortlessly between photos, video editing, color grading, VFX, and audio post, every bit of it in real time.

NOTE: Every grade and effect on still images inside albums gets applied at the source level. As a result, the grades on your stills carry across all of a project's albums, much like remote grades do.

### Using the Photo Page

### The Interface Toolbar

Across the very top of the Photo page runs a toolbar whose buttons let you reveal or conceal various parts of the interface. Reading left to right, the buttons go as follows: Photo Page Toolbar Media Pool: Reveals or conceals a compact version of the full Media Pool page, granting access to every image the project uses. Effects Library: Reveals or conceals the store of all transitions, generators, and effects usable on the Photo page. Photo Album: Brings up the Photo Album along the bottom of the interface. Quick Export: Brings up the Quick Export Dialog for an easy export of your photos. Metadata: Reveals or conceals the Metadata Editor. Capture: Reveals or conceals the capture interface that lets you grab still photos onto your computer while tethered to a camera. Inspector: Reveals or conceals the Inspector, which lets you tweak both RAW and debayered photo parameters along with any effects properties.

### The Media Pool

On the Photo page, the Media Pool holds only the still image media you've brought into the current project for editing, plus all the albums you'll use to keep your photos organized. Unlike the Media Pools on other pages, it surfaces no video, audio, timelines, or effects clips. Those still exist, naturally, merely concealed from sight, since the Photo Page is devoted exclusively to still images.

### The Media Pool in the Photo Page

Clicking the Bin list at the top left brings up a tiered list of bins for sorting your photos, which doubles as the means of sorting your albums. By default the Media Pool holds one bin called "Master," though you can add more as you need to keep timelines and clips organized by clicking the Bin List and selecting + Add Bin. Renaming any custom bin is done by double-clicking its name and typing a fresh one, or by right-clicking the bin's name and selecting Rename Bin.

Clicking on the Bins icon, opens the bin list dropdown.

Whatever folder is selected has its contents shown in the browser area. Each still photo, bin, and album turns up here. As many albums as you like can be made inside one project. Either Thumbnail or List view can display the Media Pool. While in List view, sorting the contents is possible by any of a subset of all the metadata that the Media page's Metadata Editor makes available. Importing Photos Into the Media Pool on the Photo Page True, putting photos into the Media Pool from the Media page gives you the most organizational flexibility and features, but if you find yourself over on the Photo page needing a handful of photos brought in quickly for right-now use, a pair of methods exist. Via the Import Media icon on the Photo page's Media Pool: 1 With that page open, click the Import Media list icon sitting atop the Media Pool. 2 Pick from these options:

- Import Media: Brings up a file requestor for importing the photos you chose.
- Import Media Folder: Brings up a file requestor that pulls in every photo within the folder you chose.
- Import from Photos (macOS only): Launches the macOS Photos app and has you

select photos for import.

- Import from Lightroom: Pulls in an Adobe Lightroom Catalog.
- Import Blackmagic Cloud Folder: Lets you link up a Blackmagic Cloud folder and

bring in the photos kept inside it. Via the Import Media command on the Photo page's Media Pool: 1 With that page open, right-click somewhere inside the Media Pool and select Import Media. 2 Through the Import dialog, choose one or more photos to bring in, then click Open. Those photos land in your project's Media Pool.

### Bins and Smart Bins

In fact, the Media Pool holds two sorts of bins, and each one shows up in its own area of the Bin list. The distinctions between the two kinds of bins are these:

- Bins: Plain, hand-filled bins. Drop whatever you wish into a bin, and that's its home until you choose to relocate it elsewhere. Since bins can nest hierarchically, you're free to build a Russian-doll arrangement of bins if that suits you. Making new bins takes nothing more than right-clicking inside the bin list and selecting Add Bin from the contextual menu.
- Smart Bins: These fill themselves procedurally, which means custom metadata-based rules dynamically sift the Media Pool's contents the moment you pick a Smart Bin. That turns Smart Bins into quick ways to organize the contents of projects where you (or an assistant) put in the effort to attach metadata to your photos via the Metadata Editor, adding exif data, keywords, comments, description text, and countless other details so you can locate what you want faster when the need arises. To build a new Smart Bin, click the bin list and pick + Add Smart Bin. Up comes a dialog where you can name the bin and define the rules it applies to filter clips, then click Create Smart Bin.

### Searching the Media Pool

Clicking the magnifying glass icon on the toolbar reveals a search field where you can hunt for particular image names. The new IntelliSearch feature covered elsewhere in this guide, however, lets you harness AI technology for thorough, almost instant searching of the people and objects you type into that field.

### Effects Library

Every effect you might add to your photos resides in the Effects panel. That panel presents a tiered list of all the assorted effects and filters on offer, arranged by category.

### The Photo Effects library

For a preview of an effect before you place it on a photo, confirm "Hover Scrub Preview" is ticked in the Effects option menu, then just hover your pointer over any thumbnail in the Effects tab and glide it across that thumbnail. Using its default parameters, the effect previews in the Viewer. To switch a particular effect on for a photo, simply drag the chosen effect's thumbnail onto a photo in the Album. Open the Effects tab in the Inspector to adjust that effect's parameters. A given effect is searchable by typing into the search bar atop the Effects Library. Hitting Shift-Space summons the Effects Search dialog on the Photo page. With a photo selected, clicking an effect in the search list applies it to that selected photo. Category Names work as search terms for finding effects and transitions. Search "Stylize," for instance, and every Resolve FX under the Stylize heading appears. You can likewise search for effects in whatever language is set under DaVinci Resolve > Preferences > User > UI Settings, alongside English. NOTE: Every effect gets a full write-up within the Resolve FX portion of the DaVinci Resolve Reference Manual Photo Albums Clicking this tab brings up the Photo Album along the bottom edge of the interface. As with their physical counterpart, Photo Albums on the Photo page are where you keep and arrange collections of still images. Inside DaVinci Resolve they amount to a special breed of timeline, assembled from user-curated stills. Sorting your media pool images into photo albums matters greatly for squeezing the most out of the still photo features in DaVinci Resolve 21. Photos stay independent of resolution and frame rate, whereas timelines do not. The Photo page leans on the Photo Album as its main organizational container, allowing your photos to engage with the rest of DaVinci Resolve's pages.

### The Photo Album Interface

### A Photo Album in the Media Pool

To create a Photo Album:

- Within the Media Pool, right-click and choose New Photo Album off the context menu.
- From the main menu, choose File > New Photo Album.

Adding one or more images to a Photo Album goes like this: 1 Select an image, or several, inside the Media Pool. 2 Right-click an image and choose Add Photo(s) to Album 3 Your selected photos join the current Photo Album Removing one or more images works similarly: 1 Select an image, or several, inside the Media Pool. 2 Right-click an image and choose Delete Selected. 3 Your selected photos leave the current Photo Album After an album is built and stocked with photos, the Photo Album toolset lets you rapidly arrange, sort, and label still images for later use in DaVinci Resolve. You can attach flags, colors, and tags to images in the Viewer, then lean on the Photo Album's filter tools to arrange and sort them.
