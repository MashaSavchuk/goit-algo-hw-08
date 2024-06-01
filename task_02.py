import heapq

def merge_k_lists(lists):
    # Початкове заповнення купи першими елементами кожного списку
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    
    merged_list = []
    
    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        merged_list.append(val)
        
        # Додавання наступного елемента з поточного списку до купи
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_val, list_index, element_index + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
