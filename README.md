# 🤖 Jarvis - AI Voice Assistant

Jarvis is a modular, Python-based AI voice assistant that listens, understands, and responds to your voice using cutting-edge technologies like Vosk, OpenAI, Edge TTS, and more. It features speech recognition, text-to-speech, LLM integration, and a simple GUI—all fully customizable.

---

## 🚀 Features

- 🎙️ Real-time **Speech Recognition** with [Vosk](https://alphacephei.com/vosk/)
- 🧠 **AI-generated responses** (OpenAI / OpenRouter / Ollama)
- 🔊 **Text-to-Speech** with realistic Edge TTS and offline fallback (pyttsx3)
- 🖥️ Simple **GUI Interface** with Tkinter
- 🧩 Fully **modular code structure**
- 🌐 **Socket.IO support** for remote or browser-based LLMs

---

## 📁 Project Structure

jarvis/
├── main.py # Project entry point
├── voice/ # Vosk STT implementation
├── tts/ # EdgeTTS and pyttsx3
├── llm/ # OpenAI, OpenRouter, or local LLM
├── ui/ # GUI with Tkinter
├── utils/ # Constants and helpers
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/SHYAMIII/jarvis.git
cd jarvis
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Download Vosk Model
Download a model from Vosk models
Extract it and place it in voice/models/.

▶️ Run the Assistant
bash
Copy
Edit
python main.py
🔌 Real-Time LLM via Socket.IO
For real-time browser-based LLM:

Start backend with Socket.IO

Run frontend client with WebSocket support (browser-based Ollama / OpenRouter)

Jarvis will emit and receive live AI responses

🙋 About Me
👨‍💻 Shyam — Full Stack & AI Developer
🔗 LinkedIn
🌐 Portfolio
