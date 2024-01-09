import os


def split(folder_path):
    

    # Count the number of files in the folder
    file_count = len(os.listdir(folder_path))


    # Split the files into two sizes i.e 30% and 70%
    split_size = file_count // 3 
    files = os.listdir(folder_path)
    valid = files[:split_size]
    train = files[split_size:]



    # Create the /valid/en-in and /train/en-in directories if they don't exist
    valid_path = os.path.join(folder_path, 'valid')
    os.makedirs(valid_path, exist_ok=True)
    valid_path = os.path.join(valid_path, 'en-in')
    os.makedirs(valid_path, exist_ok=True)

    train_path = os.path.join(folder_path, 'train')
    os.makedirs(valid_path, exist_ok=True)
    train_path = os.path.join(train_path, 'en-in')
    os.makedirs(train_path, exist_ok=True)

    # Move the files to the respective directories
    for file in valid:
        print(f"copying {file} to {valid_path}... ")
        src = os.path.join(folder_path, file)
        dst = os.path.join(valid_path, file)
        os.rename(src, dst)

    for file in train:
        print(f"copying {file} to {valid_path}... ")
        src = os.path.join(folder_path, file)
        dst = os.path.join(train_path, file)
        os.rename(src, dst)

    # Print the results
    print("Number of files in the folder:", file_count)
    print("Number of files in validation set :",len(valid))
    print("Number of files in training set :",len(train))



if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder_path", help="path to the folder containing the data", required=True)
    args = parser.parse_args()
    folder_path = args.input_folder_path
    split(folder_path=folder_path)