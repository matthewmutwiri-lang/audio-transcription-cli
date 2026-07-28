Markdown
# Audio Transcription CLI Pipeline

An automated, command-line audio transcription tool built in Python using OpenAI's Whisper model and PyTorch.

## Features
- Transcribes audio files (`.mp3`, `.wav`, `.m4a`) into structured text files.
- Supports flexible Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`).
- Automatic output directory management and UTF-8 encoding support.

## Installation

bash
git clone https://github.com/matthewmutwiri-lang/audio-transcription-cli.git
cd audio-transcription-cli
pip install -r requirements.txt


## Usage

bash
python transcriber.py path/to/audio.mp3 --model base
