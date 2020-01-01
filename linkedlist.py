from node import *

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # insert function
    def insertNode(self, newData):
        temp = self.head
        while temp is not None:
            if temp.data['word'] == newData['word']:
                return
            temp = temp.next
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    # delete function
    def deleteNode(self, value):
        temp = self.head
        if temp is not None:
            if temp.data['word'] == value:
                self.head = temp.next
                temp = None
                return True
        while temp is not None:
            if temp.data['word'] == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return False
        prev.next = temp.next
        temp = None
        return True

    # sort function (Bubble Sort)
    def sortList(self):
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            while nextNode is not None:
                if (currentNode.data['word']).lower() > (nextNode.data['word']).lower():
                    currentNode.data, nextNode.data = nextNode.data, currentNode.data
                nextNode = nextNode.next
            currentNode = currentNode.next

    # print function
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # simple search function
    def simpleSearch(self, value):
        temp = self.head
        while temp is not None:
            if temp.data['word'] == value:
                return temp.data
            temp = temp.next
        return False

    # simple search meaning
    def simpleSearchMeaning(self, value):
        temp = self.head
        while temp is not None:
            if temp.data['meaning'] == value:
                return temp.data
            temp = temp.next
        return False

    # advance search function
    def advanceSearch(self, value):
        matchingWords = []
        temp = self.head
        while temp is not None:
            if value in temp.data['word']:
                matchingWords.append(temp.data)
            temp = temp.next
        return matchingWords

    # advance search meaning
    def advanceSearchMeaning(self, value):
        matchingMeanings = []
        temp = self.head
        while temp is not None:
            if value in temp.data['meaning']:
                matchingMeanings.append(temp.data)
            temp = temp.next
        return matchingMeanings