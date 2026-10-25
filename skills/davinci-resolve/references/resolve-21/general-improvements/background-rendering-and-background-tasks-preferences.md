# Background rendering and background tasks preferences

Version: DaVinci Resolve 21 New Features Guide. Context: General improvements.
[Chapter index](INDEX.md)
<a id="source-background-rendering"></a> <a id="source-background-tasks-preferences"></a> <a id="source-codec-support"></a> <a id="source-expanded-data-burn-in-window"></a> <a id="source-general-improvements"></a> <a id="source-general-improvements-1"></a> <a id="source-multi-user-projects-support-dynamic-project-switching"></a> <a id="source-searchable-preferences-and-project-settings"></a> <a id="source-the-data-burn-in-window"></a> <a id="source-the-resulting-burn-in-fields-on-the-frame"></a> <a id="source-up-to-3x-faster-file-sync-performance-to-blackmagic-cloud"></a>

### General Improvements

### Background Rendering

Certain heavy, compute-bound operations can now be rendered in the background within DaVinci Resolve 21. The operations eligible for background rendering at present are Background renders, quick exports and proxy generation. Transcription and audio classification analysis can likewise be pushed to the background. Once an operation shifts into the background, you stay free to carry on with other work inside the Resolve interface rather than sitting idle until that first operation wraps up. Since background rendering can still consume a lot of compute, it may bog your machine down to an unacceptable degree depending on your workstation's processor, ram, data throughput and the like. For that reason, Background Rendering ships disabled by default. As background tasks run, a pop up along the bottom toolbar lets you keep an eye on how they are progressing. You manage Background Rendering from DaVinci Resolve > Preferences > System > Background Tasks.

### Background Tasks preferences

- Background Render: The Background Rendering parameters are governed by these options. Enable background renders: Ticking this box switches Background Rendering on; clearing it switches it off. Pause background renders on foreground activity: Tick this box and the background processes pause whenever you are actively interacting with the DaVinci Resolve interface. That frees up your full computer power for the work at hand while letting background processing resume the moment you stop.
- Tasks Options: With these options you decide which operations are rendered in the background. Transcription: Tick this box to push transcription tasks into the background. Proxy Generation: Tick this box to push proxy generation tasks into the background.

### Expanded Data Burn-In Window

For DaVinci Resolve 21 the Data Burn-In window has been reworked to give you more power and flexibility over both the Burn-In fields themselves and where they sit. You still reach the Data Burn-In window at Workspace > Data Burn-In, and you'll need to pick either the Project or Clip tabs up top. Picking the Project tab applies the Data Burn-In across every clip in your timeline. Picking the Clip tab confines the Data Burn-In to just the selected clip.

### The Data Burn-In window

Three columns make up the Data Burn-in Window. Choosing the Metadata fields that go into your burn-in happens in the leftmost column. It carries a list of common fields, plus a search box for narrowing the results, and the icon that sorts them alphabetically either up or down. Just click the "+" icon to push that field into the middle Burn-In Fields column.

Burn-In Fields is the middle column, and it lets you tailor and format precisely what data the field returns. Any blend of typed-in text, metadata fields drawn from the left column, and other custom metadata tags is fair game for any metadata field. For custom metadata tags, begin by typing the "%" sign, then start spelling the name of the metadata field you're after. A dropdown selection surfaces as you type, and you simply click the name of the exact field you want. Every Field carries its own off-on toggle, and a master on-off toggle sits at the top of the column. Clicking the Add button drops in new blank fields. Select a field and you can set its Overlay Controls within the right column. Those Overlay Controls let you tune the font format and where the Burn-In Field lands in the frame.

- Display Length: Governs the duration the field stays on screen. Pick the Entire Clip, or pick Frames when you want to dial in a custom length.
- Display During: Selecting Frames under Display Length switches these controls on. Tick the First and / or Last boxes and key in a length in frames to govern when, and for how long, the field shows.
- Font: Choose the typeface of the field.
- Size: Controls the size of the font.
- Alignment: Choose either Left, Center, or Right text justification of the field.
- Color: Opens a color picker to choose the color of the font.
- Text Opacity: Choose the level of font transparency.
- Background Color: Brings up a color picker for setting the field's background color.
- Background Opacity: Choose the level of background transparency.
- Placement: Click whichever icon matches where you'd like the field placed within the frame.
- Position X/Y: Type in a number, or drag within the field, to place the Burn-In wherever you want it in the frame.

Hit the Save button to put the Burn-In into effect.

### The resulting Burn-In fields on the frame

TIP: For a logo image in a burn-in field, bring in a logo metadata from the left column. Next, click the Import button over in the Overlay Controls and choose the image. The remaining Overlay Controls let you move the image where you want it.

### Searchable Preferences and Project Settings

DaVinci Resolve 21 brings search bars to the Preferences and the Project Settings alike. Now you can quickly track down a given setting without needing to know its spot in the settings hierarchy. To search, begin typing the setting you're hunting for into the search bar. As you type, a list of likely matches appears underneath. Click the setting name you want and you're taken straight to that setting's page. The setting itself also flashes briefly so it's easier to spot. Begin typing your setting in the search bar, then choose one from the list shown below. You land on that setting's page with it highlighted for easy locating.

### Multi User Projects Support Dynamic Project Switching

Dynamic Project Switching now works with multi-user projects too. Loading every project into RAM at once means you can copy/paste between several projects on the spot. To read more about Dynamic Project Switching, turn to Chapter 3, "Managing Projects and Project Libraries" within the DaVinci Resolve Reference Manual.

### Up to 3x Faster File Sync Performance to Blackmagic Cloud

DaVinci Resolve 21 delivers a sizable threefold jump in how fast files sync to Blackmagic Cloud.

### Codec Support

True to form, every fresh DaVinci Resolve release brings additional codecs that keep pace with the newest cameras and technologies.

- Enhanced, extended and faster MXF growing file support for broadcast workflows.
- MXF OP1a support for MPEG-2 bitrate and other encode options.
- Canon CR3 decode support and RAW control.
- Fujifilm RAF decode support and RAW control.
- Apple ProRAW decode support.
- Improved Nikon NEF decode support.
- Improved Sony ARW decode support.
- Improved EXIF metadata support for stills formats.
- HDR Vivid supplementary IMF ISXD package support.
- MainConcept H.265 and MV-HEVC 4:2:0 and 4:2:2 encode support.
- Intel QuickSync H.264 4:2:2 and AVC intra decode support.
- Intel QuickSync AV1 4:4:4 encode support.
- MV-HEVC decode support on Nvidia systems.
- Encode support for multi-output audio only ambisonic formats.
- Windows ARM H.265 4:2:2 10 bit decode support for DaVinci Resolve
- Per render job option to override RCM or ACES outputs.
- HEIF encode support on macOS and Windows.
