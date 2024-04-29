import math

A, B = map(int, input().split())
C, D = map(int, input().split())

BDgcd = math.gcd(B,D)
BDlcm = B * D // BDgcd

Amul = BDlcm // B
Cmul = BDlcm // D

top = A * Amul
bottom = C * Cmul

total = top + bottom

totalgcd = math.gcd(total, BDlcm)
totaltop = total // totalgcd
totalbottom = BDlcm // totalgcd

print(totaltop, totalbottom, end=' ')