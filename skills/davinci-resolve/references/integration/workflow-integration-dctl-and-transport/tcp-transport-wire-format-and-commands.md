# TCP transport wire format and commands

Version: DaVinci Resolve 20.3 Reference Manual. Context: Workflow integration DCTL and transport.
[Chapter index](INDEX.md) / [Previous section](dctl-spatial-mirror-example.md)
<a id="source-about-the-tcp-protocol-version-12"></a> <a id="source-command-format"></a> <a id="source-communication-delays"></a> <a id="source-connect"></a> <a id="source-data-types"></a> <a id="source-getframerate"></a> <a id="source-gettc"></a> <a id="source-goto"></a> <a id="source-play"></a> <a id="source-response-format"></a> <a id="source-status-response-values"></a> <a id="source-tcp-protocol-for-davinci-resolve-transport-control"></a> <a id="source-tcp-protocol-for-davinci-resolve-transport-control-1"></a> <a id="source-tcp-protocol-stream"></a>

## TCP Protocol for DaVinci Resolve Transport Control

### TCP Protocol for DaVinci Resolve Transport Control

Building outside utilities that drive Transport Control through DaVinci Resolve is what this chapter explains.

### About the TCP Protocol Version 1.2

The communication standard between outside applications (“Client”) and DaVinci Resolve (“Server”) over the TCP protocol is set out by this protocol. The server uses port number 9060. This protocol does not employ SSL. Exchanges happen as request-response messages, in which the Client kicks off a command and the Server answers as appropriate. Before you can use this protocol, you first have to enter the string below into the Advanced panel of the DaVinci Resolve System Preferences: `System.Remote.Control = 1`

### Data Types

This protocol makes use of the following data types:

- float (f): A 4-byte IEEE 754 single precision float
- int (i): A 4-bytes signed int
- unsigned char (uc): A 1-byte unsigned char (0–255)
- string (s): A UTF-8 encoded string. There is no terminator defined for it. This string forms a composite

type, sent as one int (i) that gives the count of characters in the string (N), trailed by N unsigned chars (uc) that hold the string’s letters.

NOTE: The float and int types have their bytes sent over in little endian order.

### Command Format

A command goes out as a single string (limited to characters a–z (0x61 – 0x7A)), trailed by whatever extra payload the command’s definition calls for.

### Response Format

Any command’s response is made up of a status byte (unsigned char), trailed by whatever extra payload the response calls for.

### Communication Delays

After the command string’s first byte goes out, the remainder of the command string plus the payload data has to come along without delay. When COMMAND finishes, the server has to answer right away. Should this process stall for over 5 seconds, whichever party is awaiting data may drop the connection, taking it that the peer has stopped responding. At present no cap exists on how long the gap between two successive commands can be.

NOTE: As an alternative, a maximum allowable delay can be set, in which event the client may fire periodic ‘connect’ commands to hold the connection open.

### Status Response Values

Here is what the status values signify:

- 0x00: Command was executed successfully. Any additional payload is sent as expected.
- 0xFF: Command could not be executed successfully. No additional payload will follow.

### TCP Protocol Stream

These are the commands you can transmit across the protocol stream.

### connect

To begin the stream, the client transmits a connect command string. No payload accompanies it. A status value of 0x00 comes back from the server.

### goto

The client transmits a goto command string trailed by four unsigned chars that stand for the timecode’s hour, minute, second, and frame. The server returns a fitting status byte reflecting how the command ran.

### play

The client transmits a play command string trailed by a floating point value. Real-time playback is 1.0, a stop is 0.0, reverse is -1.0, 2x is 2.0, and so on. The server returns a fitting status byte reflecting how the command ran.

### gettc

The client transmits a gettc command string. The server returns a fitting status byte (for example, the status byte can be 0xFF when no timeline is present). When the status byte reads 0x00, four unsigned chars follow that stand for the timecode’s hour, minute, second, and frame.

### getframerate

The client transmits a getframerate command string. The server returns a fitting status byte. When the status byte reads 0x00, a floating point value for the frame rate follows.
