import re

syntax = ["am", "are", "don't", "that", "the", "a", "do", "does", "did", "to", "from", "as", "and"]


class FileAnalysis(object):
    # static variable class,set that stores the words without meaning
    syntax_word_set = set(syntax)

    def __init__(self, filename):
        self.__file_name = filename
        self.__file_obj = None
        self.__content = None  # the content file
        self.__dic = None  # dictionary, stores pair of: word, its number of instance in the file
        self.__openFile__()
        self.__words = re.split(r"\n+|\s+", self.__content)  # list of the all file's words
        self.__lines = self.__content.splitlines()  # list of the all file's lines
        self.__sentences = None  # list of the all file's sentences

    def __openFile__(self):
        """open the file and position the file's content in self.__content variable"""
        try:
            with open(self.__file_name, 'r', encoding="ISO-8859-1") as fd:
                self.__file_obj = fd
                # a generator that return the file's text char by char. prevents memory exception.
                gen = (ch for line in fd for ch in line)
                self.__content = ''.join(gen)
        except:
            print("Error with open file")
            exit(1)

    def countLines(self):
        """returns the number of the lines in the file """
        return len(self.__lines)

    def countWords(self):
        """returns the number of the words in the file """
        return len(self.__words)

    def countUniqueWords(self):
        """returns list of the unique words in the file """
        return len(set(self.__words))

    def __getSentences__(self):
        """inner function, return list of the sentences in the file """
        if not self.__sentences:
            self.__sentences = re.split('!|\\.|\\?|;', self.__content)
        return self.__sentences

    def longestSentence(self):
        """returns the length of th longest sentence in the file"""
        return max(map(lambda s: len(s), self.__getSentences__()), default=None)

    def averageSentence(self):
        """returns the average length of the sentences in the file"""
        return len(self.__content) / len(self.__getSentences__())

    def __getDic__(self):
        """inner function, return dictionary of the file's words and their number of occurrences"""
        if self.__dic is None:
            self.__dic = dict()
            for word in self.__words:
                self.__dic[word] = self.__dic.get(word, 0) + 1
        return self.__dic

    def popularWord(self):
        """returns the popular word in the file"""
        return max(self.__getDic__().items(), key=lambda item: item[1], default=('', 0))[0]

    def popularNoSyntaxWord(self):
        """returns the popular meaning word in the file"""
        return max(filter(lambda item: item[0] not in FileAnalysis.syntax_word_set, self.__getDic__().items()),
                   key=lambda item: item[1], default=('', 0))[0]

    def longestNoKSequence(self):
        """returns the longest sequence of chars without the "k" character from the file"""
        return max(map(lambda x: (len(x), x), re.split('k|K', self.__content)), key=lambda pair: pair[0],
                   default=None)[1]

    def max_number(self):
        """returns the max number that occurs in the file"""
        return max(re.findall(r"\d+", self.__content), default=None)

    def ToString(self):
        """returns a string with the results of all file analysis functions offered by the FileAnalysis class. """
        string = f"Number of lines: {self.countLines()} \n" \
                 f"Number of Words: {self.countWords()}\n" \
                 f"Unique Words: {self.countUniqueWords()}\n" \
                 f"Max length of the Sentences: {self.longestSentence()}\n" \
                 f"Average length of the Sentences: {self.averageSentence()}\n" \
                 f"Popular word: {self.popularWord()}\n" \
                 f"Popular NoSyntax Word: {self.popularNoSyntaxWord()}\n" \
                 f"Longest No K Sequence: {self.longestNoKSequence()}\n"\
                 f"Max number: {self.max_number()}"
        return string

    def CreateReport(self, resfile="report.txt"):
        """create report with all the statistics of the file"""
        with open(resfile, "w") as f:
            f.write(f"Statistics of {self.__file_name} file:")
            f.write(self.ToString())

