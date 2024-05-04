mass = []


class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression
        self.current_token = None
        self.current_index = 0

    def get_next_token(self):
        if self.current_index < len(self.expression):
            self.current_token = self.expression[self.current_index]
            self.current_index += 1
        else:
            self.current_token = None

    def parse(self):
        self.get_next_token()
        result = self.logical_expression()
        if self.current_token is not None:
            raise SyntaxError("Invalid expression")
        return result

    def logical_expression(self):
        result = self.logical_term()
        while self.current_token == '!':
            operation = self.current_token
            self.get_next_token()
            right = self.logical_term()
            result = (operation, result, right)
        return result

    def logical_term(self):
        result = self.secondary_logical_expression()
        while self.current_token == '&':
            operation = self.current_token
            self.get_next_token()
            right = self.secondary_logical_expression()
            result = (operation, result, right)
        return result

    def secondary_logical_expression(self):
        if self.current_token == '~':
            operation = self.current_token
            self.get_next_token()
            right = self.primary_logical_expression()
            result = (operation, right)
            return result
        return self.primary_logical_expression()

    def primary_logical_expression(self):
        if self.current_token in ['t', 'f']:
            result = self.current_token
            self.get_next_token()
        elif self.current_token.isalpha():
            result = self.current_token
            self.get_next_token()
        else:
            raise SyntaxError("Invalid token")

        return result


def reverse_polish_notation(expr):
    if isinstance(expr, tuple):
        if len(expr) == 3:
            op, left, right = expr
            left_expr = reverse_polish_notation(left)
            right_expr = reverse_polish_notation(right)
            mass.append((left_expr + right_expr + op, left_expr, right_expr))
            return left_expr + right_expr + op

        elif len(expr) == 2:
            op, right = expr
            right_expr = reverse_polish_notation(right)
            mass.append((right_expr + op, op, right_expr))
            return right_expr + op
    else:

        return expr