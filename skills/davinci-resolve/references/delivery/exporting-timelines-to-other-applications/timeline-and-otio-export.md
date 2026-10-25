# Exporting timelines from DaVinci resolve and exporting to otio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exporting timelines to other applications.
[Chapter index](INDEX.md) / [Next section](edit-index-csv-txt-and-ale-export.md)
<a id="source-exporting-a-missing-clips-edl"></a> <a id="source-exporting-an-edl"></a> <a id="source-exporting-timeline-markers-to-edl"></a> <a id="source-exporting-timelines-from-davinci-resolve"></a> <a id="source-exporting-timelines-to-other-applications"></a> <a id="source-exporting-timelines-to-other-applications-part-1"></a> <a id="source-exporting-to-aafxml"></a> <a id="source-exporting-to-cdl"></a> <a id="source-exporting-to-otio"></a> <a id="source-more-about-exporting-to-aaf"></a> <a id="source-title--no-title--1-a001_c002_0820ga_001-v"></a>

### Exporting Timelines to Other Applications

After a program is edited and graded, you might have to write your finished graded timeline out as EDL, AAF, XML, or OTIO files so it can travel to another application for added finishing, effects work, or to round-trip back from an NLE. Sending a graded project onward to another application first calls for rendering the graded clips, using the Deliver page controls to lay the Timeline down as separate source clips. Under this mode, each rendered clip’s reel name and timecode metadata is carried over into the exported project file, which keeps exported EDL, XML, AAF, or OTIO data tied to the media that was rendered. For a thorough account of rendering on the Deliver page, turn to Chapter 187, “Rendering Media.” Should you render with the Easy Setups matching Final Cut Pro XML or Avid AAF round trips, an XML or AAF lands in the very same directory your render went to. Even so, exporting an XML, AAF, or EDL file on its own remains an option whenever that need comes up. Or, if a project was built from scratch inside DaVinci Resolve and a timeline has to head to another application, you’re free to write any timeline out in any format for project exchange, with no fresh media to render (your workflow permitting). Even when a timeline came in from another application, the wide-ranging project compatibility of DaVinci Resolve lets you bring in one species of project exchange file, say XML, and then send out an altogether different one, such as AAF or EDL. That turns DaVinci Resolve into a project exchange utility.

### Exporting Timelines from DaVinci Resolve

Post-production today is rarely handled under a single roof. Shuttling timelines and assets among numerous applications from all sorts of companies is a routine requirement. DaVinci Resolve carries its own proprietary .drt format for ferrying timelines between DaVinici Resolve workstations, yet the program also packs a capable toolset for sending your assets out to plenty of other well-known applications. At the time of writing, here’s the surest route for passing DaVinci Resolve timelines from one application to another. Moving from DaVinci Resolve to/from another DaVinci Resolve workstation, going either way: use Export/Import on a DaVinci Resolve Timeline file (.drt). Moving from DaVinci Resolve to/from another application, going either way: reach for Export/Import on an OpenTimelineIO file (.otio, .otioz), where it’s supported. Lacking that support, drop back to XML or AAF flies in its place.

### Exporting to OTIO

For moving timelines into and out of applications, DaVinci Resolve handles the Open Timeline IO (.otio) format. OTIO is an open source interchange format for media and timelines, the work of the Academy Software Foundation. Built to stay neutral about both application and platform, it lets you hand off your timeline along with its media assets across programs at higher compatibility than AAF or XML manage. DaVinci Resolve recognizes two distinct OTIO formats: .otio: A file of this kind holds nothing but the timeline’s metadata, with no media attached. Such files stay small and portable, leaving the recipient to relink the timeline to their own media copies. .otioz: A bundle file of this sort packs the timeline metadata together with every one of the timeline’s media assets, all zipped into a single file. That can make the file enormous, since it carries the full-length media files for each asset the timeline draws on. The upside is that whoever opens it receives all the media required, automatically linked, so the timeline rebuilds flawlessly on their machine.

Writing out an OpenTimelineIO (.otio, .otioz) file runs like so: 1 Select File > Export > Timeline (Shift-Command-O). 2 Give the timeline file a name. 3 Within the file browser, pick either .otio files or .otioz bundle files from the format selector. 4 Click Save. NOTE: Choosing to export .otioz bundle files triggers an extra OTIO-bundle-building pass, during which every complete media file from each clip in the timeline gets folded into the finished bundled file. That can run long and may demand extra storage, depending on how much media is in play and how lengthy it is.

