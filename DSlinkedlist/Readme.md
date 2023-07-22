		else:
			new_node = Node(data)
			self.last_node.next = new_node
			new_node.previous = self.last_node
			new_node.next = None
            #OK without the former line
			self.last_node = new_node



Types of Linked List
Doubly Linked List
https://www.geeksforgeeks.org/types-of-linked-list/
    def append(self, data):
        # is doubly linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None:空链表，创建头节点和末节点：
            self.head = Node(data)①创建头节点+赋值
            self.last_node = self.head②头节点的位置上创建末节点
        # adding node to the tail of doubly linked list
        else:双链表拓展
            new_node = Node(data)①新节点赋值
            self.last_node.next = new_node②——>后链指向新节点
            new_node.previous = self.last_node③<——指向之前的节点[new_node也可以写成self.last_node.next]
            new_node.next = None⑤到头“没有啦”：没有下一个节点了（空）
            self.last_node = new_node④“到头”没有啦：设置末节点为链表后面新建的节点


			new_node = Node(data)
			self.last_node.next = new_node
			new_node.previous = self.last_node
			new_node.next = None
			self.last_node = new_node

			is basically identical to

			self.new_node = Node(data)
			self.last_node.next = self.new_node
			self.new_node.previous = self.last_node
			self.new_node.next = None
			self.last_node = self.new_node

Dont forget this next
	self.last_node.next = Node(val)
	self.last_node = self.last_node.next