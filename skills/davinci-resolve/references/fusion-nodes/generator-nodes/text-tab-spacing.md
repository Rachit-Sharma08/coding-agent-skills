# Text tab spacing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Text.
[Chapter index](INDEX.md) / [Previous section](multitext-and-plasma-and-text.md) / [Next section](text-layout-tab.md) / [Text+ TXT+](multitext-and-plasma-and-text.md)
<a id="source-advanced-font-controls"></a> <a id="source-alignment"></a> <a id="source-basic-node-setup-1"></a> <a id="source-font-features"></a> <a id="source-inputs-1"></a> <a id="source-inspector-1"></a> <a id="source-manual-font-kerningplacement"></a> <a id="source-on-screen-controls"></a> <a id="source-tab-spacing"></a> <a id="source-tab-spacing-1"></a> <a id="source-text-tab"></a> <a id="source-text-text-tab-controls"></a>

### Inputs

Text+ has a single input, which takes an effect mask for cropping the text. Effect Mask: This optional blue effect mask input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask into this input confines the text to just the pixels inside the mask.

### On-screen Controls

Right within the Viewer overlay you can run a range of editing actions on Text+, among them editing text, showing a cursor, and selecting text. Switch this on by hovering over the popup toolbar inside the Fusion viewer and activating it, or else right-click the View menu. The behavior is intuitive: with Text+ selected, a double-click anywhere in the Fusion viewer turns on the in-viewer text editing mode.

Inside the Fusion viewer you'll also come across pivot points for your Character, Word, and Line transforms. To make them handy, a Pivot Points icon now sits in the popup toolbar, letting you flip their visibility while tweaking rotation and scaling transformations. The Z position-based sorting mode is a strong addition to the toolkit. Unlike the Distance mode, which orders by absolute distance from the camera, this mode orders purely on the Z distance from the camera, no matter the relative orientation. Z position lets you freely stack overlapping text elements for precise layering and depth control. Character-level styling has been polished to make offsets and translation transformations more intuitive. The improvement cuts down on manual positioning and keeps the application consistent across several separate character selections.

### Basic Node Setup

You can pair the Text+ node with plenty of other nodes to build motion graphics. In the figure below it's wired in as a Merge node's foreground.

### Inspector

Text+ node connected as the foreground to a Merge node

### Text+ Text tab controls

### Text Tab

The Inspector's Text tab splits into three parts: Text, Advanced Controls, and Tab Spacing. The Text section holds parameters anyone who's worked in a word processor will recognize. It carries the text formatting options people reach for often. The Advanced controls cover kerning options, while Tab Spacing sets where tabs sit and how they align within the layout.

Styled Text This tab's edit box is where you type the text to be built. Any ordinary character can go into this box. The standard OS clipboard shortcuts function here as well — copy with Command-C or Ctrl-C, cut with Command-X or Ctrl-X, paste with Command-V or Ctrl-V; right-clicking inside the edit box, though, brings up a custom contextual menu. Further detail on these modifiers sits at this section's close. The Styled Text contextual menu offers these options:

- Animate: Drives animation of the text across time.
- Character Level Styling: Lets you alter the font, color, size, and transformations of

separate characters or words by way of the Modifiers tab.

- Comp Name: Drops the composition's name into the Styled text box, handy for building slates.
- Follower: A text modifier that cascades animation from one character of the text to the next.
- Publish: Makes the text available for wiring to other text nodes.
- Text Scramble: A text modifier that shuffles the text's characters at random.
- Text Timer: A text modifier that shows a countdown, or else the present date and time.
- Time Code: A text modifier that shows the Time Code belonging to the current frame.
- Connect To: Wires the text up to another node's published output.

