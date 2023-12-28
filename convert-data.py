import json
import os
import datetime

def convert_data(folder_path,  lang="en"):
    # Specify the file path

    # get absolute path
    folder_path = os.path.abspath(folder_path)
    
    metadata_path = os.path.join(folder_path, "metadata")
    wav_audio_path = os.path.join(folder_path, "wav")


    new_wav_path = os.path.join(folder_path, "new_wav")
    if not os.path.exists(new_wav_path):
            os.mkdir(new_wav_path)
        
    new_wav_path = os.path.join(new_wav_path, lang)

    if not os.path.exists(new_wav_path):
        os.mkdir(new_wav_path)

    # Iterate over files in the folder
    for file_name in os.listdir(metadata_path):
        json_file_path = os.path.join(metadata_path, file_name)
        if os.path.isfile(json_file_path):
            new_wav_file_name = get_new_file_name(json_file_path)
      
            # remove the .json extension
            json_file_name = file_name[:-5]
            # create wav file name
            wav_file_name = json_file_name + ".wav"

            # create wav file path
            wav_file_path = os.path.join(wav_audio_path, wav_file_name)

            # create new wav file path
            new_wav_file_path = os.path.join(new_wav_path, new_wav_file_name)

            # print(new_wav_file_path)
            # rename the wav file
            rename_and_copy_file(wav_file_path, new_wav_file_path)




def get_new_file_name(json_file_path):
    # open the json file
    with open(json_file_path) as json_file:
        # load the json file

        file_name = os.path.basename(json_file_path)
        data = json.load(json_file)
        ts_start = data["ts_start"]
        try:
            ts_start = datetime.datetime.strptime(ts_start, "%H:%M:%S.%f").time()
        except ValueError:
            ts_start = datetime.datetime.strptime(ts_start, "%H:%M:%S").time()
        
        ts_start = ts_start.strftime("%H%M.%f")[:-3]
        ts_end = data["ts_end"]
        try:
            ts_end = datetime.datetime.strptime(ts_end, "%H:%M:%S.%f").time()
        except ValueError:
            ts_end = datetime.datetime.strptime(ts_end, "%H:%M:%S").time()
        ts_end = ts_end.strftime("%H%M.%f")[:-3]

        new_file_name = f"{file_name[:-5]}---{ts_start}-{ts_end}.wav"
        return new_file_name

def rename_and_copy_file(old_file_path, new_file_name):
    if os.path.isfile(old_file_path):
        new_file_path = os.path.join(os.path.dirname(old_file_path), new_file_name)
    if not os.path.exists(new_file_path):
    #   Copy the content of the file
        with open(old_file_path, 'rb') as f:
            with open(new_file_path, 'wb') as f1:
                for line in f:
                    f1.write(line)


if __name__ == "__main__":
    # file_name =get_new_file_name("data/nptel-pure-set/nptel-pure/metadata/000ad6c22f20b266297a26479bfde266acaef84e3accec59b5ac9330.json")
    # print(file_name)

    # get args from command line
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder_path", help="path to the folder containing the data", required=True)
    parser.add_argument("--lang", help="name of the language for the folder", default="en")
    args = parser.parse_args()
    convert_data(folder_path=args.input_folder_path,  lang=args.lang)
