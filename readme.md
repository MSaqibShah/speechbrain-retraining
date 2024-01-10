# How To Run

This script aims to finetune the [`speechbrain/lang-id-voxlingua107-ecapa`](https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa) model for improving the language identification of Indian English. The dataset used can be found below.

## 1. Run convert-data

This script is used to convert the [nptel-data](https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset?tab=readme-ov-file#downloads) into the format of [voxlingua](https://bark.phon.ioc.ee/voxlingua107/). This is done because the `create_shards.py` needs to read this data in this format.

`python convert-data.py --input_folder_path path/to/nptel-data`

## 2. Run create shards

This script is used to create WebDataset Shards from the nptel-data (converted). This is done to maxinize the tranning performance of the model.

`python create_shards.py /path/to/data/input /data/finalshards/train`

`python create_shards.py /path/to/data/input /data/finalshards/dev`

Note: The output path should be always set to `/data/finalshards/train` and `/data/finalshards/dev`. The `/train` directoty holds the data for traning and `/dev` directory holds the data for validation.

## 3. Run train

After the data shards are created we can run the `train.py` to start retraning the model.

`python train.py`

## Resources

[Model Recipie](https://github.com/speechbrain/speechbrain/tree/develop/recipes/VoxLingua107)

[Pretraining Example](https://colab.research.google.com/drive/1LN7R3U3xneDgDRK2gC5MzGkLysCWxuC3?usp=sharing#scrollTo=R3B4Dv1Wjfv6)

# How to use the model.

## 1. Download the model

Use the Link below to download the model from google drive and then extract the model files in the project root.

## 2. Test the model

Run the `test.py` to check if everything is working. Make sure to update the audio file path in test.py to a valid audio path.
