import heapq

def connect_cables(cables):
    heap = cables[:]
    heapq.heapify(heap)
    visualize_connections = ""
    expenses = 0

    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)

        merged_cable = (cable1[0] + cable2[0], f"{cable1[1]}{cable2[1]}")
        visualize_connections += f"({cable1[1]} > {cable2[1]}) { "=> " if len(heap) >= 1 else ""}" 

        heapq.heappush(heap, merged_cable)
        expenses += merged_cable[0]

    return expenses, visualize_connections


if __name__ == "__main__":
    cables = [(3, "A"), (5, "B"), (2, "C"), (8, "D"), (1, "E")]
    total_expenses, result_visualize = connect_cables(cables)

    print(f"Порядок об'єднання: {result_visualize}")
    print(f"Загальні витрати: {total_expenses}")
