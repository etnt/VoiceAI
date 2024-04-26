import os
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
#if os.getenv('PYTORCH_ENABLE_MPS_FALLBACK') != '1':
#     print ("you really need to run > export PYTORCH_ENABLE_MPS_FALLBACK=1")
#     exit(1)

from bark import SAMPLE_RATE, generate_audio
from IPython.display import Audio
import soundfile as sf
import numpy as np
from scipy.io import wavfile
from datetime import datetime as dt

text_prompt = """
I hope this will work for you.
"""
audio_array = generate_audio(text_prompt, history_prompt="en_speaker_8") #{lang_code}_speaker_{0-9}
iPyAudio = Audio(audio_array, rate=SAMPLE_RATE)

filename = 'audio-%s-%i.wav' % (dt.now().strftime('%Y%m%d-%H%M%S'), SAMPLE_RATE)
with open(filename, 'wb') as f:
    f.write(iPyAudio.data)
print ("saved %s" % filename)