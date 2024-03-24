from plot_helper import PlotHelper
from file_helper import FileHelper

file = FileHelper()

generated_normal_dfs = file.get_int_data_from_file('../DFS/files/normal/generated.txt')
generated_intelligent_dfs = file.get_int_data_from_file('../DFS/files/intelligent/generated_intelligent.txt')

visited_normal_dfs = file.get_int_data_from_file('../DFS/files/normal/visited.txt')
visited_intelligent_dfs = file.get_int_data_from_file('../DFS/files/intelligent/visited_intelligent.txt')

times_normal_dfs = file.get_float_data_from_file('../DFS/files/normal/times.txt')
times_intelligent_dfs = file.get_float_data_from_file('../DFS/files/intelligent/times_intelligent.txt')

generated_normal_bfs = file.get_int_data_from_file('../BFS/files/normal/generated.txt')
generated_intelligent_bfs = file.get_int_data_from_file('../BFS/files/intelligent/generated_intelligent.txt')

visited_normal_bfs = file.get_int_data_from_file('../BFS/files/normal/visited.txt')
visited_intelligent_bfs = file.get_int_data_from_file('../BFS/files/intelligent/visited_intelligent.txt')

times_normal_bfs = file.get_float_data_from_file('../BFS/files/normal/times.txt')
times_intelligent_bfs = file.get_float_data_from_file('../BFS/files/intelligent/times_intelligent.txt')

plot = PlotHelper()
# <--- dfs normal vs intelligent plot --->
plot.draw_compare_plot(generated_normal_dfs,
                       generated_intelligent_dfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'generated',
                       '../DFS/plots/compare/generated_compare.png',
                       'normal',
                       'intelligent')

plot.draw_compare_plot(visited_normal_dfs,
                       visited_intelligent_dfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'visited',
                       '../DFS/plots/compare/visited_compare.png',
                       'normal',
                       'intelligent')

plot.draw_compare_plot(times_normal_dfs,
                       times_intelligent_dfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'times',
                       '../DFS/plots/compare/times_compare.png',
                       'normal',
                       'intelligent')
# <--- bfs normal vs intelligent plot --->
plot.draw_compare_plot(generated_normal_bfs,
                       generated_intelligent_bfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'generated',
                       '../BFS/plots/compare/generated_compare.png',
                       'normal',
                       'intelligent')

plot.draw_compare_plot(visited_normal_bfs,
                       visited_intelligent_bfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'visited',
                       '../BFS/plots/compare/visited_compare.png',
                       'normal',
                       'intelligent')

plot.draw_compare_plot(times_normal_bfs,
                       times_intelligent_bfs,
                       'Normal vs intelligent',
                       'n-hetman',
                       'times',
                       '../BFS/plots/compare/times_compare.png',
                       'normal',
                       'intelligent')
# <--- bfs vs dfs normal --->
plot.draw_compare_plot(generated_normal_bfs,
                       generated_normal_dfs,
                       'Normal bfs vs dfs',
                       'n-hetman',
                       'generated',
                       '../compare/generated_compare.png',
                       'bfs',
                       'dfs')

plot.draw_compare_plot(visited_normal_bfs,
                       visited_normal_dfs,
                       'Normal bfs vs dfs',
                       'n-hetman',
                       'visited',
                       '../compare/visited_compare.png',
                       'bfs',
                       'dfs')

plot.draw_compare_plot(times_normal_bfs,
                       times_normal_dfs,
                       'Normal bfs vs dfs',
                       'n-hetman',
                       'times',
                       '../compare/times_compare.png',
                       'bfs',
                       'dfs')
# <--- Intelligent bfs vs dfs --->
plot.draw_compare_plot(generated_intelligent_bfs,
                       generated_intelligent_dfs,
                       'Intelligent bfs vs dfs',
                       'n-hetman',
                       'generated',
                       '../compare/generated_intelligent_compare.png',
                       'bfs',
                       'dfs')

plot.draw_compare_plot(visited_intelligent_bfs,
                       visited_intelligent_dfs,
                       'Intelligent bfs vs dfs',
                       'n-hetman',
                       'visited',
                       '../compare/visited_intelligent_compare.png',
                       'bfs',
                       'dfs')

plot.draw_compare_plot(times_intelligent_bfs,
                       times_intelligent_dfs,
                       'Intelligent bfs vs dfs',
                       'n-hetman',
                       'times',
                       '../compare/times_intelligent_compare.png',
                       'bfs',
                       'dfs')