### Exporting to AAF/XML

No matter whether your project was cut from scratch within DaVinci Resolve, or you’re round-tripping through an application that runs on AAF, on Final Cut Pro 7 XML, or on the Final Cut X XML format for project exchange, any DaVinci Resolve timeline on the Edit page can be written out to whatever project format DaVinci Resolve handles. Whatever your workflow, bear these points in mind: Timelines export on their own as you render a timeline on the Deliver page: Reach for either the “Final Cut Pro Round-Trip” preset or the “Avid AAF Round-Trip” one among the render setting presets, or some preset spun off from one of them, and a matching XML or AAF file goes out on its own beside the media you render. Even a project pulled in from another application stays open to re-editing before you export it: Where it’s called for, feel free to re-edit projects bound for export. Once you write out an AAF or XML file, the Timeline heads back to the NLE it came from, or forward to whichever finishing application you favor. Round-Trip workflows sometimes hold on to unsupported effects: When the original sequence carried effects or clip constructs that DaVinci Resolve couldn’t support, the handling of those effects hinges on the project format you’re exporting toward, and on whether the project got edited. With XML projects, unsupported effects are tucked away inside DaVinci Resolve and ride out with whatever XML file you produce, no matter what. So they ought to surface again when you reopen the exported file in the NLE it came from. With AAF projects, exporting unsupported effects works only while the project goes un-re-edited. Re-edit it, though, and the AAF file you can export is one purged of every unsupported effect. Project formats convert into other formats: Through DaVinci’s Export commands, compatible project formats can shift from one format into another. An imported EDL, for one, can come out as Final Cut Pro X XML. By the same token, Final Cut Pro 7 XML can be brought in and then sent back out as Final Cut X XML. Or an AAF file out of Media Composer can be imported and afterward exported as a Final Cut Pro XML file, ready to open in any NLE or finishing application that handles that format, Premiere Pro or Smoke among them.

To export an AAF or XML file once the graded clips are rendered: Do one of the following: 1 With the current Timeline in hand, either choose File > Export AAF, XML, or instead press Shift-Command-O.

- On the Edit page, right-click in the Media Pool the Timeline you mean to export, and choose Timelines > Export > AAF/XML.
- As the Export XML dialog comes up, key in a file name, pick a spot for the exported XML file, then click Save.

2 An XML rendition of that timeline gets written, references to the graded media you rendered and all, set to import into an NLE or finishing application.

### More About Exporting to AAF

Exporting to AAF actually puts two choices in front of you, hinging on whether you reworked the Timeline editorially on the Edit page: Where you left the imported Timeline’s edit untouched: You can choose File > Export AAF, XML, and pick “AAF Files” out of the Format dropdown menu. That writes out every bit of audio and effects drawing on data from the original AAF file Media Composer exported, whether or not DaVinci Resolve supports them. As you export an unedited AAF, DaVinci Resolve leans on the Avid AAF file you first imported to build a refreshed one, so confirm it still sits where it was the day you first brought it into DaVinci Resolve. Where you did rework the imported Timeline’s edit, or you’re exporting a project that started as something other than AAF: You then have to right-click in the Media Pool the Timeline you mean to export and choose Timelines > Export > Generate New AAF. That choice mints a wholly new AAF file, though any audio and effects an AAF import brings in that DaVinci Resolve doesn’t support are thrown out.

### Exporting an EDL

DaVinci Resolve can likewise write out EDLs that other applications can pull back in. For fuller coverage of EDL workflows, three chapters help. There’s Chapter 24, “Ingesting From Tape.” You can also see Chapter 56, “Conforming and Relinking Clips.” plus, on the conform side, Chapter 60, “Conforming EDL Files.” Here’s how an EDL gets exported: 1 Open the Edit page and, in the Media Pool, pick the Timeline you want an EDL from. 2 An exported EDL holds only one video track. On timelines carrying several tracks, just the events on whichever video track owns the destination control get exported (that destination control being the leftmost control in the track header). To export a track that isn’t Video 1, hand the destination control to the particular track you need exported. 3 Right-click the Timeline within the Media Pool, and choose Timelines > Export > AAF/XML/EDL out of the contextual menu.

4 As the Export Timeline dialog comes up, enter a name, pick a spot for the exported EDL, choose EDL Files from the dropdown menu along the bottom, then click Save. Your EDL is written out.