Font A pair of Font menus serve to pick the font family along with the typeface, such as Regular, Bold, and Italic. Color Fixes the text's basic fill color. It's the same control that shows up in the Shading tab color swatch. Size This control raises or lowers the text size. It doesn't work like picking a point size in a word processor. Size is gauged relative to the image's width. Tracking The Tracking parameter sets the even spacing placed between each text character. Line Spacing Line Spacing sets how far apart each line of text sits. Word-processing applications sometimes call this leading. V Anchor The vertical anchor controls comprise three buttons plus a slider. Those three buttons align the text vertically to the text's top, its middle, or its bottom baseline. The slider serves to fine-tune the alignment. Where you set the vertical anchor shapes both how the text rotates and where line spacing adjustments take effect. This control sees most use with the Layout type at Frame in the Layout tab. V Justify The vertical justify slider lets you tune the text's vertical alignment from the V Anchor setting all the way to full justification, so it sits evenly between the top and bottom edges. Reach for it chiefly once Frame is the Layout type over in the Layout tab.

H Anchor The horizontal anchor controls comprise three buttons plus a slider. Those three buttons set the text alignment to the text's left edge, its middle, or its right edge. The slider serves to fine-tune the justification. Where you set the horizontal anchor shapes both how the text rotates and where tracking (leading) spacing adjustments take effect. Its main use comes with Frame chosen as the Layout type inside the Layout tab. H Justify The horizontal justify slider lets you tune the text's justification from the H Anchor setting all the way to full justification, so it sits evenly between the left and right edges. You'll lean on it mostly when Frame serves as the Layout type within the Layout tab. Direction This menu hands you choices for the Direction the text runs — horizontally or vertically, and either way around. That lets certain Asian languages flow correctly through animation. Line Direction Through these menu choices the text's flow is set to one of four directions: top to bottom, bottom to top, left to right, and finally right to left. Underline and Strikeout A pair of buttons that add emphasis styling to the text. Write On This range control quickly lays simple Write On and Write Off effects over the text. For a Write On effect, animate the control's End portion from 1 to 0 across the span of time you need. For a Write Off effect, animate the range control's Start portion from 0 to 1.

### Tab Spacing

### Tab Spacing

The controls in the Tabs section set the horizontal screen positions for eight independent tab stops. Whatever tab characters the text holds will snap to these positions. You can drop tabs straight into the Styled Text input as you type. Another route is to copy from a separate document — Text on macOS or Notepad on Windows, for instance — then paste that into the text box. Position This control sets where, horizontally, the tab falls in the frame. The values run from -0.5 to 0.5, with 0 marking the center. A thin vertical white line in the viewer marks the tab's position whenever the Text node is selected. A handle sits atop each tab line in the viewer. That handle lets you place the tab by hand.

### Alignment

Any tab can be made left aligned, right aligned, or centered. This slider runs from -1.0 to 1.0, where -1.0 gives a left-aligned tab, 0.0 a centered tab, and 1.0 a right-aligned tab. Clicking a tab handle in the viewer cycles that tab's alignment through the three states.

### Advanced font controls

Reading Direction These options let you fix the text's reading direction, whether automatically or by hand. You can call out Left to Right languages such as English, German, etc. or Right to Left languages such as Arabic and Hebrew. Force Monospaced This slider control lets you bypass the kerning (the spacing between characters) the font defines. Leaving this slider at zero (its default value) makes Fusion lean entirely on the kerning each character carries. A value of one makes the spacing between characters perfectly uniform, that is, monospaced. Use Font Defined Kerning This switches on kerning as the TrueType font defines it, and it's on by default. Use Ligatures Should your font carry ligatures, switch them on here by picking All Scripts. Ligatures fuse separate letters into single glyphs, such as and . When you're animating individual text letters, you often want the ligature letters kept apart one by one rather than fused into a single glyph, so None is the default for Latin characters. Some languages such as Arabic need ligatures to render right, and call for the Non-Latin setting.

Style Can Split Ligatures Tick this box should your font carry the option to split ligatures.

Stylistic Set Should your font carry stylistic sets, you can pick them from the drop-down menu.

### Font Features

Here you assign OpenType 4 letter tags to turn on specific font features. For instance, "smcp"

will show

, while "frac" renders fractions as ½ rather than 1/2. A given font won't necessarily

carry every feature. The complete roster of OpenType feature codes lives at this address: https://docs.

microsoft.com/en-us/typography/opentype/spec/featurelist

### Manual Font Kerning/Placement

A right-click on this label brings up a contextual menu you can use to animate the text's kerning. Turn to this node's "Toolbar" section further along in this chapter for the particulars on manual kerning.
