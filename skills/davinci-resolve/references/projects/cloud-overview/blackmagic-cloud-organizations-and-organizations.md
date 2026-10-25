# Blackmagic cloud organizations and organizations

Version: DaVinci Resolve 20.3 Reference Manual. Context: Cloud overview.
[Chapter index](INDEX.md) / [Next section](storage-tab-showing-the-storage-graph-and-presentations.md)
<a id="source-blackmagic-cloud-organizations"></a> <a id="source-blackmagic-cloud-organizations-1"></a> <a id="source-blackmagic-cloud-organizations-live-sync"></a> <a id="source-blackmagic-server-vs-dedicated-server"></a> <a id="source-creating-an-organization-account"></a> <a id="source-groups"></a> <a id="source-home"></a> <a id="source-licenses"></a> <a id="source-members"></a> <a id="source-organizations"></a> <a id="source-overview"></a> <a id="source-project-servers"></a> <a id="source-storage"></a> <a id="source-the-create-organization-window"></a> <a id="source-the-project-servers-interface"></a>

## Overview

Topics in this chapter: Blackmagic Cloud Organizations; Live Sync.

## Blackmagic Cloud Organizations

### Blackmagic Cloud Organizations

For a large company juggling many collaborators, standing up an Organization within the Blackmagic Cloud puts user management, storage, licenses, and consolidated billing all under one straightforward interface.

### Organizations

With Blackmagic Cloud you can set up an Organization account that pulls storage, permissions, licensing, and billing together into a single interface. For enterprises of any size carrying multiple users, an organization is the ideal way to manage things. You get to decide which of your organization’s members reach which project libraries, bundle members into particular roles or by project, and oversee your storage and DaVinci Resolve licenses.

### Creating an Organization Account

An organization account has to wait until you’ve first set up a personal account over on the Blackmagic Cloud website. That user becomes the organization’s default owner, although you’re free to bring on additional owners and manage them down the line. With a personal account in hand, sign in and click the Organizations icon. A plain sign up window then opens. There you can enter your organization’s name along with the country you reside in for billing purposes.

### The Create Organization window

### Home

This tab lays out a dashboard and summary of the services your Organization has bought; click any pane and you’re carried off to that part of the website. The Home tab hands you a simple dashboard displaying your Organization’s current services.

### Members

From this tab you can bring members into your organization or take them out. Invitations reach members by email, and each one needs to already hold, or go sign up for, a Blackmagic Cloud account.

Adding and removing your organization’s members is handled through the Members tab.

By default the Members tab lists a project’s Active members. Clicking Pending instead surfaces invited users who haven’t yet accepted, where you can resend the invitation or rescind it altogether. Off to the right sit search and sort tools so members are easy to track down in large organizations. Only those members carrying Owner permissions may bring members into or take them out of an organization. To Add a Member to an Organization: 1 Within the Organization’s Members tab, click the Add Members button up at the top right. 2 In the Add Members dialog box, type one email address, or several at once to invite multiple members together. 3 When done, click the Add Members button to fire off the invite emails to everyone listed in the box. To Remove a Member from an Organization: 1 Under Active Members, click the 3-dot option menu beside the user you’re removing. 2 Pick Remove Member out of the option menu. 3 When the Remove Member warning pops up, click the Remove button. You can dispatch several member invitations together, yet removing members must currently be done one at a time. TIP: Individual members can be slotted into existing groups via Add to Group in the option menu.

### Groups

The Groups tab gives you a further layer of organization for your members, letting you cluster them by particular roles, projects, or whatever criteria suits your organization. With that, you can swiftly assign everyone in a group to a Project Library, or switch on whatever DaVinci Resolve Studio licenses your organization has bought.

Sorting members into user-defined groups happens through the Groups tab. By default it displays the Groups that are currently active. In the example above, we’ve set up an organization for a made-up travel show. We built two groups: one named Cinematographers, whose members can automatically push footage from the field straight into their assigned projects. The other we named editors, who need not only access to that footage but also license keys for the DaVinci Resolve Studio copies the organization purchased. Only members with

Owner permissions are needed to bring members into or pull them out of a group, and any member may belong to several groups at once.

New groups are born in the Group Settings. To Create a New Group: 1 On the Groups tab, click Add Group. 2 In the Group Settings dialog, supply a name for the new group. 3 If you like, add a Group Email for notifications by typing a forwarding address for email into the field. 4 Click Save. To Delete a Group: 1 Open, on the Groups tab, the 3-dot option menu belonging to an active group. 2 Pick Delete Group out of the option menu. 3 Within the warning dialog, press the Delete button. The deletion is instant and can’t be undone.

