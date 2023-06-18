# inport text file, and remove the punctuation marks, and save it as a new file
import string

# open the file
file_name = input("please enter the file name: ")
file_in = 'analyze\\' + file_name + ".txt"
file_out1 = 'analyze\\' + file_name + "_clean.txt"

with open(file_in, "r", encoding="utf-8") as f:
    text = f.read()



# remove the punctuation marks
remove_text = "，。、？！：:；「」『』》《）（．﹖﹕﹔﹑﹐—－─　][·…;‘’”“-"
text = text.translate(str.maketrans("", "", remove_text))

remove_word = ["◀上一回", "下一回▶", "目錄 三國演義", "三國演義", "目錄 水滸全傳", "返回頁首",
               "水滸傳_(120回本)",
               "一百二十回本全稱忠義水滸全傳明末袁無涯刊刻又稱袁本",
               "本明朝作品在全世界都属于公有领域因为作者逝世已经遠遠超过100年",
               "本作品在全世界都属于公有领域因为作者逝世已经超过100年并且于1925年1月1日之前出版",
               "本作品在全世界都属于公有领域因为作者逝世已经超过100年并且于1926年1月1日之前出版",
               "本作品在全世界都属于公有领域因为作者逝世已经超过100年并且于1927年1月1日之前出版"]
for i in remove_word:
    text = text.replace(i, "")

# save the file
with open(file_out1, "w", encoding="utf-8") as f:
    f.write(text)

