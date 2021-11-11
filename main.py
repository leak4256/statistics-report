
from FileAnalysis import FileAnalysis

if __name__ == '__main__':
    source_file = input("Enter file name\n")
    fileAnalysis = FileAnalysis(source_file)
    dest_file = input("Enter file name for report\n")
    if dest_file:
        fileAnalysis.CreateReport(dest_file)
    else:
        print(fileAnalysis.ToString())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
