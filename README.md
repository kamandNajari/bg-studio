<h1 align="center">✨ BG Studio</h1>

<p align="center">
  Remove the background from your photo and place yourself anywhere, in just a few clicks.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/UI-Streamlit-ff4b4b?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-rembg%20(U²--Net)-8b5cf6" alt="rembg">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

---

## 📖 About

**BG Studio** is a small web app that lets you:

1. Upload a photo of yourself
2. Automatically detect the person and remove the background
3. Upload a second image and use it as your new background
4. Download the final result

No design skills and no Photoshop needed. Everything runs on your own computer, so your photos are never uploaded to any external server.

---

## 🚀 Features

- 🧍 **Automatic person detection**: an AI segmentation model finds the person in the photo and cuts out everything else.
- 🪟 **Transparent cutout**: get a clean PNG with an empty background, previewed on a checkerboard so you can see exactly what was removed.
- 🖼️ **Custom background upload**: drop in any image (a beach, a city, a classroom, anything) and it becomes your new background.
- 📐 **Smart background fitting**: the new background is automatically resized and cropped to match your photo, with no stretching.
- ⬇️ **Two downloads**: save the transparent cutout, the final image, or both.
- 🎨 **Modern interface**: gradient theme, drag-and-drop upload boxes, and a clear step-by-step flow.
- ⚡ **Fast repeat use**: results are cached, so changing the background doesn't re-run the AI model on your photo.
- 🔒 **Private by design**: all processing happens locally.

---

## 🧠 How it works

```
Your photo ──► rembg (U²-Net model) ──► transparent PNG (person only)
                                              │
New background ──► resized + cropped to fit ──┴──► composited image ──► download
```

1. **Segmentation**: [rembg](https://github.com/danielgatis/rembg) runs a U²-Net neural network that predicts which pixels belong to the person and which belong to the background. The background pixels become transparent.
2. **Background fitting**: [Pillow](https://python-pillow.org/) resizes and center-crops the new background so it exactly matches your photo.
3. **Compositing**: the transparent cutout is placed on top of the new background using its alpha channel, which keeps the edges smooth.
4. **Interface**: [Streamlit](https://streamlit.io/) provides the web UI, with custom CSS for the look and feel.

---

## 🛠️ Installation

### Requirements

- Python 3.9 or newer
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/kamandNajari/bg-studio.git
cd bg-studio

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 4. Install the dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`).

> **Note:** the first time you remove a background, rembg downloads its AI model (around 170 MB). This happens only once, so the first run will be slower.

---

## 🎯 Usage

1. **Upload your photo**: drag and drop a `.png`, `.jpg`, `.jpeg` or `.webp` image into the first box.
2. **Check your cutout**: the app removes the background and shows you on a checkerboard. Download it if you only need the transparent version.
3. **Choose a new background**: upload any image in the second box.
4. **Get your result**: the final image appears instantly, ready to download.

> 💡 **Tip:** for the best results, use a photo where the person is clearly visible and well lit.

---

## 📁 Project structure

```
bg-studio/
├── app.py              # Streamlit app (UI + image processing)
├── requirements.txt    # Python dependencies
├── README.md           # You are here
├── LICENSE             # MIT license
└── .gitignore          # Files Git should ignore
```

---

## 🧰 Tech stack

| Tool | Purpose |
|------|---------|
| [Python](https://www.python.org/) | Main language |
| [Streamlit](https://streamlit.io/) | Web interface |
| [rembg](https://github.com/danielgatis/rembg) | AI background removal (U²-Net) |
| [Pillow](https://python-pillow.org/) | Image resizing and compositing |

---

## 🗺️ Roadmap

- [ ] Blur option for the original background
- [ ] Solid color and gradient backgrounds
- [ ] Move, scale and flip the person on the new background
- [ ] Batch processing for multiple photos
- [ ] Soft shadow under the person
- [ ] Live online demo

---

## 🤝 Contributing

Ideas and pull requests are welcome!

1. Fork the project
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a pull request

---

## 📜 License

Distributed under the MIT License. See the `LICENSE` file for details.

---

## 👩‍💻 Author

**Kamand Najari**
GitHub: [@kamandNajari](https://github.com/kamandNajari)

---

<p align="center">
  <b>Thank you for your support and for checking out BG Studio! 💜</b>
</p>
