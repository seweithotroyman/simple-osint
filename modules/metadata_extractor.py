import subprocess

def extract_metadata(file_path):
    result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE)
    return result.stdout.decode()
