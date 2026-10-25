# Metadata variables and where variables can be used

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using variables and keywords.
[Chapter index](INDEX.md)
<a id="source-assign-and-apply-favorite-keywords-to-clips-and-markers"></a> <a id="source-current-date-and-time-metadata-variables"></a> <a id="source-how-to-edit-metadata-variables"></a> <a id="source-keyword-dictionary"></a> <a id="source-the-keyword-dictionary"></a> <a id="source-using-keywords"></a> <a id="source-using-metadata-variables"></a> <a id="source-using-variables-and-keywords"></a> <a id="source-using-variables-and-keywords-1"></a> <a id="source-where-variables-can-be-used"></a>

### Using Variables and Keywords

The subject of this chapter is putting metadata variables and keywords to work as a way of keeping your clips organized.

### Using Metadata Variables

If clip metadata is something you embrace with enthusiasm (and you really ought to), then “metadata variables” are at your disposal: drop them into the text fields that support them and they’ll pull in other metadata belonging to that clip. As one illustration, you might enter the mix of variables and text shown in the screenshot below. Once entered, variables show up as graphical tags set off by a background, whereas any plain text characters you type sit ahead of and behind those tags.

Variables alongside text characters typed in to build a display name off of a clip’s metadata The upshot is that this clip would show “12_A_3” as its name provided scene “12,” shot “A,” and take “3” made up its metadata. While doing this, you’re free to blend metadata variables with whatever other characters you like (the underscore, like in the example above) to shape the metadata so it reads more clearly. Keep in mind that on clips where a referenced metadata field has nothing in it, that variable’s tag simply produces no characters at whatever spot it sits.

### Where Variables Can Be Used

Metadata variables bend to your needs and let you procedurally feed metadata into a number of DaVinci Resolve functions. What follows is a partial rundown of the places variables apply.

- Clip names: Drop variables into the Clip Name column of the Media Pool while in List view, or into the Clip Name field over in the Clip Attributes window’s Name panel, so each clip’s own metadata yields a display name that’s clearer and more useful.
- Other metadata fields in the Metadata Editor: Variables work here too, letting one field reference metadata held in others.
- Automatic labeling of stills in the Gallery: Pick the “Automatically label Gallery stills” choice from the Color group within the General Options panel of the Project Settings, and variables are how you fill that label out.
- Custom text in the Data Burn palette: Lean on variables to auto-fill metadata in assorted combinations as a window burn.
- The Filename field of the Render Settings in the Deliver page: With variables in play, the names of rendered clips can be made to track whatever metadata ties to a timeline or an individual clip — a real boon when you need particular file names while rendering individual source clips.

### How to Edit Metadata Variables

Anything at all in the Metadata Editor’s store of metadata is fair game as a variable, and a handful of further clip and timeline properties can be pulled in through variables as well — among them a clip’s timeline index number, its EDL event number, and the version name tied to that clip’s grade. To drop a variable into any text field set up to accept variables: 1 Punch in the percentage sign (%) and a scrolling roster pops up listing every variable on offer. 2 To zero in on one variable in a hurry, begin spelling out its name and the roster narrows itself automatically to just the variables holding the characters you’ve entered. 3 Settle on the variable you want with the Up and Down Arrow keys, then hit Return to drop that variable in.

The moment you place one or several metadata variables into a field and press Return, the string gets swapped out for its matching text. Want to edit the metadata string afresh? Just click inside that field to edit, and the metadata variables will pop back into view as the graphical tags they really are.

The variable list that shows up once you type the % character To get rid of a metadata variable: click inside a field that holds variables to start editing, click the variable so it’s selected, then press Delete.

### Current Date and Time Metadata Variables

The present Date and Time are available as metadata variables in the Data-Burn-In window as well as in delivery render paths. What these variables stand for is the genuine date and time at the moment of output, not the date and time when a clip was originally shot.

- Date Variable: Type %date into the relevant field, then pick from among the Date, Date ISO, or Date US formats.
- Time Variable: Type %time into the relevant field, then pick from among the Time, Time 24, or Time ISO formats.

Putting the Date and Time variables to use within the Data Burn-in Custom Text1 field

### Using Keywords

