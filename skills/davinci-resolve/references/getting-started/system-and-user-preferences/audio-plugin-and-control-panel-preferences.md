# Audio plugins preferences available plugins and control panels

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](video-and-audio-io-preferences.md) / [Next section](internet-accounts-and-advanced.md)
<a id="source-audio-plugins-preferences---available-plugins"></a> <a id="source-control-panels"></a> <a id="source-general"></a> <a id="source-system-and-user-preferences-part-2"></a> <a id="source-the-control-panels-status-icon"></a>

### Audio Plugins Preferences - Available Plugins

- Setup External Audio Processes: While at work on the Fairlight page, you have the option to run an audio file through a third-party application when needed—say you need another app's features to build an effect or fix something the Fairlight page alone can't handle. To pull this off, you first add one or more applications to the External Audio Process list inside the Audio Plugins panel of the System Preferences.

NOTE: VST is a trademark of Steinberg Media Technologies GmbH.

Audio Plugins Preferences - Setup External Audio Processes

Here's how to register an External Audio Process: 1 Hit the Add button. 2 In the Name column, double-click the text and retitle it after whichever application or process you mean to link up. 3 Single-click within the Path column, after which the file dialog lets you track down and select the application or script that should act as your external audio process. 4 From the Type column, open its drop-down menu, then settle on the way the chosen audio process ought to behave: Reveal (open the application), Command Line (use from Terminal), or Clipboard (which copies the audio clip file path onto the clipboard, ready to paste into the open command of some application or utility). 5 When that's all set, click Save, then relaunch DaVinci Resolve should you be prompted.

### Control Panels

A pair of sections let you declare which Color Grading Panel and Audio Console is hooked to your workstation.

- Color Grading Panel: A menu lets you pick which color grading panel is hooked to your workstation. Certain panels reveal extra controls.

When you own a DaVinci Resolve Mini or Micro Panel, keep this option on None and Resolve will detect those panels on its own as you plug them in. For a control panel wired over USB, pick your panel from the list. For a DaVinci Resolve Mini Panel running over Ethernet, pick "DaVinci Resolve Mini Panel (Ethernet)" and then pick your panel from the drop-down that surfaces. When you're on a JLCooper Eclipse, pick "JLCooper Eclipse CX" and then key the IP and Port number into the fields that surface.

- Audio Console: A menu lets you pick which Fairlight Audio Console is hooked to your workstation. Certain panels reveal extra controls.
- Use MIDI Audio Console: A checkbox lets you turn on a third-party audio console wired to your workstation. Switching this on reveals three additional menus.

MIDI Protocol: Lets you pick either the HUI or MCU protocol, whichever suits the audio console you intend to use. MIDI Input: Lets you pick the MIDI input wiring your console. MIDI Output: Lets you pick the MIDI output wiring your console.

- Head Tracker: A menu lets you pick which head tracker profile to apply for immersive audio.
- Display Control Panels Status on Main Footer: Ticking this box shows the status of every

connected control panel as an icon in the interface's lower-right footer. Clearing the box hides that icon.

### The Control Panels Status icon

### General

This panel offers assorted options covering scripting, audio processing, monitoring, and submitting problem reports.

- External Scripting Using: (Resolve Studio only) The choices here are None, Local, and Network. Left at None, only scripting from within the Console window is permitted. Set to Local, external scripts and applications sharing the same computer are able to drive DaVinci Resolve. Set to Network, external scripts and applications running on other machines across the network (or over the internet) are able to drive DaVinci Resolve.
- Use 10-bit precision in viewers if available: You'll only run across this checkbox on macOS installations of DaVinci Resolve. Switching it on permits DaVinci Resolve to show 10-bit images inside the Viewer.
- Use Mac Display Color Profile for viewers: When you run DaVinci Resolve on macOS, this checkbox tells every viewer in DaVinci Resolve to adopt whichever display profile sits chosen in the Displays panel of the System Preferences. That lets DaVinci Resolve lean on ColorSync on macOS so your Viewer image ought to line up more closely with your output display.

Viewers match QuickTime Player when using Rec.709 Scene: Tick this box so the viewers fall in step with the gamma characteristics of the QuickTime player. The effect is that the Resolve Viewers and what shows in QuickTime Player line up.

- Optimize project library cloud data traffic: Should reaching the Blackmagic Cloud through a corporate firewall give you trouble, tick this box to connect without having to arrange port mapping and firewall exceptions. https://blackmagicdesign.com still has to be whitelisted for access.
- Automatically Tag Rec.709 Scene Clips as Rec.709-A: Switch this checkbox on to have any Rec. 709 QuickTime files tagged on their own for Rec. 709-A playback. The setting comes in handy where your final QuickTime video parts ways with what shows in the Resolve viewers (gamma shift), and you'd rather export for the web than for broadcast.
- Automatically Scan other project libraries for remote rendering jobs: Switch this checkbox on so every connected project library gets scanned, not merely the current project library, for possible remote rendering jobs.
- Automatically Check for Updates: Switch this checkbox on to make staying on the newest version of DaVinci Resolve simpler. You may also pick DaVinci Resolve > Check For Updates to be alerted to new versions and pull them down once available.
- Automatically opt-in for new beta program notifications: Tips you off when public beta versions of DaVinci Resolve come out, should living on the edge appeal to you.
- Send report when application quits unexpectedly: Switched on, this setting lets DaVinci Resolve draw up a problem report on its own each time DaVinci Resolve quits unexpectedly. There's some information for you to fill in (do be as exact as you can about what you were up to when DaVinci Resolve ran into its trouble) before you press a button to dispatch the report.
- Limit Presentations upload speed to X KB/s: Lets you put a firm ceiling on the upload speed while you're on Presentations, so you don't soak up all your network bandwidth.
- Use Remote Monitoring without Blackmagic Cloud: Lets you run remote monitoring across your own network rather than routing through Blackmagic Cloud.
- Use TURN server for Remote Monitoring: Where Blackmagic Cloud is something you're avoiding for security reasons, and you instead lean on a self-configured or cloud-based TURN servers that route plus relay your monitoring streams, name that server here.
- Prevent sleeping when Blackmagic Cloud sync enabled project is open: On by default, this checkbox keeps your computer out of sleep mode for as long as a Blackmagic Cloud project stays active, ensuring every online data transfer finishes. Clear the box to let your computer drop off to sleep as it pleases.
- LUT Locations: Through this interface you add or pull directories where DaVinci Resolve will hunt for LUTs to apply across the application.
