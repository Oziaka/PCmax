from time import time
from copy import deepcopy


class Algorithm:

    def __init__(self, numberOfThreads: int, taskLength: list[int], processMatrix: list[list[int]]):
        self.numberOfThreads: int = numberOfThreads
        self.tasksLength: list[int] = taskLength
        self.processMatrix: list[list[int]] = processMatrix

    def countMinTimeUnits(self) -> int:
        pass


class Silly(Algorithm):
    def __init__(self: Algorithm, numberOfThreads: int, taskLength: list[int], processMatrix: list[list[int]]):
        super().__init__(numberOfThreads, taskLength, processMatrix)

    def countMinTimeUnits(self) -> int:
        for i in self.tasksLength:
            index: int = 0
            minLength: int = sum(self.processMatrix[0])
            for j in range(1, len(self.processMatrix)):
                currentLength = sum(self.processMatrix[j])
                if minLength > currentLength:
                    index = j
                    minLength = currentLength
            self.processMatrix[index].append(i)
        tab: list[int] = []
        for i in self.processMatrix:
            tab.append(sum(i))
        return max(tab)


class Greedy(Algorithm):
    def __init__(self: Algorithm, numberOfThreads: int, taskLength: list[int], processMatrix: list[list[int]]):
        super().__init__(numberOfThreads, taskLength, processMatrix)

    def addTaskToThreadInProcessMatrix(self: Algorithm, numberOfThread: int, taskLength: int) -> list[list[int]]:
        processMatrix: list[list[int]] = deepcopy(self.processMatrix)
        processMatrix[numberOfThread].append(taskLength)
        return processMatrix

    def countMinTimeUnits(self) -> int:
        tab2: list[int] = []
        if not self.tasksLength:
            tab: list[int] = []
            for i in self.processMatrix:
                tab.append(sum(i))
            return max(tab)
        else:
            for i in range(self.numberOfThreads):
                for j in range(len(self.tasksLength)):
                    tab2.append(Greedy(self.numberOfThreads,
                                       self.tasksLength[:j] + self.tasksLength[j + 1:],
                                       self.addTaskToThreadInProcessMatrix(i,
                                                                           self.tasksLength[j])).countMinTimeUnits())
        return min(tab2)


def solveAndPrint(clazz: __build_class__ == Greedy, filename: str = "data.txt"):
    lines = open(filename).readlines()
    numberOfThreads = int(lines[0])
    taskLength = list(map(int, lines))[2:]
    processMatrix = [list() for x in range(numberOfThreads)]
    algorithm: Algorithm = clazz(numberOfThreads, taskLength, processMatrix)
    print("Algorithm name: {}".format(algorithm.__class__.__name__))
    print("Number of threads: {}".format(algorithm.numberOfThreads))
    print("Tasks length: {}".format(algorithm.tasksLength))
    start: float = time()
    minimalTimeUnits: int = algorithm.countMinTimeUnits()
    end: float = time()
    print("Minimal time units: {}".format(minimalTimeUnits))
    print("Execution time {}".format(end - start))
    print("---------------------------------")


def main():
    print("Running finding minimal units time")
    print("---------------------------------")
    solveAndPrint(Greedy, "data2.txt")
    solveAndPrint(Silly, "data2.txt")


main()
