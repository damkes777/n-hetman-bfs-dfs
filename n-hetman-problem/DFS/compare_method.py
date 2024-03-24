from plot_helper import PlotHelper


class CompareMethod:
    @staticmethod
    def get_generated():
        data = []
        with open('files/normal/generated.txt', 'r') as file:
            for line in file:
                data.append(int(line.strip()))

        return data

    @staticmethod
    def get_generated_intelligent():
        data = []
        with open('files/intelligent/generated_intelligent.txt', 'r') as file:
            for line in file:
                data.append(int(line.strip()))

        return data

    @staticmethod
    def get_visited():
        data = []
        with open('files/normal/visited.txt', 'r') as file:
            for line in file:
                data.append(int(line.strip()))

        return data

    @staticmethod
    def get_visited_intelligent():
        data = []
        with open('files/intelligent/visited_intelligent.txt', 'r') as file:
            for line in file:
                data.append(int(line.strip()))

        return data

    @staticmethod
    def get_times():
        data = []
        with open('files/normal/times.txt', 'r') as file:
            for line in file:
                data.append(float(line.strip()))

        return data

    @staticmethod
    def get_times_intelligent():
        data = []
        with open('files/intelligent/times_intelligent.txt', 'r') as file:
            for line in file:
                data.append(float(line.strip()))

        return data


compare_method = CompareMethod()

generated_normal = CompareMethod.get_generated()
generated_intelligent = CompareMethod.get_generated_intelligent()

visited_normal = CompareMethod.get_visited()
visited_intelligent = CompareMethod.get_visited_intelligent()

times_normal = CompareMethod.get_times()
times_intelligent = CompareMethod.get_times_intelligent()

plot = PlotHelper()
plot.draw_compare_plot(generated_normal, generated_intelligent, 'Normal vs intelligent', 'n-hetman', 'generated', 'plots/compare/generated_compare.png')
plot.draw_compare_plot(visited_normal, visited_intelligent, 'Normal vs intelligent', 'n-hetman', 'visited', 'plots/compare/visited_compare.png')
plot.draw_compare_plot(times_normal, times_intelligent, 'Normal vs intelligent', 'n-hetman', 'times', 'plots/compare/timed_compare.png')

