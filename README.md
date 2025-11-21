# HEIC to PNG Converter

A simple, efficient Python tool to convert HEIC/HEIF images to PNG format. Supports both single file conversion and batch processing of entire directories.

## Features

- Convert single HEIC files to PNG
- Batch convert entire directories
- Recursive directory processing
- Preserves image quality
- Handles transparency (RGBA images)
- Command-line interface
- Verbose output option

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd heic_png
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Convert a Single File

```bash
python heic_to_png.py image.heic
```

This will create `image.png` in the same directory.

### Convert with Custom Output Name

```bash
python heic_to_png.py image.heic -o output.png
```

### Convert All HEIC Files in a Directory

```bash
python heic_to_png.py -d /path/to/images
```

### Recursive Directory Conversion

```bash
python heic_to_png.py -d /path/to/images -r
```

This will process all HEIC files in the directory and its subdirectories.

### Convert to a Different Output Directory

```bash
python heic_to_png.py -d /path/to/images -o /path/to/output
```

### Verbose Output

```bash
python heic_to_png.py image.heic -v
```

## Command-Line Options

```
positional arguments:
  input                 Input HEIC file or directory

optional arguments:
  -h, --help            Show help message and exit
  -d, --directory DIR   Process all HEIC files in directory
  -o, --output PATH     Output file or directory path
  -r, --recursive       Recursively process subdirectories
  -q, --quality NUM     PNG compression quality (0-100, default: 95)
  -v, --verbose         Verbose output
```

## Examples

```bash
# Convert a single photo
python heic_to_png.py photo.heic

# Convert all photos in a folder
python heic_to_png.py -d ./photos

# Convert all photos recursively with verbose output
python heic_to_png.py -d ./photos -r -v

# Convert to a specific output directory
python heic_to_png.py -d ./heic_photos -o ./png_photos

# Convert with custom output name
python heic_to_png.py IMG_1234.heic -o vacation_photo.png
```

## How It Works

The tool uses:
- **Pillow (PIL)**: The Python Imaging Library for image processing
- **pillow-heif**: A plugin that enables Pillow to read HEIC/HEIF files

HEIC (High Efficiency Image Container) is a modern image format used primarily by Apple devices. This tool converts these files to the widely-supported PNG format while preserving image quality.

## Troubleshooting

### Import Errors

If you see import errors, ensure you've installed the dependencies:
```bash
pip install -r requirements.txt
```

### File Not Found

Make sure the input file or directory path is correct and accessible.

### Conversion Failures

- Verify the input file is a valid HEIC/HEIF image
- Check that you have write permissions for the output directory
- Use the `-v` flag for detailed error messages

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
