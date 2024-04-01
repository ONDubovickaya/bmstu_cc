from graph import *
import os


class DFA:
    def __init__(self, nfa):
        # состояния НКА
        self.states = nfa.states

        # начальное состояние НКА
        self.startState = nfa.startState.start
        # финальные состояния НКА
        self.finalStates = nfa.finalStates

        # алфавит
        self.alphabet = nfa.alphabet

        self.startStatesSet = set()
        self.startStates = {nfa.startState.start}

    def current_info(self):
        print(self.alphabet)
        print(self.states)
        # print(self.numberOfStates)
        print(self.startState)
        print(self.startStates)
        for state in self.finalStates:
            print(state)

    def dfa_build(self):
        print("~~~ BUILDING DFA ~~~")

        # вычислим eps-замыкание для начального состояния
        epsilon_closure = list(self.define_closure(self.startState))

        # инициализация списка объединённых состояний
        # в пустой список добавляем множество epsilon_closure
        union_states = [set(epsilon_closure)]

        index = 0
        new_transitions = []

        while index < len(union_states):
            print(f"\n< Index: {index} >")

            union = " "
            for uni in union_states[index]:
                union += str(uni) + " "

            print(f"DFA 's{index}' equals NFA: {{{union}}}")

            # создание нового перехода для каждого символа алфавита
            # создаём словарь, где ключам (символам алфавита) сопоставляются пустые строки
            new_transition = {char: [] for char in self.alphabet}

            # вычисление eps-замыкания текущего состояния из union_states[index]
            epsilon_closure = list(union_states[index])

            # для каждого перехода в текущем состоянии проверим наличие переходов
            # для каждого символа алфавита
            print("~~~")
            for i in range(len(epsilon_closure)):
                # char -- ключ, value -- значение
                for char, value in epsilon_closure[i].transitions.items():
                    new_transition[char].append(value)
                    print(f"(from {epsilon_closure[i]}) By '{char}' can reach {value} ")

            print("~~~")
            for char, value in new_transition.items():
                print(f"Trans by '{char}':")
                if len(value) == 0:
                    continue

                new_state = []

                for i in range(len(value)):
                    epsilon_closure = list(self.define_closure(value[i]))
                    new_state.extend(epsilon_closure)

                new_transition[char] = new_state

                if set(new_state) not in union_states:
                    # добавляем в union_states множество new_states
                    union_states.append(set(new_state))

                    str_new_state = " "
                    for state in set(new_state):
                        str_new_state += str(state) + " "
                    print(f"In union_states for '{char}' append: {{{str_new_state}}}")
                else:
                    print(f"Already in union_states for '{char}'")
                print("~~~")

            new_transitions.append(new_transition)
            print(f"<<for s{index} in DFA>> there are transitions:")

            for key, value in new_transition.items():
                print(f"By {key}:")
                states = " "
                for state in value:
                    states += str(state) + " "
                print(f"{{{states}}}")

            index += 1

        print("\n~ RESULTS ~")
        result_states = [State("s" + str(i)) for i in range(len(union_states))]

        result = " "
        for state in result_states:
            result += str(state) + " "
        print(f"States of DFA: {{{result}}}\n")

        # correct extreme states
        for i in range(len(union_states)):
            # если множества finalStates и union_states пересекаются
            if not self.finalStates.isdisjoint(union_states[i]):
                result_states[i].isEnd = True
                print(f"{result_states[i]} added to final states")
            # если множества startStates и union_states пересекаются
            if not self.startStates.isdisjoint(union_states[i]):
                result_states[i].isStart = True
                print(f"{result_states[i]} added to start states")

        # define transitions
        print(f"\n~ Transitions of DFA ~")
        txt_file = open("dfa.txt", "w")

        gv_file = open("dfa.gv", "w")
        gv_file.write("digraph G {\nrankdir = LR;\n")

        for i in range(len(new_transitions)):
            for char, union_state in new_transitions[i].items():
                if len(union_state) == 0:
                    continue

                index_of_state = union_states.index(set(union_state))
                result_states[i].transitions[char] = result_states[index_of_state]
                print(f"{result_states[i]} ---{char}---> {result_states[index_of_state]}")
                txt_file.write(f"{result_states[i]} ---{char}---> {result_states[index_of_state]}\n")
                gv_file.write('\t"' + str(result_states[i]) + '"' + " -> " + '"' + str(result_states[index_of_state]) +
                              '"[label="' + str(char) + '"];\n')

        # define start states
        for i in range(len(result_states)):
            if result_states[i].isStart:
                self.startStatesSet.add(result_states[i])

        start_states = " "
        for state in self.startStatesSet:
            start_states += str(state) + " "
            txt_file.write(f"\nStart state: {state}\n")
            gv_file.write(f'\t"start" -> "{str(state)}"\n')
        print(f"\nStart states: {start_states}")

        final_states = " "

        for i in range(len(result_states)):
            if result_states[i].isEnd:
                self.finalStates.add(result_states[i])
                final_states += str(result_states[i]) + " "
                gv_file.write(f'\t"{str(result_states[i])}" [shape="doublecircle"];\n')
        print(f"Final states: {final_states}")
        txt_file.write(f"Final states:{final_states}")

        gv_file.write("}\n")
        gv_file.close()

        txt_file.close()

        os.system("dot -Tsvg dfa.gv -o dfa.svg")
        os.system("explorer dfa.svg")

    # определение eps-замыкания для данного состояния
    def define_closure(self, state):
        epsilon_closure = set()
        self.define_closure_recursive(state, epsilon_closure)

        eps_clos = " "
        for epsilon in epsilon_closure:
            eps_clos += str(epsilon) + " "
        print(f"Eps-closure for state {state}: {{{eps_clos}}}")

        return epsilon_closure

    # рекурсивное вычисление eps-замыкания для данного состояния
    def define_closure_recursive(self, state, epsilon_closure):
        if state in epsilon_closure:
            return

        epsilon_closure.add(state)

        for eps in state.epsilon:
            self.define_closure_recursive(eps, epsilon_closure)

    # минимизация ДКА по алгоритму Бржозовского
    def dfa_minimize(self):
        print("\n~~~ MINIMIZE DFA ~~~")
        print("~ First reverse ~")
        # inv -- словарь для хранения инвертированных переходов по состояниям
        # states -- все состояния
        inv_trans, all_states = self.first_reverse()

        new_start, not_start = self.get_states_role(all_states)
        reverse_states = [new_start, not_start]

        print("\n~ First determine ~")
        for i in range(len(reverse_states)):
            print(f"< reverse_states[{i}]: >")
            for state in reverse_states[i]:
                print(f"<<< {state}")

        queue, determ_states = self.first_determine(reverse_states)

        print("\n~ Second reverse ~")
        self.second_reverse(reverse_states, inv_trans, queue, determ_states)

        print("\n~ Second determine ~")
        self.second_determine(reverse_states, inv_trans)

    def first_reverse(self):
        # словарь для хранения инвертированного отображения состояний
        inv = {}

        current_states = self.startStatesSet

        # пустое мн-во для отслеживания уже посещённых состояний
        used_states = set()

        # пока current_states не станут пустыми
        while current_states != set():
            next_states = set()
            print("*****")
            for state in current_states:
                used_states.add(state)
                print(f"* {state} added in used_states")
                print("*****")

                for char in state.transitions.keys():
                    trans_state = state.transitions[char]

                    if trans_state not in inv:
                        inv[trans_state] = {char: [] for char in self.alphabet}

                    inv[trans_state][char].append(state)
                    print("Inverse:")
                    print(f"{state} <---{char}--- {trans_state}")

                    if trans_state not in used_states:
                        print(f"{trans_state} not in used_states yet")
                        next_states.add(trans_state)
                        print(f"{trans_state} added in next_states")
                print("*****")

            current_states = next_states

        return inv, list(used_states)

    # разбиение состояний на финальные и не финальные
    def get_states_role(self, used_states):
        new_start = set()
        not_start = set()

        for state in used_states:
            if state.isEnd:
                new_start.add(state)
            else:
                not_start.add(state)

        start_str = " "
        for state in new_start:
            start_str += str(state) + " "
        print(f"New start states: {{{start_str}}}")

        not_start_str = " "
        for state in not_start:
            not_start_str += str(state) + " "
        print(f"Not start states: {{{not_start_str}}}")

        return new_start, not_start

    # построение очереди и словаря, отображающего состояния в их эквивалентные классы
    def first_determine(self, reverse_states):
        queue = []

        # словарь для отображения состояний в соответствующие им эквивалентные классы
        determ_states = {}

        for i in range(len(reverse_states)):
            print(f"< Class {i} >")
            for char in self.alphabet:
                # создание очереди для символов алфавита
                queue.append([i, char])

            for state in reverse_states[i]:
                determ_states[state] = i
                print(f"determ_states[{state}] = {i}")

        print(f"\nQueue [№ of class, char]: {queue}")

        return queue, determ_states

    # обратное объединение эквивалентных классов состояний
    def second_reverse(self, reverse_states, inv_trans, queue, determ_states):
        print("Before second reverse:")
        for st in reverse_states:
            print("{" + ", ".join(str(item) for item in st) + "}")

        print("~~~")

        while len(queue) > 0:
            state_class, char = queue.pop()

            involved = {}

            for state in reverse_states[state_class]:
                if state not in inv_trans:
                    continue

                for st in inv_trans[state][char]:
                    # получаем номер класса состояния st
                    i = determ_states[st]

                    if i not in involved:
                        # устанавливаем пустое мн-во для класса i
                        involved[i] = set()

                    involved[i].add(st)

            # reverse переходов состояний
            for i in involved:
                if len(list(involved[i])) < len(list(reverse_states[i])):
                    # добавляем в reverse_states пустое мн-во
                    reverse_states.append(set())
                    j = len(reverse_states) - 1

                    for r_state in involved[i]:
                        reverse_states[i].remove(r_state)
                        reverse_states[j].add(r_state)
                        print(f"RS : {r_state} in class {j}")
                    print("~~~")

                    if len(list(reverse_states[j])) > len(list(reverse_states[i])):
                        reverse_states[j], reverse_states[i] = reverse_states[i], reverse_states[j]

                    for r_state in reverse_states[j]:
                        determ_states[r_state] = j
                        print(f"DS : {r_state} in class {j}")
                    print("~~~")

                    for char in self.alphabet:
                        queue.append([j, char])
                        print(f"In queue append [{j}, {char}]")
                    print("~~~")

        print("\nAfter second reverse:")
        for st in reverse_states:
            print("{" + ", ".join(str(item) for item in st) + "}")

        for idx in determ_states.keys():
            print(f"State {idx} in class {determ_states[idx]}")

    # определение эквивалентных состояний и уменьшение числа состояний в автомате
    def second_determine(self, reverse_states, inv_trans):
        for i in range(len(reverse_states)):
            print(f"< Class {i} >")
            similar_states = list(reverse_states[i])
            for state in similar_states:
                print(state)

            if len(similar_states) <= 1:
                print(f"In class {i} only 1 element\n")
                continue

            keep_state = similar_states[0]

            for q in similar_states:
                # если q и начало, и конец одновременно
                if q.isStart and q.isEnd:
                    keep_state = q
                    print(f"{q} is start and end\n")
                    break

                # q или начало, или конец
                if q.isStart or q.isEnd:
                    keep_state = q
                    if q.isStart:
                        print(f"{q} is start\n")
                    if q.isEnd:
                        print(f"{q} is end\n")

            for q in similar_states:
                # если q это keep_state -- пропускаем
                if q == keep_state:
                    continue

                for char in inv_trans[q]:
                    for st in inv_trans[q][char]:
                        st.transitions[char] = keep_state
                        print(f"Remove {st} ---{char}---> {q}")

                        if st == q:
                            print(f"Add {keep_state} ---{char}---> {keep_state}\n")
                        else:
                            print(f"Add {st} ---{char}---> {keep_state}\n")

    def output_dfa(self):
        txt_file = open("miniDfa.txt", "w")

        gv_file = open("miniDfa.gv", "w")
        gv_file.write("digraph G {\nrankdir = LR;\n")

        cur_states = self.startStatesSet
        used_states = set()
        while cur_states != set():
            next_states = set()

            for state in cur_states:
                used_states.add(state)
                for key, value in state.transitions.items():
                    txt_file.write(f"{str(state)} ---{str(key)}---> {str(value)}\n")
                    gv_file.write('\t"' + str(state) + '"' + " -> " + '"' + str(value) + '"[label="' + str(key) + '"];\n')
                    if value not in used_states:
                        next_states.add(value)
            cur_states = next_states

        for state in used_states:
            if state.isStart:
                gv_file.write(f'\t"start" -> "{str(state)}"\n')

        for state in used_states:
            if state.isEnd:
                gv_file.write(f'\t"{str(state)}" [shape="doublecircle"];\n')

        gv_file.write("}\n")
        gv_file.close()

        txt_file.close()

        os.system("dot -Tsvg miniDfa.gv -o miniDfa.svg")
        os.system("explorer miniDfa.svg")

    def modeling(self, string):
        print(f"\n~~~ MODELING FA FOR {string} ~~~")
        current_state = self.startStatesSet

        start_str = ""
        for st in current_state:
            start_str += str(st) + " "

        print(f"Now you are in {start_str}\n")

        for symbol in string:
            next_states = set()

            for state in current_state:
                if symbol in state.transitions.keys():
                    print(f">> You can move by {symbol} from {state}")
                    next_states.add(state.transitions[symbol])

                    ns_str = " "
                    for st in next_states:
                        ns_str += str(st) + " "
                    print(f"   Next state: {ns_str}\n")

            current_state = next_states

        for state in current_state:
            if state.isEnd:
                print("Current state is final")
                print(f"[ Successful operation ^^ ]")
                return True

            print("Current state isn't final")
            print(f"[ Failed.. ]")
            return False

