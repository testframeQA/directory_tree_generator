import os
import argparse
import sys
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_tree(dir_path, prefix='', file_output=None):
    dir_contents = sorted(os.listdir(dir_path), key=lambda x: x.lower())
    entries = [e for e in dir_contents if os.path.isdir(os.path.join(dir_path, e))]
    files = [f for f in dir_contents if os.path.isfile(os.path.join(dir_path, f))]

    entries_count = len(entries)
    for i, entry in enumerate(entries):
        connector = '├── ' if i < entries_count - 1 else '└── '
        file_output.write(f'{prefix}{connector}{entry}\n')
        new_prefix = prefix + ('│   ' if i < entries_count - 1 else '    ')
        generate_tree(os.path.join(dir_path, entry), prefix=new_prefix, file_output=file_output)

    files_count = len(files)
    for i, file in enumerate(files):
        connector = '├── ' if i < files_count - 1 else '└── '
        file_output.write(f'{prefix}{connector}{file}\n')
        
def main():
    date = datetime.datetime.now().strftime("%m%d%y")
    time = datetime.datetime.now().strftime("%H%M%S")
    parser = argparse.ArgumentParser(description='Generate a directory tree and write it to a file')
    parser.add_argument('dir_path', type=str, help='Path to the directory to generate tree from')
    args = parser.parse_args()
    datetime_stamp = f"{date}_{time}"

    dir_path = args.dir_path.rstrip("/")
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        stripped_directory = [part for part in dir_path.split("/") if part][-1]
        results_filename = f"./test_data/tree_maps/{datetime_stamp}_{stripped_directory}_tree.txt"
        with open(results_filename, 'w') as file_output:
            file_output.write(dir_path + '\n')
            generate_tree(dir_path, file_output=file_output)
        print(f"Directory tree written to {results_filename}")
    else:
        print(f"Error: {dir_path} is not a valid directory")

if __name__ == "__main__":
    main()
