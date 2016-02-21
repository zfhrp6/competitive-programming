# coding: utf-8


def main():
    num_of_cards = int(input())
    cards = [i for i in map(int, input().split(' '))]
    fst = 0
    cards.sort()
    cards.reverse()
    for i in range(len(cards)//2 + (len(cards)%2)):
        # print('i = ', i)
        fst += cards[2*i]
    # fst = sum([cards[2*i] for i in range(len(cards)//2+1)])
    print(fst)

if __name__ == '__main__':
    main()