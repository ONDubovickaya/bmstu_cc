symbols = ["(", ")", "*", "|"]
description = ["Left Bracket", "Right Bracket", "Kline Star", "Or"]


class Symbol:
    def __init__(self, value, desc):
        self.value = value
        self.desc = desc

    def __str__(self):
        return f"{self.value} -- {self.desc}"


def index_in_dictionary(char):
    for i in range(len(symbols)):
        if char == symbols[i]:
            return i
    return -1


class Parser:
    def __init__(self):
        # все символы из введённого регулярного выражения
        self.symbolsFromRegex = []

        # алфавит введённого регулярного
        self.alphabet = []

        self.currentSymbolIndex = 0
        self.currentSymbol = ""

        # массив символов введённого РВ в порядке выполнения операций
        self.registeredSymbols = []

    # описание и обработка введённого РВ
    def parsing(self, string):
        if len(string) < 0:
            return []

        print(f"~~~ DESCRIBING THE SYMBOLS OF {string} ~~~")
        self.describe_symbols(string)

        print(f"\n~~~ HANDLING THE SYMBOLS OF {string} ~~~")
        self.handle_symbols()

        print(f"\n~~~ REGISTERED SYMBOLS ~~~")
        number = 1
        for symbol in self.registeredSymbols:
            print(f"{number}. {symbol}")
            number += 1
        print("\n")

        return self.registeredSymbols

    # описание всех символов РВ
    def describe_symbols(self, string):
        for char in string:
            index = index_in_dictionary(char)

            if index == -1:
                symbol = Symbol(char, "Char")

                if char not in self.alphabet:
                    self.alphabet.append(symbol.value)

            else:
                symbol = Symbol(char, description[index])

            self.symbolsFromRegex.append(symbol)

        for symbol in self.symbolsFromRegex:
            print(symbol)

        print(f"\nAlphabet: {self.alphabet}")

        self.currentSymbol = self.symbolsFromRegex[self.currentSymbolIndex]
        print(f"First symbol is: {self.currentSymbol.value}")
        self.currentSymbolIndex += 1

    # обработка всех символов РВ
    def handle_symbols(self):
        self.handle_body()

        if self.currentSymbol.value == "|":
            symbol = self.currentSymbol
            self.next_symbol("Or")
            self.handle_symbols()
            self.registeredSymbols.append(symbol)
            print("'|' added to registered symbols")

    def handle_body(self):
        if self.currentSymbol.value == "(":
            self.next_symbol("Left Bracket")
            self.handle_symbols()
            self.next_symbol("Right Bracket")

        if self.currentSymbol.desc == "Char":
            self.registeredSymbols.append(self.currentSymbol)
            print(f"'{self.currentSymbol.value}' added to registered symbols")
            self.next_symbol("Char")

        if self.currentSymbol.value == "*":
            self.registeredSymbols.append(self.currentSymbol)
            print("'*' added to registered symbols")
            self.next_symbol("Kline Star")

        if self.currentSymbol.value not in ")|":
            self.handle_body()
            self.registeredSymbols.append(Symbol(".", "Concatenation"))
            print("'.' added to registered symbols")

    def next_symbol(self, desc):
        if self.currentSymbol.desc == desc:
            if self.currentSymbolIndex >= len(self.symbolsFromRegex):
                self.currentSymbol = Symbol("", "None")
            else:
                self.currentSymbol = self.symbolsFromRegex[self.currentSymbolIndex]
            self.currentSymbolIndex += 1


