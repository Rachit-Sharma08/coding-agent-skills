# Create subtitles from audio and create subtitles from audio options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Subtitles and closed captioning.
[Chapter index](INDEX.md) / [Previous section](subtitle-caption-support-and-track-viewing.md) / [Next section](adding-and-deleting-subtitle-regions-overview.md)
<a id="source-ai-animated-subtitles-studio-version-only"></a> <a id="source-create-subtitles-from-audio-language-support"></a> <a id="source-create-subtitles-from-audio-studio-version-only"></a> <a id="source-editing-subtitles-and-captions"></a> <a id="source-linking-subtitles-to-clips"></a> <a id="source-styling-subtitles-and-captions"></a> <a id="source-subtitle-regions"></a> <a id="source-subtitle-tracks-using-fusion-templates-for-styling"></a> <a id="source-the-create-subtitles-from-audio-options"></a> <a id="source-using-a-fusion-template-to-create-stylized-subtitles"></a> <a id="source-using-subtitle-track-style-presets"></a> <a id="source-using-subtitles-in-nested-timelines"></a>

### Create Subtitles from Audio (Studio Version Only)

Thanks to recent strides in AI and expert-system technology, it's now within reach to produce strikingly accurate, flawlessly timed subtitles of spoken text via DaVinci Resolve's Create Subtitles from Audio function. Create Subtitles from Audio examines the speech across a timeline and automatically builds a subtitle track holding all the spoken dialog turned into text subtitle clips. Create Subtitles from Audio doesn't merely translate phonetic speech straight into text. It also reads the context of that speech correctly and carries it over into proper punctuation and grammar for the subtitle. As an instance, Create Subtitles from Audio singles out proper names and capitalizes them, tacks a question mark onto a sentence's end when your subject poses a question, drops quotation marks into the right spots when your subject quotes something, and when it picks up music in the background, it inserts a [Music Playing] subtitle. It copes with accents and recognizes when more than one person is talking in a scene. You might be taken aback at just how precise the Create Subtitles from Audio tool can be.

The whole subtitling process runs hands-off under Create Subtitles from Audio. To run Create Subtitles from Audio on a timeline: 1 In the Edit page, open whichever Timeline you'd like Create Subtitles from Audio to work on. 2 Mark an In-Out range for the subtitles on the Timeline, or leave it empty to Create Subtitles from Audio across the whole Timeline. 3 Choose Timeline > AI Tools > Create Subtitles from Audio. 4 Within the Create Subtitles from Audio dialog, set the following options:

- Language: Which language the spoken text is in. Picking Auto has DaVinci Resolve work out the language on its own.
- Caption Preset: Whichever Caption Preset style you'd like the subtitles formatted with.
- Max Characters per Line: The ceiling on how many characters a subtitle line may hold. Bigger

figures yield longer on-screen lines of text. Smaller figures yield shorter ones.

- Lines: Decides whether the subtitle runs as a single line or a pair of lines of text.
- Gap Between Subtitles: How many frames get dropped in between subtitle clips. The default sits at 0.

5 Click the Create button.

### The Create Subtitles from Audio options

Create Subtitles from Audio then sets about transcribing the spoken text, with a dialog box showing you how far along it is. Once it wraps up, the resulting subtitles get dropped onto the Subtitle track. Where your Timeline holds no Subtitle track, it makes one for you automatically. Where more than one subtitle track sits on your Timeline, Create Subtitles from Audio always writes to the topmost track. The single spot where the Create Subtitles from Audio tool still commonly stumbles is overlapping dialog clips spread across multiple tracks. To get around that, you can mute any audio track on the Timeline you'd rather leave out of the subtitle analysis. With the Create Subtitles from Audio finished, you can hand-edit the captions to clean up any small mistakes using the tools laid out earlier in the Adding Subtitles and Captions Manually section.

### Create Subtitles from Audio Language Support

At the time of writing, Create Subtitles from Audio handles the languages below:

