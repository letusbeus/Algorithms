import view
from node import Node


class DoubleLinkedList:
    def __init__(self):
        self.start_prev = None
        self.start_node = None

    def insert_in_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            view.not_empty_list()

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            view.inserted()
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            view.empty_list()
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                view.not_in_list()
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            view.empty_list()
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                view.not_in_list()
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev = new_node

    def traverse_list(self):
        if self.start_node is None:
            view.empty_list()
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, ' ')
                n = n.next

    def delete_at_start(self):
        if self.start_node is None:
            view.empty_list()
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            view.empty_list()
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def delete_item_by_value(self, x):
        if self.start_node is None:
            view.empty_list()
            return
        if self.start_node.next is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                view.not_found()
                return
        if self.start_node.item == x:
            self.start_node = self.start_node.next
            self.start_node.pref = None
            return
        n = self.start_node
        while n.next is not None:
            if n.item == x:
                break
            n = n.next
        if n.next is not None:
            n.pref.next = n.next
            n.next.prev = n.pref
        else:
            if n.item == x:
                n.pref.next = None
            else:
                view.not_found()
        if self.start_node is None:
            view.not_empty_list()
            return
        if self.start_node.next is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                view.not_found()
            return

    def reverse_linked_list(self):
        if self.start_node is None:
            view.not_empty_list()
            return
        p = self.start_node
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.start_node = p
