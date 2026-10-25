# Email notification and server settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](loader-preferences-and-defaults.md) / [Next section](script-and-script-preferences.md)
<a id="source-creating-a-user-path-map"></a> <a id="source-deleting-a-path-map"></a> <a id="source-email-notification"></a> <a id="source-modifying-a-default-path-map"></a> <a id="source-modifying-a-system-path-map"></a> <a id="source-nesting-path-maps"></a> <a id="source-options-1"></a> <a id="source-path-maps"></a> <a id="source-preferences-part-3"></a> <a id="source-preview"></a> <a id="source-quicktime"></a> <a id="source-server-settings"></a> <a id="source-the-path-map-preferences"></a> <a id="source-the-preview-preferences"></a> <a id="source-the-quicktime-preferences"></a>

### Email Notification

The Email Notification section is where you arrange who receives status updates about the render jobs and the network.

- Notify Options: Ticking these checkboxes triggers emails when particular render events occur. The events on offer are Queue Completion, Job Done, and Job Failure.
- Send Email to: Type the address or addresses that should receive notifications, separating several addresses with a semicolon.
- Override Sender Address: Type an email address to act as the sender address. Leave this option unticked and no sender address is applied, which can lead certain spam filters to block the message from reaching the recipient.

### Server Settings

Clustering and Network Rendering are dealt with in this section. For deeper coverage of these settings and of clustering, see the DaVinci Resolve Reference Manual's Chapter 66, "Rendering Using Saver Nodes," or the Fusion Reference Manual's Chapter 4.

### Path Maps

Path Maps are virtual paths that swap out portions of file paths for variables. As an example, you might define the path 'movie_x' as really residing in X\Shows\Movie_X. Following that example, Fusion would read the path 'movie_x\scene_5\ scan.000.cin' as actually pointing to X:\Shows\ Movie_X\scene_5\scan.000.cin. Within Fusion Studio, virtual path maps offer two principal benefits over literal file paths. The first is that you can readily alter the path to media tied to Loaders (say, when relocating a comp from one drive to another) without touching the composition at all. The second benefit comes during network rendering, where you can sidestep the differing OS filename conventions.

- Enable Reverse Mapping of Paths Preferences: You'll find this checkbox up at the top of the Path Map settings. With it enabled, Fusion draws on the built-in path maps for the path's settings entries as it maps existing filenames. Fusion Studio gains the most from this. Ticking the checkbox makes Loaders adopt paths relative to where the saved composition lives the moment they're dropped into the Node Editor.

For deeper coverage of using relative paths for Loaders, see the DaVinci Resolve Reference Manual's Chapter 105, "I/O Nodes," or the Fusion Reference Manual's Chapter 45.

### The Path Map preferences

Like the other preferences in Fusion Studio, path maps come in both Global and Composition flavors. Global preferences carry over to all new compositions, whereas Composition path maps are stored only with the composition at hand. A Composition path map will take precedence over a Global path map bearing the same name. The Global path maps break down into three sections:

- System Path Maps: System path maps are set by the operating system and lay out Fusion's global locations. Particular System path maps can be overridden through the Defaults or the current Composition Path Map settings. Should you later reconsider, the System path maps always let you revert to Fusion's "factory" defaults. The System Path Map settings put several top-level path maps in place.

AllData: Where Fusion stores every bit of shared application data. AllDocs: Where Fusion stores the public/shared document folder. AllLUTs: The nested LUTs path within the Defaults section, the spot Fusion uses to store LUTs. Fusion: Where the Fusion Studio app lives once installed. As an example, open Fusion from C:\Program Files\Fusion and the path Fusion:\Help points at C:\Program Files\Fusion\Help. Had you instead run a copy of Fusion located at \\post-server\fusion\16, then Fusion:\Help would resolve to \\post-server\fusion\16\Help. FusionLibs: The Fusion libraries the application relies on. Profile: Where the default Fusion preferences file gets stored. Profiles: Where Fusion keeps each individual user's preferences. Programs: Where Fusion Studio or DaVinci Resolve resides. SystemFonts: Where the OS keeps the fonts that show up for Text+ and Text 3D nodes. Temp: Points at the temporary folder belonging to the system. UserData: Where Fusion stores all the user-specific assorted roaming data. The Default Path Maps section enumerates the separate pieces making up that roaming data. On Windows with Fusion Studio, this is "C:\Users\username\AppData\Roaming\". Under Linux, it's "$HOME/Blackmagic/Fusion". Under macOS, it's "Users/UserName/Library/Application Support/Blackmagic Design/Fusion". UserDocs: Where Fusion keeps the user's document folders.

- Default Path Maps: The Defaults are path maps you can edit yourself. As part of their paths they may point at the System paths. For example, the Temp folder, defined in the System path, is drawn on by the Default DiskCache path map to pin down the nested location (Temp:DiskCache). Default path maps can likewise redirect paths without leaning on the Global System path maps. Once you alter a Default, the new setting becomes selectable in the Preferences window, and a Reset button at the foot of the Preferences window restores the changed setting to the System default.

AutoSaves: Fixes where the Fusion Comp AutoSave document goes, as configured in the Fusion General preferences. Bins: Fixes where Fusion Studio bins reside. Because bins hold pointers to the content, the content itself isn't stored with the bin; only the metadata and pointers go into the bins. Brushes: Directs Fusion to the folder holding custom paintbrushes. Comps: Where Fusion Studio compositions get stored. Under macOS or Windows, the default spot is Users/YourUserName/Documents/Blackmagic Design/Fusion. Config: Holds Configuration files that Fusion Studio uses while running. Defaults: Marks where node default settings sit so they can be brought back if overwritten. DiskCache: Fixes where files land on disk when the Cache to Disk feature is in use. The Cache to Disk window can override this location.

