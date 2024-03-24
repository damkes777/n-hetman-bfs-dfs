import csv


class FileHelper:

    @staticmethod
    def save_as_txt(datas, file_path):
        with open(file_path, 'w') as file:
            for data in datas:
                file.write(str(data) + '\n')

    @staticmethod
    def save_as_csv(datas, file_path):
        columns = [
            'hetman_quantity',
            'solutions'
        ]

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

            for hetman_quantity, solutions in datas.items():
                for solution in solutions:
                    writer.writerow([hetman_quantity, solution])
