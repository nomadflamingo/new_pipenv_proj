import pandas as pd

def read_from_console(prompt: str = "Enter a line: ") -> str:
    """
    Reads a line from the console and returns it
    
    Parameters:
        prompt (str): The prompt to display to the user

    Returns:
        str: The line read from the console
    """
    return input(prompt)


def read_from_file(file_path: str) -> list:
    """
    Reads lines from a file and returns them as a list
    
    Parameters:
        file_path (str): The path to the file to read from

    Returns:
        list: A list of lines read from the file
    """
    with open(file_path, 'r') as file:
        return file.readlines()


def read_from_file_with_pandas(file_path: str) -> pd.DataFrame:
    """
    Reads a file using pandas and returns a DataFrame
    
    Parameters:
        file_path (str): The path to the file to read from

    Returns:
        pd.DataFrame: A DataFrame containing the data read from the file
    """
    return pd.read_csv(file_path, header=None)