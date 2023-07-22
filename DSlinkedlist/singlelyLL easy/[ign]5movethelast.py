def moveToFront(self):
    tmp = self.head
    sec_last = None
    if not tmp or not tmp.next:
        return
    while tmp and tmp.next:
        sec_last = tmp
        tmp = tmp.next
    sec_last.next = None
    # Make the last node as the first Node
    tmp.next = self.head
    self.head = tmp
