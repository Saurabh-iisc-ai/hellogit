# Define the path to your file
file_path = r"C:\Users\SAUSHRI\Downloads\captions (7).sbv"

""" # Initialize a list to hold lines with more than 40 characters
long_lines = []

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    for line_num, line in enumerate(file, start=1):
        # Remove trailing newline characters
        stripped_line = line.rstrip('\n').rstrip('\r')
        
        # Check if the line length exceeds 40 characters
        if len(stripped_line) > 40:
            # Optionally, store the line number and content
            long_lines.append((line_num, stripped_line))

# Display the results
if long_lines:
    print("Lines with more than 40 characters:")
    for line_num, content in long_lines:
        print(f"Line {line_num}: {content}")
else:
    print("No lines exceed 40 characters.") """

matched_lines = []

# Initialize a variable to keep track of the previous line
previous_line_num = None
previous_content = None

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    for line_num, line in enumerate(file, start=1):
        # Remove trailing newline characters and convert to lowercase
        stripped_line = line.rstrip('\n').rstrip('\r')
        
        # Check if the current line contains "verse"
        chars_count=len(stripped_line)
        if len(stripped_line) > 42:
            if previous_line_num is not None and previous_content is not None:
                # Append a tuple containing (preceding_line_num, preceding_content, current_line_num, current_content)
                matched_lines.append((previous_line_num, previous_content, line_num, stripped_line,chars_count))
            else:
                # Handle the case where the first line contains "verse" and there is no preceding line
                matched_lines.append((None, None, line_num, stripped_line,chars_count))
        
        # Update the previous line variables for the next iteration
        previous_line_num = line_num
        previous_content = stripped_line

# Display the results
if matched_lines:
    print("Lines with more than 42 characters:")
    for entry in matched_lines:
        prev_num, prev_content, curr_num, curr_content,chars_count = entry
        if prev_num is not None and prev_content is not None:
            print(f"\nPreceding Line {prev_num}: {prev_content}")
        else:
            print(f"\nPreceding Line: None (This is the first line)")
        print(f"Line {curr_num}: {curr_content} No of characters: {chars_count}")
else:
    print("No lines exceed 40 characters.")
