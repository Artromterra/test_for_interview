import sys
import os
import json
from typing import List


class DataHandler:
    def __init__(self, files: List[str], title: str = ''):
        self.files = files
        self.title = title
        self.reader_data = self._reader(self.files)

    @staticmethod
    def _reader(files) -> json:
        temp = {}
        result_list = []
        for name in files:
            path: str = os.path.join(os.path.abspath('data/'), name)
            with open(path, 'r') as f:
                data_list = [line.strip().split(',') for line in f]

            for i in range(1, len(data_list)):
                for j, key in enumerate(data_list[0]):
                     if key in ['hourly_rate', 'rate']:
                         temp['salary'] = data_list[i][j]
                     else:
                        temp[key] = data_list[i][j]
                result_list.append(temp)
                temp = {}
        return json.dumps(result_list)

    def payout(self) -> List[dict]:
        res_list = []
        data: dict = json.loads(self.reader_data)
        for item in data:
            salary: str = item.get('salary')
            hours: str = item.get('hours_worked')
            if self.title == 'payout':
                item[self.title] = str(int(salary) * int(hours))
            res_list.append(item)
        return res_list

    def print_console(self) -> str:
        print(f'________________________{self.title}____________________________')
        print(f'| department |    name         | hours  |  rate  | {self.title} |')
        print('__________________________________________________________\n')
        # проверка, что введено верное обозначение отчета
        if self.title == 'payout':
            for item in self.payout():
                print(
                    '| {:<10} | {:<15} | {:^6} | {:^6} | {:>5} |'.format(
                        item.get('department'),
                        item.get('name'),
                        item.get('hours_worked'),
                        item.get('salary'),
                        item.get(self.title))
                )
        else:
            for item in self.payout():
                print(
                    '| {:<10} | {:<15} | {:^6} | {:^6} |'.format(
                        item.get('department'),
                        item.get('name'),
                        item.get('hours_worked'),
                        item.get('salary'),
                    )
                )
        return '__________________________________________________________'


def main(arguments: List[str]) -> str | DataHandler:
    try:
        # args: List[str] = sys.argv
        # проверка, что присутствует команда и после команды есть наименование отчета
        if '--report' not in arguments or arguments[-1] == '--report':
            raise ValueError('You have no command (--report) or title in terminal command')
        for file in arguments[1:-2]:
            # проверка, что файл имеет расширение csv
            if file.split('.')[-1] != 'csv':
                raise TypeError('File is not "csv" file')
    except (ValueError, TypeError)  as e:
        print(e)
        return e
    else:
        res = DataHandler(files=arguments[1:-2], title=arguments[-1])
        print(res.print_console())
        return res


if __name__ == '__main__':
    args = sys.argv
    main(args)