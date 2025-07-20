# Multi-Format to WebP Converter

Welcome to the **Multi-Format to WebP Converter**, a simple and efficient command-line tool written in Python. It allows you to convert various image formats (PNG, JPG, JPEG, BMP) into the WebP format — helping reduce image sizes and improve web performance.

## 🔧 Features

* **Supports Multiple Formats**: Converts PNG, JPG, JPEG, BMP to WebP.
* **Batch Processing**: Accepts single files or directories.
* **Custom Output Quality**: Adjust compression quality (0–100).
* **Organized Output**: Automatically creates a `webp_output/` folder to store converted files.
* **Size Reduction Report**: Displays size savings per file and total.
* **Cross-Platform**: Works on Windows, macOS, and Linux.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/xoxxel/multi-format-to-webp.git
cd multi-format-to-webp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
# or manually:
pip install Pillow
```

### 3. Run the converter

```bash
python convertor.py path/to/image.jpg
```

## 📚 Usage Examples

* Convert a single image:

```bash
python convertor.py image.jpg
```

* Convert all images in a folder:

```bash
python convertor.py images/
```

* Save output to a custom folder:

```bash
python convertor.py images/ -o output/
```

* Set quality level:

```bash
python convertor.py photo.png -q 90
```

## 📈 Example Output

```
✅ sample.jpg → sample.webp | 🪶 -42.3%
✅ logo.png → logo.webp | 🪶 -35.7%

📊 Conversion Summary
🖼️  Files processed: 2
✅ Successfully converted: 2
📉 Total size reduction: -39.05%
```

## ⚙️ How It Works

1. Accepts file(s) or directory path(s).
2. Filters out unsupported formats.
3. Creates an output folder (default: `webp_output/`).
4. Converts images to WebP using Pillow.
5. Applies selected quality settings.
6. Calculates and logs size savings per image and total.

## 🌍 Why WebP?

* Smaller file sizes (25–35% reduction on average).
* Maintains high image quality.
* Improves page load speed and SEO.

## 🤝 Contributing

1. Fork the repo and create a branch.
2. Commit your changes.
3. Push and open a pull request.

## 🐛 Issues & Feedback

Found a bug or have a suggestion? Open an issue here:
[GitHub Issues](https://github.com/xoxxel/multi-format-to-webp/issues)

## 📄 License

MIT License – See [LICENSE](https://github.com/xoxxel/multi-format-to-webp/blob/main/LICENSE)

---

If you'd like a visual chart (e.g., size reduction pie chart), let us know your data and we'll help create it!
