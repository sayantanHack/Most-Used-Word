#file_read = raw_input("Enter the File : ")
F_open = open("textfile.txt")

word_dic = {}

for line in F_open:
    line.rstrip()
    words = line.split()

    for word in words:
        word_dic[word] = word_dic.get(word,0) + 1

largest_number = 0
largest_word = None
for key,value in word_dic.items():
    if value > largest_number:
        largest_number = value
        largest_word = key
print 'The largest word is :', largest_word ,'.It`s been appear :', largest_number,'times.'
    
