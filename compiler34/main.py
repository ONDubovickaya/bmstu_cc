# Вариант 4. Грамматика G4 -- логические выражения
from program import *
from expression import *
from graph import *


print("~~~ EXPRESSION PARSING ~~~")
expression = "true & ~false"
# expression = "A ! ~B & false"
# expression = "~A & B"
clear_expr = expression.replace(" ", "")
clear_expr = clear_expr.replace("true", "t")
clear_expr = clear_expr.replace("false", "f")
print(clear_expr)

parser_expr = ExpressionParser(clear_expr)
result_expr = parser_expr.parse()
print(result_expr)

convert_to_graph_expression(expression, result_expr)


print("\n~~~ PROGRAM PARSING ~~~")
program = "{ x = A ! B & ~false; y = ~D ; z = ~A ! C; w = C & ~true }"
# program = "{ y = ~D ; z = A & ~C }"
# program = "{ x = A ! B & ~false }"
clear_prog = program.replace(" ", "")
clear_prog = clear_prog.replace("true", "t")
clear_prog = clear_prog.replace("false", "f")
print(clear_prog)

parser_prog = ProgramParser(clear_prog)
result_prog = parser_prog.parse()
print(result_prog)

convert_to_graph_program(program, result_prog)