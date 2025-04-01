def write_to_console(data: str) -> None:
    """
    Writes a string to the console
    
    Parameters:
        data (str): The string to write to the console
    """
    print(data)

def write_to_file(file_path: str, data: str) -> None:
    """
    Writes a string to a file
    
    Parameters:
        file_path (str): The path to the file to write to
        data (str): The string to write to the file
    """
    with open(file_path, 'w') as file:
        file.write(data)

