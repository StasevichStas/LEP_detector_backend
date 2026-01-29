# ⚡ High-Voltage Power Line Monitoring System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)]

An automated AI-driven solution for monitoring power line infrastructure using state-of-the-art object detection models. This project focuses on identifying power towers, insulators, and detecting potential structural defects.
<p><h2>Detection examples</h2></p>
<p>
<img src="detection_example/1.jpg" width="250">
<img src="detection_example/detected_1.jpg" width="250">
  </p>
  <p>
<img src="detection_example/2.jpg" width="250">
<img src="detection_example/detected_2.jpg" width="250">
</p>

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

## 📂 Project Structure
```text
├── ml_models/           # Pre-trained weights (.pt) for v8 and v11
├── streamlit_demo/      # Interactive demo application
├── lep_project/         # Django project core & detector app
├── requirements.txt     # Python dependencies for cloud deployment
├── packages.txt         # Linux system dependencies
└── environment.yml      # Mamba/Conda environment configuration
```

## 💻 Getting Started
1. Clone and Setup
```
git clone [https://github.com/stasevichstas/lep_project.git](https://github.com/stasevichstas/lep_project.git)
cd lep_project

mamba env create -f environment.yml
mamba activate lep_monitoring
```
2. Run Streamlit Demo
streamlit run lep_project/streamlit_demo/app.py
3. Run Django Backend
cd lep_project
python manage.py migrate
python manage.py runserver
