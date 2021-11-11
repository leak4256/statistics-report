
from FileAnalysis import Statistics

if __name__ == '__main__':
    source_file = input("Enter file name\n")
    dest_file = input("Enter file name for report(optional)\n")
    fileAnalysis = Statistics(source_file)
    fileAnalysis.CreateReport(dest_file)
    # print("count word",fileAnalysis.countLines())
    # print("count word", fileAnalysis.countWords())
    # print("count word", fileAnalysis.countUniqueWords())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
