# https://www.acmicpc.net/problem/10828

from collections import deque
N = int(input())
st = deque()

for _ in range(N):
    arr = input().split()
    if (arr[0] == "push"):
        # print(int(arr[1]))
        st.append(int(arr[1]))
    elif (arr[0] == "pop"):
        if(st):
            print(st.pop())
        else:
            print(-1)
    elif (arr[0] == "size"):
        print(len(st))
    elif (arr[0] == "top"):
        if (st):
            print(st[-1])
        else:
            print(-1)
    elif (arr[0] == "empty"):
        if(st):
            print(0)
        else:
            print(1)
