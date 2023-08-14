import subprocess

def check_command_output(command, text):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return text in result.stdout
    except subprocess.CalledProcessError:
        return False