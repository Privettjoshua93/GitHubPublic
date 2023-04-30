import numpy as np
from scipy.io.wavfile import read, write
import os

def reduce_volume(signal, reduction_percentage):
    return signal * (1 - reduction_percentage / 100)

def main():
    # Get input file path from the user
    input_file_path = input("Enter the .wav file path: ")

    if not os.path.isfile(input_file_path) or not input_file_path.endswith(".wav"):
        print("Invalid file path. Please provide a valid .wav file.")
        return

    # Get the percentage of volume reduction
    volume_reduction = float(input("Enter the percentage to reduce the volume: "))

    if not (0 <= volume_reduction <= 100):
        print("Invalid percentage. Please provide a value between 0 and 100.")
        return

    # Read audio file
    sr, audio_data = read(input_file_path)

    # Reduce the volume
    reduced_volume_audio = reduce_volume(audio_data, volume_reduction)

    # Save the processed audio file
    output_file_path = os.path.splitext(input_file_path)[0] + "_reduced_volume.wav"
    write(output_file_path, sr, reduced_volume_audio.astype(np.int16))

    print(f"Processed audio file saved as {output_file_path}")

if __name__ == "__main__":
    main()
