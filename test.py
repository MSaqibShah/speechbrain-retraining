import torchaudio
from speechbrain.pretrained import  EncoderClassifier, SpeakerRecognition
from speechbrain.utils.checkpoints import Checkpointer
import os
# from classifier import EncoderClassifier

model_path = "model/epaca/1988/save/CKPT+2024-01-09+16-55-38+00"
print(os.path.exists(model_path))
model = SpeakerRecognition.from_hparams(source=model_path)

print("model loaded")

prediction = model.classify_file("/home/ubuntu/output.wav")

print(prediction[1].exp())
# # #  tensor([0.9850])
# # The identified language ISO code is given in prediction[3]
print(prediction[3])
# #  ['th: Thai']
  
