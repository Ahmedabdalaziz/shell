# MiniFATSystem

MiniFATSystem is a mini file management system that functions as a custom command-line interface, allowing users to perform file and directory operations easily using Python.

## Features
- Navigate between directories (`cd`)
- List directory contents (`dir`)
- Create a directory (`md`)
- Remove a directory (`rd`)
- Copy files (`copy`)
- Delete files (`del`)
- Rename files (`rename`)
- Display file contents (`type`)
- Search for files (`search`)
- Check if a file is empty (`empty`)
- Show file size (`size`)
- Show file details (`details`)
- Clear the screen (`cls`)
- Display help (`help`)
- Exit the system (`quit`)

## How to Run
1. Ensure Python is installed on your system.
2. Run the program using:
   ```bash
   python shell_project.py
   ```
3. Use the available commands to interact with the system.

## Example Commands
```bash
FCI >>>>> (C:/Users/Username)> dir
FCI >>>>> (C:/Users/Username)> md new_folder
FCI >>>>> (C:/Users/Username)> cd new_folder
FCI >>>>> (C:/Users/Username/new_folder)> copy file1.txt file2.txt
FCI >>>>> (C:/Users/Username/new_folder)> details file2.txt
FCI >>>>> (C:/Users/Username/new_folder)> quit
```

## Notes
- Commands function similarly to the Command Prompt.
- All operations are performed within the user's current directory.
- Some commands may require confirmation (e.g., `del`).


