N, M = map(int, input().split())
package = []
indiv = []

p = N // 6
e = N % 6

for i in range(M):
    A, B = map(int, input().split())
    package.append(A)
    indiv.append(B)

package.sort()
indiv.sort()

sum = 0
if package[0] < indiv[0] * 6:
    sum += package[0] * p
else:
    sum += indiv[0] * (p * 6)

if package[0] < indiv[0] * e:
    sum += package[0]
else:
    sum += indiv[0] * e
print(sum)


