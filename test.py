import torchaudio
from speechbrain.pretrained import EncoderClassifier

# load model from checkpoint
# model = EncoderClassifier.from_hparams(source="speechbrain/lang-id-voxlingua107-ecapa", savedir="pretrained_models/lang-id-voxlingua107-ecapa")
model = EncoderClassifier.from_hparams(source="results/epaca/1988/save/CKPT+2023-12-28+14-12-51+00")

# load audio file
signal = model.load_audio("data/final/en/00067107569155d10c1e73ecb11d7890c29ef9ccaebee78149e3bf2f---0028.388-0028.028.wav")
prediction =  model.classify_batch(signal)
print(prediction)

print(prediction[1].exp())
#  tensor([0.9850])
# The identified language ISO code is given in prediction[3]
print(prediction[3])
#  ['th: Thai']
  
