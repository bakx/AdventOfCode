import math


class Present:
    def __init__(self, size):
        self.papersize = size.split('x')
        self.l = int(self.papersize[0])
        self.w = int(self.papersize[1])
        self.h = int(self.papersize[2])

    def getsize(self):
        return 2 * self.l * self.w + \
               2 * self.w * self.h + \
               2 * self.h * self.l

    def getextra(self):
        sorted = [self.l, self.w, self.h]
        sorted.sort()
        return int(sorted[0]) * int(sorted[1])

    def gettotal(self):
        return self.getsize() + self.getextra()

requiredPaper = 0

f = open('day2.txt', 'r')
for line in f:
    requiredPaper += Present(line).gettotal()

print 'Paper required is ' + str(requiredPaper)