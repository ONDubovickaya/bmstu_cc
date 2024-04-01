from graph import *
import os


class NFA:
    def __init__(self):
        # состояния
        self.states = []
        # количество состояний
        self.numberOfStates = 0

        # начальное состояние
        self.startState = None
        # финальные состояния
        self.finalStates = set()

        # алфавит
        self.alphabet = []

    def nfa_build(self, string):
        print("~~~ BUILDING NFA ~~~")
        txt_file = open("nfa.txt", "w")

        char_set = set()

        for symbol in string:
            if symbol.desc == "Char":
                print(f"~ Current is '{symbol.value}' ~")
                s0 = self.create_state()
                s1 = self.create_state()

                s0.transitions[symbol.value] = s1
                # print(f"Transition from {s0} to {s1} by {symbol.value}")
                print(f"{s0} ---{symbol.value}---> {s1}")
                txt_file.write(f"{s0} ---{symbol.value}---> {s1}\n")

                self.add_node(s0, s1)

                if symbol.value not in char_set:
                    char_set.add(symbol.value)

            elif symbol.desc == "Concatenation":
                print(f"~ Current is '{symbol.value}' ~")
                n2 = self.states.pop()
                n1 = self.states.pop()

                print(f"Node1: {str(n1)}")
                print(f"Node2: {str(n2)}")

                n1.end.isEnd = False

                if n1.end in self.finalStates:
                    self.finalStates.remove(n1.end)

                """
                1) Для добавления eps-переходов явно:
                n1.end.epsilon.append(n2.start)
                
                print(f"{n1.end} ---eps---> {n2.start}")
                file.write(f"{n1.end} ---eps---> {n2.start}\n")
                
                2) Для добавления eps-переходов, без добавления дополнительных стрелок:
                n1.end.epsilon = n2.start.epsilon
                
                n1.end.transitions = n2.start.transitions
                print(f"Copy all transitions from {n2.start} to {n1.end}")
                """

                n1.end.epsilon.append(n2.start)

                print(f"{n1.end} ---eps---> {n2.start}")
                txt_file.write(f"{n1.end} ---eps---> {n2.start}\n")

                self.add_node(n1.start, n2.end)
                # print(f"Add node with start in {n1.start} and end in {n2.end}\n")

            elif symbol.desc == "Or":
                print(f"~ Current is '{symbol.value}' ~")
                n2 = self.states.pop()
                n1 = self.states.pop()

                print(f"Node1: {str(n1)}")
                print(f"Node2: {str(n2)}")

                s0 = self.create_state()
                s1 = self.create_state()

                s0.epsilon = [n1.start, n2.start]
                # print(f"Added eps-transition from {s0} to {n1.start} and {n2.start}")
                print(f"{s0} ---eps---> {{{n1.start}, {n2.start}}}")
                txt_file.write(f"{s0} ---eps---> {{{n1.start}, {n2.start}}}\n")

                n1.end.epsilon.append(s1)
                # print(f"Added eps-transition from {n1.end} to {s1}")

                n2.end.epsilon.append(s1)
                # print(f"Added eps-transition from {n2.end} to {s1}")
                print(f"{{{n1.end}, {n2.end}}} ---eps---> {s1}")
                txt_file.write(f"{{{n1.end}, {n2.end}}} ---eps---> {s1}\n")

                n1.end.isEnd = False
                n2.end.isEnd = False

                if n1.end in self.finalStates:
                    self.finalStates.remove(n1.end)

                if n2.end in self.finalStates:
                    self.finalStates.remove(n2.end)

                self.add_node(s0, s1)
                # print(f"Add node with start in {s0} and end in {s1}\n")

            elif symbol.desc == "Kline Star":
                print(f"~ Current is '{symbol.value}' ~")
                n1 = self.states.pop()
                print(f"Node1: {str(n1)}")

                s0 = self.create_state()
                s1 = self.create_state()

                s0.epsilon = [n1.start]
                # print(f"Added eps-transition from {s0} to {n1.start}")

                s0.epsilon.append(s1)
                # print(f"Added eps-transition from {s0} to {s1}")
                print(f"{s0} ---eps---> {{{n1.start}, {s1}}}")
                txt_file.write(f"{s0} ---eps---> {{{n1.start}, {s1}}}\n")

                n1.end.epsilon.extend([s1, n1.start])
                # print(f"Added eps-transition from {n1.end} to {s1} and {n1.start}")
                print(f"{n1.end} ---eps---> {{{s1}, {n1.start}}}")
                txt_file.write(f"{n1.end} ---eps---> {{{s1}, {n1.start}}}\n")

                n1.end.isEnd = False

                if n1.end in self.finalStates:
                    self.finalStates.remove(n1.end)

                self.add_node(s0, s1)
                # print(f"Add node with start in {s0} and end in {s1}\n")

        self.alphabet = list(char_set)
        print(f"Alphabet: {self.alphabet}")

        self.startState = self.states.pop()
        print(f"Start state: {self.startState.start}")
        txt_file.write(f"\nStart state: {self.startState.start}\n")

        final_states = "Final states: "
        for state in self.finalStates:
            final_states += state.name + " "

        print(final_states, '\n')
        txt_file.write(final_states)

        txt_file.close()

        # вывод НКА в gv файл
        gv_file = open("nfa.gv", "w")
        gv_file.write("digraph G {\nrankdir = LR;\n")

        ind = 0
        state_array = [self.startState.start]
        while ind < len(state_array):
            current_state = state_array[ind]

            for eps_state in current_state.epsilon:
                gv_file.write('\t"' + str(current_state) + '"' + " -> " + '"' + str(eps_state) + '"[label="eps"];\n')
                if eps_state not in state_array:
                    state_array.append(eps_state)

            for char, state in current_state.transitions.items():
                gv_file.write('\t"' + str(current_state) + '"' + " -> " + '"' + str(state) + '"[label="' + str(char) + '"];\n')
                if state not in state_array:
                    state_array.append(state)

            ind += 1

        gv_file.write(f'\t"start" -> "{self.startState.start}";\n')

        for state in self.finalStates:
            gv_file.write(f'\t"{str(state)}" [shape="doublecircle"];\n')

        gv_file.write("}\n")
        gv_file.close()

        os.system("dot -Tsvg nfa.gv -o nfa.svg")
        os.system("explorer nfa.svg")

    def add_node(self, start, end):
        new_node = NodeGraph(start, end)

        self.finalStates.add(end)
        self.states.append(new_node)
        print(f"Append {new_node} in states\n")

    def create_state(self):
        new_state = State("s" + str(self.numberOfStates))
        print(f"Created state s{self.numberOfStates}")

        self.numberOfStates += 1
        return new_state