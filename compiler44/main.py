# Вариант 4. Грамматика G4 -- логические выражения
from tree import *


print("~~~ EXPRESSION PARSING ~~~")
# expression = "true & ~false"
# expression = "A ! B & ~false"
expression = "true & ~B ! A"
print(f"Input expression: {expression}")
clear_expr = expression.replace(" ", "")
clear_expr = clear_expr.replace("true", "t")
clear_expr = clear_expr.replace("false", "f")
print(f"Expression without spaces: {clear_expr}")

parser_expr = ExpressionParser(clear_expr)
result_expr = parser_expr.parse()
print(f"Result of parsing: {result_expr}")

convert_to_graph_expression(expression, result_expr)

print("~~~ REVERSE POLISH NOTATION ~~~")
result = reverse_polish_notation(result_expr)
result = ' '.join(result)
print(f"Reverse polish notation: {result}")

create_tree(expression)