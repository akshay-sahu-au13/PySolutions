heap = [1, 2, 3, 4, 5, 6, 7, 8]
 
 
def heapify(idx):
    global heap
 
    left = 2 * idx + 1
    right = 2 * idx + 2
 
    if left >= len(heap) and right >= len(heap):
        return
 
    max_idx = idx # i am assuming i am the max idx
 
    if left < len(heap) and heap[left] > heap[max_idx]: # if my left was bigger than me then i am updating max idx to left
        max_idx = left
 
    if right < len(heap) and heap[right] > heap[max_idx]:
        max_idx = right
 
    if idx != max_idx:
        heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
        heapify(max_idx)
 
 
def popElement():
    global heap
    heap[0], heap[-1] = heap[-1], heap[0]
    x = heap[-1]
    heap = heap[:-1]
    heapify(0)
    return x
 
def buildHeap():
    global heap
 
    for i in range(len(heap) - 1, -1, -1): # i -> 7: 0
        heapify(i)
 
def heapSort():
    global heap
    while len(heap) != 0:
        print(popElement())
 
if __name__ == "__main__":
    # print("before: ", heap)
    buildHeap()
    # print("after: ", heap)
    heapSort()