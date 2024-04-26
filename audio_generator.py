from transformers import AutoProcessor, BarkModel
import scipy

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

voice_preset = "v2/en_speaker_6"

inputs = processor("Hello, my dog is cute", voice_preset=voice_preset)

audio_array = model.generate(**inputs)
#audio_array = audio_array.cpu().numpy().squeeze()
audio_array = audio_array.cpu().numpy().squeeze()

# Save the .wav file to disk
sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("output.wav", rate=sample_rate, data=audio_array)