Whereas the bulk of metadata in the Metadata Editor gets entered through text fields, checkboxes, or sets of buttons (Flags and Clip Color among them), the Keyword field stands apart in relying on a graphical “tag” style of data entry. The point of that is to keep keyword spelling consistent by making it simple to draw on both a built-in roster of standardized keywords and any other keywords you’ve already applied to other clips. Once they’re in place, keywords prove tremendously handy for searching and sorting within the Media Pool, for setting up Smart Bins on the Media and Edit pages, and for driving Smart Filters over on the Color page. Enjoying those payoffs by adding and editing keywords is easy and runs much like the metadata-variable entry method covered above. To add a keyword: 1 Pick one or more clips, click into the Keyword field of the Metadata Editor, and start spelling out the keyword you have in mind. The instant you start typing, a scrolling roster shows up listing all keywords reachable from the run of characters you’ve just entered. 2 To track down one keyword in the list, begin spelling its name and the list narrows itself automatically to only the keywords containing the characters you’ve typed. Settle on the keyword you want in the list with the Up and Down Arrow keys, then hit Return to add it. 3 If more than one clip was selected, remember to click Save or your edits will vanish. With only a single clip selected, your edits save on their own. As soon as you tack on one or more keywords, each shows up as a graphical tag. To rework any keyword, simply click somewhere inside the Keyword field to edit it.

The keyword list that surfaces as you type inside the Keyword field To edit a keyword:

- Give any keyword a double-click to open it up for editing, change it just as you would any ordinary text, and press Return to turn it back into a graphical keyword tag.

To remove a keyword:

- Click any keyword to select it, and press Delete.

### Keyword Dictionary

DaVinci Resolve ships with a recommended collection of built-in keywords, but through the Keyword Dictionary you’re able to bring in a fresh batch of keywords or strike out previously entered ones that no longer fit your project.

- To reach the Keyword Dictionary, head to Workspace > Keyword Manager. There the Keyword Dictionary lays out every keyword currently suggested and assigned, a search field, and a way to push your own keywords onto the list. Whatever keyword you add ends up in both the Project and User keyword dictionaries.
- To flip between Keyword Dictionaries, choose Project or User from the toolbar menu.

The User Dictionary The User Dictionary lists keywords that get remembered and offered up for autocomplete across every project in this library. What the User Dictionary reflects is always the most recent inputs you entered. The Project Dictionary The Project Dictionary lists keywords that get remembered and offered up for autocomplete within this one project alone. You’re also able to Import and Export keywords as .txt format into and out of the Project Dictionary. That lets you draft a list of custom keywords in any text editor and bring them all into the Keyword Dictionary in a single pass.

### The Keyword Dictionary

Pulling a .txt File into the Keyword Dictionary works like so: 1 Build a plain text file (.txt) holding your keywords, set out either one word to a line or as comma-separated values. 2 Within the Keyword Dictionary Option Menu (three dots), pick Import Project Dictionary. 3 Browse to your .txt file in the file browser and press Open. By the same token, custom keywords sitting in the Keyword Dictionary can be written out to a plain text file (.txt) at one word per line. Pushing a .txt File out of the Keyword Dictionary goes as follows: 1 Within the Keyword Dictionary Option Menu (three dots), pick Export Project Dictionary. 2 Browse to wherever you’d like the .txt file saved in the file browser and press Save. Adding custom keywords of your own to the Keyword Dictionary happens one at a time, as the need arises. Here’s how you tack a new keyword onto the Keyword Dictionary: 1 Click the Add Keyword button. 2 Into the text field, enter the new keyword and hit return. At first the new keyword lands at the foot of the Keyword list so it’s easy to get at, but after the Keyword Dictionary has been shut and opened again, that new keyword falls into alphabetical order. By the same token, a keyword can be pulled out of the Keyword list once it stops being relevant, or turns out misspelled. Here’s how you remove a keyword from the Keyword Dictionary: 1 Float the pointer above the keyword you intend to delete. 2 Click the trashcan icon sitting just to the keyword’s right. That keyword drops off the list straight away, and the action can’t be reversed. Do note that the default keyword set bundled with DaVinci Resolve cannot be deleted.

### Assign and Apply Favorite Keywords to Clips and Markers

These days you’re able to set as many as nine keywords as favorites within the Keyword Manager in the Workspace menu. Just type your fresh keyword into the slots along the left side of the Keyword Manager to lock them in. Assigning these keywords to selected clips, or inside a marker window, goes quickly from the Mark > Favorite Keywords menu. Quicker still, lean on the default keyboard shortcuts Option‑Shift 0 through 9. That very same menu also carries an action that wipes every keyword from a clip or marker.

The nine Favorite Keywords slots in the Keyword Manager
