print("Assignment 4:\n")

print("Exercise 1:\n")

class MatchingPairs:
    def __init__(self):
        self.match = {")": "(", "}": "{", "]": "["}    
        self.element = []

    def push(self, val):
        for n in val:
            if n in "({[":
                self.element.append(n)

            elif n in ")}]":
                if not self.element or self.element.pop() != self.match[n]:
                    return False
        
        return len(self.element) == 0

c = MatchingPairs()

print(c.push("(1+2)-3*[41+6]"))
print(c.push("(1+2)-3*[41+6}"))
print(c.push("(1+2)-3*[41+6"))
print(c.push("(1+2)-3*]41+6["))
print(c.push("(1+[2-3]*4{41+6})"))


print("\nExercise 2:\n")