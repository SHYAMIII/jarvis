
# Jarvis – Your Python LLM Voice Assistant 🔊🤖

An interactive voice assistant built in Python, powered by a Mistral-style LLM and Google Text‑to‑Speech (gTTS) for live conversational responses.

## 🚀 Features

- **Large Language Model (LLM) integration**  
  Sends spoken user input to a Mistral-compatible LLM API and gets text responses.

- **Text-to-Speech (TTS) via gTTS**  
  Converts LLM-generated responses into speech that plays back to the user.

- **Live audio interaction**  
  Accepts microphone input, transcribes (if you added STT), queries LLM, and speaks answer—simulating a “Jarvis” experience.

## 🧩 Project Structure

```
jarvis/
├── main.py              # Core flow: capture input → query LLM → speak response
├── mistral_client.py    # Handles LLM API integration (model, key, endpoint)
├── tts_handler.py       # Uses gTTS, saves playback-ready audio
├── requirements.txt     # Dependencies (httpx, gtts, etc.)
├── .env                 # Stores MISTRAL_API_KEY, optional configs
└── README.md            # This file
```

## ⚙️ Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/SHYAMIII/jarvis.git
   cd jarvis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate.bat      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your `.env` file with:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## 🏁 How to Run

Start the assistant:

```bash
python main.py
```

**Workflow**:

1. Speak into the mic to ask a question.  
2. Audio is optionally transcribed or directly sent to the LLM.  
3. The LLM returns a text reply.  
4. gTTS converts it to speech and plays it back.

## 🤖 How It Works

- **`main.py`** orchestrates the flow: listen → query → speak.
- **`mistral_client.py`** sends your prompt to the Mistral API and fetches completion.
- **`tts_handler.py`** uses gTTS to synthesize voice from text, saved as audio or played live.

## 📁 Example Usage

```python
# main.py (simplified)
from mistral_client import get_llm_response
from tts_handler import speak_text

while True:
    prompt = input("You: ")
    if prompt.lower() in ("exit", "quit"):
        break
    reply = get_llm_response(prompt)
    print("Jarvis:", reply)
    speak_text(reply)
```

## 📦 Dependencies

- `httpx` – for async LLM API requests  
- `gtts` – Google Text‑to‑Speech  
- `playsound` or similar – for audio playback  
- (Optional) STT library if you included transcription  

See `requirements.txt` for exact versions.

## 🔧 Customization & Extensions

- Swap out LLM – support other models or endpoints  
- Enhance STT – use Whisper/Vosk/STT  
- Add hotword activation (e.g., “Hey Jarvis…”)  
- Save conversation logs or adapt personalities

## 📝 License

MIT License — see the `LICENSE` file.  
You’re welcome to use, modify, fork, and contribute improvements!
