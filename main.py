import sys
import json
from typing import List


class DataHandler:
    def __init__(self, files: list, title: str = None):
        self.files = files
        self.title = title
        self.reader_data = self.reader(self.files)

    def reader(self, files) -> json:
        temp = {}
        result_list = []
        # TODO: добавить проверку на ввод пользователя в терминале
        for file in files:
            with open(file, 'r') as f:
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
            item[self.title] = str(int(salary) * int(hours))
            res_list.append(item)
        return res_list

    def print_console(self) -> str:
        # print(self.payout())
        print(f'________________________{self.title}____________________________')
        print('| department |    name         | hours  |  rate  | payout |')
        print('__________________________________________________________\n')
        for item in self.payout():
            print(
                '| {:<10} | {:<15} | {:^6} | {:^6} | {:>5} |'.format(
                    item.get('department'),
                    item.get('name'),
                    item.get('hours_worked'),
                    item.get('salary'),
                    item.get(self.title))
            )
        return '__________________________________________________________'


if __name__ == '__main__':
    # print(sys.argv)
    res = DataHandler(files=sys.argv[1:-2], title=sys.argv[-1])
    print(res.print_console())