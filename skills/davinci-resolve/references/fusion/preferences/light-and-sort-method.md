# Light and sort method

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](vr-headsets-3d.md) / [Next section](library-and-application.md)
<a id="source-binssecurity"></a> <a id="source-binsserver"></a> <a id="source-light"></a> <a id="source-password"></a> <a id="source-password-1"></a> <a id="source-permissions"></a> <a id="source-server"></a> <a id="source-servers"></a> <a id="source-sort-method"></a> <a id="source-the-bin-servers-preferences"></a> <a id="source-the-bins-security-preferences"></a> <a id="source-user"></a> <a id="source-user-1"></a> <a id="source-users-list"></a>

### Light

- Disabled lighting is off.
- Auto will detect if lighting is on in the view.
- On will force lighting on in the VR view.

### Sort Method

- Z buffer sorting is OpenGL's quick approach to ordering polygons.
- Quick Sort orders polygon depth so transparency renders more cleanly.
- Full Sort applies a sturdy sort-and-render approach to draw transparency .
- Shadows can be on or off.
- Show Matte Objects toggles matte objects between visible and hidden in the view.

### Bins/Security

You'll only find Bins preferences inside Fusion Studio. They serve to administer the Bin users along with their permissions.

### The Bins Security preferences

### Users List

Each user and the permissions they hold are enumerated in the Users List. Pick any entry to revise its settings through the User and Password edit boxes.

- Add: Pressing the Add button registers a fresh user on the list once you supply a username and password.
- Remove: Click this button to remove the selected entry.

### User

For whichever Bin Server item is selected, this editable field displays its username. When the username isn't known, give “Guest” a try with no password.

### Password

Type into this field the password belonging to the Bin user listed in the Users list.

### Permissions

Distinct permission types can be assigned to users by the administrator.

- Read: Grants the user read-only access to the bins.
- Create: Lets the user make new bins.
- Admin: Hands the user complete authority over the bins system.
- Modify: Permits the user to alter bins that already exist.
- Delete: Lets the user take bins away.

### Bins/Server

Through these preferences you register Bin Servers on the roster of bins Fusion shows in the Bins dialog.

### The Bin Servers preferences

### Servers

Whatever servers currently sit in the connection list are shown by this dialog. Pick any entry to revise its settings.

- Add: Use this button to add a new server to the list.
- Remove: Click this button to remove the selected entry.

### Server

This editable field reports the name or IP address belonging to the server of the chosen list entry.

### User

The username tied to the selected Bin Server item appears in this editable dialog.

### Password

Type into this field the password for whichever server you listed in the Server list.
