# Project manager and preferences and project settings

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Next section](hide-page-navigation-altogether-and-media-page.md)
<a id="source-hide-pages-you-dont-use"></a> <a id="source-individual-preferences-and-settings-based-on-login"></a> <a id="source-introduction-to-davinci-resolve"></a> <a id="source-introduction-to-davinci-resolve-part-1"></a> <a id="source-minimizing-the-resolve-page-bar"></a> <a id="source-preferences"></a> <a id="source-preferences-and-project-settings"></a> <a id="source-project-manager-and-project-settings-buttons"></a> <a id="source-project-settings"></a> <a id="source-switching-among-pages"></a> <a id="source-switching-pages-using-keyboard-shortcuts"></a> <a id="source-system-preferences"></a> <a id="source-the-project-manager"></a> <a id="source-user-preferences"></a>

### Introduction to DaVinci Resolve

Within one application that does not take long to pick up, DaVinci Resolve brings together a full sweep of disciplines: editing; compositing and motion graphics; color correction; the recording and mixing of audio; and finishing. Seasoned artists arriving from other programs will recognize the editing, compositing, grading, and audio tools in DaVinci Resolve right away, while those new to post-production will still find them welcoming. On top of that, a set of purpose-built on-set tools folds jobs like media duplication, shot and metadata organization, and on-location look management into one cohesive toolset, carrying you seamlessly from the camera original media captured in the field through to organizing and using that footage across a broad spread of post‑production pipelines, all centered on DaVinci Resolve. Because DaVinci Resolve is woven together so tightly, you can glide from one stage of your project to the next without a hitch — backing up and sorting a shoot’s media, then plunging straight into the cut, ducking over to drop in a fast composite or grade a handful of clips mid-edit, hopping back to cutting, and adding a touch of mixing to confirm the sound holds up, none of it asking you to export the project or launch another program. You can push further still: the collaborative features of DaVinci Resolve let several artists — an editor, a colorist, and assistants, say — share one timeline at the same moment, the very height of an integrated workflow. Naturally, no post-production professional works in isolation, and DaVinci Resolve smooths the handoff with other facilities by importing projects and exporting project exchange formats plus rendered or managed media. Among the programs it interchanges with are these: Apple’s Final Cut Pro X; Premiere Pro from Adobe; Media Composer and Pro Tools by Avid; Autodesk’s Flame Premium; and a good many more — all riding on solid XML, AAF, and EDL import and export support. What this chapter sets out to do is walk you through the DaVinci Resolve user interface (UI): where each cluster of features sits, and how the sharply focused, closely knit Media, Edit, Fusion, Color, Fairlight, and Deliver pages work in concert so you can take on just about any post‑production workflow you might dream up. After this quick tour, the rest of Part 1 digs much deeper into project management, preferences, project settings, and other subjects worth knowing as you get under way.

### The Project Manager

For the majority of people, the Project Manager is the very first window that greets them on launching DaVinci Resolve. It acts as one central hub for handling every project owned by whoever is signed in at the moment — that person’s name shows up in the project title bar over at the top right. Through the Project Manager you also bring projects into and send them out of DaVinci Resolve, whether shuttling them between users or moving them from one DaVinci Resolve workstation onto another. On top of all that, the Project Manager, by way of the Project Library sidebar, lets you arrange the project libraries that DaVinci Resolve uses to keep track of everything. Double-click any project to open it. For a fresh one, double-click the Untitled Project icon or press the New Project button.

Every project owned by the signed-in user is on display in the Project Manager. To dig deeper into the Project Manager, turn to Chapter 3, “Managing Projects and Project Libraries.”

### Preferences and Project Settings

After a project is open, you may tune the System and User Preferences that steer how DaVinci Resolve is installed on your workstation, along with the Project Settings that steer the project currently open. The installer’s onboarding questions already pick the weightiest of these settings when you first install DaVinci Resolve. Still, on your very first launch of DaVinci Resolve it is wise to look these over and confirm they suit your system.

### Individual Preferences and Settings Based on Login

Beginning with DaVinci Resolve 16, every login account on a given computer carries its own preferences and settings. So several artists can each keep a personal login, and DaVinci Resolve holds onto distinct workspace layouts and preference states per artist, swapping them according to who is signed in.

### Preferences

Split into System preferences and User preferences panels, the Preferences window is where you shape the broad environment of your DaVinci workstation — deciding which hardware DaVinci Resolve should use and which user interface settings you favor while working.

The DaVinci Resolve preferences let you set up your environment

Below you will find a brief rundown of the System and User preferences that matter most, plus pointers on which settings to tackle first as you get DaVinci Resolve going on your workstation. For the full picture and further detail, though, consult Chapter 4, “System and User Preferences.”

### System Preferences

