# ⚡ High-Voltage Power Line Monitoring System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](ССЫЛКА_НА_ТВОЕ_ДЕМО)

An automated AI-driven solution for monitoring power line infrastructure using state-of-the-art object detection models. This project focuses on identifying power towers, insulators, and detecting potential structural defects.


> **<img width="1280" height="1280" alt="изображение" src="https://github.com/user-attachments/assets/270c049a-83e8-4dfc-a860-d56456e75514" />
** Самый лучший результат детекции, где нейронка четко нашла изоляторы.

## 🚀 Overview
Manual inspection of power lines is dangerous and time-consuming. This project demonstrates how Computer Vision can automate the process, providing real-time detection and health monitoring of critical electrical infrastructure.

### Key Features
* **Multi-Object Detection:** Real-time localization of transmission towers and insulators.
* **Fault Identification:** Specifically trained to recognize damaged components and environmental risks.
* **Dual-Model Comparison:** Implementation and testing of both **YOLOv8n** and the latest **YOLOv11n** architectures.
* **Interactive Web UI:** A user-friendly Streamlit interface for quick image inference and testing.
* **Django Backend:** Scalable architecture for future API integration and data management.

## 📊 Model Performance & Comparison

I evaluated two versions of the YOLO (You Only Look Once) architecture to find the optimal balance between inference speed and detection accuracy.

| Metric | YOLOv8n (Baseline) | YOLOv11n (Optimized) |
| :--- | :---: | :---: |
| **Model Weight (.pt)** | ~6.5 MB | **~5.8 MB** |
| **mAP@50 (Accuracy)** | 0.XX | **0.XX** | 
| **Inference Speed (CPU)** | ~18 FPS | **~26 FPS** |
| **Best For** | Stability | Accuracy on small objects |

> **ПОДСКАЗКА:** Замени 0.XX на реальные цифры mAP из твоего обучения (возьми из файла results.csv или results.png).


> **СЮДА ПОСТАВЬ ФОТО:** Твой график обучения (results.png), чтобы показать, что модель реально обучалась.

## 🛠 Tech Stack
* **Frameworks:** Python 3.10, PyTorch, Django 5.2.
* **Computer Vision:** Ultralytics YOLOv8/v11, OpenCV.
* **Deployment:** Streamlit Cloud (Demo), Mamba/Conda (Environment).
* **Tools:** OS-level dependencies (libGL, libglib2.0) for cloud rendering.

## 📂 Project Structure
```text
├── ml_models/           # Pre-trained weights (.pt) for v8 and v11
├── streamlit_demo/      # Interactive demo application
├── lep_project/         # Django project core & detector app
├── requirements.txt     # Python dependencies for cloud deployment
├── packages.txt         # Linux system dependencies
└── environment.yml      # Mamba/Conda environment configuration
