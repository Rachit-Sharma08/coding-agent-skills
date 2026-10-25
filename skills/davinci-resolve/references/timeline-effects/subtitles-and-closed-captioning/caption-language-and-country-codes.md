# Caption language and country codes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Subtitles and closed captioning.
[Chapter index](INDEX.md) / [Previous section](subtitle-regions.md) / [Next section](subtitle-export-burn-in-and-embedding.md)
<a id="source-arabic"></a> <a id="source-chinese"></a> <a id="source-danish-dutch"></a> <a id="source-english"></a> <a id="source-exporting-subtitles-and-closed-captions"></a> <a id="source-exporting-subtitles-via-the-file-menu"></a> <a id="source-exporting-subtitles-via-the-subtitle-track-header"></a> <a id="source-iso-3166-1-country-code"></a> <a id="source-language-amharic"></a> <a id="source-language-bengali"></a> <a id="source-language-swedish-tagalog-thai-turkish-urdu-vietnamese"></a> <a id="source-naming-subtitle-tracks"></a> <a id="source-the-initial-sequential-subtitle-track"></a>

### The initial sequential subtitle track

That identical subtitle track after a new region was inserted, which permits both subtitles to display at once

### Naming Subtitle Tracks

Should you wish, a double-click on any subtitle track’s name lets you retitle it to better describe that track’s contents — perhaps the language it holds, plus whether it carries subtitles or closed captions. Established schemes already exist for labeling languages, depending on your pipeline and the delivery spec you are meeting; among them are ISO-639-1 (which governs 2-letter codes) and ISO-639-2/B (which governs 3-letter codes). The International Organization for Standardization publishes these on its site, at http://www.loc.gov/standards/iso639-2/php/code_list.php. Certain schemes call for a language code together with a country code. Facebook, as one case, expects SubRip (.srt) files carrying the naming format “VideoFilename.[language code]\_[country code].srt” so embedding works properly. Should you wish to apply such codes when identifying and outputting subtitle tracks, what follows is a sample alphabetical roster of standardized language and country codes drawn from across the globe:

| Language | ISO 639-1 | ISO 639-2 | Example ISO 3166-1 countries |
| --- | --- | --- | --- |
| Amharic | am | amh | ET (Ethiopia) |
| Arabic | ar | ara | EG (Egypt); AE (United Arab Emirates); LB (Lebanon) |
| Bengali | bn | ben | IN (India) |
| Chinese | zh | chi (B); zho (T) | CN (China); HK (Hong Kong); TW (Taiwan) |
| Danish | da | dan | DK (Denmark) |
| Dutch | nl | dut (B); nld (T) | NL (Netherlands) |
| English | en | eng | GB (UK); IN (India); US (US) |
| Finnish | fi | fin | FI (Finland) |
| French | fr | fre (B); fra (T) | CA (Canada); FR (France) |
| German | de | ger (B); deu (T) | DE (Germany) |
| Greek Modern | el | gre (B); ell (T) | GR (Greece) |
| Hausa | ha | hau | NG (Nigeria); TD (Chad) |
| Hebrew | he | heb | IL (Israel) |
| Hindi | hi | hin | IN (India) |
| Indonesian | id | ind | ID (Indonesia) |
| Italian | it | ita | IT (Italy) |
| Japanese | ja | jpn | JP (Japan) |
| Malay | ms | may (B); msa (T) | MY (Malaysia) |
| Maori | mi | mao (B); mri (T) | NZ (New Zealand) |
| Norwegian | no | nor | NO (Norway) |
| Polish | pl | pol | PL (Poland) |
| Portuguese | pt | por | BR (Brazil); PT (Portugal) |
| Punjabi | pa | pan | IN (India) |
| Russian | ru | rus | RU (Russia) |
| Spanish Castilian | es | spa | CO (Colombia); ES (Spain); MX (Mexico) |
| Swahili | sw | swa | KE (Kenya) |
| Swedish | sv | swe | SE (Sweden) |
| Tagalog | tl | tgl | PH (Philippines) |
| Thai | th | tha | TH (Thailand) |
| Turkish | tr | tur | TR (Turkey) |
| Urdu | ur | urd | PK (Pakistan) |
| Vietnamese | vi | vie | VN (Vietnam) |

### Exporting Subtitles and Closed Captions

After you have built one or more subtitle tracks populated with subtitles or captions, several distinct routes are open to you for exporting them.

### Exporting Subtitles Via the File Menu

Pick File > Export Subtitle, then rely on the export dialog to set both a destination and a file type for the subtitle file you are writing out. The .srt and .vtt formats are both available for export.

### Exporting Subtitles Via the Subtitle Track Header

On the track header belonging to a subtitle track, right-click and pick Export Subtitle out of the contextual menu. From the export dialog, set where the subtitle file goes and which file type it takes. The .srt and .vtt formats are both available for export.
