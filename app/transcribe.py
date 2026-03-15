import whisper

# file_path = "/Users/srushtirs/GitHub/conversation_insights/data/audio/audio_10s.m4a"

def transcribe_audio(file_path):
    model = whisper.load_model("medium")
    result = model.transcribe(file_path, language="en")
    return result["text"]