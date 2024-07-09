import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def Sol():
    N = int(input())

    def prime(num):
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True

    def backtracking(n):
        if len(str(n)) == N:
            print(n)

        else:
            for i in range(1, 10, 2):
                if prime(10*n + i):
                    backtracking(10*n + i)

    backtracking(2)
    backtracking(3)
    backtracking(5)
    backtracking(7)

Sol()