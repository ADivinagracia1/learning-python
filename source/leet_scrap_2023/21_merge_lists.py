# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def mergeTwoLL(list1, list2):

    head = ListNode() # assign to dummy node (Sentinel Nodes)
    cursor = head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            new_node = ListNode(list1.val) # append
            list1 = list1.next 
        else:
            new_node = ListNode(list2.val)
            list2 = list2.next 
        # new_node = ListNode(min(list1.val, list2.val)) and increment lists  #make new node
        cursor.next = new_node 
        cursor = new_node

    while list1 is not None:
        new_node = ListNode(list1.val)
        cursor.next = new_node
        cursor = new_node
        list1 = list1.next

    while list2 is not None:
        new_node = ListNode(list2.val)
        cursor.next = new_node
        cursor = new_node
        list2 = list2.next

    # pop
    head = head.next

    return head

# def mergeTwoLL(list1, list2):

#     head = None
#     cursor = None

#     while list1 is not None and list2 is not None:
#         if list1.val < list2.val:
#             new_node = ListNode(list1.val)
#             if head == None:    head = new_node
#             if cursor != None:  cursor.next = new_node
#             cursor = new_node
#             list1 = list1.next 
#         else:
#             new_node = ListNode(list2.val)
#             if head == None:    head = new_node
#             if cursor != None:  cursor.next = new_node
#             cursor = new_node
#             list2 = list2.next 

#     while list1 is not None:
#         new_node = ListNode(list1.val)
#         cursor.next = new_node
#         cursor = new_node
#         list1 = list1.next

#     while list2 is not None:
#         new_node = ListNode(list2.val)
#         cursor.next = new_node
#         cursor = new_node
#         list2 = list2.next

#     return head


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(2, ListNode(3, ListNode(4, None)))
out = mergeTwoLL(list1, list2)

while out is not None:
    print(out.val)
    out = out.next


# def mergeTwoLists(list1, list2):
#     i,j=0,0
#     new_node = []
#     # loop through both arrays simultaneously
#     while i < len(list1) and j < len(list2):
#         # comapre each element and insert to merged array
#         if list1[i] < list2[j]:
#             new_node.append(list1[i])
#             i+=1
#         else:
#             new_node.append(list2[j])
#             j+=1

#     # insert leftover elements of left array
#     while i < len(list1):
#         new_node.append(list1[i])
#         i+=1

#     # insert leftover elements of right array
#     while j < len(list2):
#         new_node.append(list2[j])

#     return new_node