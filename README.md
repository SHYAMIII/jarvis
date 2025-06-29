# 🧠 Jarvis – Your AI Voice Assistant (Python Desktop App)

Jarvis is a personal voice-based assistant built using Python. It integrates an open-source LLM (like Mistral) for intelligent responses and uses `pyttsx3` for offline text-to-speech. This project enables real-time spoken interaction on your local machine.

---

## 🎯 Features

- ✅ Offline Text-to-Speech using `pyttsx3`
- ✅ Real-time prompt and response handling
- ✅ Integration with open-source LLMs (like Mistral via OpenRouter)
- ✅ Voice input via microphone
- ✅ Modular, beginner-friendly codebase

---

## 🛠️ Tech Stack

| Layer        | Tech             |
|--------------|------------------|
| LLM Backend  | Mistral via OpenRouter |
| TTS          | `pyttsx3` (offline) |
| Audio Input  | `speech_recognition` |
| Language     | Python |
| UI/UX        | Terminal / CLI |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SHYAMIII/jarvis.git
cd jarvis
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Your .env File
Create a .env file and add your OpenRouter API key:

env
Copy
Edit
OPENROUTER_API_KEY=your_key_here
5. Run Jarvis
bash
Copy
Edit
python main.py
🧩 File Structure
bash
Copy
Edit
jarvis/
├── main.py              # Entry point
├── modules/
│   ├── llm.py           # Handles LLM requests
│   ├── tts.py           # Text-to-speech
│   └── stt.py           # Speech-to-text
├── .env                 # API Keys (not tracked)
└── requirements.txt     # All dependencies
💡 Example Commands
Just speak naturally. Example:

vbnet
Copy
Edit
You: What is the capital of France?
Jarvis: The capital of France is Paris.
🤖 Future Improvements
 Add wake word detection

 GUI version (Tkinter / PyQt)

 Multilingual support

 More natural speech via Edge TTS

👤 Author
Shyam
🔗 LinkedIn
📦 GitHub