- English, French, German, Italian, Spanish, Portuguese, Dutch, Danish, Norwegian, Swedish, Russian, Japanese, Korean, and Chinese (Simplified Mandarin).
- Plenty of further languages can be reached too by way of the Extended AI Transcription Support Package in the Extras Downloads Manager. The roster runs: Arabic, Afrikaans, Armenian, Azerbaijani, Belarusian, Bulgarian, Bosnian, Catalan, Croatian, Czech, Finnish, Estonian, Greek, Galician, Hindi, Hebrew, Hungarian, Indonesian, Icelandic, Kazakh, Kannada, Lithuanian, Latvian, Malay, Macedonian, Maori, Marathi, Nepali, Polish, Persian, Romanian, Slovak, Serbian, Slovenian, Swahili, Tamil, Tagalog, Turkish, Thai, Urdu, Ukrainian, Welsh, and Vietnamese.

### Editing Subtitles and Captions

Subtitle clips can be picked one at a time or in groups, and slipped, slid, resized, rolled, and rippled exactly like any other clip on the Timeline, whether with the mouse or with keyboard commands, using the Selection, Trim, or Razor tools. You can select subtitle clips whole, or only their edit points, in readiness for nudging or dynamic trimming. Put simply, subtitle clips can be edited, in most respects, just the way any other clips can.

### Styling Subtitles and Captions

For styling subtitle text, a rich array of styling controls lives in the Track Style panel of the Inspector. To change the styling of every title on a given subtitle track: 1 Click the header of the subtitle track you'll work on, or else pick a clip belonging to a given subtitle track—whether from within the subtitle track itself or out of the Captions panel's subtitle list in the Inspector. 2 Open the Inspector, then open the Track panel that turns up within it. 3 Edit whichever parameters you need to fix the default style of all the subtitles and closed captions that show up on that track. The Track panel carries far more options than the Captions panel, including a cluster of Style and Position controls covering Color, Font and Font Face, Size, Kerning, Line Spacing, Alignment, Zoom X and Y, Position X and Y, Text Anchoring, and Opacity.

Choosing a Font Case over in the Subtitle Inspector's Track tab Do remember that additional clusters of controls let you add a Drop Shadow, Stroke, and/or Background to every bit of text on that track, sitting at the bottom of the Track panel of the Inspector. You're also free to alter how each subtitle clip looks one by one, right down to a single word or letter, whatever the Track panel's settings happen to be.

To change the styling of a single subtitle on a given subtitle track: 1 Choose a clip belonging to a given subtitle track, taken either from the subtitle track itself or from the Captions panel's subtitle list within the Inspector. 2 Tick the Customize Caption check box beneath the Caption. 3 Edit whichever parameters you need to fix the style of this one subtitle alone. Every other title in the track keeps the original track style. To change the styling of a single word or words within a given subtitle: 1 Select a clip riding a given subtitle track, drawn either out of the subtitle track or out of the subtitle list found in the Inspector's Captions panel. 2 Tick the Customize Caption check box beneath the Caption. 3 Highlight the text you'd like to change in the Caption panel. 4 Edit whichever parameters you need to fix the style of this subtitle's highlighted text. Every other title in the track keeps the original track style.

Ticking the Customize Caption box brings up the tools that let you restyle one individual subtitle or its text.

### Using Subtitle Track Style Presets

