# Human Eye Disease Prediction Platform

🔗 **Live Demo:**  
https://eye-disease-prediction-using-oct-scan.streamlit.app/

---

## Overview

The **Human Eye Disease Prediction Platform** is a deep learning–powered web application designed to assist in the automated analysis of **retinal Optical Coherence Tomography (OCT) scans**.  

Using a fine-tuned **MobileNetV3** convolutional neural network, the platform classifies OCT images into four clinically relevant categories:

- **CNV** (Choroidal Neovascularization)
- **DME** (Diabetic Macular Edema)
- **Drusen** (Early Age-Related Macular Degeneration)
- **Normal Retina**

The application provides both **predictions** and **educational clinical insights**, helping users better understand retinal conditions detected in OCT scans.

---

## Why OCT Matters

Optical Coherence Tomography (OCT) is a non-invasive imaging technique that produces high-resolution cross-sectional images of the retina.  
Over **30 million OCT scans** are performed annually worldwide to diagnose and monitor retinal diseases that can lead to irreversible vision loss if left untreated.

This platform aims to:
- Reduce diagnostic time
- Support clinical decision-making
- Improve accessibility to AI-assisted retinal screening

---

## Key Features

- 📤 **OCT Image Upload**
- 🔍 **CLIP-Based Input Validation** — Rejects non-OCT images before classification using OpenAI's CLIP model
- 🤖 **Deep Learning–Based Classification**
- 📊 **4-Class Retinal Disease Prediction with Confidence Score**
- 📚 **Clinical Recommendations & Explanations**
- 🌐 **Deployed with Streamlit Cloud**

---

## Input Validation

To ensure the platform only processes valid medical images, a **CLIP (Contrastive Language–Image Pretraining)** model by OpenAI is used as a semantic gate before any disease classification occurs.

When an image is uploaded, CLIP evaluates its visual content against descriptors including:
- `"an OCT retinal scan"`
- `"a photograph of a person"`
- `"a natural photograph"`
- `"a medical image that is not an eye scan"`

If the image does not match the OCT scan descriptor with sufficient confidence, the app rejects it with a clear error message — preventing misclassification of portraits, photographs, or unrelated medical images.

---

## Model Information

- **Architecture:** MobileNetV3 (pre-trained + fine-tuned)
- **Framework:** TensorFlow 2.10.0
- **Input Validation:** OpenAI CLIP (`ViT-B/32`)
- **Input Size:** 224 × 224 RGB images
- **Output Classes:** 4 (CNV, DME, Drusen, Normal)
- **Metrics Used (Training):**
  - Accuracy
  - F1 Score
- **Model File:** `Trained_Model.h5` (~66 MB, managed via Git LFS)

---

## Dataset

The model was trained on a large, clinically validated OCT dataset containing **84,495 images**, split into training, validation, and testing sets.

### Classes:
- **CNV**
- **DME**
- **Drusen**
- **Normal**

Images were obtained from multiple international medical institutions and underwent a **multi-tier expert grading process**, including ophthalmologists and senior retinal specialists, ensuring high label accuracy.

---

## Running the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/iamsamuelk/Eye_Disease_Prediction_OCT_Scan.git
cd Eye_Disease_Prediction_OCT_Scan
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv tensorflow_env
source tensorflow_env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install git+https://github.com/openai/CLIP.git
```

**Note: This project is built with TensorFlow 2.10.0. For best compatibility, use Python 3.10.**

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

> On first run, CLIP will automatically download the `ViT-B/32` model weights (~350MB) and cache them locally. Subsequent runs load instantly.

---

## How to Use the App

1. **Upload** an OCT image via the interface.
2. The app **validates** the image using CLIP — non-OCT images are rejected immediately.
3. Click **Predict**.
4. **View** the predicted retinal condition and confidence score.
5. Expand **"Learn More"** to read clinical explanations and recommendations.

---

## Predictions & Clinical Insights

### 🔴 CNV (Choroidal Neovascularization)
* **Action:** Immediate referral to a retinal specialist.
* **Treatment:** Common treatments include Anti-VEGF therapy and photodynamic therapy.
* **Monitoring:** Requires frequent OCT monitoring.

### 🟠 DME (Diabetic Macular Edema)
* **Action:** Coordinated care with an endocrinologist and ophthalmologist.
* **Treatment:** Options include Anti-VEGF injections and corticosteroids.
* **Lifestyle:** Strict blood sugar and blood pressure control is essential.

### 🟡 Drusen (Early AMD)
* **Diet:** Antioxidant-rich diet and AREDS2 supplements.
* **Lifestyle:** Modifications needed (UV protection, smoking cessation).
* **Monitoring:** Regular OCT scans and Amsler grid self-monitoring.

### 🟢 Normal Retina
* **Action:** Maintain routine eye examinations.
* **Lifestyle:** Continue healthy diet and sun protection.
* **Monitoring:** Monitor systemic health conditions.

---

## ⚠️ Disclaimer

> This application is intended for **educational and research purposes only**.  
> It does **not** replace professional medical diagnosis or treatment.  
> Always consult a qualified ophthalmologist or healthcare provider for medical advice.

---

## 🙌 Acknowledgments

* Retinal OCT Dataset Contributors
* TensorFlow & Keras
* OpenAI CLIP
* Streamlit
* Open-source community
* Spotless Tech

⭐ **If you find this project helpful, please consider giving it a star on GitHub!**
