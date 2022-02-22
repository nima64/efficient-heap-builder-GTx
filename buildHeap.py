from __future__ import annotations
from typing import List 

class Heap:
    data = []
    def __init__(self, initData: List):
        if (initData != None):
            self.data = initData.copy()
    def getParent(self, i) -> int:
        return (i+1)//2 - 1
    def getLeftChild(self, i) -> int:
        return (i+1)*2-1
    def getRightChild(self, i) -> int:
        # return (i+1)*2+1-1
        return (i+1)*2
    def __str__(self) -> str:
        return self.data.__str__()

#condLambda(a,b) a is curtn, b is parnt
def upHeap(condLambda, heap: Heap, idx) -> bool:
    pidx = heap.getParent(idx)
    if (idx > 0 and condLambda(heap.data[idx], heap.data[pidx])):  
        heap.data[pidx], heap.data[idx] = heap.data[idx], heap.data[pidx]
        return pidx
    return -1

def recursvUpHeap(condlambda, heap: Heap, idx):
    pidx = upHeap(condlambda,heap, idx)
    if pidx > 0:
        return recursvUpHeap(condlambda, heap, pidx)+1
    return 1

def downHeap(condLambda, heap: Heap, idx):
    crnt = heap.data[idx]
    leftChildIdx, rightChildIdx = heap.getLeftChild(idx), heap.getRightChild(idx)
    hasRightChild = rightChildIdx < len(heap.data)
    hasLeftChild = leftChildIdx < len(heap.data)
    canSwapLeft, canSwapRight = False, False

    canSwapLeft = hasLeftChild and condLambda(crnt, heap.data[leftChildIdx])
    canSwapRight  = hasRightChild and condLambda(crnt, heap.data[rightChildIdx])

    if(canSwapLeft and canSwapRight):
        leftChild, rightChild = heap.data[leftChildIdx], heap.data[rightChildIdx] 
        #retun the child which is the opposite cond of the lambda cond
        targetChildIdx = leftChildIdx if not condLambda(leftChild, rightChild) else rightChildIdx
        heap.data[targetChildIdx], heap.data[idx] = heap.data[idx], heap.data[targetChildIdx] 
        return targetChildIdx
    elif(canSwapLeft):
        heap.data[leftChildIdx], heap.data[idx] = heap.data[idx], heap.data[leftChildIdx] 
        return leftChildIdx
    elif(canSwapRight):
        heap.data[rightChildIdx], heap.data[idx] = heap.data[idx], heap.data[rightChildIdx] 
        return rightChildIdx
    return -1

def recursvDownHeap(condlambda, heap: Heap, idx):
    pidx = downHeap(condlambda,heap, idx)
    if pidx > 0:
        recursvDownHeap(condlambda, heap, pidx)

def recursvDownHeapCount(condlambda, heap: Heap, idx ):
    pidx = downHeap(condlambda,heap, idx)
    if pidx > 0:
        return recursvDownHeapCount(condlambda, heap, pidx) + 1
    return 1

class MaxHeap(Heap):
    def __init__(self):
        pass
    def __init__(self, initData: List):
        super().__init__(initData)
    def add(self, item):
        self.data.append(item)
        recursvUpHeap(lambda a,b: a > b, self, len(self.data)-1)
    def downHeap(self, idx: int): 
        compLamda = lambda a,b: a < b
        recursvDownHeap(compLamda, self, idx)
    def remove(self, idx):
        recursvDownHeap(lambda a,b: a < b, self, idx)
    def __str__(self) -> str:
        return super().__str__()

class MinHeap(Heap):
    def __init__(self, initData: List = None):
        super().__init__(initData)
    def add(self, item):
        compLamda = lambda a,b: a < b
        self.data.append(item)
        return recursvUpHeap(compLamda, self, len(self.data)-1)
    def downHeap(self, idx: int): 
        compLamda = lambda a,b: a > b
        return recursvDownHeapCount(compLamda, self, idx)
    def __str__(self) -> str:
        return super().__str__()

def test():
    dataset = [x for x in range(10000, -1,-1)]

    def naiveBuild():
        minhp = MinHeap()
        cmp_tot = 0
        for x in dataset:
            cmp_tot += minhp.add(x)
        print(f"comparisons for naive build {cmp_tot}")

    def effBuild():
        minhp = MinHeap(dataset)
        cmp_tot = 0
        for x in range(len(dataset)-1,-1,-1):
            cmp_tot += minhp.downHeap(x)
        print(f"comparisons for effcient build {cmp_tot}")

    print("\nnaive vs effecient heap builder algorithm")
    print("number of comparisons for ordered(DESC) set\n")
    naiveBuild()
    effBuild()
test()
    