Edit templates: Where Fusion macros are kept so they turn up as templates inside the DaVinci Resolve Effects Library. Filters: Aims at a folder holding Convolution filters such as sharpen, usable by the Custom Filter node. Fonts: The default Fonts path map aims at the operating system fonts folders. Altering it shifts which fonts are on hand in the Text+ or Text 3D nodes, plus any Fusion Title Template. In DaVinci Resolve. This path map leaves untouched the five extra Edit page titles: L Lower 3rd, R Lower 3rd, plus M Lower 3rd, together with Scroll and the Text title. Fuses: Aims at a folder holding Fusion Fuses plugins. FusionTemplates: Where Fusion macros are kept so they appear as templates in Fusion's Effects Library. Guides: Where custom viewer guide overlays get stored. Help: Marks where Fusion Studio PDF files sit. Layouts: Where Fusion Studio custom window layouts are kept. Libraries: Aims at a support folder able to hold custom Effects Library items. LoaderCache: Fusion Studio's Loader preferences permit the Loader to cache while reading from a slow network. This path map aims at the local drive spot used for that cache. LuaModules: Where Lua Scripting modules reside. LUTs: Aims at a folder holding Look Up Tables (LUTs). Macros: Aims at the spot for user-created macros. Macros stored there show up in the Effects Library's macros category and in the right-click Edit Macro contextual menu. Plugins: Denotes user-specific OpenFX plugins you'd rather not have loaded for everyone. Previews: The path map serving the older-style, file sequence flipbook previews. Queues: Where the Render manager list lives. Scripts: Where Lua and Python scripts reside. This path can be narrowed further into particular scripts for tools (nodes), comps, and other specific script types. Settings: Where custom Node settings are kept. Stamps: Where preview movies built in a Fusion Studio bin go. This path map is now obsolete given that bins carry the Studio Player. Templates: Where the Templates folder sits. Saving Macros into the Template folder makes them appear in the Effects Library under a Templates category. Within Fusion Studio, that Templates category stays hidden until a Macros is saved into the folder. Thumbs: Where clip thumbnails built in a Fusion Studio bin go. A leftover path map by now, seeing as the Studio Player ships inside bins. UserPaths: Serves spots for studio- or facility-specific tools, such as custom plugins and scripts kept on a central server.

- User Path Maps: User paths are fresh paths you've defined that aren't already in the Defaults settings. Comp denotes the folder holding the current composition. As an example, keeping media folders alongside your Fusion Studio comp file lets Loaders rely on relative file paths rather than literal ones.

### Modifying a System Path Map

To change an existing System path map, pick the path map within the System section. Press the folder icon at the foot of the Preferences window, then type the path map's name into the From field below. Type the path map's value into the To: field.

### Modifying a Default Path Map

To change an existing Default path map, pick the path map within the Default section. Press the folder icon at the foot of the Preferences window, then type the path map's name into the From field below. Type the path map's value into the To: field.

### Creating a User Path Map

To build a path map, press the New button and type the path map's name into the From field below. Type the path map's value into the To: field.

### Deleting a Path Map

To remove a path map you created, choose it from the list and press the Delete button. System and Default path maps can't be removed; only the path maps a user created can be taken out of the Path Maps list.

### Nesting Path Maps

While defining a path map of your own, you may incorporate an existing path map into the new definition. As an example, define a path map named 'Episode' pointing to MyDrive\ Projects\Episode1. Then build new path maps named Renders and Stills pointing to Episode\ Renders_v1 and Episode\Stills_v1.

### Preview

Preview exists only in Fusion Studio. Within DaVinci Resolve, previews rely on the Scratch Disk setting found in the Media Storage preferences. The Preview preferences are where you set up the creation and playback options for preview renders.

### The Preview preferences

### Options

- Render Previews Using Proxy Scaling: When ticked, this option shrinks the images down to preview size for the Loader and Creator tools, which renders far quicker. Leave it off and frames render at full size before being scaled down.
- Skip Frames to Maintain Apparent Framerate: When ticked, frames get dropped while Flipbooks and file sequences play, holding the frame rate setting steady.
- Show Previews for Active Loaders: This setting decides whether the preview playback controls appear beneath the Inspector once a Loader carrying a valid file is activated.
- Show Previews for Active Savers: This setting decides whether the preview playback controls beneath the Inspector appear once a Saver carrying a valid file is activated.
- Display File Sequences On: This setting decides which viewer or external monitor handles the interactive and file sequence playbacks, plus the scrubbing function within the bins.

### QuickTime

The QuickTime preferences exist only in Fusion Studio on macOS. These settings establish the default QuickTime codec settings for when you choose QuickTime as the rendering file format in the Saver node.

### The QuickTime preferences

- Compressor: This drop-down menu lists the QuickTime codecs your computer makes available. At startup Fusion checks each codec, and so a codec may be left out when those checks find it unfit for use inside Fusion.
- Quality: This slider governs how much compression the codec applies. Raise it and images grow clearer while files grow bigger. The Quality setting isn’t honored by every codec.
- Key Frame Every X Frames: Ticked, this has the codec lay down key frames at the interval you set. Since key frames aren’t compressed against earlier frames, seeking to them in the finished movie is faster. The key frame setting isn’t honored by every codec.
- Limit Data Rate To X KB/Second: Ticked, this caps the rendered file’s data rates at the amount you name. Not every codec supports this option. Where it applies, enter the data rate that limits the QuickTime in kilobytes (kB) per second. Leave the Limit Data Rate To option unticked and this control does nothing.
