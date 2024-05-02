import sys
input = sys.stdin.readline

N, ATK = map(int, input().rstrip().split())
rooms = []

for _ in range(N):
    T, A, H = map(int, input().rstrip().split())
    rooms.append((T, A, H))

def fight(heroAttack, heroHp, heroMaxHp, monsterAttack, monsterHp):
    if monsterHp <= heroAttack:
        return heroHp

    else:
        attackCount = monsterHp // heroAttack if not monsterHp % heroAttack else monsterHp // heroAttack + 1
        returnHp = heroHp - (attackCount - 1) * monsterAttack
        return returnHp

def potion(heroAttack, heroHp, heroMaxHp, potionAttack, potionHp):
    heroAttack += potionAttack
    heroHp = min(heroHp + potionHp, heroMaxHp)

    return (heroAttack, heroHp)

def moveToRoom(heroAttack, heroHp, heroMaxHp, room):
    type, attack, hp = room

    if type == 1:
        return (heroAttack, fight(heroAttack, heroHp, heroMaxHp, attack, hp))
    elif type == 2:
        return potion(heroAttack, heroHp, heroMaxHp, attack, hp)

def checkDragon(heroAttack, heroMaxHp):
    attack = heroAttack
    hp = heroMaxHp
    for room in rooms:
        attack, hp = moveToRoom(attack, hp, heroMaxHp, room)
        if hp <= 0:
            return False
    return True

left = 1
right = N * int(1e6) * int(1e6)
result = 0
while left <= right:
    mid = (left + right) // 2

    if checkDragon(ATK, mid):
        right = mid - 1
        result = mid
    else:
        left = mid + 1
    # print(left)
    # print(right)
    # print(result)
    # print()


print(result)
