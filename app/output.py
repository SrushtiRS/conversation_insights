from pathlib import Path


def separate_segments(transcription_result):
    """
    Separate segments and join them in a string that can be saved to .md file.
    """
    segments = transcription_result['segments']
    # Collect text from each segment and remove extra whitespaces.
    cleaned_segments = [seg['text'].strip() for seg in segments]
    # Join the string with double newlines so that they appear as paragraphs in markdown
    segemnts_in_paragraphs = "\n\n".join(cleaned_segments)
    return segemnts_in_paragraphs


def save_transcript(audio_file_path, transcript_text):
    """
    Saves the transcript to data/transcript folder in a markdown format.
    TODO: In future, you will be able to save it in a given folder.
    """
    output_dir = Path("data/transcripts")
    output_dir.mkdir(parents=True, exist_ok=True)
    transcript_file_name = audio_file_path.stem + ".md"
    output_path = output_dir / transcript_file_name

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(transcript_text)
    
    return output_path