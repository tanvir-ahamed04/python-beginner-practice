# Open the original file for reading and writing
with open('companies.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

    # Append the new line
    new_line = '\nAlibaba.'
    content += new_line

    # Save the modified content in a new file
    with open('scompanies.txt', 'w') as new_file:
        new_file.write(content)
