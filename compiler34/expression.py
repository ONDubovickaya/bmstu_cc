class ExpressionParser:
    def __init__(self, expression):
        self.expression = expression
        self.current_token = None
        self.current_index = 0

    def get_next_token(self):
        if self.current_index < len(self.expression):
            self.current_token = self.expression[self.current_index]
            print(f"\nCurrent token: {self.current_token}")
            self.current_index += 1
        else:
            self.current_token = None
            print(f"\nCurrent token: {self.current_token}")

    def parse(self):
        self.get_next_token()
        result = self.logical_expression()
        print(f"Result: {result}")
        if self.current_token is not None:
            print("Current token isn't None!")
            raise SyntaxError("Invalid expression")
        return result

    def logical_expression(self):
        print("\n~ parsing logical expression ~")
        result = self.logical_term()
        print(f"~Logical term: {result}")
        while self.current_token == '!':
            operation = self.current_token
            print(f"~Operation is {operation}")
            self.get_next_token()
            right = self.logical_term()
            print(f"\n~Right logical term is {right}")
            result = (operation, result, right)
            print(f"~Result is {result}")
        return result

    def logical_term(self):
        print("\n~~ parsing logical term ~~")
        result = self.secondary_logical_expression()
        print(f"~~Secondary LE is {result}")
        while self.current_token == '&':
            operation = self.current_token
            print(f"~~Operation is {operation}")
            self.get_next_token()
            right = self.secondary_logical_expression()
            print(f"\n~~Right secondary LE is {right}")
            result = (operation, result, right)
            print(f"~~Result is {result}")
        return result

    def secondary_logical_expression(self):
        print("\n~~~ parsing secondary logical expression ~~~")
        if self.current_token == '~':
            operation = self.current_token
            print(f"~~~Operation is {operation}")
            self.get_next_token()
            right = self.primary_logical_expression()
            print(f"\n~~~Right primary LE is {right}")
            result = (operation, right)
            print(f"~~Result is {result}")
            return result
        return self.primary_logical_expression()

    def primary_logical_expression(self):
        print("\n~~~~ parsing primary logical expression ~~~~")
        if self.current_token in ['t', 'f']:
            result = self.current_token
            if result == 't':
                print(f"~~~~Current token is {result} (in grammar it's True)")
            if result == 'f':
                print(f"~~~~Current token is {result} (in grammar it's False)")
            self.get_next_token()
        elif self.current_token.isalpha():
            result = self.current_token
            print(f"~~~~Current token is alpha. It means {result}")
            self.get_next_token()
        else:
            raise SyntaxError("Invalid token")

        return result