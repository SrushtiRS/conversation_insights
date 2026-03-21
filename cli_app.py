import argparse
from pathlib import Path

from app.transcribe import load_transcription_model, transcribe_audio

# TODO: add logging

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Transcribe audio files and gain intelligent insights"
    )

    parser.add_argument(
        "-i",
        "--input-path",
        help="Path to the input file/folder to be transcribed and analyzed"
    )

    parser.add_argument(
        "-m",
        "--model-name",
        default="medium",
        help="Choose a Whisper trascription model from 'base', 'medium', 'large'."
    )

    return parser.parse_args()


def validate_input_file(audio_file_path):
    """
    Ensures that the file exists and has a supported format.
    """
    audio_path = Path(audio_file_path)

    if not audio_path.exists():
        raise FileNotFoundError(f"File not found: {audio_file_path}")
    
    if audio_path.suffix != ".m4a":
        raise ValueError("Only .m4a files are supported")
    
    return audio_path

def save_transcript(audio_file_path, transcript_text):
    """
    Saves the transcript to data/transcript folder.
    TODO: In future, you will be able to save it in a given folder.
    """
    output_dir = Path("data/transcripts")
    output_dir.mkdir(parents=True, exist_ok=True)
    transcript_file_name = audio_file_path.stem + ".txt"
    output_path = output_dir / transcript_file_name

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(transcript_text)
    
    return output_path

def main():
    
    arguments = parse_arguments()

    input_file = arguments.input_path
    model_name = arguments.model_name

    audio_file_path = validate_input_file(input_file)

    print(f"Transcribing {str(audio_file_path)} ...")

    model = load_transcription_model(model_name)
    transcript_text = transcribe_audio(str(audio_file_path), model)

    output_path = save_transcript(audio_file_path, transcript_text)

    print(f"Transcript saved to {output_path}")

if __name__ == "__main__":
    main()
