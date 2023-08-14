import subprocess

# Read the SVG IDs from the text file
with open('assets.txt', 'r') as file:
    svg_ids = file.read().splitlines()

# Loop through each SVG ID and export as PNG
for svg_id in svg_ids:
    export_filename = f'{svg_id}.png'
    command = [
        'inkscape',
        '--export-id-only',
        f'--export-id={svg_id}',
        f'--export-filename={export_filename}',
        'assets.svg',
        '--export-dpi=96'
    ]
    
    subprocess.run(command)

    export_filename_dubble = f'{svg_id}@2.png'
    command = [
        'inkscape',
        '--export-id-only',
        f'--export-id={svg_id}',
        f'--export-filename={export_filename_dubble}',
        'assets.svg',
        '--export-dpi=192'
    ]
    
    subprocess.run(command)

print("Export completed.")


