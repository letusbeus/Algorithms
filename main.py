import view
from linked_list import DoubleLinkedList

view.init()
new_linked_list = DoubleLinkedList()
new_linked_list.insert_in_empty_list(50)
new_linked_list.insert_at_start(8)
new_linked_list.insert_at_start(6)
new_linked_list.insert_at_start(13)
new_linked_list.insert_at_start(19)
new_linked_list.traverse_list()
view.reverse()
new_linked_list.reverse_linked_list()
new_linked_list.traverse_list()
