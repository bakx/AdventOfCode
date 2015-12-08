import math


class Present:
    def __init__(self, size):
        self._size = size.split('x')
        self.l = int(self._size[0])
        self.w = int(self._size[1])
        self.h = int(self._size[2])

    def get_size(self):
        return 2 * self.l * self.w + \
               2 * self.w * self.h + \
               2 * self.h * self.l

    def get_extra(self):
        sorted = [self.l, self.w, self.h]
        sorted.sort()
        return int(sorted[0]) * int(sorted[1])

    def get_total(self):
        return self.get_size() + self.get_extra()

    def get_ribbon(self):
        sorted = [self.l, self.w, self.h]
        sorted.sort()
        return ((sorted[0] * 2) + (sorted[1] * 2)) + self.l * self.w * self.h


requiredPaper = 0
requiredRibbon = 0

f = open('day2.txt', 'r')
for line in f:
    currentPresent = Present(line)
    paperForPresent = currentPresent.get_total()
    ribbonForPresent = currentPresent.get_ribbon()

    requiredPaper += paperForPresent
    requiredRibbon += ribbonForPresent

    print line
    print "For this present, Paper required is: " + str(paperForPresent)
    print "For this present, Ribbon required is: " + str(ribbonForPresent)

print "\n"
print "Total Paper required is: " + str(requiredPaper)
print "Total Ribbon required is: " + str(requiredRibbon)

f.close()
