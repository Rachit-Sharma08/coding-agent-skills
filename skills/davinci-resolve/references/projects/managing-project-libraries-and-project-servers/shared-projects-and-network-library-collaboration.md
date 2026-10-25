# Multiple users sharing projects and collaborative workflow for network project libraries

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing project libraries and project servers.
[Chapter index](INDEX.md) / [Previous section](what-is-a-project-library-and-project-libraries.md) / [Next section](project-server-and-library-details.md)
<a id="source-backing-up-a-network-project-library"></a> <a id="source-connecting-to-a-network-project-library-on-a-davinci-resolve-project-server"></a> <a id="source-connecting-to-an-existing-network-project-library"></a> <a id="source-connecting-to-an-existing-network-project-library-1"></a> <a id="source-creating-a-network-project-library"></a> <a id="source-creating-a-new-network-project-library"></a> <a id="source-disconnecting-from-a-network-project-library"></a> <a id="source-duplicating-a-network-project-library"></a> <a id="source-installing-the-davinci-resolve-project-server"></a> <a id="source-multiple-users-sharing-projects"></a> <a id="source-optimizing-a-project-library"></a> <a id="source-restoring-a-network-project-library"></a> <a id="source-sharing-a-key-to-a-network-project-library"></a> <a id="source-the-davinci-resolve-project-server-interface"></a> <a id="source-using-collaborative-workflow-for-network-project-libraries"></a> <a id="source-using-the-davinci-resolve-project-server-application"></a>

### Multiple Users Sharing Projects

The most straightforward case has users just open a project on the Project Server and get to work. Working like this, should you ever need to switch rooms or workstations, you can readily open that same project from any machine joined to the server on the same network, with no need to export and import it first. As an example, an assistant might team up with a colorist to ready files for the next reel — conforming shots, handling VFX replacements, doing dust busting repairs, and the like — within an unsupervised editing suite somewhere in the building, then save and close the project so the colorist can open that same project right away in the grading theater across the hall. A second way to capitalize on shared Project Servers is to carve large projects into sections, letting several artists work in parallel on different chunks of the whole across different suites, passing them off as required. For instance, a feature film might be carved into reels, or a film can be separated from

the trailer and electronic press kit projects with which it shares media. Here each project can be cut, mixed, and graded by different people tapping into the Project Server. When someone opens a shared project that another person already has open, a dialog tells you it’s opening in Read-only mode so that multiple users can’t reach the project simultaneously. If you load a Read-only project yet decide you want to make edits regardless, you’ll have to use the Save As command to spin off a duplicate project file under a fresh name in order to keep your work.

### Using Collaborative Workflow for Network Project Libraries

As an alternative, the Collaborative Workflow features in DaVinci Resolve let several collaborators on several workstations across several rooms open and work the exact same project at the same time. For example, one editor can cut a project’s main timeline in one room while an assistant arranges media and adds metadata within the same project in a second room, and a colorist grades dailies in that same project in a third, all reaching the same Project Server that lets them work side by side in parallel. For more detail, refer to Chapter 197, “Collaborative Workflow.” Everyone taking part in a Collaborative Workflow has to be on a network project library hosted by a properly configured Project Server.

### Connecting to a Network Project Library on a DaVinci Resolve Project Server

What chiefly sets a local project library apart from a network project library is that the network project library lives on another computer joined to the same network and running the DaVinci Resolve Project Server. Configuring the Project Server itself is dealt with further on, yet anyone who works network projects within DaVinci Resolve should understand the way a local workstation connects out to the Project Server. Once the hardware and software are installed (in essence, every computer joined to the same network, all running DaVinci Resolve, with one computer running the Project Server), you must authorize your computer to reach the network project libraries on the Project Server, and that’s managed through “keys.” To gain access to a network project library you have to be handed a key for it that the Project Server generates. The key is nothing more than an .xml file bearing the extension “.resolvedbkey”. To rely on an access key for a hassle-free connection to a Project Server: 1 Start DaVinci Resolve, and once the Project Manager appears, reveal the Project Libraries sidebar. 2 Grab the .resolvedbkey file and let it drop at any spot inside the Project Manager. 3 At this point the shared project library ought to surface in the Project Libraries sidebar, and selecting it reveals all the projects sitting in that project library on the Project Server. You might also have been registered as a Member of the Project Server and given your own username and password. Where that applies, consult the section “Connecting to an Existing Network Project Library” below. After you’ve joined a network project library, managing it works just as it would if you were connected locally.

### Creating a New Network Project Library

Spinning up a fresh network project library is quick and uncomplicated. To create a new network project library: 1 At the upper left of the Project Manager, click the Show/Hide Project Libraries icon so the sidebar appears. 2 From the Project Library options, choose the Network icon. 3 Along the bottom of the sidebar, click the “Add Project Library” button. 4 Choose the Create option to build a new project library. 5 Give your project library a fresh name. 6 Supply the IP address for whatever DaVinci Resolve Project Server you’re connecting to. 7 As a Member of the Project Server, enter your Username and Password; otherwise lean on the default user: postgres and password: DaVinci. 8 Click the Create button. From here, fresh projects can be built or imported right into your new network project library.

### Creating a network project library

### Connecting to an Existing Network Project Library

