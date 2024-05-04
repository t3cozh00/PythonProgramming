##10.3 Exercise: More list methods

filename = open('words.txt', 'r')
words = filename.read().splitlines()
words.sort()
print('Words in an alphabetical order: ')
for i in words:
    print(i)
filename.close()

