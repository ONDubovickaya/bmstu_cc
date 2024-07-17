from code_generator.my_visitor import generate_ir
from executor import execute

print("Введите название TinyC файла:")
tinyc_file = input()

print(f"\nГенерируем ll-файл для {tinyc_file}")

print(f"~~ Input file: {tinyc_file}")
ll_file = tinyc_file[:-3] + ".ll"
print(f"~~ Output file: {ll_file}")

generate_ir(tinyc_file, ll_file)

print("\nЗапускаем ll-файл:")
result = execute(ll_file)
print(f"Program {ll_file} exits with code {result}\n\nResult of program:")
