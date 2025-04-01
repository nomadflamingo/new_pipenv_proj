from app.io import input, output

def main():
    # Read data from console and file
    path = input.read_from_console("Please enter a file path: ")
    
    # Log the path that was read from the console
    output_str = f"Path read from console: {path}"

    try:
        data = input.read_from_file(path)
        pandas_data = input.read_from_file_with_pandas(path)
    except FileNotFoundError:
        output.write_to_console(f"File not found: {path}")
        return
    except Exception as e:
        output.write_to_console(f"An error occurred: {e}")
        return
    
    output.write_to_console(output_str)
    output.write_to_file('data/path_log.txt', output_str)

    # Output the data to console and file
    output.write_to_console(''.join(data))
    output.write_to_file('data/output.txt', ''.join(data))
    
    # Output the pandas DataFrame to console and file
    output.write_to_console(pandas_data.to_string())
    output.write_to_file('data/pandas_output.txt', pandas_data.to_string())


if __name__ == "__main__":
    main()
