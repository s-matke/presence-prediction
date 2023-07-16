import os
import urllib.request
from zipfile import ZipFile
import time
import argparse

# url where dataset is hosted
DATA_URL = "https://figshare.com/ndownloader/articles/9582962/versions/1"

# output name passed to downloaded file from data_url
OUTPUT_NAME = "data.zip"

# allowed number of re-attempts for downloading data
TIMEOUT_ATTEMPTS = 5

# Download required dataset
def download_data():
    attempts = 0
    while attempts < TIMEOUT_ATTEMPTS:
        try:
            path, _ = urllib.request.urlretrieve(DATA_URL, OUTPUT_NAME)
            print("Data downloaded at path: ", os.getcwd())
            return True
        except:
            print("Something went wrong downloading data, trying again... [{attempts}]".format(attempts=attempts+1), end='\r')
            attempts += 1
            time.sleep(attempts)
    return False

# Extract files from .zip file
def extract_data():
    attempts = 0
    if not os.path.exists(PATH_OUTPUT):
        print("Error: couldn't find file " + OUTPUT_NAME + " in /data/ dir")
        exit(0)
    while attempts < TIMEOUT_ATTEMPTS:
        try:
            with ZipFile(PATH_OUTPUT, 'r') as zf:
                zf.extractall(path=os.getcwd())
            print("Successfully extracted data!")
            os.remove(OUTPUT_NAME)
            break
        except:
            print("Failed to extract files from " + OUTPUT_NAME)
            attempts += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", type=str, default="true", help="Set to 'true' to enable download, or 'false' to disable it.", required=False)
    args = parser.parse_args()

    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir("../../data")
        PATH_OUTPUT = os.path.join(os.getcwd(), OUTPUT_NAME)
    except:
        print("Error: Couldn't change directory")
        exit(0)

    if args.download.lower() == "true":
        if not download_data():
            print("\nError: Couldn't fetch data! Check your internet connection and DATA_URL...")
            exit(0)
    extract_data()