Through the System preferences you set up the hardware that DaVinci Resolve talks to. Should your rig stay much the same over time, you may scarcely open the Preferences window at all. But if you run a mobile setup whose video interfaces, control panels, and scratch volumes keep shifting, you will likely turn to this window far more often. NOTE: Alter certain core System Settings in the Preferences and you may need to quit and relaunch DaVinci Resolve before those changes kick in. Memory and GPU Offers an array of options that govern how the GPUs in your computer get used and how Viewers are configured across the various pages. For reference, this panel also lays out every hardware and computer trait that bears on DaVinci Resolve running smoothly, the installed GPUs among them. Media Storage Here sits a list in which you spell out the scratch disk your system relies on. Because the first volume on this list holds Gallery stills and cache files, you will want to point it at the fastest connected storage volume. Decode Options These controls let you pick from assorted hardware options for decoding RAW files along with H.264/H.265. They also let you turn on the easy DCP decoder and the option to refresh growing files (those still being written) inside the Media Pool. Video and Audio I/O The settings in this panel decide which video and audio Capture and Monitor interfaces DaVinci Resolve draws on at your workstation. Where several Blackmagic Design I/O interfaces are hooked up, you get to choose among them. Video Plugins Any third-party Open FX plugins you have installed show up here, ready to be enabled or disabled. Audio Plugins Likewise, installed third-party VST plugins appear here for you to enable or disable. Control Panels Lets you select and, if need be, configure a connected control panel for use while grading in DaVinci Resolve.

General Gives you a spread of settings that tweak how DaVinci Resolve behaves. By way of the LUT Locations section you can direct DaVinci Resolve to whatever external folders hold the LUTs your project needs. Internet Accounts This panel acts as a login manager for the Blackmagic Cloud and various social media sites. Advanced You turn to this tab for special DaVinci Resolve configurations and for SAN parameters that pertain to older file systems.

### User Preferences

User preferences steer how the user interface in DaVinci Resolve is set up, so you can shape it to suit your taste. UI Settings Up top, a Language drop-down menu lets you state which language the DaVinci Resolve user interface shows. At present DaVinci Resolve handles English, Chinese, Japanese, and Spanish, Portuguese, French, Russian, Thai, Vietnamese, and Korean. Further checkboxes let you set which project opens at startup and how the Viewers on each DaVinci Resolve page are configured. Project Save and Load Here live the crucial auto-save controls, the Live Save option among them, which has Resolve save your work incrementally as you go. Editing A host of controls on this panel let you tailor the editing experience on the Edit page — defaults for building new timelines, plus general settings that rule standard effects durations and trim behaviors. Color This set lets you tailor grading on the Color page, offering control over video scope display, how UI overlays look, and assorted other color-specific functions. Fairlight Here you tailor editing on the Fairlight page by way of options for video offset, automation, and general settings. Playback Settings With these you shape how DaVinci Resolves handles video playback; when playback drags, adjusting them can sometimes help. Control Panels These let you tune the settings of whatever control surface you have attached. Metadata And these let you tune the Metadata Presets.

### Project Settings

After a project exists, every setting specific to it lives in the Project Settings window. Open that window by clicking the gear button down in the lower right of any page.

### Project Manager and Project Settings buttons

The Project Settings appear centered on screen, broken into a run of panels you pick from a sidebar on the left. Each panel gathers a set of related settings touching some category of DaVinci Resolve functionality. To bring up any panel, just click its name in that left-hand sidebar.

The Project Settings show all project-specific settings and attributes.

A project’s chief attributes — timeline resolution, timeline frame rate, color science, and bit depth — are laid down in the Master Settings. The Image Scaling settings dictate how clips whose size differs from the timeline resolution get scaled to fit. Additional panels cover Color Management, Camera Raw, Capture and Playback, and so on. For fuller detail on Project Settings, see Chapter 4, “System and User Preferences.”

### Switching Among Pages

Down at the bottom of the UI you will find the buttons that switch between pages. DaVinci Resolve breaks into seven principal pages of functionality, each serving a distinct specialty of the usual post production workflow, and each reachable through buttons along the very bottom of the DaVinci Resolve interface. Laid out in workflow order and always within reach, these buttons let you jump in a structured way from importing media to fast editing, detailed editing, compositing, grading, audio mixing, and finally outputting your project.

### Minimizing the Resolve Page Bar

Right-click anywhere inside the Resolve Page bar along the bottom of the DaVinci Resolve UI and a contextual menu offers two choices: “Show Icons and Labels” and “ Show Icons Only.” Opt for icons only and the Resolve Page bar down below occupies less space.

The Page bar showing icons only, to save space

### Switching Pages Using Keyboard Shortcuts

Pages can likewise be changed with the keyboard shortcuts listed here, all of which you can look up under the Workspace > Switch to Page submenu.

### Hide Pages You Don’t Use

It is possible to keep the page navigation bar in view while hiding only the buttons for certain pages. As an example:

- Perhaps you value this bar’s quick navigation yet there are pages you have no intention of touching
- Or perhaps you are configuring a DaVinci Resolve workstation for an artist with a narrow role on a

project, and you would rather hide ready access to pages of functionality they will not (or should not) be touching; this proves handy on collaborative workflow projects in particular. Each page’s buttons can be switched off or back on through the Workspace > Show Page submenu. Any effects and adjustments applied on hidden pages keep right on shaping the current project — they are merely out of sight — and you can still reach them via the Workspace > Switch to Page submenu commands or the keyboard shortcuts.
