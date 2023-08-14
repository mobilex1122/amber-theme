import subprocess
import os

# List of directories to process
directories = ['common/gtk-2.0/assets-dark/', 'common/gtk-3.0/assets', 'common/gtk-4.0/assets']  # Add your directory names here

for directory in directories:
    svg_ids_file = os.path.join(directory, 'assets.txt')
    svg_file = os.path.join(directory, 'assets.svg')

    if os.path.exists(svg_ids_file) and os.path.exists(svg_file):
        # Read the SVG IDs from the text file
        with open(svg_ids_file, 'r') as file:
            svg_ids = file.read().splitlines()

        # Loop through each SVG ID and export as PNG
        for svg_id in svg_ids:
            export_filename = os.path.join(directory, f'{svg_id}.png')
            command = [
                'inkscape',
                '--export-id-only',
                f'--export-id={svg_id}',
                f'--export-filename={export_filename}',
                svg_file,
                '--export-dpi=96'
            ]
            
            subprocess.run(command)

            export_filename_dubble = os.path.join(directory, f'{svg_id}@2.png')
            command = [
                'inkscape',
                '--export-id-only',
                f'--export-id={svg_id}',
                f'--export-filename={export_filename_dubble}',
                svg_file,
                '--export-dpi=192'
            ]
            
            subprocess.run(command)

        print(f"Export completed for directory: {directory}")
    else:
        print(f"Files not found for directory: {directory}")

print("All exports completed.")
