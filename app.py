import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image
import time
import io
import os

# --- 1. Page Configuration & 3D Space UI ---
st.set_page_config(page_title="Neural Style Nexus", layout="wide")

st.markdown("""
    <style>
    /* 3D Deep Space Animated Background */
    .stApp {
        background: #000 url('https://w0.peakpx.com/wallpaper/547/697/HD-wallpaper-deep-space-galaxy-planets-stars-universe.jpg') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Twinkling Star Overlay */
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: transparent url('https://www.script-tutorials.com/demos/360/images/twinkling.png') repeat;
        animation: move-twink-back 200s linear infinite; opacity: 0.4; z-index: 0;
    }
    @keyframes move-twink-back { from {background-position:0 0;} to {background-position:-10000px 5000px;} }

    /* Neon Nexus Header */
    h1 {
        background: linear-gradient(90deg, #00d2ff, #92fe9d, #ff00c1);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-weight: 900; font-size: 4.5rem !important;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.4));
    }

    /* Round Glassmorphism Orbs */
    div[data-testid="stImage"] img {
        border-radius: 50% !important;
        aspect-ratio: 1/1 !important;
        object-fit: cover !important;
        border: 3px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 0 50px rgba(0, 210, 255, 0.4), inset 0 0 20px rgba(255,255,255,0.1);
        backdrop-filter: blur(15px);
        transition: 0.5s ease;
    }
    
    div[data-testid="stImage"] img:hover {
        transform: scale(1.05);
        border-color: #ff00c1 !important;
        box-shadow: 0 0 60px rgba(255, 0, 193, 0.6);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 10, 20, 0.9) !important;
        border-right: 1px solid rgba(0, 210, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. Neural Engine (Sub-Second Synthesis) ---

@st.cache_resource
def load_hyper_model():
    """Loads the Fast Arbitrary Image Stylization model"""
    return hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def process_img(img_input):
    """Converts image to normalized float32 tensor"""
    if img_input:
        img = PIL.Image.open(img_input).convert('RGB')
        img = np.array(img).astype(np.float32) / 255.0
        # Magenta model requires 4D tensor: [batch, height, width, channel]
        return tf.image.resize(img[tf.newaxis, :], (512, 512))
    return None

# --- 3. Sidebar Mission Control ---
st.sidebar.title("🪐 Mission Control")

# Feature: Style Strength Slider to fix unrelated outputs
st.sidebar.markdown("### Fusion Settings")
style_strength = st.sidebar.slider("Style Intensity", 0.0, 1.0, 0.8)

# Preset Mission Path with Local Samples
st.sidebar.markdown("### Orbital Presets")
samples = {
    "Custom Discovery": None,
    "Marble Voyager": {"c": "content1.png", "s": "style2.png"},
    "Cosmic Stained Glass": {"c": "content2.png", "s": "style3.png"},
    "Infinite Zenith": {"c": "content3.png", "s": "style6.png"},
    "Digital Aurora": {"c": "content5.png", "s": "style5.png"},
    "Neon Singularity": {"c": "content9.png", "s": "style9.png"},
    "Cybernetic Pulse": {"c": "content4.png", "s": "style4.png"},
    "Stardust Explorer": {"c": "content7.png", "s": "style7.png"},
    "Obsidian Core": {"c": "content8.png", "s": "style8.png"}
}
selection = st.sidebar.selectbox("Select Orbit:", list(samples.keys()))

# --- 4. Main Stage Layout ---
st.markdown("<h1>NEURAL NEXUS</h1>", unsafe_allow_html=True)
col_left, col_mid, col_right = st.columns([2, 0.5, 2])

c_tensor, s_tensor = None, None

with col_left:
    st.markdown("<h3 style='color:#00d2ff; text-align:center;'>CONTENT ORB</h3>", unsafe_allow_html=True)
    if selection == "Custom Discovery":
        c_file = st.file_uploader("Upload Target", type=['jpg', 'png'], key="c_up", label_visibility="collapsed")
        if c_file:
            c_tensor = process_img(c_file)
            st.image(c_file)
    else:
        # Load local content file
        path_c = samples[selection]["c"]
        if os.path.exists(path_c):
            c_tensor = process_img(path_c)
            st.image(path_c)
        else:
            st.warning(f"Local file {path_c} missing.")

with col_right:
    st.markdown("<h3 style='color:#ff00c1; text-align:center;'>STYLE NEBULA</h3>", unsafe_allow_html=True)
    if selection == "Custom Discovery":
        s_file = st.file_uploader("Upload Art", type=['jpg', 'png'], key="s_up", label_visibility="collapsed")
        if s_file:
            s_tensor = process_img(s_file)
            st.image(s_file)
    else:
        # Load local style file
        path_s = samples[selection]["s"]
        if os.path.exists(path_s):
            s_tensor = process_img(path_s)
            st.image(path_s)
        else:
            st.warning(f"Local file {path_s} missing.")

# --- 5. Fusion Activation ---
st.write("---")
if c_tensor is not None and s_tensor is not None:
    # 2026 Streamlit standard: width="stretch" replaces container_width
    if st.button("⚡ ACTIVATE FUSION REACTOR ⚡", type="primary", width="stretch"):
        
        with st.spinner("Synthesizing Cosmic Artifact..."):
            # Speed of Light Iteration: Instant Forward Pass
            model = load_hyper_model()
            stylized = model(tf.constant(c_tensor), tf.constant(s_tensor))[0]
            
            # Blend Logic: Ensures output stays related to content
            if style_strength < 1.0:
                stylized = (style_strength * stylized) + ((1 - style_strength) * c_tensor)
            
            # Post-process for display
            res_img = PIL.Image.fromarray(np.array(stylized[0] * 255, dtype=np.uint8))
        
        # Display Result Stage
        st.markdown("<h2 style='text-align:center; color:#fff;'>FUSION COMPLETE</h2>", unsafe_allow_html=True)
        _, res_col, _ = st.columns([1, 2, 1])
        with res_col:
            st.image(res_img, caption="Synthetic Artifact Result", width=500)
            
            # Instant Retrieve (Download) Feature
            buf = io.BytesIO()
            res_img.save(buf, format="PNG")
            st.download_button("📥 RETRIEVE ARTIFACT", buf.getvalue(), "nexus_fusion.png", width="stretch")