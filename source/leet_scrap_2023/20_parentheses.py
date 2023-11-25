class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            # Linked list code
            new_node = Node(data)
            new_node.next = self.head # ****************
            self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            # Removes the head node and makes
            # the preceding one the new head
            node_pop = self.head
            self.head = self.head.next
            node_pop.next = None
            return node_pop.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
    def display(self):
        iter_node = self.head
        if self.isEmpty():
            print("Stack Underflow")
        else:
            while iter_node != None:
                print(iter_node.data, end = "")
                iter_node = iter_node.next
                if iter_node != None:
                    print(" -> ", end="")
                



def isValid1(s: str) -> bool:
    
    stack = []
    dict = { "(":")", "[":"]", "{":"}", }

    for char in s:
        # If open bracket, add it
        if char in dict:
            stack.append(char)
        # Not Stack checks if the stack is empty and we added a close bracket
        # Throw the last appended character (open bracket) into the dict
        # if the char does not match the dict value (close bracket) --> return false
        elif not stack or dict[stack.pop()] != char:
            return False
        
    return len(stack) == 0



if __name__ == "__main__":

    inp = "()[]{}}"
    isValid1(inp)

    # myStack = Stack()
    # myStack.push(11)
    # myStack.push(21)
    # myStack.push(43)
    # myStack.push(67)
    # myStack.push(420)

    # myStack.display()