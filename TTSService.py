import torch
from TTS.api import TTS
import tempfile

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# wav = tts.tts(text="مرحبا بك", speaker_wav="my-speech.wav", language="ar")
speaker_wav = "speaker.wav"
language = "ar"

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output

# Text to speech to a file
# tts.tts_to_file(text="مرحبا بك", speaker_wav="my-speech.wav", language="ar", file_path="output.wav")

class TTSService:
    def __init__(self) -> None:
        self.tts = tts
        self.speaker_wav = speaker_wav
        self.language = language
    

    def text_to_speech(self,text:str) -> bytes:
        
        with tempfile.NamedTemporaryFile(suffix='.wav') as tf:
            self.tts.tts_to_file(text=text,language=language,speaker_wav=speaker_wav,file_path=tf.name,sample_rate=16000)
            buffer = tf.read()
            return buffer
        