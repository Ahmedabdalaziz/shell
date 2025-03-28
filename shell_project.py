import os
from datetime import datetime

class MiniFATSystem:
    def __init__(self):
        self.current_path = os.getcwd()
        self.show_banner()

    def show_banner(self):
        print("""
███████╗ ██████╗██╗     █████╗ ███████╗███████╗██╗   ██╗██╗████████╗
██╔════╝██╔════╝██║    ██╔══██╗██╔════╝██╔════╝██║   ██║██║╚══██╔══╝
█████╗  ██║     ██║    ███████║███████╗███████╗██║   ██║██║   ██║   
██╔══╝  ██║     ██║    ██╔══██║╚════██║╚════██║██║   ██║██║   ██║   
██║     ╚██████╗██║    ██║  ██║███████║███████║╚██████╔╝██║   ██║   
╚═╝      ╚═════╝╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝   ╚═╝                                                                  
""")
    
    def help(self, command=None):
        commands = {
            "cd": "Change the current default directory.",
            "cls": "Clear the screen.",
            "dir": "List the contents of the current directory.",
            "quit": "Quit the shell.",
            "copy": "Copy a file to another location.",
            "del": "Delete a file.",
            "help": "Provides help information for commands.",
            "md": "Create a directory.",
            "rd": "Remove a directory.",
            "rename": "Rename a file.",
            "type": "Display the contents of a text file.",
            "search": "Search for a file in a directory.",
            "empty": "Check if a file is empty.",
            "size": "Show the size of a file.",
            "details": "Show details of a file."
        }
        if command:
            print(commands.get(command, f"No help available for '{command}'."))
        else:
            print("\n")
            for cmd, desc in commands.items():
                print(f"{cmd}: {desc}")
            print("\n")
    
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def quit(self):
        print("Exiting FCI Assuit Shell...")
        exit()

    def change_directory(self, path=None):
        if not path:
            print(f"Current directory: {self.current_path}")
        else:
            try:
                os.chdir(path)
                self.current_path = os.getcwd()
                print(f"Changed directory to {self.current_path}")
            except FileNotFoundError:
                print("Error: Directory not found.")

    def list_directory(self):
        print("Contents of directory:")
        for item in os.listdir(self.current_path):
            print(f"- {item}")
        print("Directory listing completed.")

    def create_directory(self, dirname):
        try:
            os.mkdir(dirname)
            print(f"Directory '{dirname}' created successfully.")
        except FileExistsError:
            print("Error: Directory already exists.")

    def remove_directory(self, dirname):
        try:
            os.rmdir(dirname)
            print(f"Directory '{dirname}' removed successfully.")
        except FileNotFoundError:
            print("Error: Directory not found.")
        except OSError:
            print("Error: Directory is not empty.")

    def copy_file(self, src, dest):
        try:
            with open(src, 'rb') as f_src:
                with open(dest, 'wb') as f_dest:
                    f_dest.write(f_src.read())
            print(f"File '{src}' copied to '{dest}'.")
        except FileNotFoundError:
            print("Error: Source file not found.")

    def delete_file(self, filename):
        try:
            confirm = input(f"Are you sure you want to delete '{filename}'? (yes/no): ").lower().strip()
            if confirm == 'yes':
                os.remove(filename)
                print(f"File '{filename}' deleted successfully.")
            else:
                print("File deletion Cancel.")
        except FileNotFoundError:
            print("Error: File not found.")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"File '{old_name}' renamed to '{new_name}'.")
        except FileNotFoundError:
            print("Error: File not found.")

    def display_file(self, filename):
        try:
            with open(filename, 'r') as f:
                print(f.read())
            print(f"Displayed content of '{filename}'.")
        except FileNotFoundError:
            print("Error: File not found.")
        except UnicodeDecodeError:
            print("Error: Cannot display binary files.")
    
    def search_files(self, filename, directory=None):
        directory = directory or self.current_path
        for root, _, files in os.walk(directory):
            if filename in files:
                print(f"Found: {os.path.join(root, filename)}")
                return
        print("File not found.")
    
    def is_file_empty(self, filename):
        try:
            if os.path.getsize(filename) == 0:
                print(f"File '{filename}' is empty.")
            else:
                print(f"File '{filename}' is not empty.")
        except FileNotFoundError:
            print("Error: File not found.")
    
    def file_size(self, filename):
        try:
            size = os.path.getsize(filename)
            print(f"Size of '{filename}': {size} bytes")
        except FileNotFoundError:
            print("Error: File not found.")
    
    def file_details(self, filename):
        try:
            stats = os.stat(filename)
            modified_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            created_time = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Details of '{filename}':")
            print(f"Size: {stats.st_size} bytes")
            print(f"Created: {created_time}")
            print(f"Modified: {modified_time}")
        except FileNotFoundError:
            print("Error: File not found.")
    
    
    
    def run(self):
        while True:
            command = input(f"FCI >>>>> ({self.current_path})> ").strip().split()
            if not command:
                continue
            
            cmd, *args = command
            if cmd == "help":
                self.help(*args)
            elif cmd == "cls":
                self.cls()
            elif cmd == "quit":
                self.quit()
            elif cmd == "cd":
                
                self.change_directory(*args)
            elif cmd == "dir":
                self.list_directory()
            elif cmd == "md":
                self.create_directory(*args)
            elif cmd == "rd":
                self.remove_directory(*args)
            elif cmd == "copy":
                if len(args) == 2:
                    self.copy_file(args[0], args[1])
                else:
                    print("copy <source> <destination>")
            elif cmd == "del":
                self.delete_file(*args)
            elif cmd == "rename":
                if len(args) == 2:
                    self.rename_file(args[0], args[1])
                else:
                    print("rename <old_name> <new_name>")
            elif cmd == "type":
                self.display_file(*args)
            elif cmd == "search":
                self.search_files(*args)
            elif cmd == "empty":
                self.is_file_empty(*args)
            elif cmd == "size":
                self.file_size(*args)
            elif cmd == "details":
                self.file_details(*args)
            else:
                print("mosh 3ndna dah, 2ktb 'help' 3lshan tshof el commands.")

if __name__ == "__main__":
    system = MiniFATSystem()
    system.run()
