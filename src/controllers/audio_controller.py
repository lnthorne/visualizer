import wave
import numpy as np

class AudioController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)

    def load_file(self, file_path):
        with wave.open(file_path, "rb") as wav_file:
            params = wav_file.getparams()
            num_channels = params.nchannels
            sample_rate = params.framerate
            num_frames = params.nframes
            audio_data = wav_file.readframes(num_frames)

        # Convert the raw audio bytes to a numpy array
        audio_samples = np.frombuffer(audio_data, dtype=np.int16)
        audio_samples = audio_samples.reshape(-1, num_channels)

        # Normalize the audio samples from -1.0 to 1.0
        audio_samples = audio_samples / np.max(np.abs(audio_samples), axis=0)

        left_channel = audio_samples[:, 0]
        right_channel = audio_samples[:, 1]

        self.view.display_waveform(left_channel, right_channel)
        self.view.display_info(num_frames, sample_rate)

