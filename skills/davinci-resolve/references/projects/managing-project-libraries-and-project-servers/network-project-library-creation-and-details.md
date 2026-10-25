# Project library details exposed and creating new network project libraries

Version: DaVinci Resolve 20.3 Reference Manual. Context: Managing project libraries and project servers.
[Chapter index](INDEX.md)
<a id="source-assigning-members-to-specific-project-libraries"></a> <a id="source-backing-up-and-restoring-project-libraries"></a> <a id="source-cloud-project-libraries"></a> <a id="source-creating-new-network-project-libraries"></a> <a id="source-managing-project-libraries-and-project-servers-part-2"></a> <a id="source-member-management-in-the-davinci-resolve-project-server"></a> <a id="source-optimizing-project-libraries"></a> <a id="source-project-library-details-exposed"></a> <a id="source-sharing-network-project-libraries-via-the-project-server"></a> <a id="source-the-davinci-resolve-project-server-mange-members-window"></a> <a id="source-the-network-interface-menu"></a> <a id="source-upgrading-project-libraries"></a> <a id="source-viewing-project-library-contents"></a>

### Project Library details exposed

### Creating New Network Project Libraries

Should you need to, you can spin up fresh network project libraries straight from the DaVinci Resolve Project Server. Here's how to make one: 1 Click the Add Project Library button sitting at the foot of the Project Libraries list. 2 Once the Create Project Library window comes up, enter a name for your new library in the Name field. Since every project belonging to a network project library lives internally inside that library, nothing else needs adjusting. 3 Click Create, after which the new network project library shows up in the Project Libraries list.

### Backing Up and Restoring Project Libraries

