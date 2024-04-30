##8.1 Exercise: The random module, coin flipping
# import random
# flips = random.randint(0, 1)
# if flips == 1:
#     print('Head!')
# else:
#     print('Tails!')

import random
def coinflip():
    flips = random.randint(0, 1)
    if flips == 1:
        return 'Heads!'
    else:
        return 'Tails!'

def main():
    print('5 coin flips:')
    for _ in range(5):
        print(coinflip())

if __name__ == "__main__":
    main()