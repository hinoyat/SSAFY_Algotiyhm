# 선형 큐
# def isFull():
#     return rear == len(Q) - 1
#
#
# def isEmpty():
#     return front == rear
#
# def enQueue(item):
#     global rear
#     if isFull():
#         print('Full')
#     else:
#         rear += 1
#         Q[rear] += item
#
# def deQueue():
#     if(isEmpty())

#
# front = -1
# rear = -1
# Q = [0] * N
# N = 10



# circular
Q_size = 4
cQ = [0] * Q_size
front = rear = 0

rear = (rear+1) % Q_size
cQ[rear] = 1

rear = (rear+1) % Q_size
cQ[rear] = 2

rear = (rear+1) % Q_size
cQ[rear] = 3

front = (front +1) % Q_size
print(cQ[front])