Within Manage Members, the assigned group members sit on the right and every Organization member sits on the left.

To Add a Member to a Group: 1 Open, on the Groups tab, the 3-dot option menu belonging to an active group. 2 Pick Group Settings from the option menu 3 Inside Group Settings, click the Manage Members button. 4 Within the Manage Members interface, choose one or more members out of the left-hand column. 5 Press Add Selected to Group. 6 Press Update. Removing a member from a group goes like this: 1 From the Groups tab, bring up the 3-dot option menu attached to an active group. 2 Pick Group Settings from the option menu 3 Inside Group Settings, click the Manage Members button. 4 Within the Manage Members interface, choose one or more members out of the right column. 5 Press Remove Selected. 6 Press Update.

### Project Servers

The Project Servers tab lets you view your existing cloud project libraries, purchase more, or remove ones your organization no longer uses. Keep in mind that a single project library can house multiple projects, so there’s no real need to spin up a fresh library for every episode, video project, or film. Members and Groups, though, are granted access at the project library level, meaning they can view and edit every project housed in that library. For that reason you might prefer separate project libraries for things such as distinct clients, social media channels, or shows.

### The Project Servers interface

### Blackmagic Server vs. Dedicated Server

The very first decision for your organization is whether a Blackmagic or Dedicated server will host your project libraries and media. Blackmagic Design runs the Blackmagic servers, and, as with most cloud services, several users and accounts share them at once. That doesn’t put other users’ files within your reach; it only means everyone’s data lives on the same machine. Should security, performance, or insurance considerations lead your Organization to want a private dedicated server shared with no one, you can choose Buy Dedicated Server instead.

The Buy Blackmagic and Dedicated Project Server interface To buy project libraries, click the Buy Libraries button, just enter the number or the dedicated plan you want, then press Add to Cart. After that, click the cart to wrap up the purchase details. To take a project library away, click the Remove Libraries button, then dial the count down to drop unused project libraries from your plan. Do note that you can’t bring your project libraries below the number currently active or in use; attempt it and up pops a message explaining that project libraries cannot be reduced below the amount currently active, and asking you to please disable or delete the active ones, then try again. TIP: Once you’ve hit your Project Library limit, think about “disabling” a Cloud Project Library — over within the Project Server section — instead of removing it outright. Libraries you’ve disabled don’t count against your Project Library Limit, escape deletion, and can be “enabled” once more whenever the need returns. Treat the Project Library Limit as the number of “active” libraries you require right now, not as the grand total you’ve created.

### Licenses

Organizations may rent individual DaVinci Resolve Studio licenses on a month-to-month basis. This tab is where they buy, hand back, and administer those licenses as the need arises. By default, the Licenses tab opens onto a view of who holds assigned licenses and the overall number of licenses you have.

The Licenses interface, with the Editors group shown holding 2 assigned licenses To Rent Monthly Licenses of DaVinci Resolve Studio: 1 On the Licenses tab, click Rent Licenses. 2 In the Rent Licenses window, choose how many licenses you require. 3 Click Add to Cart, then complete the checkout procedure. To Assign Licenses of DaVinci Resolve Studio: 1 On the Licenses tab, click Assign Licenses. 2 In the Assign Licenses window, key in the Member or Group name you’re assigning licenses to. 3 Press Assign Licenses. That member and the count of licenses assigned now appear back on the main Licenses tab. To Unassign Licenses of DaVinci Resolve Studio: 1 On the Licenses tab, click the 3-dot option menu beside the member or group you’re unassigning. 2 Pick Unassign Licenses. 3 In the warning box, press Remove. Unassigned licenses go back into the license pool, ready for other members and groups to use.

To Remove Monthly Licenses of DaVinci Resolve Studio: 1 On the Licenses tab, click Remove Licenses. 2 In the Remove Licenses window, choose how many surplus licenses you no longer require. 3 Press Continue to refresh your billing. You can’t pull more licenses than are currently assigned to members. To trim the license count further, you’ll first need to unassign these licenses. To Activate a Monthly License of DaVinci Resolve Studio on a Workstation

- Launch DaVinci Resolve Studio and press the Use Blackmagic ID button.
- Sign into Blackmagic Cloud with the member credentials that

have a license assigned to them.

- Pick the Organization that carries your license.
- DaVinci Resolve lets you know whether an active license has turned up.
- Press Continue.

### Storage

The Storage tab puts up a simple graph charting how much storage you’ve consumed, how much remains free, and what kinds of data are being held. You can likewise buy additional storage or pare back the amount your Organization is using.
