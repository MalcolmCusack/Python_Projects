# -----------------------------------------+
# Malcolm Cusack                           |
# CSCI 127, Program 2                      |
# Last Updated: ???, 2019                  |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def same_suit(hand):
    same_suit = True
    suit = None
    for card in hand:
        if not suit:
            suit = card[1]
        elif suit != card[1]:
            same_suit = False
    return same_suit

def all_royal(hand):
    count = 0
    for card in hand:
        if card[0] == 10:
            count += 1
        elif card[0] == 11:
            count += 1
        elif card[0] == 12:
            count += 1
        elif card[0] == 13:
            count += 1
        elif card[0] == 14:
            count += 1
    if count == 5:
        return True
    else:
        return False

def five_in_row(hand):
    ranks = get_all_ranks(hand)
    ranks.sort()
    if ranks[0] + 1 == ranks[1] and ranks[1] + 1 == ranks[2] and ranks[2] + 1 == ranks[3] and ranks[3] + 1 == ranks[4]:
        return True
    else:
        return False

def n_of_kind(ranks, n):
    of_kind = False
    for i in range (len(ranks)):
        flag = ranks[i]
        count = 0
        for rank in ranks:
            if flag == rank:
                count += 1
        if count == n:
            of_kind = True
    return of_kind

def royal_flush(hand):
    return same_suit(hand) and all_royal(hand)
        
def straight_flush(hand):
    return same_suit(hand) and five_in_row(hand)

def straight(hand):
    return five_in_row(hand)
    
def four_of_a_kind(ranks):
    return n_of_kind(ranks, 4)
        
def full_house(ranks):
    return n_of_kind(ranks, 3) and n_of_kind(ranks, 2)

def three_of_a_kind(ranks):
    return n_of_kind(ranks, 3)

def two_pair(ranks):
    seen = list()
    for i in range (len(ranks)):
        flag = ranks[i]
        count = 0
        if flag in seen:
            continue
        for rank in ranks:
            if flag == rank:
                count += 1
        if count == 2:
            seen.append(flag)
    return len(seen) == 2


def one_pair(ranks):
    return n_of_kind(ranks, 2)


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+
main()
