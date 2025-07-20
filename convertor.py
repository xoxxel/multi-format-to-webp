import argparse
from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=80):
    try:
        img = Image.open(input_path).convert("RGB")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        original_size = os.path.getsize(input_path)
        img.save(output_path, "WEBP", quality=quality)
        new_size = os.path.getsize(output_path)

        reduction = ((original_size - new_size) / original_size) * 100
        print(f"✅ {os.path.basename(input_path)} → {os.path.basename(output_path)} | 🪶 -{round(reduction, 2)}%")
        return original_size, new_size, True
    except Exception as e:
        print(f"❌ Failed: {input_path} | Error: {str(e)}")
        return 0, 0, False

def main():
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument("input", nargs="+", help="Image file(s) or folder(s) to convert")
    parser.add_argument("-o", "--output", help="Optional output directory")
    parser.add_argument("-q", "--quality", type=int, default=80, help="WebP quality (0-100, default=80)")
    args = parser.parse_args()

    supported = (".png", ".jpg", ".jpeg", ".bmp")
    total_files = total_converted = 0
    total_original = total_converted_size = 0

    for item in args.input:
        item = os.path.abspath(item)

        if os.path.isdir(item):
            images = [f for f in os.listdir(item) if f.lower().endswith(supported)]
            output_dir = args.output or os.path.join(item, "webp_output")
            for idx, file in enumerate(images, 1):
                input_path = os.path.join(item, file)
                output_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".webp")
                orig, new, ok = convert_to_webp(input_path, output_path, args.quality)
                if ok:
                    total_files += 1
                    total_converted += 1
                    total_original += orig
                    total_converted_size += new
        elif os.path.isfile(item) and item.lower().endswith(supported):
            total_files += 1
            input_dir = os.path.dirname(item)
            output_dir = args.output or os.path.join(input_dir, "webp_output")
            output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(item))[0] + ".webp")
            orig, new, ok = convert_to_webp(item, output_path, args.quality)
            if ok:
                total_converted += 1
                total_original += orig
                total_converted_size += new
        else:
            print(f"⚠️ Skipped: {item} (unsupported format or not found)")

    # Final summary
    if total_files > 0:
        reduction = ((total_original - total_converted_size) / total_original) * 100 if total_original else 0
        print("\n📊 Conversion Summary")
        print(f"🖼️  Files processed: {total_files}")
        print(f"✅ Successfully converted: {total_converted}")
        print(f"📉 Total size reduction: -{round(reduction, 2)}%")
    else:
        print("🚫 No valid image files found.")

if __name__ == "__main__":
    main()
