class State:
    def __init__(self, name):
        self.name = name
        self.epsilon = []
        self.transitions = {}

        self.isEnd = False
        self.isStart = False

    def __str__(self):
        return self.name


class NodeGraph:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        end.isEnd = True

    def __str__(self):
        return f"NodeGraph({self.start} -> {self.end})"