import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class Node: 
    def __init__(self, name: str, is_file: bool = False): 
            self.name = name 
            self.is_file = is_file 
            self.left = None   # First child (subdirectory or file) 
            self.right = None  # Sibling directory/file 

def add_node(parent: Node, name: str, is_file: bool = False) -> bool: 
        if parent.is_file == True:
            return False
        elif parent.left == None:
            new_node = Node(name, is_file)
            parent.left = new_node
            return True
        current = parent.left
        while True:
            if current.name == name:
                return False
            if current.right is None:
                break
            current = current.right
        current.right = Node(name, is_file)
        return True

def search(node: Node, name: str) -> Node | None:
        if node is None:
            return None
        if node.name == name:
            return node
        found = search(node.left, name)
        if found is not None:
            return found
        return search(node.right, name)


def print_tree(node: Node, level: int = 0) -> None:
    if node is None:
        return None
    indent = "    " * level       
    if node.is_file == True:
        icon = "📄"
    else:
        icon = "📂"
    print(indent + icon + " " + node.name)
    print_tree(node.left, level + 1)
    print_tree(node.right, level)

def main() -> None:
    root = Node("Root")         
    while True:
        print("\nChoose an action:")
        print("1. Add Directory or File")
        print("2. Print File System Structure")
        print("3. Search for a File/Directory")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            parent_name = input("Enter the parent directory name: ").strip()
            parent = search(root, parent_name)
            if parent is None:
                print(f"Parent directory '{parent_name}' not found.")
                continue
            if parent.is_file:
                print(f"Cannot add items inside '{parent_name}' because it is a file.")
                continue

            name = input("Enter the name of the file or directory: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            kind = input("Is it a file or directory? (f/d): ").strip().lower()
            if kind not in ("f", "d"):
                print("Invalid type. Please enter 'f' or 'd'.")
                continue

            is_file = (kind == "f")
            if add_node(parent, name, is_file):
                label = "file" if is_file else "directory"
                print(f"Added {label} '{name}' under '{parent_name}'.")
            else:
                print(f"'{name}' already exists under '{parent_name}'.")

        elif choice == "2":
            print("\nFile System Structure:")
            print_tree(root)

        elif choice == "3":
            name = input("Enter the name of the file or directory to search: ").strip()
            result = search(root, name)
            if result:
                label = "File" if result.is_file else "Directory"
                print(f"Found: {result.name} ({label})")
            else:
                print(f"'{name}' not found.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()