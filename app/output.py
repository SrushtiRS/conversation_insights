from pathlib import Path


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