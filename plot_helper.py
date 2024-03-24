import matplotlib.pyplot as plt


class PlotHelper:

    @staticmethod
    def draw_plot(data, title, x_label, y_label, start_range, end_range, path):
        plt.close('all')
        n_range = range(start_range, end_range)

        plt.plot(n_range, data, marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.savefig(path)
        plt.show()


    @staticmethod
    def draw_compare_plot(a_data, b_data, title, x_label, y_label, path):
        plt.close('all')

        plt.plot(a_data, label='Normal')
        plt.plot(b_data, label='Intelligent')

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.legend()
        plt.savefig(path)
        plt.show()

