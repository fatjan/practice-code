from heapq import heappush, heappop 
  
# Creating empty heap 
heap = [] 
  
# Adding items to the heap using heappush function 
print(heap)
heappush(heap, 10) 
print(heap)

heappush(heap, 30) 
print(heap)

heappush(heap, 20) 
print(heap)

heappush(heap, 400) 
print(heap)

element = heappop(heap) 
print(element) # 10

element = heappop(heap) 
print(element) # 20