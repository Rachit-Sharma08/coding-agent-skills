# Internet accounts and advanced

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](audio-plugin-and-control-panel-preferences.md) / [Next section](load-settings-and-save-settings.md)
<a id="source-advanced"></a> <a id="source-internet-accounts"></a> <a id="source-project-save-and-load"></a> <a id="source-saving-user-preference-presets"></a> <a id="source-ui-settings"></a> <a id="source-user"></a>

### Internet Accounts

The Internet Accounts panel acts as a login manager for the Blackmagic Cloud along with other social media sites. DaVinci Resolve carries close integration with YouTube, Vimeo, TikTok, Dropbox, and Frame.io, letting you render and push files straight to each service. Buttons on this panel let you log into your YouTube, Vimeo, TikTok, Dropbox, and Frame.io accounts and also name a local cache location for media being kept in sync with Frame.io. Every service you log into brings up a floating window holding the interface where you supply your login name and password to switch on integration, then complete any twofactor identification and the remaining required steps. After you've entered them, DaVinci Resolve logs into each of these services on its own whenever DaVinci Resolve launches.

Inside the DaVinci Resolve Preferences window, the Internet Accounts panel shown under its System tab

### Advanced

You turn to this tab for special Resolve configurations together with SAN parameters that bear on older file systems.

### User

Through this panel you pick user preferences tied to your own workstation. They govern keyboard shortcut mappings, control panel action, editing and color defaults, auto save settings, plus how the UI behaves and looks. TIP: A good many of the settings sitting in the User panel once lived in the Project Settings window before version 14, yet they were relocated here to support collaborative workflows in which each user keeps their own independent general, editing, and color settings along with their own keyboard shortcuts.

### Saving User Preference Presets

You can keep several presets on hand for one-click recall of differing User Preference settings, by way of the Option menu in the UI Settings window.

Found in the Option menu of the UI Seµttings window, the commands that handle User Preference presets Ways to handle User Preference presets:

- To save a preset: Settle on whatever settings you'd like to use, then open the UI Settings window Option menu and pick Save User Preferences as Preset. Type a name in the dialog, then press OK. That preset then turns up at the head of the Option menu.
- To load a preset: Open the UI Settings window Option menu, then pick Load Preset off the submenu of whichever preset you want to load.
- To update a preset: Load whichever preset you want to edit, adjust whatever settings you need, then pick Update Preset off that preset's submenu in the Option menu.
- To export a preset: Pick Export Preset off the submenu of any preset in the Option menu. A file carrying the .userprefs extension lands at the location you picked.
- To import a preset: Pick Import User Preferences as Preset in the Option menu, work the dialog to locate the exported .userprefs preset file you want to bring in, then press Open.
- To delete a preset: Pick Delete Preset off the submenu of any preset in the Option menu.
- To reset all presets: Pick Reset User Preferences off the Option menu to put every User Preference back to its default settings.

### UI Settings

A set of operational preferences.

- Language: At the top a Language dropdown lets you name which language the DaVinci Resolve user interface shows. As things stand, the languages DaVinci Resolve handles are Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Thai, and Vietnamese.
- Reload last working project on startup: On its own reopens the last project a user had going each time that user logs back into DaVinci Resolve. You can only switch this checkbox on while editing a preset configuration in the Presets panel, so that it stays on no matter which project you open as long as you're running that particular preset.
- Use Optimized UI layouts for vertical video: Ticking this box has the UI refresh on its own to suit vertical timelines and video sources. Clearing this box keeps the normal UI whatever the video orientation.
- Show focus indicators in the user interface: Lets you switch on or off a red line atop each panel marking which panel currently holds focus.
- Use gray background for user interface: Out of the box, DaVinci Resolve runs a blue-gray UI background, meant to give a more pleasing experience to users centered on the less colorcritical sides of DaVinci Resolve, editing chief among them. Switching this checkbox on flips DaVinci Resolve over to a wholly neutral, desaturated gray UI, which can serve as a reference point for colorists worried the blue-gray UI might bias the eye amid the dark surroundings of the grading suite.
- Use gray background in viewers: Switched on, it paints the background of every viewer gray, making image blanking or slight sizing tweaks easier to judge than against the default dark background.
- Resize image in viewer to square pixels: This control picks between a square or nonsquare pixel aspect ratio inside the Viewer. It matters where you handle SD images, which lack a square pixel aspect ratio.
- Delay viewer display by X frames: Switched on, it lets you enter a count of frames by which to hold back the DaVinci Resolve Viewers as they show on your computer displays, so the image on your computer display syncs more closely with the same image shown on external displays held up by assorted signal processing processes.
- Output single field when paused: This setting cuts flicker while grading on a computer monitor or while working with interlaced material. By default, viewing interlaced material in Stop or Pause mode shows field one followed by field two. Depending on the image, that can leave a flicker on the display. With this option on, only field one shows on the monitor while playback sits paused; both fields, however, show once the clips play.
- Stop playback when a dropped frame is detected: Switched on, it tells DaVinci Resolve to halt playback any time a frame drops on output, alerting you to performance issues on your workstation. That's especially handy where you're outputting to tape.
- Stop renders when a frame or clip cannot be processed: Switched on, this stops a render the moment DaVinci Resolve spots an error in the encoding, rather than pressing on to try processing it.
- Show playhead shadow: Ticking this box switches on the playhead shadow, a transparent orange range for visually gauging that reaches a set number of frames ahead of and behind the playhead. You can tune the count of frames in the range before or after the playhead over in the Editing section of the User Preferences.
- 2D timeline scrolling: Ticking this box scrolls the Timeline vertically through all the Video or Audio tracks as you spin the mouse wheel. Clearing this box scrolls the whole Timeline horizontally as you spin the mouse wheel.
- Timeline sort order: A user setting that lets you fix the default sort order of the Timelines that show in the Viewer drop-down menus throughout DaVinci Resolve.

Alphabetic: Orders Timelines from A-Z by name. Creation Date: Orders Timelines with the oldest one made coming first. Recently Used (default): Orders Timelines according to the 10 most recently active timelines.

### Project Save and Load

Through the Project Save and Load panel you steer how projects get opened, along with how they get saved.
