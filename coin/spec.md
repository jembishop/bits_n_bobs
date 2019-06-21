# Coin
## Introduction
Coin stands for COnsistant INterface. Coin is a specification how
window managers and the applications they show provide a user interface that is
consistant, memorable, and fast using only the keyboard.

The fundamentals of coin are:

### Windows
Windows are rectangular views associated with viewing collections of the 4 Coin objects:
### Read-Write Text
This is text that can be navigated and edited.

Eg:
- The document in a text editor
- The contents of a search bar
### Read Text
This is text which can be navigated but not edited in any way

Eg:
- The contents of the shell output
- Buttons in ui elements
- Files in file tree bar

### Non-Read Text
This is text which cannot by default be accessed by navigation (though you can switch mode
to navigate to this)
Eg:
- The status bar in a text editor
### Unknown

Any object which does not contain any of the above falls into this classification.
Eg:
- Gif, Image, Icon
### Modes
A mode is invoked when one of the 4 special mode keys is pressed.  The keys are:

