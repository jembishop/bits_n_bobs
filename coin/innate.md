# Innate 
## Introduction
Innate is a minimal text editor designed to be the proof of concept of the Navigation and 
Insertion modes of the Coin specification.

### Design Principles 
- Find is your friend - To move somewhere you should type the text there
- Manipulate blobs not cursors - Innate unites selections, multiple selections and cursors can be united
into one concept, the blob
- You can relearn it - Innate thinks a better interface is fundamentally better than a familiar one
- Less keys are better - Innate by only uses the alphabetical characters, comma, period, colon and 4 control characters.
## Modes 
Innate has two modes Navigation mode and Modify mode.
Navigation mode concerns itself with the creation, manipulation, and deletion of the blob. Modify mode 
concerns itself with modifying the content of the blob. 
### Navigation mode
Pressing Caps at any point will bring you to the root of the navigation tree.
From here you can either press a key execute a command or enter another submode.
 

