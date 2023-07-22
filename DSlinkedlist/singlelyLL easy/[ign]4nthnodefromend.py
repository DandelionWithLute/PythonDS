def printNthFromLast(self, n):
    temp = self.head
    length = 0
    while temp:
        temp = temp.next
        length += 1
    if n > length:
        print("Location is greater than the" + " length of LinkedList")
        return
    temp = self.head
    for i in range(0, length - n):
        temp = temp.next
    print(temp.data)
