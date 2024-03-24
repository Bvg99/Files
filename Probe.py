# file_name = 'Статья.doc'
# file = open(file_name, mode='r', encoding='utf8')
# file_content = file.read()
# #file.write(file_content)
# file.close()t
# #file_content.decode('utf8')
from pprint import pprint

# text = open('one.txt', 'rb')
# ooo = text.read()
# pprint(ooo)

text = open('one.txt', 'r')
print(text.read(2))
print(text.tell())