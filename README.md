# HEIC to PNG Converter

A simple, efficient Python tool to convert HEIC/HEIF images to PNG format. Supports both single file conversion and batch processing of entire directories.

**✅ Fully compatible with Windows 11, Windows 10, macOS, and Linux**

## Features

- Convert single HEIC files to PNG
- Batch convert entire directories
- Recursive directory processing
- Preserves image quality
- Handles transparency (RGBA images)
- Command-line interface and drag-and-drop support (Windows)
- Verbose output option
- Cross-platform compatibility

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

### Windows 11 / Windows 10 (Easy Method)

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - **Important**: Check "Add Python to PATH" during installation
   - Recommended: Python 3.11 or newer

2. **Download this tool**:
   - Download and extract the ZIP from GitHub
   - Or clone: `git clone <repository-url>`

3. **Run the installer**:
   - Double-click `install_windows.bat`
   - Wait for installation to complete

That's it! You're ready to convert HEIC files.

### Windows 11 / Windows 10 (Manual Method)

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Open Command Prompt or PowerShell
3. Navigate to the tool directory:
   ```cmd
   cd path\to\heic_png
   ```
4. Install dependencies:
   ```cmd
   python -m pip install -r requirements.txt
   ```

### macOS / Linux

1. Ensure Python 3.7+ is installed:
   ```bash
   python3 --version
   ```

2. Clone this repository:
   ```bash
   git clone <repository-url>
   cd heic_png
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt
   ```

## Usage

### Windows 11 / Windows 10 - Drag and Drop (Easiest!)

**Super easy method - No command line needed!**

1. Locate `convert_drag_drop.bat` in the tool folder
2. Drag and drop your HEIC file(s) or folder onto `convert_drag_drop.bat`
3. Wait for conversion to complete
4. Find your PNG files in the same location as the originals

### Windows 11 / Windows 10 - Command Line

Open Command Prompt or PowerShell in the tool folder, then:

**Convert a single file:**
```cmd
heic_to_png.bat image.heic
```

**Convert with custom output name:**
```cmd
heic_to_png.bat image.heic -o output.png
```

**Convert all HEIC files in a folder:**
```cmd
heic_to_png.bat -d C:\Users\YourName\Pictures
```

**Convert folder recursively:**
```cmd
heic_to_png.bat -d C:\Users\YourName\Pictures -r -v
```

**Note**: You can also use `python heic_to_png.py` instead of `heic_to_png.bat`

### macOS / Linux

**Convert a single file:**
```bash
python heic_to_png.py image.heic
```

**Convert with custom output name:**
```bash
python heic_to_png.py image.heic -o output.png
```

**Convert all HEIC files in a directory:**
```bash
python heic_to_png.py -d /path/to/images
```

**Recursive directory conversion:**
```bash
python heic_to_png.py -d /path/to/images -r
```

**Convert to a different output directory:**
```bash
python heic_to_png.py -d /path/to/images -o /path/to/output
```

**Verbose output:**
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

### Windows Examples

```cmd
REM Convert a single photo
heic_to_png.bat photo.heic

REM Convert all photos in Downloads folder
heic_to_png.bat -d C:\Users\YourName\Downloads

REM Convert all photos in Pictures folder recursively
heic_to_png.bat -d C:\Users\YourName\Pictures -r -v

REM Convert iPhone photos to a new folder
heic_to_png.bat -d "C:\Users\YourName\Pictures\iPhone Photos" -o "C:\Users\YourName\Pictures\PNG"

REM Convert with custom output name
heic_to_png.bat IMG_1234.heic -o vacation_photo.png
```

### macOS / Linux Examples

```bash
# Convert a single photo
python heic_to_png.py photo.heic

# Convert all photos in a folder
python heic_to_png.py -d ~/Pictures/iPhone

# Convert all photos recursively with verbose output
python heic_to_png.py -d ~/Pictures -r -v

# Convert to a specific output directory
python heic_to_png.py -d ~/heic_photos -o ~/png_photos

# Convert with custom output name
python heic_to_png.py IMG_1234.heic -o vacation_photo.png
```

## How It Works

The tool uses:
- **Pillow (PIL)**: The Python Imaging Library for image processing
- **pillow-heif**: A plugin that enables Pillow to read HEIC/HEIF files

HEIC (High Efficiency Image Container) is a modern image format used primarily by Apple devices. This tool converts these files to the widely-supported PNG format while preserving image quality.

## Troubleshooting

### Windows-Specific Issues

**"Python is not recognized as an internal or external command"**
- Python is not installed or not in PATH
- Reinstall Python and check "Add Python to PATH" during installation
- Or download from Microsoft Store: search "Python" in Windows Store

**"pip is not available"**
- Run: `python -m ensurepip --upgrade`
- Or reinstall Python with pip included

**Installation fails with permission errors**
- Run Command Prompt as Administrator
- Or use: `python -m pip install --user -r requirements.txt`

**Drag-and-drop doesn't work**
- Make sure you've run `install_windows.bat` first
- Try right-clicking `convert_drag_drop.bat` and "Run as administrator"

**Paths with spaces don't work**
- Use quotes around paths: `heic_to_png.bat -d "C:\My Photos"`

### General Issues

**Import Errors**

If you see import errors, ensure you've installed the dependencies:
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
pip install -r requirements.txt
```

**File Not Found**

- Make sure the input file or directory path is correct and accessible
- On Windows, use backslashes `\` or forward slashes `/` in paths
- Use quotes around paths containing spaces

**Conversion Failures**

- Verify the input file is a valid HEIC/HEIF image
- Check that you have write permissions for the output directory
- Use the `-v` flag for detailed error messages
- Some HEIC files may use proprietary codecs - try with different HEIC files

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
