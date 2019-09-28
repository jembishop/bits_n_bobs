# Coin
## Introduction
Coin stands for COnsistant INterface. Coin is a specification how
computers should provide a user interface that is
consistant, memorable, and fast using only the keyboard.

The fundamentals of building blocks of coin are:

### Windows
Windows are rectangular views associated with viewing collections of areas.
These areas can be of the following types .
#### Read-Write Text
This is text that can be navigated and edited.

Eg:
- The document in a text editor
- The contents of a search bar
#### Read Text
This is text which can be navigated but not edited in any way

Eg:
- The contents of the shell output
- Buttons in ui elements
- Files in file tree bar

#### Non-Read Text
This is text which cannot by default be accessed by navigation (though you can switch mode
to navigate to this)
Eg:
- The status bar in a text editor
#### Unknown

Any object which does not contain any of the above falls into this classification.
Eg:
- Gif, Image, Icon

A selection is a pair of numbers which correspond to a contiguous chunk of characters in a text area.
There can be multiple selections at the same time. All the selections are called the blob. When we refer to
operations on the blob they refer to acting on each selection in the blob individually.

Windows can be of two types:

#### Permanant
These windows:
- Are the only windows recognised using window mode.
- Can only be created by a split of a parent window
- Cannot overlap with other permanant windows

Eg:
- file tree window in IDE
- text in text editor
- shell window

Typically there should be a color coding per application such that all windows
in the application can be recognised as part of the application.
#### Ephemeral
These windows:
- Are not recognised by window mode
- Can be created at any point at any size
- Always on top of permanant windows

Eg:
- autocomplete bar
- notification
- menu option



### Modes
A mode is invoked when one of the 4 special mode keys is pressed. Invoking a mode at any time
takes you to the root of that modes command tree. Pressing keys will either take you to another node in
the command tree or execute a command.
The modes are:
- Window mode (Super)
is about creating, switching, moving and resizing windows, and
recording and executing user macros.
- Navigation mode (Caps Lock)
is about moving the current selection.
- Insertion mode (Shift)
is about changing the current selection in Read-Write objects.
- Application mode (Ctrl)
These are for application specific actions, not related to navigation or insertion of text.

Within each mode there are default and application specific commands which can be part of the
command tree (with the exception of the application mode which only has application specific commands).

Each command can return you to an arbitrary mode, or leave you at the same node to execute more commands in that node.

### Window mode

The window mode root node has the following commands:

- Switch Window Focus {Left, Up, Down, Right } ({h,j,k,l})
- Switch to last focused window (b)

And the following nodes:

- Resize(r)
    - Expand window {Left, Up, Down, Right } ({h,j,k,l})
    - Expand window {Diagonal Out, Diagonal In} ({d,f})
- Macros (m)
    - Record macro (r)
- Delete (x)
- Open(a)
- Keymap (k)
- Options (o)
- Move(s)
- Displays (d)


### Navigation mode
All commands below act on the blob.
Navigation mode has the following commands:

- Move {backward, forward} one character ({j,k})
- Undo last action (u)
- Redo last action (r)
- Select entire line (a)
- Select entire area (s)


And the following nodes:

- Find (f)
- Inclusive Find (d)
- Expand (e)
- Shrink (s)

