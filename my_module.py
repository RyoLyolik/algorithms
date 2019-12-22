import math
import random
import tkinter


def prime(n):
    lis = []
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0 and i * i <= n + 1 and not (i in lis and n // i in lis):
            lis.append(i)
            lis.append(n // i)

    if len(lis) >= 1:
        return False
    else:
        return True


def factorization(n):
    divs = []
    i = 2
    while 2 <= i and i * i <= n:
        if n % i == 0:
            divs.append(i)
            n //= i

        else:
            i += 1
    divs.append(n)
    return divs


def factor(n):
    divs = []
    for i in range(1, n // 2):
        if n % i == 0 and i * i < n + 1:
            divs.append(i)
            divs.append(n // i)
    return sorted(list(set(divs)))


def upsearch(lis, n):
    l, r = 0, len(lis)
    while r - l > 1:
        m = (l + r) // 2
        if lis[m] <= n:
            l = m
        else:
            r = m
    return l


def lowsearch(lis, n):
    l, r = 0, len(lis)
    while l != r:
        m = (l + r) // 2
        if lis[m] < n:
            l = m + 1
        else:
            r = m
    return l


def graph(lis):
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, bg='white', height=920, width=920)
    canvas.pack()
    points = []
    rand = [i for i in range(10, 910)]

    for i in range(len(lis)):
        g = random.choice(rand)
        s = random.choice(rand)
        points.append((g, s))
        canvas.create_oval(((g) - 5, (s) - 5), ((g) + 5, (s) + 5), fill="black")
        canvas.create_text((g, s), text=i, fill="white")

    for i in range(len(lis)):
        for j in range(len(lis[i])):
            canvas.create_line(points[i], points[lis[i][j]], fill="black")
            canvas.create_text(points[i], text=i, fill="white")
    master.mainloop()


def sieve(n):
    tr = [True] * (n + 1)
    ret = []
    for i in range(2, n + 1):
        if i ** 2 <= n:
            for j in range(i ** 2, n + 1, i):
                tr[j] = False

    for i in range(2, n + 1):
        if tr[i]:
            ret.append(i)
    return ret


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def quadro_uravn(a, b, c):
    if b % 2 == 0:
        k = b // 2
        disc = k ** 2 - a * c
        if disc >= 0:
            return (-math.sqrt(disc) - k) / a, (math.sqrt(disc) - k) / a
    else:
        disc = b ** 2 - 4 * a * c
        if disc >= 0:
            return (-math.sqrt(disc) - b) / 2 * a, (math.sqrt(disc) - b) / 2 * a


def random_pass(n, len,
                symbols='qwertyuiopasdfghjklzxcvbnm_QWER-TYUIOPL___KJHGFDSAZXCVBNM1234567890'):
    all_passwords = []

    def gener_one_pass(len, symbols):
        pas = ''
        for i in range(len):
            pas += random.choice(symbols)
        return pas

    for i in range(n):
        all_passwords.append(gener_one_pass(len, symbols))
    return '\n'.join(all_passwords)


def gcd(a, b):
    if a != 0 and b != 0:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
    else:
        return a + b


def lcm(a, b):
    return a * b // gcd(a, b)


def fraction_reduction(chisl, znamen):  # сокращение дроби
    g = gcd(chisl, znamen)
    return (chisl // g, znamen // g)


def all_combinations(lis):
    end = lis[:]
    k = []
    for i in range(len(lis)):
        for j in range(len(lis)):
            end[-i] = lis[j]
            k.append(end[:])
    return k


def num_of_combinations(chars, lenght):
    return len(chars) ** lenght


def standart_number(x):
    l = str(x).split('.')
    if float(l[0]) > 10:
        y = x / (10 ** len(str(int(l[0]))) / 10)
        syblim = len(str(int(l[0]))) - 1
        print(str(round(y, 3)) + ' * ' + '10^' + str(syblim))
    elif float(l[0]) < -10:
        y = x / (10 ** len(str(int(l[0]))) / 100)
        syblim = len(str(int(l[0]))) - 2
        print(str(round(y, 3)) + ' * ' + '10^' + str(syblim))
    if x < 1 and x > -1:
        coun = 0
        while x < 1 and x > -1:
            x *= 10
            coun += 1
        print('{0} * 10^-{1}'.format(str(round(x, 3)), str(coun)))
    elif (x <= 10 and x >= -10):
        print(round(x, 3))


def count_system(num, by=10, to=2):
    ans_temp = 0
    if by <= 10:
        k = 0
        while num != 0:
            ans_temp += (num % 10) * (by ** k)
            k += 1
            num //= 10

    ans = ''
    while ans_temp != 0:
        ans += str(ans_temp % to)
        ans_temp //= to

    return int(ans[::-1])


def qsort(s, l, r):
    if l >= r:
        pass
    else:
        q = sum(s[l:r]) // (r - l)
        i = l
        j = r
        while j - i >= 0:
            while s[i] < q:
                i += 1

            while s[j] > q:
                j -= 1
            if i - j <= 0:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        qsort(s, l, j)
        qsort(s, i, r)

    return s


def deikstr(s, n, matrix):
    was = []
    weights = [math.inf for _ in range(n)]
    weights[s] = 0
    now = s
    was.append(now)
    while math.inf in weights:
        for i in range(n):
            if i not in was and matrix[now][i] + weights[now] < weights[i]:
                weights[i] = matrix[now][i] + weights[now]

        mn = math.inf
        for i in range(n):
            if mn > weights[i] and weights[i] != 0 and i not in was:
                mn = i
        now = mn
        was.append(now)

    for i in range(n):
        if i not in was and matrix[now][i] + weights[now] < weights[i]:
            weights[i] = matrix[now][i] + weights[now]

    return weights


def bfs(now, matrix):
    l = len(matrix)
    done = {now}
    q = [now]
    vers = []
    while len(q) != 0:
        now = q[0]
        vers.append(now)
        for i in range(l):
            if matrix[now][i] != math.inf and i not in done:
                q.append(i)
                done.add(i)
        q.pop(0)

    if len(q) == 0:
        return vers
