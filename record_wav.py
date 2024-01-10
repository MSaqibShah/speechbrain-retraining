import sounddevice as sd
import soundfile as sf

# Set the sample rate and duration
sample_rate = 8000
duration = 10  # in seconds

# Record the audio
recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1)

# Wait for the recording to complete
sd.wait()

# Save the recording to a WAV file
sf.write('output-en-8k.wav', recording, sample_rate)

