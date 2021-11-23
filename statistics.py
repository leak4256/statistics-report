import re
from colors import colors
noMeaning = ["am", "are", "don't", "that", "the", "a", "do", "does", "did", "to", "from", "as", "and", "of"]

start = '^'
end = '$'


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
        except Exception as err:
            raise Exception(f"Error with open file, {err}")

    def __getWords__(self):
        """inner function, returns list of the words in the file"""
        if self.__words is None:
            self.__words = re.split(r"\W+", self.__content)
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
        ln = len(self.__getSentences__())
        if ln > 0:
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
        # temp = ''
        # maxi = None
        # for word in self.__getWords__():
        #     if (word_to_num(word) or word == 'point') and not word.isdigit():
        #         temp = temp + word
        #     else:
        #         if maxi is None or word_to_num(temp) > maxi:
        #             maxi = word_to_num(temp)
        #         temp = ''
        #     if word.isdigit():
        #         if int(word) > maxi:
        #             maxi = int(word)
        # return maxi
        return max((int(x) for x in re.findall(r"\d+", self.__content)), default=None)

    def countColors(self):
        """return the number of the instances of each color in the file """
        colors_dic = dict()
        for word in self.__getWords__():
            if word in colors:
                colors_dic[word.lower()] = colors_dic.get(word.lower(), 0) + 1
        st = ""
        for item in colors_dic.items():
            st = st + f"{start}{item[0]}{end} occur {item[1]} times\n"
        return st


    def ToString(self):
        """returns a string with the results of all file analysis functions offered by the Statistics class. """
        string = f"{start}Number of lines:{end} {self.countLines()}\n\n" \
                 f"{start}Number of Words:{end} {self.countWords()}\n\n" \
                 f"{start}Unique Words:{end} {self.countUniqueWords()}\n\n" \
                 f"{start}Max length of the Sentences:{end} {self.longestSentence()}\n\n" \
                 f"{start}Average length of the Sentences:{end} {self.averageSentence()}\n\n" \
                 f"{start}Popular word:{end} {self.popularWord()}\n\n" \
                 f"{start}Popular NoSyntax Word:{end} {self.popularNoSyntaxWord()}\n\n" \
                 f"{start}Longest No K Sequence:{end} {self.longestNoKSequence()}\n\n" \
                 f"{start}Max number:{end} {self.max_number()}\n\n"\
                 f"{start}quantity of the instances of each color:{end}\n{self.countColors()}"
        return string


def CreateReportHtml(src_file):
    """return string in html format with all the statistics of the file"""
    statistics = Statistics(src_file)
    return statistics.ToString().replace(start, '<b>').replace(end, '</b>').replace('\n', '<br>')


def CreateReportFile(src_file, res_file="report.txt"):
    """create report file with all the statistics of the file"""
    try:
        statistics = Statistics(src_file)
        with open(res_file, "w") as f:
            f.write(f"Statistics-report {src_file}:\n\n")
            st = statistics.ToString().replace(start, '').replace(end, '')
            f.write(st)
            return res_file
    except Exception as e:
        raise Exception("Problem with create report", e)

