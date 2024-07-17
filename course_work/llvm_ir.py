from code_generator.my_visitor import generate_ir
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Wrong command!")
        print("You need to write: ' python llvm_ir.py input_file '")
        print("Example: ' python llvm_ir.py example.tc '")
    else:
        input_file = sys.argv[1]
        print(f"Input file: {input_file}")

        output_file = input_file[:-3] + ".ll"
        print(f"Output file: {output_file}")

        generate_ir(input_file, output_file)
