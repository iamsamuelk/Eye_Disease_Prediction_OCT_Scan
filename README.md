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
- 🤖 **Deep Learning–Based Classification**
- 📊 **4-Class Retinal Disease Prediction**
- 📚 **Clinical Recommendations & Explanations**
- 🌐 **Deployed with Streamlit Cloud**

---

## Model Information

- **Architecture:** MobileNetV3 (pre-trained + fine-tuned)
- **Framework:** TensorFlow 2.10.0
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
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv tensorflow_env
source tensorflow_env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Note: This project is built with TensorFlow 2.10.0. For best compatibility, use Python 3.10.**

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

## How to Use the App

1. **Upload** an OCT image via the interface.
2. Click **Predict**.
3. **View** the predicted retinal condition.
4. Expand **"Learn More"** to read clinical explanations and recommendations.

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


## 🙌 Acknowledgments

* Retinal OCT Dataset Contributors
* TensorFlow & Keras
* Streamlit
* Open-source community
* Spotless Tech

⭐ **If you find this project helpful, please consider giving it a star on GitHub!**
