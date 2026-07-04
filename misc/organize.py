from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

# Iterate through everything in the directory
for path in current_dir.iterdir():
    # 1. Skip directories (like .git or folders we just created)
    # 2. Skip this script itself so it doesn't move while running
    if path.is_dir() or path.name == Path(__file__).name:
        continue

    # Get the file name without its extension (e.g., 'script' from 'script.py')
    folder_name = path.stem

    # Define the target directory path
    target_dir = current_dir / folder_name

    # Safely create the folder if it doesn't exist yet
    target_dir.mkdir(exist_ok=True)

    # Move the file into the new folder
    path.rename(target_dir / path.name)

print("Files organized successfully!")