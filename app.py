import io

import streamlit as st
from PIL import Image, ImageOps
from rembg import remove

st.set_page_config(page_title="BG Studio", page_icon="✨", layout="centered")

# ---------- Styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp, button, p, span, label, div {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Background */
    .stApp {
        background: radial-gradient(circle at 15% 10%, #3b1d6e 0%, transparent 45%),
                    radial-gradient(circle at 85% 30%, #0e4d6b 0%, transparent 45%),
                    linear-gradient(160deg, #0f0c29 0%, #1a1740 50%, #0b132b 100%);
        color: #f5f3ff;
    }
    header[data-testid="stHeader"] { background: transparent; }
    .block-container { padding-top: 2.5rem; max-width: 760px; }

    /* Hero */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        line-height: 1.15;
        background: linear-gradient(90deg, #a78bfa, #f472b6, #fbbf24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .hero-sub {
        text-align: center;
        color: #c4b5fd;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Step headers */
    .step {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin: 1.8rem 0 0.8rem 0;
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
    }
    .step-num {
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        box-shadow: 0 4px 14px rgba(236, 72, 153, 0.45);
    }

    /* Upload boxes */
    [data-testid="stFileUploader"] section {
        border: 2px dashed #a78bfa;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.06);
        padding: 1.6rem;
        transition: all 0.25s ease;
    }
    [data-testid="stFileUploader"] section:hover {
        border-color: #f472b6;
        background: rgba(244, 114, 182, 0.10);
        box-shadow: 0 0 24px rgba(244, 114, 182, 0.25);
    }
    [data-testid="stFileUploader"] section * { color: #e9e5ff !important; }
    [data-testid="stFileUploader"] small { color: #a5b4fc !important; }
    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        color: white !important;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
    }

    /* Buttons */
    .stDownloadButton button {
        width: 100%;
        background: linear-gradient(135deg, #06b6d4, #8b5cf6);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.7rem 1rem;
        font-weight: 600;
        font-size: 1rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(139, 92, 246, 0.5);
        color: white;
    }

    /* Images */
    [data-testid="stImage"] img {
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
    }

    /* Transparent-checker look for the cutout preview */
    .st-key-checker [data-testid="stImage"] img {
        background-image:
            linear-gradient(45deg, #2a2a4a 25%, transparent 25%),
            linear-gradient(-45deg, #2a2a4a 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, #2a2a4a 75%),
            linear-gradient(-45deg, transparent 75%, #2a2a4a 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0;
        background-color: #1d1d3a;
    }

    hr { border-color: rgba(255, 255, 255, 0.12); }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.markdown('<div class="hero-title">BG Studio ✨</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Remove the background from your photo and put yourself anywhere.</div>',
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner="Removing background...")
def cut_out(image_bytes: bytes) -> bytes:
    """Remove the background and return a transparent PNG (as bytes)."""
    return remove(image_bytes)


def step(number: int, text: str) -> None:
    st.markdown(
        f'<div class="step"><span class="step-num">{number}</span>{text}</div>',
        unsafe_allow_html=True,
    )


# ---------- Step 1 ----------
step(1, "Upload your photo")
photo_file = st.file_uploader(
    "Drag and drop your photo here",
    type=["png", "jpg", "jpeg", "webp"],
    label_visibility="collapsed",
)

if photo_file:
    cutout = Image.open(io.BytesIO(cut_out(photo_file.getvalue()))).convert("RGBA")

    step(2, "Your cutout")
    with st.container(key="checker"):
        st.image(cutout, use_container_width=True)

    buf = io.BytesIO()
    cutout.save(buf, format="PNG")
    st.download_button("⬇ Download transparent PNG", buf.getvalue(), "cutout.png", "image/png")

    # ---------- Step 3 ----------
    step(3, "Choose a new background")
    bg_file = st.file_uploader(
        "Drag and drop a background image here",
        type=["png", "jpg", "jpeg", "webp"],
        key="bg",
        label_visibility="collapsed",
    )

    if bg_file:
        bg = Image.open(bg_file).convert("RGBA")
        # Fit the background to the size of the photo (crop to fill)
        bg = ImageOps.fit(bg, cutout.size, Image.LANCZOS)
        bg.alpha_composite(cutout)

        step(4, "Final result")
        st.image(bg, use_container_width=True)

        out = io.BytesIO()
        bg.convert("RGB").save(out, format="PNG")
        st.download_button("⬇ Download final image", out.getvalue(), "result.png", "image/png")
