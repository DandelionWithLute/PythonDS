def deleteAlt(head):
    if head == None:
        return
    prev = head
    now = head.next
    while prev != None and now != None:
        # Change next link of previous node
        prev.next = now.next
        # Free memory
        now = None
        # Update prev and node
        prev = prev.next
        if prev != None:
            now = prev.next
