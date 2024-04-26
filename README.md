# Experiments with audio and AI

## Install

See also: https://youtu.be/o8-1hb7hFTI?si=DiQF6CpeOt18AeDA

```shell
python3 -m venv bark
. ./bark/bin/activate
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install git+https://github.com/suno-ai/bark.git
pip install git+https://github.com/huggingface/transformers.git
pip install soundfile
pip install nltk
```

