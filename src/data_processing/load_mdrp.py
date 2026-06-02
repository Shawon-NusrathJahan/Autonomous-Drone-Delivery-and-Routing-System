import pandas as pd
import os

def load_mdrp(path):
    """
    Loads all CSV files from the MDRP dataset folder.
    
    'path' must be a folder (like '../datasets/mdrp/'), NOT a single file.
    It will find every .csv file inside and load each one into a DataFrame.
    
    Returns:
        A dictionary where each key is the filename and each
        value is the loaded pandas DataFrame.
    """

    # Make sure the folder actually exists before we try to read it.
    # If it does not exist, this gives a clear error message instead
    # of a confusing Permission denied.
    if not os.path.isdir(path):
        raise FileNotFoundError(
            f"Folder not found: '{path}'\n"
            f"Current working directory is: {os.getcwd()}\n"
            f"Please check that the path is correct."
        )

    all_data = {}   # empty dictionary — will hold one DataFrame per file

    # os.listdir() returns a list of every file and folder inside 'path'
    for filename in os.listdir(path):

        # We only want CSV files — skip anything else (like .DS_Store, folders, etc.)
        if filename.endswith('.csv'):

            # os.path.join safely combines the folder path and filename.
            # On Windows this produces: ..\datasets\mdrp\customers.csv
            full_path = os.path.join(path, filename)

            # NOW we pass a single file path to pd.read_csv — this is what it expects.
            df = pd.read_csv(full_path)

            # Store it in the dictionary using the filename as the key
            all_data[filename] = df

            print(f"Loaded: {filename}  |  Rows: {df.shape[0]}  |  Columns: {df.shape[1]}")

    if len(all_data) == 0:
        print(f"Warning: No CSV files found in '{path}'")

    return all_data