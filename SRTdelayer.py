import os
class subtitle:
    def __init__(self, s):
        d, f = s.split("-->")
        
        self.debut = time(d[:-1])
        self.fin = time(f[1:])

    def delay(self, delay):
        self.debut.delay(delay)
        self.fin.delay(delay)

    def __str__(self):
        return str(self.debut)+" --> "+str(self.fin)+"\n"

class time:
    def __init__(self, s):
        self.value=s.split(":")
        self.value+=self.value[2].split(",")
        del self.value[2]
        self.intvalues=map(int, self.value)
    
    def delay(self, other):
        other=time(other)
        r=0
        s=0
        mod=1000
        for i in xrange(3, -1, -1):
            if i == 2:
                mod=60
            elif i == 0:
                mod == 100
            s = self.intvalues[i] + other.intvalues[i] + r
            r = s / mod
            s = s % mod
            self.intvalues[i]=s
            self.value[i]=str(s)
            self.value[i].rjust(2, '0')
             
    def __repr__(self):
        return ":".join(self.value[:2])+":"+",".join(self.value[2:])

    def __str__(self):
        return self.__repr__()

delay="00:00:1,250"
with open("test.srt") as f:
    content=f.readlines()
    for i in xrange(len(content)):
        if content[i][:-1].isdigit():
            sub=subtitle(content[i+1][:-1])
            sub.delay(delay)
            content[i+1]=str(sub)

with open("resultat.srt", "w+") as f:
    f.writelines(content)
