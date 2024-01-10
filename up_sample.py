import soundfile as sf
from scipy import signal

# Specify the file paths
input_file = 'output-en-8k.wav'
output_file = 'output-en-16k-up.wav'

# Read the input file
data, sample_rate = sf.read(input_file)

# Resample the audio to 16kHz using scipy's signal.resample
resampled_data = signal.resample(data, int(len(data) * 16000 / sample_rate))

# Export the resampled audio as a 16kHz WAV file
sf.write(output_file, resampled_data, 16000)
