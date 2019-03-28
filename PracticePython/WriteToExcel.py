import json
import xlwt
import os
from collections import OrderedDict


def write(file, path):
    if (os.path.isfile(file)):
        with open(file, encoding="utf-8") as f:
            student_dict = OrderedDict(json.load(f))
            wb = xlwt.Workbook(encoding="ascii")
            ws = wb.add_sheet("student")
            row = 0
            for k, v in student_dict.items():
                ws.write(row, 0, k)
                col = 1
                for item in v:
                    ws.write(row, col, item)
                    col += 1
                row += 1
            wb.save(path)
    else:
        print("file is no exist")


if __name__ == "__main__":
    file = "student.txt"
    path = "student.xls"
    write(file, path)
    pass
