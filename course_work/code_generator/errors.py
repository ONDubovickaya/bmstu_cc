from antlr4.error.ErrorListener import ErrorListener


# класс, который наследуется от Exception
# он используется для создания исключений, связанных с семантическими ошибками
class SemanticError(Exception):
    def __init__(self, msg, ctx=None):
        super().__init__()
        # если передан параметр ctx (контекст ошибки)
        if ctx:
            self.line = ctx.start.line
            self.column = ctx.start.column
        else:
            self.line = 0
            self.column = 0
        self.msg = msg

    def __str__(self):
        return f"SemanticError: {str(self.line)} : {str(self.column)} {self.msg}"


# класс, который наследуется от класса ErrorListener из библиотеки antlr4
class TinyCErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    # переопределение метода обработки синтаксических ошибок из ErrorListener
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        exception = f"Syntax Error: {str(line)} : {str(column)} {msg}"
        self.errors.append(exception)

    def register_semantic_error(self, error):
        self.errors.append(str(error))

    def print_errors(self):
        for err in self.errors:
            print(err)
        print(f"{len(self.errors)} errors generated")