### Exporting a Missing Clips EDL

This command writes out a quick report naming every clip that sits offline in the track you currently have selected on the Edit page’s Timeline. That report comes in EDL format, an event per offline clip, each spelling out the missing media’s reel number and source timecode, plus the record timecode marking where the missing media falls on the Timeline. An example of an exported Missing Clips EDL follows:

### TITLE: ( no title ) 1 A001_C002_0820GA_001 V

C 10:28:27:03 10:28:28:00 01:00:00:00 01:00:00:21

2 A004_C012_0820MC_001 V C 14:07:31:21 14:07:35:13 01:00:12:13 01:00:16:05

3 A017_C001_0820CV_001 V C 21:16:14:22 21:16:15:00 01:00:16:05 01:00:16:07

With this information exported, you can pass it along to whoever is able to help you run down the media that’s gone missing. Exporting a Missing Clips EDL goes thus: 1 Open the Edit page and, in the Timeline browser, open the Timeline you want a Missing Clips EDL for. 2 On timelines with several tracks, the hunt for missing clips covers only the events on whichever video track holds the destination control. To scan a track other than Video 1, pass the destination control to the specific track you need checked for missing clips. 3 Right-click the Timeline within the Media Pool, and choose Timelines > Export > Missing Clips EDL out of the contextual menu. 4 As the Save Missing Clips EDL dialog comes up, enter a name, pick a spot for the exported EDL, then click Save.

### Exporting Timeline Markers to EDL

Should you stash project notes inside the notes field of Timeline markers, the ones sitting in the Timeline ruler, those notes can be written out as an EDL. Here are the steps for putting timeline markers out this way: 1 Right-click that timeline within the Media Pool, and choose Timelines > Export > Timeline Markers to EDL. 2 From the Export Edit Index dialog, settle on a location and export format, then click Save. The resulting EDL names every Timeline marker, folding in whatever notes there are along with a duration wherever that applies.

### Exporting to CDL

Through a Color Decision List (CDL), DaVinci Resolve can move basic grading data both out to and in from other applications. The CDL is an industry-standard file format that first came out of the technology committee at the American Society of Cinematographers. DaVinci Resolve handles the 1.2 CDL standard, which, channel by channel across red, green, and blue, lays down the slope, offset, and power, and on top of that captures every clip’s overall saturation throughout a program. A CDL file is laid out much like an EDL, its SOP (Slope/Offset/Power) and SAT (Saturation) values tucked in as metadata roughly the way comments sit inside a more ordinary EDL. Here’s an example of a single CDL event: 020 001 V C 03:02:49:13 03:02:53:00 01:01:28:11 01:01:31:22 *ASC_SOP (1.109563 1.717648 0.866061)(-0.238880 -0.390357 0.353743) (0.672948 1.384022 0.889876) *ASC_SAT 1.000000 Since a CDL pins down a grade so narrowly, any project you intend to send out to other applications by way of a CDL has to stay within just the operations the CDL defines mathematically. A few things are worth bearing in mind:

- What gets exported is limited to the primary corrections sitting in each clip’s first node.
- Keep yourself to the Lift/Gamma/Gain, Offset, and Saturation controls and nothing else.
- No keyframes ever go out. Where a grade carries keyframes, only the parameter values living at

the clip’s opening frame come into play.

- Both the track grade and any group grades are passed over entirely.
- Should the first node hold an HSL Qualifier or a Power Window, that gets skipped, and the corrections sitting in

that node are exported as though they were a primary correction.

- Steer clear of Y’ only adjustments; CDLs can’t accommodate them. So that the CDL you export

stays accurate, set the Lum Mix parameter, found in the Primary Controls palette, to 0 on every grade. When CDL export crops up often in your workflow, switching on the “Luminance Mixer defaults to zero” option, over in the Color section of the General Options panel within the Project Settings, locks this parameter at 0 every time. Once your timeline satisfies all of the limits above, a CDL export is within reach. The steps run thus: 1 Open the Edit page, right-click in the Media Pool the Timeline you mean to export, and choose Timelines > Export > CDL out of the contextual menu. 2 Give the CDL a name, pick where to save it, and click OK.

For more on bringing in a CDL to layer grades onto your project, turn to Chapter 149, “Copying and Importing Grades Using ColorTrace.”
