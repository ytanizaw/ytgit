#! coding:utf8
class Hanoi:
    def __init__(self, n):
        self.height =n
        self.left=range(n,0,-1)
        self.center=[]
        self.right=[]

    def show(self):
        n=self.height
        def getNth(x,n):
            try:
                return x[n]
            except IndexError:
                return 0
        ret=[]
        for i in range(n):
            ret.append((getNth(self.left,i), getNth(self.center,i) ,getNth(self.right,i)))
        ret.reverse()

        seps=3
        for row in ret:
            line =""
            for i in row:
                if i==0:
                    line+="　"*(n*2+1) +"　"*seps
                else:
                    line += "　"*(n-i+1) + "■"*(i*2-1) +"　"*(n-i+1)  +"　"*seps
            line=line[:-seps]
            print line
        print

    def solve(self, n, from_, to, via):
        def move(from_, to):
            FROM=getattr(self, from_)
            TO=getattr(self, to)
            TO.append(FROM.pop())

        if n == 1:
            move(from_, to)
            self.show()
            print "%s => %s" % (from_, to)
        else:
            self.solve( n - 1, from_, via, to)
            move(from_, to)
            self.show()
            print "%s => %s" % (from_, to)
            self.solve(n - 1, via, to, from_)


hanoi=Hanoi(5)
hanoi.show()
hanoi.solve(5,"left","center","right")



def get_hanoiNum(n):
    if n==1:
        return 1
    else:
        return 2*get_hanoiNum(n-1) +1
print get_hanoiNum(64)

