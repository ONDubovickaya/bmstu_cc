from parsing import *
from nfa import *
from dfa import *

# regex = "(a(b|c))*c"
# regex = "(a|b)*abb"
regex = input("Enter regex: ")

print(">>> Выполним парсинг регулярного выражения <<<")
parser = Parser()
regularString = parser.parsing(regex)

print(">>> №1. Построим НКА по введённому регулярному выражению <<<")
nfa = NFA()
nfa.nfa_build(regularString)

print(">>> №2. По НКА построим эквивалентный ему ДКА <<<")
dfa = DFA(nfa)
dfa.dfa_build()

print(">>> №3. По ДКА построим эквивалентный ему КА с min кол-вом состояний -- алгоритм Бржозовского <<<")
dfa.dfa_minimize()
dfa.output_dfa()

print(">>> №4. Моделируем минимальный КА для входной цепочки <<<")
# terminalString = "babb"
terminalString = input("Enter terminal string: ")
dfa.modeling(terminalString)

