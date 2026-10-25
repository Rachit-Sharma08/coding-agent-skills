# Basic documentation terminology and what is the UI or gui

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the DaVinci resolve user interface.
[Chapter index](INDEX.md) / [Next section](single-and-dual-monitor-edit-layouts.md)
<a id="source-about-keyboard-shortcuts"></a> <a id="source-adjusting-the-size-of-different-panels"></a> <a id="source-basic-documentation-terminology"></a> <a id="source-beforeafter-expanding-the-keyframe-editor"></a> <a id="source-beforeafter-resizing-ui-regions"></a> <a id="source-customizing-the-davinci-resolve-interface"></a> <a id="source-panels-and-panel-focus"></a> <a id="source-showing-and-hiding-panels-in-the-workspace-submenu"></a> <a id="source-showing-and-hiding-panels-using-the-interface-toolbar"></a> <a id="source-using-the-davinci-resolve-user-interface"></a> <a id="source-using-the-davinci-resolve-user-interface-part-1"></a> <a id="source-what-is-the-pointer"></a> <a id="source-what-is-the-ui-or-gui"></a> <a id="source-working-full-screen-vs-within-a-floating-window"></a>

### Using the DaVinci Resolve User Interface

Here you'll find a tour of the implicit rules and ways of interacting that the DaVinci Resolve graphical user interface (GUI) relies on. Topics covered include the manner in which the buttons on your mouse, pen and tablet, or trackpad get used by the assorted windows and interface widgets, the way commands are spread across the program through the menu bar, contextual menus, and option menus, plus how you work with fields and the rest of the controls. A number of these rules line up with the familiar interface behaviors of your platform's file system and of other media tools, yet a few are particular to DaVinci Resolve, which is why even seasoned users of other software will benefit from a read-through.

### Basic Documentation Terminology

For those completely new to the software, here's a quick note on a few foundational terms this manual uses.

### What Is the “UI” or “GUI”

Throughout these docs, UI is shorthand for “user interface,” and GUI stands for “graphical user interface.” Both point to the windows, screens, and controls through which you do your creative work in DaVinci Resolve. There's no shame in not having known that; this is a far more common question than you'd expect.

### What Is “the Pointer”

Any time you see “the pointer” mentioned here, it means the arrow on your screen that you use for clicking interface elements, whichever device happens to be driving it: a mouse, trackpad, pen and tablet, trackball, or anything else. Given how many distinct ways exist to operate a computer, calling it merely “the mouse” would be misleading.

### About Keyboard Shortcuts

Every keyboard shortcut in this manual is written in the macOS style, using the Command key and the Option key. So that things stay consistent on Windows and Linux, no default shortcut maps to the macOS Control key (you can still bind it yourself when customizing shortcuts). Wherever macOS uses the Option key, Windows and Linux substitute the ALT key, and wherever macOS uses the Command key, those platforms substitute the Control key.

### Customizing the DaVinci Resolve Interface

At a glance the DaVinci Resolve interface might look fairly rigid, but in practice it offers plenty of ways to shape the panels on each page around how you personally work.

### Working Full Screen vs. Within a Floating Window

Based on your preferred workflow, you can run DaVinci Resolve inside a floating window whose title bar lets you resize, reposition, minimize, and run it next to other windows. Alternatively, picking Workspace > Full Screen drops DaVinci Resolve into Full Screen mode, in which the title bar vanishes and the program fills the entire span of your monitor. Someone editing across several apps at once might lean toward the windowed approach. Colorists and mixers often gravitate to Full Screen mode, since it removes the pale title bar that some people find distracting and frees up a sliver of extra space for everything else on screen.

### Panels and Panel Focus

A DaVinci Resolve page is built from several panels. Every panel gathers the controls and readouts tied to one slice of that page's job. Take the partial screenshot below of the upper Media page: the Media Storage panel is for browsing files, the Viewer panel is where you watch video, and the Audio panel shows playback level through a bank of audio meters. Though each panel carries its own set of controls, all of them live inside the one main window of the DaVinci Resolve user interface.

A trio of panels lined up across the Media Page: Media Storage, the Viewer, and the Audio panel Whichever panel you're using takes on “focus”: clicking any item or control inside a panel promotes it to the active panel, and that routes the keyboard shortcuts shared by many panels to whichever one you're currently in. To make the focused panel visible, switch on the “Show focus indicators in the User Interface” checkbox found in the UI Settings panel of the User Preferences. With it enabled, a red line across the top of the active panel marks that it holds focus.

### Showing and Hiding Panels Using the Interface Toolbar

Every DaVinci Resolve page carries an Interface Toolbar stretched across its top edge. The buttons on this toolbar reveal and conceal the various functional panels so you can tackle different jobs:

- Panels that stay hidden by default can be brought up, because the majority of pages hold lots of functional panels that remain tucked away until you call for them.
- Individual panels can be toggled on and off via keyboard shortcuts you assign, giving you instant UI reconfiguration. Use the Keyboard Customization window to map those toggle shortcuts.
- You can swap which panel occupies a given spot in the UI, such as alternating between the Media Pool and Effects in the top-left corner of the Cut or Edit pages.
- Panels you have no use for can be dismissed to open up more room within the ones you're actively working in.

On the Color page, its Interface toolbar is where you tailor that page's controls A right-click anywhere on the UI toolbar surfaces two choices: “Show Icons and Labels” and “Show Icons Only.” Choosing icons only trims the clutter from the UI toolbar. The choices on offer vary from page to page, mirroring what each page is able to do.

The Edit page's UI Toolbar set to icons only, conserving space

### Showing and Hiding Panels in the Workspace Submenu

With this feature you can enable or disable panels by selecting them from the Workspace > Show Panel in Workspace drop-down menu. Which panels are listed, for instance Inspector, Media Pool, Metadata, and so on, hinges on the page you're currently in. As another option, you can give these panels their own keyboard shortcuts.

### Adjusting the Size of Different Panels

To resize neighboring panels, place the pointer on the dividing edge between any two of them and drag, which grows one panel while shrinking the other.

### (Before/After) Resizing UI regions

A handful of panels and palettes will grow larger, shifting some other portion of the UI in the process, when you click a little gray Expand button. As an example, clicking the expand button in the upper-right of the Keyframe Editor on the Color page widens the Keyframe Editor and, to make space, conceals the controls sitting in the middle.

### (Before/After) Expanding the Keyframe Editor

A few of the tall, vertical panels, including the Media Pool, Effects Library, Metadata Editor, and Inspector, can be sized to either half-display-height or full-display-height, letting you add or remove space for their contents or controls on demand. You trigger this with a small button on the UI toolbar that flips between expanding and contracting whichever UI element it governs.

The button for expanding a panel to full height

The button for contracting a panel to half height

The upshot is that the targeted panel either grows or shrinks. In the screenshots that follow, the Inspector of the Edit page appears first in half height mode, leaving the Timeline space to stretch out, and then in full height mode, where the Timeline gets shorter but the Inspector gains the room to display every control.

(Left) A half-height Inspector that frees space for the Timeline, (Right) A full-height Inspector that frees space for its controls
