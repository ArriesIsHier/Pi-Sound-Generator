import numpy as np
from scipy.io.wavfile import write

# Constants
sample_rate = 44100  # Sample rate in Hz
duration = 1.0       # Duration of each tone in seconds
volume = 0.3         # Volume of the sound (0.0 to 1.0)

# Digits of pi
pi_digits = "314159265358979323846264338327950288419716939937510"

# Create an empty array to store the sound
sound = np.array([])

# Generate the sound
for digit in pi_digits:
    # Map the digit to a frequency between 200 Hz and 2000 Hz
    freq = 200 + int(digit) * 200
    
    # Generate the samples for this digit's tone
    samples = volume * np.sin(2 * np.pi * np.arange(sample_rate * duration) * freq / sample_rate)
    
    # Append the samples to the sound
    sound = np.append(sound, samples)

# Normalize to 16-bit range and convert to data type int16
sound = np.int16(sound / np.max(np.abs(sound)) * 32767)

# Write the .wav file
write('pi_sound.wav', sample_rate, sound)
