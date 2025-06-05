# (a*b)%c = (a%c)*(b%c)%c 임을 활용(나머지 분배 법칙)

a, b, c = map(int, input().split())

def mult(n: int, exp: int) -> int:
    if exp == 1:
        return n % c
    res = mult(n, exp // 2)
    if exp % 2 == 0:
        return res**2 % c
    else:
        return (res**2 * n) %c

print(mult(a, b))