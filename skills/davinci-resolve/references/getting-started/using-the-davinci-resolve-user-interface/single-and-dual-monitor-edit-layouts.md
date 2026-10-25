# Single vs dual monitor layouts and edit page in dual screen mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the DaVinci resolve user interface.
[Chapter index](INDEX.md) / [Previous section](basic-documentation-terminology-and-what-is-the-ui-or-gui.md) / [Next section](virtual-sliders-and-numeric-keyboard-editing.md)
<a id="source-a-floating-media-pool-window"></a> <a id="source-adjusting-parameters"></a> <a id="source-contextual-menus"></a> <a id="source-davinci-resolve-user-interface-conventions"></a> <a id="source-drop-down-menus"></a> <a id="source-mode-drop-down"></a> <a id="source-option-menus"></a> <a id="source-resetting-to-the-default-layout"></a> <a id="source-saving-custom-screen-layouts"></a> <a id="source-selecting-a-monitor-for-full-screen-display"></a> <a id="source-sliders-and-dials"></a> <a id="source-the-edit-page-in-dual-screen-mode"></a> <a id="source-the-edit-page-in-dual-screen-timeline-mode"></a> <a id="source-undocking-specific-panels-of-the-interface"></a> <a id="source-using-single--vs-dual-monitor-layouts"></a> <a id="source-using-the-full-screen-timeline-option-in-the-edit-page"></a> <a id="source-video-clean-feed-studio-version-only"></a> <a id="source-video-scopes-in-a-floating-window"></a> <a id="source-virtual-sliders-and-fields"></a>

### Using Single- vs. Dual-Monitor Layouts

You move the Media, Edit, Color, and Fairlight pages between single-screen and dual-screen layouts by selecting Workspace > Dual Screen > On. A dual-screen layout puts far more controls in view simultaneously, typically across a wider workspace that helps you handle more clips, more Gallery stills, and the like. You can resize the second display of a dual-screen layout, though you can't rearrange it. Owners of a single ultra-wide monitor can adopt the dual-monitor layout too, and DaVinci Resolve will scale its interface as though two ordinary monitors sat side by side.

### The Edit page in Dual-screen mode

While in Single-screen mode, you decide which monitor presents the DaVinci Resolve UI through Workspace > Primary Display > (Monitor Name). While in Dual-screen mode, the same command swaps what each of the two monitors shows.

### Using the Full Screen Timeline Option in the Edit Page

When you're on the Edit page in Dual-screen mode and want the largest possible timeline for cutting through your program, selecting Workspace > Dual Screen > Full Screen Timeline reveals a layout that devotes one whole screen to a single oversized timeline while parking every other Edit page panel on the second display.

### The Edit page in Dual-screen Timeline mode

### Video Clean Feed (Studio Version Only)

You can now drive a full-screen Viewer onto a second monitor wired straight to your computer. Turn this monitor on by choosing Workspace > Video Clean Feed and then picking your display from the submenu.

### Selecting a monitor for full-screen display

### Saving Custom Screen Layouts

Once you've arranged a specific group of resized panels you expect to reach for repeatedly, you can store it next to any other handy screen layouts you've already kept. Ways to work with custom screen layouts: Storing a custom screen preset: Set up the various DaVinci Resolve pages for whatever you're tackling, then choose Workspace > Layout Presets > Save Layout As Preset. Give it a name in the Save Layout as Preset dialog, then confirm with OK. Recalling one you stored earlier: Choose Workspace > Layout Presets > LAYOUT NAME > Load. As many as five separate presets may be tied to keyboard shortcuts through the Keyboard Customization window (Application > Workspace > Layout Presets). Refreshing a stored preset: Pull the layout you're after from the Workspace > Layout submenu, make your edits, and finish via Choose Workspace > Layout Presets > LAYOUT NAME > Update Preset. Removing one: Choose Workspace > Layout Presets > LAYOUT NAME > Delete Preset. Sending one out so another DaVinci Resolve installation can use it: Choose Workspace > Layout Presets > LAYOUT NAME > Export Preset. Bringing one in: Choose Workspace > Layout Presets > Import Layout as Preset.

### Resetting to the Default Layout

Should the present layout not suit you and you'd rather return to the original, choose Workspace > Reset UI Layout.

### Undocking Specific Panels of the Interface

A number of interface elements have a choice: they can stay docked within their home pages, or they can pop out into their own windows.

### A floating Media Pool window

To float a Media Pool bin in its own window, just right-click the bin and pick Open As a New Window from the contextual menu. Although it looks like you're only revealing that bin's contents, what you actually get is a whole second Media Pool, including the Bin list, Browsing area, and every organizational control the docked Media Pool carries. There's no cap on how many floating Media Pools you keep open. Each one can be dragged onto other monitors and dismissed with a button at the top-left of its title bar. On the Color page, the video scopes give you an exact read on the color and contrast of your clips. Clicking the Video Scope button on the Color page toolbar shows them in their docked spot at the right of the Color page palettes.

The video scope sitting in its docked spot beside the remaining palettes along the lower Color page As an alternative, clicking the expand button at the upper-right of the video scope floats the video scopes into their own window, where you can show all four at once, or any one on its own, on whichever monitor is attached to your workstation.

### Video scopes in a floating window

On top of that, plenty of the dual-screen layouts in DaVinci Resolve include both the Audio Mixer and the video scopes. The scopes aren't confined to the Color page; they show up on the Media and Deliver pages too, for moments when you need an objective look at the video signal, like preparing to capture from tape, scan from film, or set up for output. Within the DaVinci Resolve single screen layout, the scopes can be sent to a second computer display when one exists, and they'll briefly vanish if you switch pages or move to a different application.

### DaVinci Resolve User Interface Conventions

Each chapter goes into the distinctive on-screen controls belonging to its own DaVinci Resolve page, but this section recaps how to operate several of the more widespread controls you'll run into.

### Contextual Menus

Almost every panel across every page offers extra functions through contextual menus that pop up when you right-click the relevant item. In some cases the commands you get differ based on whether you right-click a panel's empty background or land directly on an item like a still or node.

Contextual menus expose additional controls in the Color page Viewer

### Drop-Down Menus

A single click is all it takes to fire most of the buttons and drop-down menus scattered across the toolbars. As one example, a great many panels, palettes, and windows carry an Option menu shown as three horizontal dots (folks tend to call them “three dot menus,” though they're really option menus) that reveal further options or commands tied to what that panel does.

### Option menus

### Mode drop-down

What's more, a lot of panels and palettes (though not every one) carry a “Mode” drop-down in the top-right corner that lets you switch to a different category of function inside that palette. Certain buttons, like transport controls and toolbar icons, show a small downward-pointing arrow when the pointer hovers over them, signaling that a right-click opens checkmark options controlling how those controls behave.

(Left) Hovering on a button to show that it conceals a menu, (Right) Right-clicking that button to surface its options inside a drop-down

### Adjusting Parameters

In general there are several ways to change a numeric parameter.

### Sliders and Dials

Dragging a slider shifts a parameter's value within a defined range. A dial, by contrast, signals that the value can be adjusted without limit in either direction. Sliders tend to suit big, coarse moves on a parameter. The “virtual sliders” covered next are what you reach for when you want finer control.

### Virtual Sliders and Fields

Wherever a number field shows up, it doubles as a “virtual slider”: hover the pointer over it until the “virtual slider cursor” appears, then click and drag rightward to push the value up or leftward to bring it down (white arrows show which way it's heading). As a rule, a field's virtual slider gives you tighter precision than the real slider sitting to its left.

A slider and a dial with their accompanying number fields
