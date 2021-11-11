import re

noMeaning = ["am", "are", "don't", "that", "the", "a", "do", "does", "did", "to", "from", "as", "and"]


class Statistics(object):
    # static variable class,set that stores the words without meaning
    noMeaning_set = set(noMeaning)

    def __init__(self, filename):
        self.__content = None  # the content file
        self.__dic = None  # dictionary, stores pair of: word, its number of instance in the file
        self.__openFile__(filename)
        self.__words = None  # list of the all file's words
        self.__lines = None  # list of the all file's lines
        self.__sentences = None  # list of the all file's sentences

    def __openFile__(self, filename):
        """open the file and position the file's content in self.__content variable"""
        try:
            with open(filename, 'r', encoding="ISO-8859-1") as fd:
                self.__content = ''.join([line for line in fd])
        except:
            print("Error with open file")
            exit(1)

    def __getWords__(self):
        """inner function, returns list of the words in the file"""
        if self.__words is None:
            re.split(r"\W+", self.__content)
        return self.__words

    def __getLines__(self):
        """inner function, returns list of the lines in the file """
        if self.__lines is None:
            self.__lines = self.__content.splitlines()
        return self.__lines

    def countLines(self):
        """returns the number of the lines in the file """
        return len(self.__getLines__())

    def countWords(self):
        """returns the number of the words in the file """
        return len(self.__getWords__())

    def countUniqueWords(self):
        """returns list of the unique words in the file """
        return len(set((w.lower() for w in self.__getWords__())))

    def __getSentences__(self):
        """inner function, return list of the sentences in the file """
        if not self.__sentences:
            self.__sentences = re.findall(r"[A-Z].*?[\.!?]", self.__content, re.DOTALL)
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
            # create dictionary
            self.__dic = dict()
            # Go through all the words in the file
            # converts each word to its lowercase
            # increases the value of the word
            for word in self.__getWords__():
                word = word.lower()
                self.__dic[word] = self.__dic.get(word, 0) + 1
        return self.__dic

    def popularWord(self):
        """returns the popular word in the file"""
        return max(self.__getDic__().items(), key=lambda item: item[1], default=('', 0))[0]

    def popularNoSyntaxWord(self):
        """returns the popular meaning word in the file"""
        return max(filter(lambda item: item[0] not in Statistics.noMeaning_set, self.__getDic__().items()),
                   key=lambda item: item[1], default=('', 0))[0]

    def longestNoKSequence(self):
        """returns the longest sequence of chars without the "k" character from the file"""
        return max(map(lambda x: (len(x), x), re.split('k|K', self.__content)), key=lambda pair: pair[0],
                   default=None)[1]

    def max_number(self):
        """returns the max number that occurs in the file"""
        return max((int(x) for x in re.findall(r"\d+", self.__content)), default=None)

    def ToString(self):
        """returns a string with the results of all file analysis functions offered by the Statistics class. """
        string = f"Number of lines: {self.countLines()} \n" \
                 f"Number of Words: {self.countWords()}\n" \
                 f"Unique Words: {self.countUniqueWords()}\n" \
                 f"Max length of the Sentences: {self.longestSentence()}\n" \
                 f"Average length of the Sentences: {self.averageSentence()}\n" \
                 f"Popular word: {self.popularWord()}\n" \
                 f"Popular NoSyntax Word: {self.popularNoSyntaxWord()}\n" \
                 f"Longest No K Sequence: {self.longestNoKSequence()}\n" \
                 f"Max number: {self.max_number()}"
        return string

    def CreateReport(self, desfile):
        """create report with all the statistics of the file"""
        if not desfile:
            desfile = "report.txt"
        with open(desfile, "w") as f:
            f.write(f"Statistics of {self.__file_name} file:")
            f.write(self.ToString())

