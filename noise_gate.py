import librosa
import numpy as np

def apply_noise_gate(audio_path, threshold):
    # Load the audio file
    audio, sr = librosa.load(audio_path, sr=None)

    # Compute the short-time Fourier transform (STFT)
    stft = librosa.stft(audio)

    # Calculate the magnitude spectrogram
    mag_spec = np.abs(stft)

    # Compute the frame-wise energy
    frame_energy = librosa.feature.rms(audio, frame_length=len(audio), hop_length=1)

    # Apply the noise gate to identify frames with noise
    noisy_frames = np.where(frame_energy > threshold)

    # Create a binary mask to separate noise from the audio
    mask = np.zeros_like(mag_spec)
    mask[:, noisy_frames] = 1

    # Apply the mask to the magnitude spectrogram
    mag_spec_filtered = mag_spec * mask

    # Reconstruct the filtered audio using the inverse STFT
    filtered_audio = librosa.istft(mag_spec_filtered)

    return filtered_audio

# Example usage
audio_path = 'D:/audio_features/assets/audio_to_gate.wav'
threshold = 0.1  # Adjust this threshold according to your audio

filtered_audio = apply_noise_gate(audio_path, threshold)


