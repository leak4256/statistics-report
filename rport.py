# import re
#
# syntax = ["am", "are", "don't", "that", "the", "a", "do", "does", "did", "to", "from"]
#
#
#
# # def ReadFile():
# #     with open('dickens.txt', 'r', encoding="ISO-8859-1") as fd:
# #         content = ''.join(gen(fd))
# #     lines = content.splitlines()
# #     words = content.split()
#
#
#     #
#     # num_lines = len(lines)
#     # num_words = len(words)
#     # num_unique_word = len(set(words))
#     # sentences = re.split('!|\\.|\\?|;', content)
#     # max_sentence = max(map(lambda s: len(s), sentences))
#     # average_sentence = len(content) / len(sentences)
#     #
#     # print(f"max_sentence{max_sentence}",end="\n")
#     # print(f"average_sentence{average_sentence}",end="\n" )
#     # print(f"num_unique_word{num_unique_word}", end="\n")
#
#     dic = dict()
#
#     for word in words:
#         dic[word] = dic.get(word, 0) + 1
#
#     popular_word = max(dic)
#     #
#     # if popular_word not in syntax_word_set:
#     #     popular_no_syntax_word = popular_word
#     # else:
#     #     popular_no_syntax_word = max(filter(lambda p: p in syntax_word_set, dic).values())
#     # print(f"popular_word {popular_word}", end="\n")
#     # print(f"popular_no_syntax_word {popular_no_syntax_word}", end="\n")
#
#     longest_no_K_squence = max(map(lambda x: len(x), re.split('k|K', content)))
#     print(f"longest_no_K_squence {longest_no_K_squence}", end="\n")
#     max_number = 0
#     text = content
#     next_res = re.search(r"\d+", text)
#
#     while next_res:
#         if int(next_res[0]) > max_number:
#             max_number = int(next_res[0])
#         text = text[next_res.span()[1]:]
#         next_res = re.search(r"\d+", text)
#
#     print(f"max_number {max_number}", end="\n")
#
#
#
#
# x =dict
# for i in x.items(:
#     i.
# # with open('dickens.txt', 'r',encoding = "ISO-8859-1") as fd:
# #     #print(14537750/1024)
# #     # x = x.join(d)
# #     # print(x)
# #     # print("***************************************************************************************")
# #     # d = fd.read(1024)
# #     # print(d)
# #
# #
# #     content = gen(fd)
# #     x = ''.join(content)
# #     print(set(gen(fd)))
# #     # # print(fd.read())
# #     # fd.seek(4)
# #     # print("***********************************************************")
# #     # print(fd.read(100))

    def __gen__(self):
        for line in self.__file_obj:
            for ch in line:
                yield ch

max_number:
# check
while next_res:
    if int(next_res[0]) > max_number:
        max_number = int(next_res[0])
    text = text[next_res.span()[1]:]
    next_res = re.search(r"\d+", text)
return
def __gen__(self):
        block = self.__file_obj.read(1024)
        while not block == "":
            for ch in block:
                yield ch
            block = self.__file_obj.read(1024)max_number