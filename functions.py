from linkedlist import *

# initialize dictionary as linked list
wordsDictionary = LinkedList()

def readFromFile():
    fileObj = open('wordsFile.txt', 'r');
    fileData = fileObj.read().splitlines()
    fileObj.close()

    for line in fileData:
        word = line.split('%%')
        wordObj = {}
        wordObj['word'] = word[0]  # word
        wordObj['meaning'] = word[1]  # meaning
        wordsDictionary.insertNode(wordObj)

# writing in file
def writeToFile():
    fileObj = open('wordsFile.txt', 'w+')
    current_word = wordsDictionary.head

    while current_word is not None:
        var = current_word.data
        string_to_write = '{}%%{}\n'.format(var['word'], var['meaning'])
        fileObj.write(string_to_write)
        current_word = current_word.next

    fileObj.close()