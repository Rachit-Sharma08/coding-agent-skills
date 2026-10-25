# List panel of the adr interface and record panel

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](separate-bin-windows-and-color-filters.md) / [Next section](preview-and-audition-controls-and-sound-effect-list.md)
<a id="source-choosing-a-library-to-search"></a> <a id="source-display-controls-and-the-search-field"></a> <a id="source-library-controls"></a> <a id="source-literal-searches"></a> <a id="source-orandnot-searches"></a> <a id="source-sound-library-browser"></a> <a id="source-the-list-panel-of-the-adr-interface"></a> <a id="source-the-record-panel"></a> <a id="source-the-record-panel-of-the-adr-interface"></a> <a id="source-the-search-field-and-filter-by-menu"></a> <a id="source-the-setup-panel"></a> <a id="source-the-setup-panel-of-the-adr-interface"></a> <a id="source-the-sound-library-panel"></a>

### The List panel of the ADR interface

### The Record Panel

Here is where you actually carry out the ADR recording session you've prepared, working from the dialog cues you placed in the Cue list. It offers controls for showing and choosing which cues to record, for previewing and kicking off recording, and for attaching metadata to rate the various takes you've captured and to track which cues are done.

### The Record panel of the ADR Interface

### The Setup Panel

The Setup panel is where your ADR session gets configured. Pick your audio input, your record track, and the tracks to monitor. Then reach the beeps, video streamers, and onscreen text the actors will watch on the video output display to help keep their performance on time.

### The Setup panel of the ADR interface

For more on working with the ADR panel, refer to Chapter 174, “ADR (Automated Dialog Replacement).”

### Sound Library Browser

You reach a Sound Library panel from the Interface toolbar to browse the sound effects libraries you have at hand, whether on your own system or on network storage you're attached to (a SAN, for one). It can scan file paths you specify to catalog the sound files it finds along with their metadata, tucking that data into the currently chosen project library (or any other project library you point it at) for later use when you go hunting your library for the right sound effect. Once your sound effects collection is cataloged, searching for sounds, previewing the hits in the list, and cutting your favorite into the Timeline all come easily. TIP: You can grab the Fairlight sound library — a royalty-free set of over 500 professionally recorded foley sounds free for your own projects — straight from the Sound Library panel. The Fairlight sound library spans everything from atmospheric ambient beds to foley such as foot steps, hits, effects, and the like. This free sound library is built to pair with the Fairlight FX Foley Sampler plugin, which lets a MIDI keyboard trigger sounds so they land at exactly the right instant in your program.

### The Sound Library panel

### Library Controls

Clicking the Library button (to the right of the Search field) brings up a menu where you pick which project library handles searching (and cataloging) of sound effects collections. Every network project library can hold its own catalog. NOTE: The Sound Library results pane stays empty until you run a search. The Sound Library can lean on the Mapped Mount option in the Preferences' Media Storage panel to reach sound effects sitting on remote volumes run by other operating systems.

### Choosing a library to search

To catalog every audio file inside a given file path so the Sound Library can search them: 1 With the Project Manager, build an empty network project library to hold the sound effects catalog. 2 Open a project, go to either the Edit or the Fairlight page, and then bring up the Sound Library. 3 (Optional) Press the Library button (sitting to the right of the Search field), then choose the project library you built from the dropdown menu that appears. By default the current project library is chosen. When you're inside a local project library instead, the highest compatible project library on the list becomes the default. 4 Do one of these: a) When no library of sound effects is connected yet, an Add Library button shows in the middle of the Sound Library. Click it, and from the file dialog that opens, choose the top-most directory of a file path holding sound effects; pick a directory with subdirectories inside and each one gets checked for content. b) When you're adding more sound effects to a library that already exists, click the Option menu and pick Add Library. From the file dialog that opens, choose the top-most directory of a file path holding sound effects; pick a directory with subdirectories inside and each one gets checked for content. 5 Click Open. A progress bar reports how long the job will run. Once it's done, a dialog tells you how many clips landed in the current library.

### Display Controls and the Search Field

The Sound Library title bar carries controls for ordering the sound effects list, for showing it in List or Icon view, and an Option menu holding assorted other settings and commands.

Display controls give you a say in how the Sound Effects list's contents get shown

Below that, a text field takes your search terms, while a dropdown menu off to the right lets you decide whether to comb the current project library for sound effects by name, by description metadata, or by all.

### The Search field and Filter By menu

To hunt down a particular sound effect and cut it into the Timeline:

- Enter a search term in the Search field. Letter case in your terms is disregarded, save for boolean operators.

To help you weed out false positives, the search field copes with a range of search styles: literal searches, then and/or/not boolean searches, plus wildcard searches, as well as character ranges. NOTE: For Boolean searches, the Boolean operators have to be typed entirely in upper caps, as in “AND,” “OR” and “NOT.” Type them lower case and “and,” “or” and “not” count as plain search words instead.

### Or/And/Not Searches

Just typing words split by spaces runs as a string of OR searches, each word looked for on its own, whether as a standalone or buried inside another word. For instance, type either of these: car door car OR door and you get the same hits. Every sound effect in your library that holds the letters “car” or “door” (or both) turns up, regardless of whether those letters stand alone or sit inside other words. Hits will take in files like “CarExDoorClose,” “Doormouse_Squeak,” “Carburetor dropped on cement,” and “Carpet Shake.” AND (which has to be upper caps) lets you stack multiple criteria onto a search, so each returned file must hold every word you type somewhere inside, in whatever order. For instance, type: car AND door and every sound effect in your library carrying both the strings “car” and “door” shows, whether those words appear alone, together, or tucked within other words, like “NewCarDoorSlam” and “Carpet_Footsteps_Indoors,” and “GarageDoorHitsCar.” NOT lets you drop sound effects that hold a given word. For instance, type: car NOT door and only sound effects with “car” surface, while every sound effect with “door” is dropped.

### Literal Searches

Quotation marks call for a literal search of just the named term, set off from surrounding text by a space. For instance, type: “cat” and every sound effect in your library carrying the lone word “cat” shows up. Sound effects with “cats” and “caterpillar” drop out. Hits will take in “Space cat drone” or “Cat meowing.” Wildcard and Range Searches The _ (asterisk) calls for a wildcard search across any number of characters. Drop an _ between two search terms and it finds any sound effect where those two terms are joined by any number or mix of characters with no spaces (even none at all). For instance, type: close*door and the hits cover “Door-Wood Cheap-Wooden-Closet-Door-Kick-In-Flimsy-Rattle,” as well as “ElevatorCabinCloseDoor,” plus “LatchSwingCloseSqueakDoorSecur.” Type instead: door*close and the hits take in “DoorHvyMetalCloseSlam,” “DoorLidWoodenChestCloseAntique,” and “ElevatorDoorCloseSlam.” Type instead: c\*r and the hits take in “lectrohummin,” “KiaShumaEXTBootCloseTrunkaka,” and “Ambience with Piana, Louder.” The ? (question mark) calls for a wildcard search of just one character. However many question marks you type sets how many wildcard characters get matched. For instance, type: door?close and you may turn up nothing at all, unless a sound effect named “door-close” exists. Yet type: door????close and the hits take in “DoorWoodClose,” since wood runs four letters, matching the count of wildcard letters you set. TIP: Typing “\*\*\*” surfaces every file in your Sound Library
