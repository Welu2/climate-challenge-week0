# 🌍 Climate Challenge - Week 0

This repository contains the setup and implementation for the **Climate Data Analysis Dashboard**.
It includes environment configuration, dependency management, and an interactive Streamlit application for visualizing climate data.

---

## 🚀 Project Setup

Follow the steps below to reproduce the environment on your local machine.

---

### 1. Clone the Repository

```bash
git clone https://github.com/Welu2/climate-challenge-week0.git
cd climate-challenge-week0
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Verify Installation

```bash
python --version
pip list
```

---

## ▶️ Run the Application

```bash
streamlit run app/main.py
```

---

## 🌐 Live Demo

👉 https://welela-climate-dashboard.streamlit.app/

---

## 📊 Features

* Country multi-select filter
* Year range slider
* Temperature trend visualization (T2M)
* Precipitation distribution (boxplot)
* Additional climate variable exploration
* Clean and interactive dashboard UI

---



## ☁️ Deployment

* Platform: Streamlit Community Cloud
* Entry Point: `app/main.py`
* Data Source: Google Drive

---

## 🧑‍💻 Author

**Welela Bekele**

---

## 📌 Notes

* Ensure Google Drive files are publicly accessible
* App uses caching for faster performance
* Local fallback supported for development
