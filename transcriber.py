import argparse
import os
import sys
from pathlib import Path
import whisper


def process_audio(file_path: Path, model_size: str = "base", output_format: str = "txt") -> None:
    """
    Transcribes an audio file using OpenAI's Whisper model and saves output.
    """
    if not file_path.exists():
        print(f"Error: Input file '{file_path}' does not exist.")
        sys.exit(1)

    print(f"Loading Whisper model '{model_size}'...")
    model = whisper.load_model(model_size)

    print(f"Transcribing '{file_path.name}'...")
    result = model.transcribe(str(file_path))

    output_dir = file_path.parent / "transcripts"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"{file_path.stem}_transcript.{output_format}"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"].strip())

    print(f"Success! Transcript saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Automated Audio Transcription Pipeline using OpenAI Whisper"
    )
    parser.add_argument("audio_path", type=str, help="Path to input audio file (.wav, .mp3, .m4a)")
    parser.add_argument(
        "--model",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base)",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="txt",
        choices=["txt", "srt"],
        help="Output format (default: txt)",
    )

    args = parser.parse_args()
    process_audio(Path(args.audio_path), args.model, args.format)


if __name__ == "__main__":
    main()
