
# 🗂️ MiniFATSystem

A Python-based mini shell simulation that mimics basic file system operations, inspired by classic command-line interfaces. Developed for educational purposes, especially for understanding how a File Allocation Table (FAT)-like interface could be implemented.

## 📦 Features

- List directory contents
- Navigate between directories
- Create, remove, rename files/directories
- Copy and delete files
- View file contents and details
- Search files recursively
- Check if a file is empty
- Show file size
- Clean console screen
- Built-in help system

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the Shell

```bash
python mini_fat_system.py
```

> Make sure you're running the script from a terminal that supports input/output (not just an IDE console if interaction fails).

## 🛠️ Available Commands

| Command    | Description                                |
|------------|--------------------------------------------|
| `cd`       | Change the current working directory.      |
| `cls`      | Clear the console screen.                  |
| `dir`      | List contents of the current directory.    |
| `quit`     | Exit the shell.                            |
| `copy`     | Copy a file to another location.           |
| `del`      | Delete a file (confirmation required).     |
| `help`     | Display help information.                  |
| `md`       | Create a new directory.                    |
| `rd`       | Remove a directory (must be empty).        |
| `rename`   | Rename a file.                             |
| `type`     | Show the contents of a text file.          |
| `search`   | Search for a file within directories.      |
| `empty`    | Check if a file is empty.                  |
| `size`     | Show the size of a file in bytes.          |
| `details`  | Show creation and modification dates.      |

## 📷 Screenshot

```
███████╗ ██████╗██╗     █████╗ ███████╗███████╗██╗   ██╗██╗████████╗
██╔════╝██╔════╝██║    ██╔══██╗██╔════╝██╔════╝██║   ██║██║╚══██╔══╝
█████╗  ██║     ██║    ███████║███████╗███████╗██║   ██║██║   ██║   
██╔══╝  ██║     ██║    ██╔══██║╚════██║╚════██║██║   ██║██║   ██║   
██║     ╚██████╗██║    ██║  ██║███████║███████║╚██████╔╝██║   ██║   
╚═╝      ╚═════╝╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝   ╚═╝ 
```

## 📌 Notes

- The system is case-sensitive on Unix-like systems.
- This shell is a simulation; it's not meant to replace the OS shell.
- All operations are limited to the user's file system permissions.

## 📄 License

This project is for **educational use only**.
