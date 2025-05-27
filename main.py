import sys


class DataHandler:
    def __init__(self, files: list, title: str = None):
        self.files = files
        self.title = title
        self.reader_data = self.reader(self.files)

    def reader(self, files):
        temp = {}
        result_list = []

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
        return result_list

    def payout(self):
        res_list = []
        for _dict in self.reader_data:
            salary = _dict.get('salary')
            hours = _dict.get('hours_worked')
            _dict[self.title] = str(int(salary) * int(hours))
            res_list.append(_dict)
        return res_list

    def __str__(self):
        print(self.payout())
        print('department        name            hours    rate     payout\n')
        for _dict in self.payout():
            print(f'{_dict.get("department")}     '
                  f'{_dict.get("name")}        '
                  f'{_dict.get("hours_worked")}     '
                  f'{_dict.get("salary")}        ' 
                  f'{_dict.get(self.title)}')
        # return (
        #         f'{self.payout()[0].get("department")}     '
        #         f'{self.payout()[0].get("name")}        '
        #         f'{self.payout()[0].get("hours_worked")}     '
        #         f'{self.payout()[0].get("salary")}        '
        #         f'{self.payout()[0].get(self.title)}\n'
        #         )




if __name__ == '__main__':
    print(sys.argv)
    res = DataHandler(files=sys.argv[1:-2], title=sys.argv[-1])
    print(res)