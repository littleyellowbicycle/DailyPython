import xlrd
import xml.dom.minidom as md
from collections import OrderedDict


def GetFileFromExcel(filepath):
    wb = xlrd.open_workbook(filepath)
    ws = wb.sheet_by_index(0)
    content = OrderedDict()
    for i in range(ws.nrows):
        content[i + 1] = ws.row_values(i)[1:]
    return content
    pass


def WriteToXml(content):
    xmlfile = md.Document()
    root = xmlfile.createElement('root')
    student = xmlfile.createElement('student')
    xmlfile.appendChild(root)
    root.appendChild(student)

    comment = xmlfile.createComment("学生信息表 'id' : [名字, 数学, 语文, 英文]")
    student.appendChild(comment)
    xmlcontent = xmlfile.createTextNode(str(content))
    student.appendChild(xmlcontent)

    with open("./student.xml", "wb") as f:
        f.write(xmlfile.toprettyxml(encoding="utf-8"))  #写入文件
    pass


if __name__ == "__main__":
    filepath = "./student.xls"
    content = GetFileFromExcel(filepath)
    WriteToXml(content)
    pass