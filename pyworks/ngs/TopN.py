#!/usr/local/bin/python
#coding:utf8

class TopN(object):
    def __init__(self,N,reverse=False):
        self.keys=[]
        self._items=[]
        self.N=N
        self.reverse=reverse

    def add(self,key,obj):
        if self.reverse:
            idx=len([x for x in self.keys if x<=key])
        else:
            idx=len([x for x in self.keys if x>=key])
        self.keys.insert(idx,key)
        self._items.insert(idx,obj)
        self.keys=self.keys[0:self.N]
        self._items=self._items[0:self.N]

    def get(self,n):
        return self._items[n]

    def __getitem__(self, n):
        return self.get(n)

    def __len__(self):
        return len(self._items)

    def __delitem__(self, n):
        del self.keys[n]
        del self._items[n]

    def __str__(self):
        return self._items.__str__()

    def items(self):   ##generator
        for i in range(len(self)):
            yield self[i]

    def __iter__(self):
        self.index=-1
        return self

    def next(self):
        self.index += 1
        if self.index ==len(self):
            raise StopIteration
        return self[self.index]

class TopNstring(TopN):

    def add(self,string):
        key=len(string)
        TopN.add(self,key, string)


def main():
    top5=TopN(5)
    for item in top5:
        print item,
    top5.add(5,"A")
    top5.add(3,"B")
    iter(top5)
    print "test:",top5.next()
    print "test:",top5.next()
    top5.add(1,"O")
    top5.add(2,"C")
    top5.add(6,"D")
    top5.add(6,"DD")
    top5.add(6,"DDD")
    top5.add(8,"E")
    print len(top5)
    print top5[1]
    print "==="

    for i in range(len(top5)):
        print top5[i],
    print

    del top5[3]
    print "TOP5",top5
    print [item*5 for item in top5]
    for item in top5:
        print item,
#    gen= top5._items()
#    print gen.next()
    for item in top5.items():
        print item
    gen=top5.items()
    print gen.next()


#print __name__ +" called ====="
if __name__=="__main__":
    main()
