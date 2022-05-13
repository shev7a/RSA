from random import choice, randint
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
d = 0
open_key = dict()


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    nod, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return nod, x, y


def generate_keys():
    global d, open_key
    p = choice(prime_nums)
    q = choice(prime_nums)
    while q == p:
        q = choice(prime_nums)
    n = p * q
    f = (p - 1) * (q - 1)
    e = randint(2, f - 1)
    while gcd(e, f) != 1:
        e = randint(2, f - 1)
    nod, x, y = extended_gcd(e, f)
    while nod != 1:
        e = randint(2, f - 1)
        while gcd(e, f) != 1:
            e = randint(2, f - 1)
        nod, x, y = extended_gcd(e, f)
    d = ((x % f + f) % f)
    open_key['e'] = e
    open_key['n'] = n


def encrypt(original):
    ciphertext = []
    for c in original:
        if c not in rus_letters:
            continue
        else:
            ciphertext.append(alphabet[c] ** open_key['e'] % open_key['n'])
    print(*ciphertext)


def decrypt(cipher):
    original_text = ''
    for n in cipher:
        original_text += alphabet_2[n ** d % open_key['n']]
    print(original_text)


exit_program, need_encrypt, need_decrypt = False, False, False
rus_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
alphabet = dict()
alphabet_2 = dict()
i = 1
for l in rus_letters:
    alphabet[l] = i
    alphabet_2[i] = l
    i += 1
generate_keys()

while not exit_program:
    print('Введите номер нужной функции:\n 1. Зашифровать\n 2. Расшифровать\n 3. Выйти из программы')
    user_choice = int(input())
    if user_choice == 1:
        exit_program, need_encrypt, need_decrypt = False, True, False
    elif user_choice == 2:
        exit_program, need_encrypt, need_decrypt = False, False, True
    else:
        exit_program, need_encrypt, need_decrypt = True, False, False
        continue
    print('Введите исходный текст:') if need_encrypt else print('Введите зашифрованный текст:')
    text = input()
    if need_encrypt:
        encrypt(text.upper())
        continue
    if need_decrypt:
        text = map(int, text.split())
        decrypt(text)
        continue
