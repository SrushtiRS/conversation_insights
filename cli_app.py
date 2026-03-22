import argparse
from pathlib import Path

from app.file_utils import validate_input
from app.output import save_transcript, separate_segments
from app.transcribe import load_transcription_model, transcribe_audio

# TODO: add logging
# TODO: add testing

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

def main():
    
    arguments = parse_arguments()

    input_file = arguments.input_path
    model_name = arguments.model_name
    
    is_file, file_paths = validate_input(input_file)

    model = load_transcription_model(model_name)
    for file_path in file_paths:
        print(f"Transcribing {file_path.as_posix()}")
        transcription_result = transcribe_audio(file_path, model)
        transcript_text = separate_segments(transcription_result)
        output_path = save_transcript(file_path, transcript_text)
        print(f"Transcript saved to {output_path}")
   

if __name__ == "__main__":
    main()