Should you wish to store and reuse a particular subtitle style, you can drop it into the Subtitle Style Preset menu, reached by clicking the Subtitle option menu (3 dots) up in the top-right corner of the Subtitle Inspector. You can likewise export and import presets so a subtitle style can be shared between systems. To add a new subtitle style preset: 1 Build a subtitle track and tune its style as to fonts, position, colors, etc. 2 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 3 From the drop-down menu, choose Save Track as Preset. 4 Hand your preset a fresh name. From that point on, the Subtitle Inspector's option menu lists your subtitle style preset. To switch a subtitle track over to a different style preset: 1 Pick an existing subtitle track you'd like to change. 2 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 3 Pick the subtitle style preset from the drop-down menu. 4 Pick Load Preset from the submenu. Your subtitle track updates instantly to the new style preset. This command can be undone. To update a subtitle style preset: 1 Out of the Subtitle Inspector option menu, load whichever subtitle style preset you want. 2 Make whatever changes you need to the style as to fonts, position, colors, etc. 3 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 4 Pick the subtitle style preset you'd like to update from the drop-down menu. 5 Pick Update Preset in the submenu. 6 Pick Update from the dialog box. Your subtitle style preset then replaces the existing preset bearing the same name. This action has no undo. To delete a subtitle style preset: 1 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 2 Pick the subtitle style preset you'd like to delete from the drop-down menu. 3 Pick Delete Preset in the submenu. 4 Pick Delete from the dialog box. The subtitle style preset gets removed from the Subtitle Inspector's option menu. This action has no undo. To export a subtitle style preset: 1 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 2 Pick the subtitle style preset you'd like to export from the drop-down menu. 3 Pick Export Preset in the submenu. 4 Using the file browser, pick the spot where the ".preset" file should land. 5 Press Save. That writes the subtitle style preset file onto the user's computer, the file taking the preset's name plus a .preset extension.

To import a subtitle style preset: 1 Click the option menu (3 dots) up in the top-right corner of the Subtitle Inspector. 2 Pick Import Preset in the submenu. 3 Choose where the ".preset" file lives from the file browser. 4 Press Open. The subtitle style preset gets added to the Subtitle Inspector's option menu.

The Subtitle Style Preset menu, which lives within the Subtitle Inspector's option menu

### AI Animated Subtitles (Studio Version Only)

In the Titles tab there's a collection of Fusion Title Templates called Animated. You can drop these templates onto subtitle tracks, making it simple to build animated subtitle effects. They work hand in hand with DaVinci Resolve's transcription engine to match and highlight spoken audio against subtitle timing. You can preview the prebuilt templates in the Animated section of the Titles tab, and naturally, with Fusion you can craft your own custom templates as well. To animate your subtitles, just drag the animated template out of your Titles library onto the header of the subtitle track. Their parameters are yours to customize in the Inspector.

Here the Word Highlight animated template is in use, lighting up each word in red at the moment it's spoken in the clip.

### Subtitle Tracks Using Fusion Templates for Styling

You're able to style a subtitle track with a Fusion template. To do so, simply drag any Fusion title template out of the effects library onto the subtitle track header. The Fusion effects then take precedence over any track-level or per-caption styling the Inspector applied to the track, letting you craft finely tuned text looks out of the underlying Fusion compositions.

### Using a Fusion template to create stylized subtitles

### Linking Subtitles to Clips

If you'd like, you can tie one or more subtitles to the clip they go with, so that when you re-edit a subtitled scene, each clip's subtitles travel along with the clips. This setup doesn't always behave the way you'd anticipate while trimming, but it shines when you're shuffling clips around. To link a subtitle to another clip: 1 Select a clip together with its subtitles all at once.

Picking a video clip together with the subtitle that goes with it so the two can be linked 2 Choose Clip > Linked Clips (Option-Command-L). A Link icon then appears, marking that the subtitle clips are now tied to the video/audio clip.

Carrying link badges, the freshly linked clip and subtitle make their tied state plain

### Using Subtitles in Nested Timelines

Subtitles carry over with their original timelines as part of a nested timeline. Just drag one subtitled timeline either out of the Media Pool or the Source Viewer into a fresh timeline. Should you want the original timeline's subtitles folded into the new timeline's caption list, you have to Decompose in Place the nested timeline.

### Subtitle Regions

Now and then you'll need several subtitles shown on the screen all at once. A frequent case is two characters on screen whose dialog overlaps. By placing the subtitles thoughtfully, where each sits on the screen can signal who is speaking which subtitle. Subtitle regions let you keep multiple subtitle clips active and overlapping simultaneously, all the while held inside one overall subtitle track.
