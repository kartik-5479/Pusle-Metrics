# ❤️ Pulse Metrics — AI Medical Report Analyzer

<p align="center">
  <strong>Understand Your Health Reports Better with AI</strong>
</p>

<p align="center">
  An AI-powered Streamlit application that transforms complex medical reports into structured, easy-to-understand health insights.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/PyMuPDF-PDF%20Processing-005571?style=for-the-badge">
  <img src="https://img.shields.io/badge/Pillow-Image%20Processing-3776AB?style=for-the-badge">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

# 🚀 Streamlit Live Demo

<p align="center">

### ❤️ [Launch Pulse Metrics — Live Demo](https://pusle-metrics-kartik.streamlit.app/)

</p>


---

# 🎯 About The Project

**Pulse Metrics** is an AI-powered medical report analysis platform built with **Python, Streamlit, and Google Gemini**.

Medical reports often contain technical terminology, laboratory values, units, and reference ranges that can be difficult to understand.

Pulse Metrics helps simplify this information by allowing users to upload supported medical reports and receive a structured, plain-language analysis.

The application extracts information from the uploaded document and uses **Google Gemini** to identify reported parameters, compare values against the reference ranges provided in the report, summarize the findings, and present the results through an intuitive dashboard.

### The goal is simple:

> **Turn complicated medical report language into information that is easier to understand.**

---

# ✨ Key Features

## 📄 Medical Report Upload

Upload medical reports directly through the Streamlit interface.

### Supported formats

- 📑 PDF
- 🖼️ JPG
- 🖼️ JPEG
- 🖼️ PNG

### Upload limit

**Maximum file size: 10 MB**

The application validates uploaded files before processing them.

---

# 📊 Health Status Classification

Each supported parameter can be classified based on the information provided by the report.

| Status | Meaning |
|---|---|
| 🟢 **Normal** | Result appears within the supplied reference range |
| 🟠 **Borderline** | Result appears close to or slightly outside the supplied range |
| 🔴 **Abnormal** | Result appears outside the supplied reference range |
| ⚪ **Not Available** | Insufficient information to classify the result |

The application prioritizes the **reference range provided by the uploaded report** instead of blindly applying generic medical ranges.

---

# 📈 Analysis Dashboard

After analysis, Pulse Metrics presents the results through a structured dashboard.

The dashboard includes:

### ❤️ Overall Health

A high-level summary of the report based on the analyzed findings.

### 🟢 Normal Results

Displays the number of parameters classified as normal.

### 🟠 Borderline Results

Displays parameters that may require additional context or attention.

### 🔴 Abnormal Results

Displays parameters that appear outside the provided reference ranges.

---

# 💡 Key Health Insights

Pulse Metrics generates concise insights based on the findings in the uploaded report.

The system is designed to:

- Identify meaningful findings
- Connect findings with reported values
- Highlight potentially important results
- Avoid unsupported conclusions
- Avoid unnecessary generic advice

The application does not intentionally generate filler insights when the report does not provide enough information.

---

# ⚠️ Precautions & Recommendations

The application can provide general educational precautions and recommendations related to the findings.

Examples include:

- Discussing unexpected findings with a healthcare professional
- Considering the report's reference ranges
- Avoiding interpretation of a single value in isolation
- Seeking appropriate professional context for persistent or concerning findings

The application **does not prescribe medication or recommend changing medical treatment**.


---

# 🛡️ Medical Safety Disclaimer

> **Pulse Metrics is an educational and informational tool. It is not a medical diagnostic system and does not replace professional medical advice, diagnosis, or treatment. AI-generated information may contain errors or require additional context. Always consult a qualified healthcare professional for interpretation of medical results and decisions about your health.**


---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core application logic |
| 🎈 **Streamlit** | Web application and interactive UI |
| 🤖 **Google Gemini** | AI-powered medical report analysis |
| 📑 **PyMuPDF** | PDF document processing and text extraction |
| 🖼️ **Pillow** | Image report validation and processing |
| 🐼 **Pandas** | Data processing |
| 🔢 **NumPy** | Numerical operations |
| 🔐 **python-dotenv** | Environment variable management |
| 🎨 **Custom CSS** | UI styling and visual design |

---
---

# 🌟 Project Highlights

### 🤖 AI-Powered

Uses Google's Gemini API to analyze medical report content and produce structured explanations.

### 📄 Multi-Format Support

Supports both document and image-based medical reports.

### 📊 Structured Results

Transforms unstructured report content into organized patient information, parameters, statuses, insights, and recommendations.

### 🎯 Report-Aware Classification

Uses reference ranges and explicit information from the uploaded report whenever available.

### 🧠 Plain-Language Explanations

Medical terminology is explained in language intended for non-medical users.

### 🛡️ Safety-Focused

The AI is instructed not to fabricate missing information, prescribe medication, or present the analysis as a diagnosis.

### 🎨 Modern Healthcare UI

A clean, responsive interface designed specifically for medical-report readability.

---

# 🔮 Future Improvements

Potential future enhancements include:

- 📚 Analysis history
- 🔎 Advanced laboratory parameter detection
- 🌐 Multi-language medical explanations
- 🧠 Improved medical terminology coverage
- 📱 Further mobile UI optimization
- 🔐 Authentication and secure user accounts
- 🏥 Integration with healthcare data platforms

---


# 👨‍💻 Author

## Kartik

**Computer Science Student | AI/ML & Full-Stack Developer**

### GitHub

[github.com/kartik-5479](https://github.com/kartik-5479)

---

# ⭐ Support

If you find **Pulse Metrics** useful:

⭐ **Star** the repository  
🍴 **Fork** the project  
🐛 **Report** bugs  
💡 **Suggest** improvements  
📢 **Share** the project

---

<p align="center">

## ❤️ Understand Your Health Better.

### Built with Python • Streamlit • Gemini • PyMuPDF • Pillow

</p>
