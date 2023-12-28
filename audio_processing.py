# audio_processing.py

import random
from typing import Dict
import speechbrain as sb

def audio_pipeline(sample_dict: Dict, snt_len_sample, label_encoder, random_chunk=True):
    key = sample_dict["__key__"]
    language_id = sample_dict["language_id"].decode("ascii")
    audio_tensor = sample_dict["audio.pth"]

    # determine what part of audio sample to use
    audio_tensor = audio_tensor.squeeze()

    if random_chunk:
        if len(audio_tensor) - snt_len_sample - 1 <= 0:
            start = 0
        else:
            start = random.randint(0, len(audio_tensor) - snt_len_sample - 1)

        stop = start + snt_len_sample
    else:
        start = 0
        stop = len(audio_tensor)

    sig = audio_tensor[start:stop]

    # determine the language ID of the sample
    lang_id_idx = label_encoder.encode_label(language_id)

    return {
        "sig": sig,
        "lang_id_encoded": lang_id_idx,
        "id": key,
    }
