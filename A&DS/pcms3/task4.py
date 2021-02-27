global numofexecution, lenofheap, numberofpush, queue  # номер операции, длина heap, номер операции push, очередь
# команд (номер push, остальные команды - "-1")
numofexecution, lenofheap, numberofpush = 1, 0, 0 
queue = [-1]


def buildheapreverse(arr, num, heap_size):  # heapify наоборот, т.е. heap - антипирамида
    global numofexecution, lenofheap, queue
    l = 2 * num + 1
    r = 2 * num + 2
    smallest = num
    if l < heap_size and arr[l][1] < arr[smallest][1]:
        smallest = l
    if r < heap_size and arr[r][1] < arr[smallest][1]:
        smallest = r
    if smallest != num:
        arr[num], arr[smallest] = arr[smallest], arr[num]
        queue[arr[num][0]], queue[arr[smallest][0]] = queue[arr[smallest][0]], queue[arr[num][0]]
        buildheapreverse(arr, smallest, heap_size)


def heapyup(arr, num):  # поднимает элемент до нужного уровня
    global numofexecution, lenofheap, queue
    while (num > 0) and arr[(num - 1) // 2][1] > arr[num][1]:
        arr[(num - 1) // 2], arr[num] = arr[num], arr[(num - 1) // 2]
        queue[arr[(num - 1) // 2][0]], queue[arr[num][0]] = queue[arr[num][0]], queue[arr[(num - 1) // 2][0]]
        num = (num - 1) // 2


def push(heap, num):  # в heap добавляет элемент и номер операции, на которой он был добавлен, в queue номер push
    global numofexecution, lenofheap, queue, numberofpush
    heap.append([numofexecution, num])
    lenofheap += 1
    queue.append(numberofpush)
    numberofpush += 1
    numofexecution += 1
    heapyup(heap, len(heap) - 1)


def extract_min(heap):  # если длина heap не равна 0, печатаем первый её элемент и сортируем
    global numofexecution, lenofheap, queue
    numofexecution += 1
    queue.append(-1)
    if lenofheap == 0:
        print("*", file=fout)
    else:
        print(heap[0][1], file=fout)
        heap[0][1] = 10**9
        lenofheap -= 1
        buildheapreverse(heap, 0, len(heap))


def decrease_key(heap, num, x):
    global numofexecution, lenofheap, queue
    numofexecution += 1
    queue.append(-1)
    heap[queue[num]][1] = x
    heapyup(heap, queue[num])


fin = open("priorityqueue.in")
fout = open("priorityqueue.out", "w")
heap = []
for line in fin:
    inp = line.split()
    if inp[0] == 'push':
        push(heap, int(inp[1]))
    elif inp[0] == 'extract-min':
        extract_min(heap)
    elif inp[0] == 'decrease-key':
        decrease_key(heap, int(inp[1]), int(inp[2]))
fout.close()
