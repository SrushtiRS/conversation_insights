import whisper

def load_transcription_model(model_name="medium"):
    model = whisper.load_model(model_name)
    return model

def transcribe_audio(file_path, model):
    result = model.transcribe(file_path.as_posix(), language="en")
    return result