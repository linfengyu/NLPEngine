import os

def concatenate_files(output_filename, input_filename_pattern, num_parts):
    with open(output_filename, 'wb') as output_file:
        for part_num in range(1, num_parts + 1):
            # Generate the file name for each part
            part_filename = f"{input_filename_pattern}_part_{part_num}"
            
            # Check if the part file exists
            if os.path.exists(part_filename):
                with open(part_filename, 'rb') as part_file:
                    # Read and write the content of the part file into the output file
                    output_file.write(part_file.read())
                print(f"Added {part_filename} to {output_filename}")
            else:
                print(f"Error: {part_filename} does not exist.")
                break

if __name__ == "__main__":
    # Input pattern of file names (without the part number)
    input_filename_pattern = '/Users/linfengyu/SrcData/output/搬书匠-4666-Learn Generative AI with PyTorch-2024-英文版.dat'  # Change this to your pattern (e.g., 'video.mp4')
    
    # Output file name to concatenate the parts into
    output_filename = '/Users/linfengyu/SrcData/output/large_file.pdf'  # Change this to the desired output file name
    
    # Total number of parts to concatenate
    num_parts = 5  # Change this number based on how many parts you have (e.g., 5 for parts 1-5)

    concatenate_files(output_filename, input_filename_pattern, num_parts)
