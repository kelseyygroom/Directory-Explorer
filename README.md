# ICS-32-Directory-Explorer

A project from ICS 32: Programming with Software Libraries at UC Irvine.

This project implements a Command Line Interface for exploring directories, filtering files based on various criteria, and performing specific actions on selected files. It supports recursive directory traversal, file filtering, and actions like duplicating, printing, or modifying files. It uses the pathlib, os, shutil, and datetime modules from the Python Standard Library.

## Features:
**Directory Listing:**
1. D: Lists files in a directory (non-recursive)
2. R: Recursively lists files ina directory and its subdirectories

**File Filtering:**
1. A: No filtering (all files).
2. N name: Filters files by name.
3. E extension: Filters files by file extension.
4. T phrase: Filters files containing a specified text/phrase.
5. < size: Filters files smaller than a specified size (in bytes).
6. \> size: Filters files larger than a specified size (in bytes).

**Actions on Filtered Files:**
1. F: Prints the first line of text in text files or indicates if the file is not a text file.
2. D: Duplicates each file in the list, appending .dup to the filename.
3. T: Updates the last modified time of each file to the current time.
