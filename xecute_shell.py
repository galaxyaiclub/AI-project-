import os
import subprocess
import logging

def execute_shell_command_in_directory(directory, command):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Directory {directory} does not exist")

        # Change the directory
        os.chdir(directory)

        # Execute the shell command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

        # Return the output of the command
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during command execution
        logging.error(f"Error executing command: {e}")
        logging.error(f"Command output: {e.output}")
    except Exception as e:
        # Handle any other exceptions
        logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    directory_to_enter = "freegpt-webui-v2"
    command_to_execute = "python run.py"

    output = execute_shell_command_in_directory(directory_to_enter, command_to_execute)
    if output:
        print(output)
