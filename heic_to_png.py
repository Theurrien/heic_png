#!/usr/bin/env python3
"""
HEIC to PNG Converter
Converts HEIC/HEIF images to PNG format with support for single files and batch processing.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Tuple

try:
    from PIL import Image
    from pillow_heif import register_heif_opener
except ImportError as e:
    print(f"Error: Required dependencies not installed.", file=sys.stderr)
    print("Please run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# Register HEIF opener with Pillow
register_heif_opener()


class HeicConverter:
    """Handles conversion of HEIC images to PNG format."""

    HEIC_EXTENSIONS = {'.heic', '.heif'}

    def __init__(self, quality: int = 95, verbose: bool = False):
        """
        Initialize the converter.

        Args:
            quality: PNG compression quality (0-100)
            verbose: Enable verbose output
        """
        self.quality = quality
        self.verbose = verbose

    def convert_file(self, input_path: Path, output_path: Path = None) -> bool:
        """
        Convert a single HEIC file to PNG.

        Args:
            input_path: Path to input HEIC file
            output_path: Path for output PNG file (optional)

        Returns:
            True if conversion successful, False otherwise
        """
        try:
            if not input_path.exists():
                print(f"Error: Input file not found: {input_path}", file=sys.stderr)
                return False

            if input_path.suffix.lower() not in self.HEIC_EXTENSIONS:
                print(f"Warning: {input_path} doesn't appear to be a HEIC file", file=sys.stderr)

            # Generate output path if not provided
            if output_path is None:
                output_path = input_path.with_suffix('.png')

            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if self.verbose:
                print(f"Converting: {input_path} -> {output_path}")

            # Open and convert image
            with Image.open(input_path) as img:
                # Convert to RGB if necessary (HEIC can have transparency)
                if img.mode in ('RGBA', 'LA', 'P'):
                    # Keep transparency for RGBA images
                    img.save(output_path, 'PNG', optimize=True)
                else:
                    # Convert to RGB for other modes
                    rgb_img = img.convert('RGB')
                    rgb_img.save(output_path, 'PNG', optimize=True)

            if self.verbose:
                print(f"✓ Successfully converted: {output_path}")

            return True

        except Exception as e:
            print(f"Error converting {input_path}: {e}", file=sys.stderr)
            return False

    def convert_directory(self, input_dir: Path, output_dir: Path = None,
                         recursive: bool = False) -> Tuple[int, int]:
        """
        Convert all HEIC files in a directory.

        Args:
            input_dir: Input directory path
            output_dir: Output directory path (optional, uses input_dir if not specified)
            recursive: Recursively process subdirectories

        Returns:
            Tuple of (successful_conversions, failed_conversions)
        """
        if not input_dir.exists() or not input_dir.is_dir():
            print(f"Error: Invalid input directory: {input_dir}", file=sys.stderr)
            return 0, 0

        # Use input directory as output if not specified
        if output_dir is None:
            output_dir = input_dir

        # Find all HEIC files
        pattern = '**/*' if recursive else '*'
        heic_files = []
        for ext in self.HEIC_EXTENSIONS:
            heic_files.extend(input_dir.glob(f'{pattern}{ext}'))
            heic_files.extend(input_dir.glob(f'{pattern}{ext.upper()}'))

        if not heic_files:
            print(f"No HEIC files found in {input_dir}", file=sys.stderr)
            return 0, 0

        print(f"Found {len(heic_files)} HEIC file(s) to convert")

        successful = 0
        failed = 0

        for heic_file in heic_files:
            # Calculate relative path for maintaining directory structure
            rel_path = heic_file.relative_to(input_dir)
            output_path = output_dir / rel_path.with_suffix('.png')

            if self.convert_file(heic_file, output_path):
                successful += 1
            else:
                failed += 1

        return successful, failed


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Convert HEIC/HEIF images to PNG format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single file
  %(prog)s image.heic

  # Convert a single file with custom output name
  %(prog)s image.heic -o output.png

  # Convert all HEIC files in a directory
  %(prog)s -d /path/to/images

  # Convert all HEIC files recursively
  %(prog)s -d /path/to/images -r

  # Convert directory to a different output directory
  %(prog)s -d /path/to/images -o /path/to/output
        """
    )

    # Input options
    parser.add_argument('input', nargs='?', type=str,
                       help='Input HEIC file or directory')
    parser.add_argument('-d', '--directory', type=str,
                       help='Process all HEIC files in directory')
    parser.add_argument('-o', '--output', type=str,
                       help='Output file or directory path')

    # Processing options
    parser.add_argument('-r', '--recursive', action='store_true',
                       help='Recursively process subdirectories')
    parser.add_argument('-q', '--quality', type=int, default=95,
                       help='PNG compression quality (0-100, default: 95)')

    # Display options
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')

    args = parser.parse_args()

    # Validate input
    if not args.input and not args.directory:
        parser.print_help()
        sys.exit(1)

    # Initialize converter
    converter = HeicConverter(quality=args.quality, verbose=args.verbose)

    # Process directory or single file
    if args.directory:
        input_dir = Path(args.directory)
        output_dir = Path(args.output) if args.output else None

        successful, failed = converter.convert_directory(
            input_dir, output_dir, args.recursive
        )

        print(f"\nConversion complete:")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")

        sys.exit(0 if failed == 0 else 1)

    else:
        input_path = Path(args.input)
        output_path = Path(args.output) if args.output else None

        if converter.convert_file(input_path, output_path):
            print("Conversion successful!")
            sys.exit(0)
        else:
            print("Conversion failed!", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
