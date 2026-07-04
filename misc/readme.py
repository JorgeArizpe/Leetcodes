import os

def add_readme_to_subfolders(target_directory):
    # Iterate through all items in the specified directory
    for item in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item)
        
        # Check if the item is a directory
        if os.path.isdir(item_path):
            readme_path = os.path.join(item_path, 'README.md')
            
            # Check if README.md already exists
            if not os.path.exists(readme_path):
                try:
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        # Writes a default heading with the folder name
                        f.write( f'{item}\n\nThis is the README for {item}.\n')
                    print(f'Created: {readme_path}')
                except Exception as e:
                    print(f"Error creating {readme_path}: {e}")

if __name__ == "__main__":
    # Replace with your target directory path (e.g., '.')
    target_dir = '.' 
    add_readme_to_subfolders(target_dir)