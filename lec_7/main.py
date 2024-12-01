import os

def main():
    while True:
        filename = input('Enter the name of the file: ')

        try:
            # Debugging: Print current directory
            print(f"Current directory: {os.getcwd()}")

            # Check if the filename is numeric
            if filename.isdigit():
                raise ValueError('File name cannot be a number.')

            # Attempt to open the file in read mode
            file = open(filename, 'r')
            content = file.read()
            file.close()

        except FileNotFoundError:
            print(f'File {filename} not found. Please enter a valid filename.')

        except ValueError:
            print('Please enter a non-digit file name.')

        else:

            print("\nFile Content:")
            print(content)

            # Ask the user if they want to write to the file
            choice = input('Do you want to write to the file? yes or no: ')
            if choice == 'yes':
                new_file = input('Do you want to write to the same file or a new file? yes or no: ')

                if new_file == 'no':
                    # Writing to the same file
                    file = open(filename, 'w')
                    new_content = input('Enter the content you want to write: ')
                    file.write(new_content)
                    file.close()
                    print(f'Content successfully written to {filename}')

                else:

                    new_filename = input('Enter a new file name: ')
                    new_content = input('Enter the content you want to write: ')
                    file = open(new_filename, 'w')
                    file.write(new_content)
                    file.close()
                    print(f'Content successfully written to {new_filename}')

            break

        finally:
            print("I hope the code has succeeded")

if __name__ == "__main__":
    main()
