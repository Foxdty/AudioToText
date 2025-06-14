# 🎙️ YouTube/MP3 to Text Converter using OpenAI Whisper

A simple Python-based web app to **convert audio (MP3 or YouTube link)** into **transcribed text** using [OpenAI Whisper](https://github.com/openai/whisper). Built with [Gradio](https://gradio.app/) for an easy-to-use web interface.

---

## 🚀 Features

- 🎧 Upload `.mp3` files directly or paste a YouTube link
- 💬 Transcribe speech into text using Whisper
- 🖥️ Simple and clean Gradio web interface
- 📉 Progress bar for real-time transcription status
- 🧠 Whisper model options (e.g., `base`, `small`, `medium`, `large`)
- 🚀 GPU acceleration (optional with CUDA)

---

## 📦 Installation

### 1. Clone the repository
bash
git clone https://github.com/Foxdty/AudioToText.git

Install whisper and gradio
pip install git+https://github.com/openai/whisper.git
pip install gradio

Make sure ffmpeg is installed and accessible from the command line:
# Debian/Ubuntu
sudo apt install ffmpeg

# Optional: Install GPU-enabled PyTorch (if you have CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Otherwise, install the CPU version:
pip install torch torchvision torchaudio
