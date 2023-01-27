from collections import Counter


def calcu(a, b, n, k):
    arr = b.sort(reverse=True)
    # ans = arr[0] + arr[1]
    # print(min(ans,k))
    print(arr)


if __name__ == '__main__':

    n = int(input())
    k = int(input())
    a = []
    b = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        b.append(int(input()))

    result = calcu(a, b, n, k)
