import subprocess
import time
import tempfile

while True:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the content to the temporary file
        temp_file.write("Sesh tumar laptop ses,\n eida r kaj korbe nah (:--------------")

    # Open the temporary file with Notepad
    process = subprocess.Popen(['notepad', temp_file.name])
    process.wait()  # Wait for the Notepad process to finish

    # Read the content of the file after Notepad is closed
    with open(temp_file.name, 'r') as f:
        content = f.read()
        print("Content written to Notepad and read back:", content)

    # Clean up: Delete the temporary file
    import os
    os.remove(temp_file.name)
    time.sleep(1)  # Fixed the sleep function

