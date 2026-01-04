# 🌌 Neural Style Nexus

### Fast Neural Style Transfer using Magenta Arbitrary Stylization

**Prodigy InfoTech Internship – Generative AI Task 05**

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![TensorFlow Hub](https://img.shields.io/badge/Model-Magenta%20NST-orange.svg)](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit%20%7C%20CSS-red.svg)](https://streamlit.io/)
[![Deployment](https://img.shields.io/badge/Deploy-Streamlit%20Cloud-black.svg)](https://streamlit.io/cloud)
[![Prodigy Internship](https://img.shields.io/badge/Prodigy-Internship-orange.svg)](https://prodigyinfotech.dev/)

---

## 🌐 Project Overview

**Neural Style Nexus** is an elite, high-performance web application designed for **Fast Neural Style Transfer (NST)**. Built for the final task of the Prodigy InfoTech Generative AI internship, this system allows users to blend the content of one image with the artistic style of another at the **"Speed of Light"**.

Unlike traditional NST which requires hundreds of optimization iterations, this project utilizes a **Pre-trained Magenta model** that performs stylization in a single forward pass. The interface is wrapped in a deep-space, high-fidelity **Glassmorphism UI**.

---

## 🚀 The Core Idea

Neural Style Transfer is a technique that uses Deep Neural Networks (specifically VGG19) to extract content representations from a target image and texture representations (Gram Matrices) from a style image.

**Neural Style Nexus** optimizes this by:
- **Eliminating Iteration Latency** using an arbitrary stylization encoder.
- **Structural Integrity Control** via a Style Intensity slider to prevent unrelated/abstract outputs.
- **Visual Storytelling** through "Mission Control" orbital presets.

---

## 🛠️ Technical Stack

### Core Logic
- **Magenta Arbitrary Stylization v1** – The neural engine for sub-second artistic fusion.
- **TensorFlow Hub** – Seamless integration of high-performance pre-trained weights.
- **NumPy & PIL** – High-speed tensor manipulation and image processing.

### Frontend & UI
- **Streamlit** – The framework for the interactive AI dashboard.
- **3D Parallax CSS** – A moving midnight starfield background for an immersive space aesthetic.
- **Glassmorphism Design** – Circular "Orbs" and frosted containers that respond to user interaction.

---

## 📂 Project Structure

- **PRODIGY_GA_05/**
- ├── **app.py** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Main application logic and UI layout
- ├── **lit.mp4** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # High-voltage lightning connection video
- ├── **requirements.txt** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Python dependencies (TensorFlow, Streamlit, etc.)
- ├── **README.md** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Project documentation
- ├── **content1.png - content9.png** # Local sample content assets
- └── **style1.png - style9.png** &nbsp;&nbsp;&nbsp;&nbsp; # Local sample style assets

---

## ⚙️ How the Nexus Works

### 1️⃣ Image Preparation
Images are loaded locally from the project directory to avoid network latency. Tensors are resized to **512x512** and normalized to align with the VGG19 input requirements.

---

### 2️⃣ Neural Fusion Reactor
The **Magenta Generator** receives the content and style tensors. It uses an encoder to map the style features onto the content's spatial map in a single pass.

---

### 3️⃣ Intensity Modulation
A custom blending algorithm allows users to adjust **Style Intensity**. This blends the stylized output with the original content tensor, ensuring structural features remain visible even with complex styles.

---

## ✨ Key Features

### 🪐 Orbital Presets (Mission Control)
Pre-mapped combinations like **"Marble Voyager"** and **"Neon Singularity"** allow for instant demonstration of the model's capabilities.

### ⚡ Fusion Strike Visuals
A local **lightning connection video** is dynamically positioned via CSS to bridge the gap between input orbs during the synthesis process.

### 🎨 Elite Space UI
The entire interface is themed around space exploration, featuring a twinkling starfield, neon-gradient titles, and glassmorphism containers.

---

## 📦 Installation & Local Deployment

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/threesshad-cpu/PRODIGY_GA_05.git](https://github.com/threesshad-cpu/PRODIGY_GA_05.git)
cd PRODIGY_GA_05
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 🚀 Live Deployment - 🔗 **Live Web App:** [https://neural-style-imagen.streamlit.app]([https://neural-style-imagen.streamlit.app)

---

## 📚 Learning Outcomes

- Implementation of Fast Neural Style Transfer using TF-Hub.

- Managing high-performance AI inference in a real-time Streamlit environment.

- Advanced CSS-in-Streamlit for absolute positioning and background animations.

- Feature balancing (Content vs. Style) using linear interpolation of tensors.

---

## 🏁 Conclusion

Neural Style Nexus demonstrates that artistic expression and artificial intelligence can merge instantly. By moving beyond slow optimization loops, this project highlights the future of real-time creative AI tools.

---

## 🤝 Credits

- **Developer:** Threesssha D  
- **Role:** Generative AI Intern  
- **Organization:** Prodigy InfoTech  
- **Task ID:** PRODIGY_GA_05
