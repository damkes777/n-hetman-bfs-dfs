from queue import Queue
from file_helper import FileHelper
from plot_helper import PlotHelper
import time


def prepare_data(n, intelligent_flag):
    time_start = time.time()
    hetman_problem = HetmanProblemBFS(n, intelligent_flag)
    time_end = time.time()

    final_time = round((time_end - time_start) * 1000, 2)
    solutions = hetman_problem.get_solution()
    visited = hetman_problem.get_visited()
    generated = hetman_problem.get_generated()

    return final_time, solutions, visited, generated


class HetmanProblemBFS:
    def __init__(self, n, intelligent_flag):
        self.n = n
        self.intelligent_flag = intelligent_flag

        self.visitedCounter = 0
        self.generatedCounter = 0
        self.solutions = []

        self.find_solutions()

    def get_solution(self):
        return self.solutions

    def get_generated(self):
        return self.generatedCounter

    def get_visited(self):
        return self.visitedCounter

    def find_solutions(self):
        queue = Queue()
        queue.put([])

        while not queue.empty():
            check = queue.get()
            self.visitedCounter += 1

            if len(check) < self.n:
                if self.intelligent_flag:
                    children = self.intelligent_generate_children(check)
                else:
                    children = self.generate_children(check)

                for child in children:
                    queue.put(child)

            if self.check_correct(check):
                self.solutions.extend([check])

        return

    def generate_children(self, parent):
        children = []

        for i in range(1, self.n + 1):
            self.generatedCounter += 1

            template_parent = parent.copy()
            template_parent.append(i)
            children.extend([template_parent])

        return children

    def intelligent_generate_children(self, parent):
        children = []

        for i in range(1, self.n + 1):
            template_parent = parent.copy()
            template_parent.append(i)

            if not len(set(template_parent)) == len(parent):
                self.generatedCounter += 1
                children.extend([template_parent])

        return children

    def check_correct(self, to_check):
        if not self.check_hetman(to_check):
            return False

        if not self.intelligent_flag:
            if not self.check_row(to_check):
                return False

        if not self.check_diagonal(to_check):
            return False

        return True

    def check_hetman(self, to_check):
        return len(to_check) == self.n

    @staticmethod
    def check_row(to_check):
        return len(to_check) == len(set(to_check))

    @staticmethod
    def check_diagonal(to_check):
        for i in range(len(to_check)):
            for j in range(i + 1, len(to_check)):
                if abs(to_check[i] - to_check[j]) == abs(i - j):
                    return False

        return True


data = []
for i in range(4, 9):
    time_for_n, solutions_for_n, visited_for_n, generated_for_n = prepare_data(i, False)
    data.append({
        'n': i,
        'time': time_for_n,
        'solutions': solutions_for_n,
        'visited': visited_for_n,
        'generated': generated_for_n
    })

times = [entry['time'] for entry in data]
visited = [entry['visited'] for entry in data]
generated = [entry['generated'] for entry in data]
solutions = {f"{entry['n']}_hetman": entry['solutions'] for entry in data}

data_intelligent = []
for i in range(4, 11):
    time_for_n, solutions_for_n, visited_for_n, generated_for_n = prepare_data(i, True)
    data_intelligent.append({
        'n': i,
        'time': time_for_n,
        'solutions': solutions_for_n,
        'visited': visited_for_n,
        'generated': generated_for_n
    })

times_intelligent = [entry['time'] for entry in data_intelligent]
visited_intelligent = [entry['visited'] for entry in data_intelligent]
generated_intelligent = [entry['generated'] for entry in data_intelligent]
solutions_intelligent = {f"{entry['n']}_hetman": entry['solutions'] for entry in data_intelligent}


file = FileHelper()
plot = PlotHelper()

file.save_as_txt(times, 'files/normal/times.txt')
file.save_as_txt(visited, 'files/normal/visited.txt')
file.save_as_txt(generated, 'files/normal/generated.txt')
file.save_as_csv(solutions, 'files/normal/solutions.csv')

plot.draw_plot(visited, 'Visited', 'n-hetman', 'visited', 4, 9, 'plots/normal/visited.png')
plot.draw_plot(generated, 'Generated', 'n-hetman', 'generated', 4, 9, 'plots/normal/generated.png')
plot.draw_plot(times, 'Times', 'n-hetman', 'times', 4, 9, 'plots/normal/times.png')


file.save_as_txt(times_intelligent, 'files/intelligent/times_intelligent.txt')
file.save_as_txt(visited_intelligent, 'files/intelligent/visited_intelligent.txt')
file.save_as_txt(generated_intelligent, 'files/intelligent/generated_intelligent.txt')
file.save_as_csv(solutions_intelligent, 'files/intelligent/solutions_intelligent.csv')

plot.draw_plot(visited_intelligent, 'Visited intelligent', 'n-hetman', 'visited', 4, 11, 'plots/intelligent/visited_intelligent.png')
plot.draw_plot(generated_intelligent, 'Generated intelligent', 'n-hetman', 'generated', 4, 11, 'plots/intelligent/generated_intelligent.png')
plot.draw_plot(times_intelligent, 'Times intelligent', 'n-hetman', 'times', 4, 11, 'plots/intelligent/times_intelligent.png')
