import subprocess

def compile_cpp(file_path, output_path):
    try:
        # Run the compilation command
        subprocess.check_call(['g++', file_path, '-o', output_path])
        print("Compilation successful!")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:", e)

# Specify the path to your C++ source file and the desired output path for the executable
cpp_file_path = 'C:/Users/Ahmed/programming/magit/test.cpp'
output_path = 'C:/Users/Ahmed/programming/magit/test'

# Call the function to compile the C++ file
compile_cpp(cpp_file_path, output_path)
