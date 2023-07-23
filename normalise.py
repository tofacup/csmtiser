import os
import sys

from csmtiser import Csmtiser
from csmtiser.config import load_config_file

def process_file(file_path, normalizer):
    new_path = normalizer.normalise(pth=file_path)
    os.rename(new_path, file_path + '.norm')
    print("Processed file: {}".format(file_path))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        config_path = sys.argv[1]
        file_paths = sys.argv[2:]
    else:
        config_path = sys.argv[1]
        file_paths = []

    normalizer = Csmtiser(load_config_file(config_path))

    for path in file_paths:
        process_file(path, normalizer)

    print("All files processed successfully.")
