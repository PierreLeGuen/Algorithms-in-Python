class Pile:
    def __init__(self, alist=None):
        self.alist = alist
    def push(self,x):
        self.alist.append(x)
    def pop(self):
        self.alist.pop()
    def top(self):
        i=0
        while i < len(self.alist)-1:
            i+=1
        return self.alist[i]
    def isEmpty(self):
        if len(self.alist) != 0:
            return False
        return True

p = Pile([1, 2, 3, 4])
p.push(5)
p.pop()
print(p.top())
print(p.isEmpty())
## FAIRE LA SUITE