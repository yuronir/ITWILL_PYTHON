# Heap의 특징 : 가장 작은 값이 언제나 첫번째에 들어있다.(pop하면 새로운 최소값이 들어온다)
# O(logN)
# nsmallest, nlargest : 찾을 값의 갯수가 적으면 heappop을 반복, 많으면 sort해서 반환
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap) #[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heapq.heappop(heap)) # -4
print(heap) #[1, 2, 2, 23, 7, 8, 18, 23, 42, 37]
