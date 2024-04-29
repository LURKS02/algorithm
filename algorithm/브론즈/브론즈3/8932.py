import math

T = int(input())

def getGrade1(P):
    return math.floor(9.23076 * pow(26.7 - P, 1.835))
def getGrade2(P):
    return math.floor(1.84523  * pow(P - 75, 1.348))
def getGrade3(P):
    return math.floor(56.0211 * pow(P - 1.5, 1.05))
def getGrade4(P):
    return math.floor(4.99087 * pow(42.5 - P, 1.81))
def getGrade5(P):
    return math.floor(0.188807 * pow(P - 210, 1.41))
def getGrade6(P):
    return math.floor(15.9803 * pow(P - 3.8, 1.04))
def getGrade7(P):
    return math.floor(0.11193 * pow(254 - P, 1.88))

for i in range(T):
    A, B, C, D, E, F, G = map(int, input().split())
    print(getGrade1(A) + getGrade2(B) + getGrade3(C) + getGrade4(D) + getGrade5(E) + getGrade6(F) + getGrade7(G))