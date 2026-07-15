# Table of Contents

- [Project Overview](#project-overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)

## 📌 Project Overview

This project implements **Intrinsic Reflectance Recovery** using a **Retinex-inspired image decomposition** to separate illumination and reflectance from a single image affected by uneven lighting.

The implementation follows the imaging model:

> **I(x,y) = R(x,y) × L(x,y)**

where the illumination component is estimated manually using an **integral image** and **box filter**, while the reflectance is recovered through **log-domain decomposition**.

The project supports both **grayscale** and **RGB image processing**. For RGB images, a shared illumination map is estimated to preserve the original color relationships across all three channels.

A Flask-based web application provides an interactive interface for uploading images, processing them, and visualizing the recovered outputs along with processing statistics.

## ⚙️ How It Works

| Step | Description |
|------|-------------|
| **1** | Upload a grayscale or RGB image through the Flask interface. |
| **2** | Load the image and normalize pixel intensities. |
| **3** | Apply logarithmic transformation to linearize the illumination model. |
| **4** | Estimate the illumination map using a manually implemented integral image and box filter. |
| **5** | Recover the reflectance by subtracting the illumination component in the log domain. |
| **6** | Normalize the recovered reflectance for visualization. |
| **7** | For RGB images, apply the estimated illumination to each channel and reconstruct the corrected RGB image. |
| **8** | Display the processed outputs and image statistics through the web application. |

## ✨ Features

- Intrinsic reflectance recovery from a single image
- Manual logarithmic image transformation
- Manual integral image implementation
- Manual box filter for illumination estimation
- Grayscale reflectance reconstruction
- RGB illumination correction using shared illumination estimation
- Image normalization and visualization
- Processing statistics generation
- Interactive Flask web interface
- Modular Python implementation
- ## 💻 Tech Stack

| Layer | Technologies |
|--------|--------------|
| Programming | Python |
| Image Processing | OpenCV, NumPy |
| Backend | Flask |
| Frontend | HTML, CSS |
| Visualization | Matplotlib |
| Development | Visual Studio Code |
| Version Control | Git & GitHub |

## 🚀 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Naveenchandra29/Intrinsic-Reflectance-Recovery.git
cd Intrinsic-Reflectance-Recovery
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```
## 🌍 Deployment

The application is deployed locally using the Flask development server.

Deployment Steps:

1. Clone the repository.
2. Create and activate the virtual environment.
3. Install all project dependencies.
4. Run the Flask application.
5. Open **http://127.0.0.1:5000** in a browser.
6. Upload an image to perform intrinsic reflectance recovery and visualize the outputs.
