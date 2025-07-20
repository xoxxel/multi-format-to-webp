\# Multi-Format to WebP Converter



Welcome to the \*\*Multi-Format to WebP Converter\*\*, a simple and efficient command-line tool written in Python. It allows you to convert various image formats (PNG, JPG, JPEG, BMP) into the WebP format — helping reduce image sizes and improve web performance.



\## 🔧 Features



\* \*\*Supports Multiple Formats\*\*: Converts PNG, JPG, JPEG, BMP to WebP.

\* \*\*Batch Processing\*\*: Accepts single files or directories.

\* \*\*Custom Output Quality\*\*: Adjust compression quality (0–100).

\* \*\*Output Control\*\*: Save files in a chosen directory or overwrite in-place.

\* \*\*Size Reduction Report\*\*: See size savings for each file.

\* \*\*Cross-Platform\*\*: Works on Windows, macOS, and Linux.



\## 🚀 Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/xoxxel/multi-format-to-webp.git

cd multi-format-to-webp

```



\### 2. Install dependencies



```bash

pip install -r requirements.txt

\# or manually:

pip install Pillow

```



\### 3. Run the converter



```bash

python convert.py path/to/image.jpg

```



\## 📚 Usage Examples



\* Convert a single image:



```bash

python convert.py image.jpg

```



\* Convert all images in a folder:



```bash

python convert.py images/

```



\* Save output to a custom folder:



```bash

python convert.py images/ -o output/

```



\* Set quality level:



```bash

python convert.py photo.png -q 90

```



\## 📈 Example Output



```

Successfully converted: logo.jpg -> logo.webp (-40.12%)

Successfully converted: banner.png -> banner.webp (-28.35%)

Total size reduction: -34.23%

```



\## ⚙️ How It Works



1\. Accepts file(s) or directory path(s).

2\. Filters out unsupported formats.

3\. Converts images to WebP using Pillow.

4\. Applies selected quality settings.

5\. Calculates size savings per image.



\## 🌍 Why WebP?



\* Smaller file sizes (25–35% reduction on average).

\* Maintains high image quality.

\* Improves page load speed and SEO.



\## 🤝 Contributing



1\. Fork the repo and create a branch.

2\. Commit your changes.

3\. Push and open a pull request.



\## 🐛 Issues \& Feedback



Found a bug or have a suggestion? Open an issue here:

\[GitHub Issues](https://github.com/xoxxel/multi-format-to-webp/issues)



\## 📄 License



MIT License – See \[LICENSE](https://github.com/xoxxel/multi-format-to-webp/blob/main/LICENSE)



---



If you'd like a visual chart (e.g., size reduction pie chart), let us know your data and we'll help create it!



