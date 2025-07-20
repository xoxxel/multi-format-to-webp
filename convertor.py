import argparse
from PIL import Image
import os

def convert_to_webp(input_path, output_path=None, quality=80):
    """Convert an image to WebP format and return original and new sizes."""
    try:
        # Open the image
        img = Image.open(input_path).convert("RGB")
        
        # Set output path if not provided
        if output_path is None:
            output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".webp"
            output_path = os.path.join(os.path.dirname(input_path) or ".", output_filename)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        
        # Get original file size
        original_size = os.path.getsize(input_path)
        
        # Save as WebP
        img.save(output_path, "WEBP", quality=quality)
        
        # Get new file size
        new_size = os.path.getsize(output_path)
        
        # Calculate percentage reduction
        size_reduction = ((original_size - new_size) / original_size) * 100
        size_reduction = round(size_reduction, 2)
        
        print(f"Successfully converted: {os.path.basename(input_path)} -> {os.path.basename(output_path)} (-{size_reduction}%)")
        return original_size, new_size, True
    except Exception as e:
        print(f"Error converting {os.path.basename(input_path)}: {str(e)}")
        return None, None, False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument("input", nargs="+", help="Path to the image file(s) or directory to convert")
    parser.add_argument("-o", "--output", help="Output directory or file path (optional)")
    parser.add_argument("-q", "--quality", type=int, default=80, help="Quality of the output WebP (0-100, default: 80)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process each input
    total_converted = 0
    total_files = 0
    total_original_size = 0
    total_new_size = 0
    
    supported_extensions = (".png", ".jpg", ".jpeg", ".bmp")
    
    for input_path in args.input:
        input_path = os.path.abspath(input_path)
        
        if os.path.isdir(input_path):
            # Handle directory
            for filename in os.listdir(input_path):
                if filename.lower().endswith(supported_extensions):
                    total_files += 1
                    full_input_path = os.path.join(input_path, filename)
                    orig_size, new_size, success = convert_to_webp(full_input_path, os.path.join(args.output or input_path, filename.replace(filename.split(".")[-1], "webp")), args.quality)
                    if success:
                        total_converted += 1
                        total_original_size += orig_size
                        total_new_size += new_size
        elif os.path.isfile(input_path) and input_path.lower().endswith(supported_extensions):
            # Handle single file
            total_files += 1
            orig_size, new_size, success = convert_to_webp(input_path, args.output, args.quality)
            if success:
                total_converted += 1
                total_original_size += orig_size
                total_new_size += new_size
        else:
            print(f"Skipping {input_path}: Not a supported image file or directory")
    
    # Summary
    if total_files > 0:
        overall_reduction = ((total_original_size - total_new_size) / total_original_size) * 100
        overall_reduction = round(overall_reduction, 2)
        print(f"\nConversion summary: {total_converted} of {total_files} files converted successfully.")
        print(f"Total size reduction: -{overall_reduction}%")

if __name__ == "__main__":
    main()