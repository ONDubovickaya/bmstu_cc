class ProgramParser:
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
        result = self.program()
        if self.current_token is not None:
            raise SyntaxError("Invalid program")
        return result

    def program(self):
        print("Parsing program/block")
        # в рамках данной грамматики <program> это и есть <block>
        if self.current_token == '{':
            self.get_next_token()
            result = self.operators_list()
            if self.current_token == '}':
                self.get_next_token()
                print("BLOCK PARSED SUCCESSFULLY")
                return result
            else:
                raise SyntaxError("Missing close '}'")
        else:
            raise SyntaxError("Invalid program")

    def operators_list(self):
        print("Parsing operators list")
        result = self.operator()
        result += self.tail()
        return result

    def tail(self):
        print("Parsing tail")
        if self.current_token == ';':
            self.get_next_token()
            result = self.operator()
            result += self.tail()
            return result
        return ""

    def operator(self):
        print("Parsing some operator")
        if self.current_token.isalpha():
            identifier = self.current_token
            self.get_next_token()
            if self.current_token == '=':
                self.get_next_token()
                expression = self.expr()
                return [identifier, expression]
            else:
                raise SyntaxError("Missing '='")
        else:
            raise SyntaxError("Invalid operator")

    def expr(self):
        return self.logical_expression()

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