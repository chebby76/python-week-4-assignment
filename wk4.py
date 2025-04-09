def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Open and read the file
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content 
        modified_content = []
        for i, line in enumerate(content, start=1):
            modified_content.append(f"{i}: {line}")

        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write to: ")

        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File modified and written to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read/write file. Ensure you have the correct permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
read_and_modify_file()
