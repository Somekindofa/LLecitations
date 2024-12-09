###     The  test.py  script is a simple Python script that loads the Whisper model, 
#       transcribes the input audio file, and prints the transcript.
###

import whisper
import time
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Device count: {torch.cuda.device_count()}")

audio_path = "data\input\GBL_Maxime_Pipe_Elicitation.wav"
model_type = "small"
language = "en"

print("Loading Whisper model...")
time_model_load = time.time()
model = whisper.load_model(model_type)
time_model_load = time.time() - time_model_load
print(f"Whisper model loaded: {model_type} in {time_model_load:.2f} seconds")

# use the "van-gogh-quote.wav" as input
print("Processing audio...")
time_transcribe = time.time()
transcript = whisper.transcribe(model, audio_path)
time_transcribe = time.time() - time_transcribe
print(f"Transcription completed in {time_transcribe:.2f} seconds")

# print the transcript
print(transcript["text"])
# print 2 blank lines for readability
print("\n\n")
 