Joining a project library already present on a Project Server is a matter of working through the steps below. To connect to an existing project library on a Project Server: 1 At the upper left of the Project Manager, click the Show/Hide Project Libraries icon so the sidebar appears. 2 From the Project Library options, choose the Network icon. 3 Along the bottom of the sidebar, click the “Add Project Library” button. 4 Choose the Connect option so as to reach the existing project library. 5 Enter the project library’s name as it sits on the Project Server. 6 Provide the IP address for whatever DaVinci Resolve Project Server you’re connecting to. 7 As a Member of the Project Server, enter your Username and Password; otherwise lean on the default user: postgres and password: DaVinci. 8 Hit the Connect button. From here, every existing project can be browsed and used right from the existing network project library.

### Connecting to an existing network project library

### Disconnecting from a Network Project Library

You can detach and drop an existing project library from the Project Libraries list with the steps below. To disconnect from a network project library: 1 At the upper left of the Project Manager, click the Show/Hide Project Libraries icon to reveal the sidebar. 2 From the Project Library options, choose the Network icon. 3 Single out the library you mean to detach. 4 Click that Display Project Library Details icon — the circled “i” positioned to the library’s right. 5 Choose the Remove button. 6 In the confirmation dialog, hit the disconnect button. Detaching a project library merely strips it from the available options in the Project Libraries sidebar. It leaves the project library itself intact. You can either remove it by hand in the OS filesystem, or reconnect to it via the steps outlined in Connecting to an Existing Local Project Library.

### Backing up a Network Project Library

Exporting project libraries and pulling them back in later is another route to backing them up. To backup/export a network project library: 1 Single out the library you intend to back up. 2 Click that Display Project Library Details icon — the circled “i” over to the library’s right. 3 Choose the Back Up button. 4 Inside the Backup Project library dialog, name a destination for the backup, then click Save.

### Restoring a Network Project Library

Bringing in project libraries that already exist is how you shuttle multiple projects from one system to another. To restore/import a network project library: 1 At the top left of the Project Manager, click the Show/Hide Project Libraries icon so the sidebar appears. 2 From the Project Library options, choose the Network icon. 3 Up at the top of the Project Libraries sidebar, click the Restore button.

The Restore button 4 Through the file import dialog, track down the library you want imported, and click Open. 5 Within the Add Project Library dialog, do this: a) Give your project library a fresh name. b) Key in the IP address of whichever DaVinci Resolve Project Server you’re reaching. c) Should you be a Member of the Project Server, hand over your Username and Password. If not, rely on the default user: postgres and password: DaVinci. d) Click the Create button, whereupon the imported local project library shows up in the Network section of the Project Libraries sidebar.

### Duplicating a Network Project Library

You can also clone a network project library for an extra backup, or as a save point partway through a large project. To duplicate a network project library: 1 Single out the library you intend to duplicate. 2 Click that Display Project Library Details icon, the circled “i” sitting to the library’s right. 3 Choose the Duplicate button. 4 Pick a fresh, one-of-a-kind name for the duplicated library and click OK.

### Optimizing a Project Library

Now and then, project libraries in DaVinci Resolve swell to a size that drags on performance. When that happens you may have to optimize them to quicken access by “vacuuming” the project library of needless spaces and reindexing it. The Optimize command can also prove a worthwhile troubleshooting move in certain situations where you’re struggling to open, import, or otherwise work with projects held in network project libraries. To optimize a project library: 1 Single out the library you mean to optimize. 2 Click that Display Project Library Details icon — the circled “i” to the right of the library. 3 Click the Optimize button. 4 Up comes a warning dialog. Hit Optimize to carry on, or click cancel to leave the project library exactly as it is.

### Sharing a Key to a Network Project Library

If you wish, your access key for a network project library can be handed to a fellow user sharing the same local network. To send a network project library’s key outward: 1 At the upper left of the Project Manager, click the Show/Hide Project Libraries icon so the sidebar shows. 2 From the Project Library options, choose the Network icon. 3 Single out the library whose key you intend to share. 4 Click that Display Project Library Details icon — the circled “i” to the right of the library. 5 Click the Share Key button. 6 Choose the file-system directory where the key should be saved and click save. 7 Pass the resulting .resolvedbkey file on to the other user.

### Using the DaVinci Resolve Project Server Application

A stand-alone application, DaVinci Resolve Project Server hands you the means to create, manage, backup, restore, and — above all — share project libraries on any workstation. Thanks to it, firing up DaVinci Resolve just to manage your project libraries becomes unnecessary.

### Installing the DaVinci Resolve Project Server

The hardware and software needed to install the DaVinci Resolve Project server is spelled out in the User’s Guide document bundled with the program download. The first time it launches, you’re shown a screen for setting up an Admin account for the server. That account grants you full permissions to tweak any facet of the project libraries and to change the Project Server itself.

The first time it launches, the DaVinci Resolve Project Server prompts you to create an administrator account.

### The DaVinci Resolve Project Server Interface

The DaVinci Resolve Project Server interface closely mirrors the DaVinci Resolve Project Manager with the Project Libraries sidebar open. It does, however, surface every project library management tool there is for creating and handling project libraries, including controls for sharing project libraries and minting access keys that are key to quickly and easily creating and joining Project Servers.