Backing up and restoring project libraries is also possible without ever launching DaVinci Resolve. On top of that, you can back up project libraries belonging to older DaVinci Resolve versions, which makes safeguarding them simple before any upgrade. To backup/export a project library: 1 Pick the project library you intend to back up. 2 Click the Display Project Library Details icon (that's the circled letter “i” over to the right of the library). 3 Click the Back Up button. 4 In the Backup Project library dialog, pick where the backup should be saved, then click Save. Bringing one back in, or importing it, goes like this: 1 Click the Restore button at the head of the Project Libraries sidebar.

The Restore button 2 Locate the project library you wish to import through the file import dialog, then click Open. 3 Within the Add Project Library dialog, enter a name for the new library in the Name field. Doing so renames the imported library while leaving everything inside it untouched. You're equally free to reuse the same name as the original library. 4 Click Create, after which the imported local project library turns up in the Project Libraries sidebar.

### Upgrading Project Libraries

Every so often, a fresh DaVinci Resolve version alters how projects get created, and that means any project library built under an older DaVinci Resolve version has to be upgraded before you can reach the projects it holds. Happily, the procedure is straightforward. Backing up a library before you upgrade it is usually wise, just in case something goes sideways. As a rule, moving from one full version release of DaVinci Resolve up to the next full release typically demands an upgrade, whereas moving to a dot release within the same version might or might not. Whenever the library currently in use needs updating, you'll get a notice when the application launches.

The upgrade warning shown in the Project Manager signals that a library needs upgrading Here's the way to bring a library built under an older DaVinci Resolve up to date: Click the library that wants updating, then choose the Upgrade Project Library button. A dialog pops up to make sure you genuinely want to upgrade that library. Click Upgrade to carry on.

### Viewing Project Library Contents

When you rely on several project libraries to keep your projects sorted, you can look through each library's contents to track down whatever you need. Just click a library in the sidebar to select it, and an orange highlight shows up. Every project tied to that library then appears within the Project Manager window.

### Optimizing Project Libraries

On occasion, a DaVinci Resolve project library grows large enough that its bulk starts to drag on performance. When that happens, you might have to optimize it to speed up access, which works by “vacuuming” the library of needless gaps and rebuilding its index. Reaching for the Optimize command can also serve as a handy troubleshooting move in cases where opening, importing, or otherwise working with projects stored in network project libraries gives you trouble. Optimizing a project library runs like this: 1 Pick out whichever library needs the work. 2 Click the Display Project Library Details icon (the circled letter “i” over to the right of the library). 3 Click the Optimize button. 4 A warning dialog shows up. Click Optimize to carry on, or click cancel to leave the library exactly as it is.

### Member Management in the DaVinci Resolve Project Server

You're able to tie particular users to particular project libraries and tune the roles they hold. That affords finer-grained security on intricate projects shared among lots of users. Each network project library begins with the default user: postgres and password: DaVinci. Until fairly recently that was the sole means of signing into the DaVinci Resolve Project Server from afar, but you can now register custom users and passwords on top of it. Each member can then sign into network projects in the Project Manager with their own credentials.

The DaVinci Resolve Project Server Members management window Bringing a fresh member onto the DaVinci Resolve Project Server goes as follows: 1 Over in the top-right corner of the DaVinci Resolve Project Server, click the Members button. 2 Click the Create New Member button down at the foot of the Members window. 3 Choose a username and password for that member, and if you like you can attach a thumbnail photo too. That thumbnail serves to mark the user while in collaboration mode. 4 Do this again for however many new users you wish to add. 5 Click the Save button to commit the new users, or click Cancel to throw away your changes.

The DaVinci Resolve Project Server Create New Member window

Removing a member who already exists from the DaVinci Resolve Project Server runs like this: 1 Over in the top-right corner of the DaVinci Resolve Project Server, click the Members button. 2 Locate the user you intend to remove and hit the trash can icon sitting in that user's row. No warning dialog accompanies the deletion and there's no undoing it, so be certain you've picked the right user. Adjusting the permissions of an existing member within the DaVinci Resolve Project Server runs like this: 1 Over in the top-right corner of the DaVinci Resolve Project Server, click the Members button. 2 Flip the user's role between Administrator and Collaborator by way of the selection menu. 3 Edit a user's name and password details through the Pencil icon.

### Assigning Members to Specific Project Libraries

After you've set up a few members, you can attach them to particular project libraries. That arrangement lets several teams of people work on various projects off the one Project Server without the risk that one team accidentally wipes out another team's projects or gains access to confidential material. Adding a member to a particular library, or pulling one out, works this way: 1 Bring up a library's details settings by clicking the “i” icon to the right of its name. 2 Click the Manage Members button down at the foot of the library. 3 To bring in a member, tick the box beside their name in the All Members field. 4 To drop a member, click the “x” beside their name in the Added Members field.

### The DaVinci Resolve Project Server Mange Members window

Anyone added to a project library by this method can then log in with their credentials from the Network Libraries area of the Project Manager inside DaVinci Resolve.

### Sharing Network Project Libraries via the Project Server

The DaVinci Resolve Project Server also makes it painless to stand up a shared Project Server across your local network. For that to come together, though, you'll have to meet the requirements below:

- Each workstation has to be joined to the Project Server over a local network.
- Every network link ought to be decently quick (Gigabit Ethernet or better is preferable).
- The machine acting as the Project Server should be decently quick, yet it has no

need for powerful GPU processing. The steps that follow lay out how to stand up a shared Project Server and how to export an access key that makes hooking up other workstations effortless. To configure the DaVinci Resolve Project Server: 1 Launch the DaVinci Resolve Project Server application. 2 Within the File > Network Interface menu, pick the IP address you'd like to use for reaching the client workstations.

### The Network Interface menu

IMPORTANT: Before you build and share a project library or generate an access key, you have to choose the correct Network Interface IP address — the one matching the network your client computers sit on — or else a connection error crops up. To share a project library using the DaVinci Resolve Project Server: 1 Pick or build a DaVinci Resolve project library you'd like to share, then switch the Project Library Enabled slider on; you'll find it at the top of that library's details section. 2 Once a dialog pops up asking whether you want to authorize configuring your Project Server, click Authorize. From here, other DaVinci Resolve workstations on the same network can share that library. After a Project Server is up, linking additional machines to it is simple thanks to access keys you generate from the DaVinci Resolve Project Server application. Generating one of these keys for painless server connection works as follows: 1 Pick a library you've configured for sharing, open its details section, and from the settings icon in the upper right select the Export Access Key option. 2 Through the Create Access Key dialog, pick a location and click Save. The access key file lands at the spot you picked carrying the file extension .resolvedbkey. 3 Copy that .resolvedbkey file onto the workstation you'd like to join to the shared library.

4 Launch DaVinci Resolve, and once the Project Manager shows up, open the Project Libraries sidebar, then drag the .resolvedbkey file and drop it anywhere inside the Project Manager. The shared library ought to now appear in the Project Libraries sidebar, and selecting it reveals every project housed in that library on the Project Server. When you need to, you can also turn off sharing for any given library, which blocks remote access to it from other workstations on the network. Switching sharing off goes like this: 1 With the DaVinci Resolve Project Server application running, pick a library you had enabled for sharing, then switch the Project Library Enabled slider off; it's at the top of that library's details section. 2 Once a dialog pops up asking whether you want to authorize configuring your PostgreSQL server, click Authorize. That library stops being shared. IMPORTANT: Should you enable sharing on a computer that later relocates to a different network (say, you'd set up Project Server sharing on a laptop), you'll have to turn sharing off and then back on before generating access key files capable of connecting successfully at the new network location.

### Cloud Project Libraries

Cloud project libraries live on Blackmagic's Project Library servers out on the internet, which lets DaVinci Resolve users link up and collaborate on the very same projects from anywhere on earth. For fuller details on Cloud Project Libraries, consult Chapter 191, “Blackmagic Cloud Project Server.”
