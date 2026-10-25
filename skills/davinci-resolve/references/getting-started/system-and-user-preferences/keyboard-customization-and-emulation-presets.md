# Keyboard customization window and choosing keyboard shortcut emulation presets

Version: DaVinci Resolve 20.3 Reference Manual. Context: System and user preferences.
[Chapter index](INDEX.md) / [Previous section](general-settings-and-automation.md) / [Next section](command-key-remapping-and-extras-manager.md)
<a id="source-choosing-keyboard-shortcut-emulation-presets"></a> <a id="source-managing-keyboard-mappings"></a> <a id="source-panel-specific-keyboard-mappings"></a> <a id="source-searching-for-keyboard-shortcuts"></a> <a id="source-system-and-user-preferences-part-4"></a> <a id="source-the-keyboard-customization-window"></a> <a id="source-viewing-commands-assigned-to-specific-key-combinations"></a>

### The Keyboard Customization window

### Choosing Keyboard Shortcut Emulation Presets

A drop-down at this menu’s top right lets you pick the default DaVinci Resolve set or any of the others that aim to imitate other NLEs you may know better. Keep in mind that shortcuts can be remapped only to commands that genuinely exist inside DaVinci Resolve, so where a given feature of another NLE has no counterpart here, that key shortcut might not map the same way. Happily, DaVinci Resolve’s editorial feature set overlaps heavily with what’s common across other NLEs, so most of the features you’re accustomed to should have a working equivalent.

You can settle on one of the preset keyboard mappings to imitate an NLE you know or fall back on the default DaVinci Resolve keyboard mapping.

You can likewise put together your own custom sets of keyboard shortcuts. The Commands list underneath presents a tiered roster of commands grouped by the menu each lives in. From this list you select individual commands to remap, and you can search it whenever the item you’re after proves hard to spot. More detail on that follows later in this section.

### Viewing Commands Assigned to Specific Key Combinations

To learn which command a given key is bound to, click whatever combination of modifier and ordinary keys you like on the window’s virtual keyboard up top. The keys you’ve currently chosen show their binding in the “Active Key” list beneath. Choosing keys and modifiers on the virtual keyboard surfaces their command mapping below TIP: From DaVinci Resolve 15.2 onward, a command can carry several keys or key combinations, and the number keys on an extended keyboard’s numeric keypad can be bound separately from the keys along the top row.

### Panel-Specific Keyboard Mappings

As you customize shortcuts, you can bind one to the “Application” so it behaves the same throughout every applicable corner of the DaVinci Resolve UI, or you can map a particular shortcut to fire a particular command inside one specific panel.

Shortcuts can now be bound per panel, so one shortcut may carry out a different action in each panel that holds it

Panel-specific shortcuts let a single key behave differently depending on which panel holds focus; one key, for instance, might trigger separate actions in the Media Pool, do something else again in the Edit Timeline, and act differently still in both the Metadata Editor and the Sound Library — to cite a handful of Edit Page cases. That brings huge flexibility, yet taking this path means you have to keep track of which panel has focus. Helpfully, from DaVinci Resolve 15.2 onward, focus is flagged by a colored highlight along the top of each panel.

### Searching for Keyboard Shortcuts

Whether you want to survey the available shortcuts or track down a single command to customize, a Search field sitting above the Commands list lets you search whichever command group you choose (All Commands included). To hunt down specific keyboard shortcuts: 1 Pick DaVinci Resolve > Keyboard Customization. 2 From the Commands list, pick a command group to search inside. To comb through the whole of DaVinci Resolve, pick “All Commands.” 3 Enter a term in the Search field, and the Command/Keystroke list refreshes to display whatever commands fit the criteria you typed.

With “All Commands” chosen, running a search that turns up every shortcut tied to the word “ripple”

### Managing Keyboard Mappings

From the Option menu within the Keyboard Customization menu, DaVinci Resolve offers these ways to build and manage keyboard mappings:

Through the Keyboard Customization window’s Option menu you can export, import, and remove keyboard mappings

- To build a fresh keyboard mapping: Pick an existing mapping from the drop-down as the basis to begin from, select Save As New Preset under the Keyboard Customization Option menu, type a name for the preset into the dialog, and confirm with OK. The new preset then shows up in the preset drop-down menu.
- To save out a keyboard shortcut file so a second DaVinci Resolve workstation can use it: Pick a preset from the Export Preset submenu under the Keyboard Customization Option menu, then assign a name and folder for the new file, and click Save.
- To bring in a keyboard shortcut file: Pick Import Preset from the Keyboard Customization Option menu, point it at a DaVinci Resolve keyboard shortcut file, and click Open.
- To remove a keyboard mapping: Select the keyboard mapping preset you no longer want, then click the trash can button.
