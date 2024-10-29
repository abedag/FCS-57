from typing import Any


print("Assignment 4:\n")
print("Stacks and Queues:\n")

print("1.\n")

class Stack:
    def __init__(self):
        self.sequence = []
    
    def push(self,val):
        self.sequence.append(val)

    def pop(self):
        if len(self.sequence) == 0:
            return None
        return self.sequence.pop()
    
    def isEmpty(self):
        return len(self.sequence) == 0


class Queue:
    def __init__(self):
        self.sequence = []
    
    def enqueue(self,val):
        self.sequence.append(val)

    def dequeue(self):
        if len(self.sequence) == 0:
            return None
        return self.sequence.pop(0)
    
    def isEmpty(self):
        return len(self.sequence) == 0
    
seq = input("Input your sequence to check if it's palindrome or not:")

def isPalid(seq):
    seq = seq.replace(""," ").lower()
    stack = Stack()
    queue = Queue()

    for s in seq:
        stack.push(s)
        queue.enqueue(s)
        
    while not stack.isEmpty() and not queue.isEmpty():
        if stack.pop() != queue.dequeue():
            return False
    return True

print(isPalid(seq))


print("\n 2.\n")

class MatchingPairs:
    def __init__(self):
        self.match = {")": "(", "}": "{", "]": "["}    

    def pushPop(self, val):
        self.element = []
        for n in val:
            if n in "({[":
                self.element.append(n)
            elif n in ")}]":
                if not self.element or self.element.pop() != self.match[n]:
                    return False
        
        return len(self.element) == 0

c = MatchingPairs()

print(c.pushPop("(1+2)-3*[41+6]"))
print(c.pushPop("(1+2)-3*[41+6}"))
print(c.pushPop("(1+2)-3*[41+6"))
print(c.pushPop("(1+2)-3*]41+6["))
print(c.pushPop("(1+[2-3]*4{41+6})"))



print("\nStack:\n")

class MIB:
    def __init__(self):
        self.stack = []

    def decode(self, message): 
        for m in message:
            if m.isalpha() or m == " ":
                self.stack.append(m)
            elif m == "*":
                if self.stack:
                    self.stack.pop()

        decoded_message = ""
        while self.stack:
            decoded_message += self.stack.pop()
        return decoded_message if decoded_message else "Try Again!"

    
m = MIB()
print(m.decode("SIVLE ****** DAED TNSI ***"))


print("\nQueues:\n")

