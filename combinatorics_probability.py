##Here is the code printing all 3-permutations of letters
##a, b, c, d, e, f. Run the code and observe the result for
##better understanding of permutations.

from itertools import permutations
for p in permutations("abcdef", 3):
    print("".join(p))

##Here is the code that lists all salads from the previous
##video. Here T=`tomato', B=`bell pepper', L=`lettuce',
##E=`eggplant'. You can run this code and observe the result.

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))

##The following code simulates an experiment we discussed in the
##previous video: we simulate a dice throw 100000 times and
##compute the average value. Run this code and compare the
##value with the result we obtained in the video.

from random import randint, seed
from datetime import datetime

seed(datetime.now())

num_rounds = 10**5
sum_of_values = 0

for _ in range(num_rounds):
    sum_of_values += randint(1, 6)

print("The average is {}".format(sum_of_values/(num_rounds*1.0)))

##The following code simulates the game from the previous video
##for 100000 rounds. Run the code and observe the result.

from random import randint, seed
from datetime import datetime

seed(datetime.now())

dice1=[2, 2, 2, 2, 3, 3]
dice2=[1, 1, 1, 1, 6, 6]

num_rounds = 10**5

assert len(dice1) == 6 and len(dice2) == 6

num_dice1_wins = 0
num_dice2_wins = 0

for _ in range(num_rounds):
    dice1_result = dice1[randint(0, 5)]
    dice2_result = dice2[randint(0, 5)]

    if dice1_result > dice2_result:
            num_dice1_wins += 1
    elif dice2_result > dice1_result:
            num_dice2_wins += 1

if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice1, dice2, num_rounds, num_dice1_wins-num_dice2_wins))
elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice2, dice1, num_rounds, num_dice2_wins-num_dice1_wins))
else:
        print("A tie")

##The following code simulates the games between all pairs of
##dices from the previous video for 100000 rounds. Run the code
## and observe the result.

from random import randint, seed
from datetime import datetime

seed(datetime.now())

dice1=[2, 2, 2, 2, 3, 3]
dice2=[1, 1, 1, 1, 6, 6]

num_rounds = 10**5

assert len(dice1) == 6 and len(dice2) == 6

num_dice1_wins = 0
num_dice2_wins = 0

for _ in range(num_rounds):
    dice1_result = dice1[randint(0, 5)]
    dice2_result = dice2[randint(0, 5)]

    if dice1_result > dice2_result:
            num_dice1_wins += 1
    elif dice2_result > dice1_result:
            num_dice2_wins += 1

if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice1, dice2, num_rounds, num_dice1_wins-num_dice2_wins))
elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice2, dice1, num_rounds, num_dice2_wins-num_dice1_wins))
else:
        print("A tie")

##First Task: Compare Two Dices
##Implement a function that takes two dices as input and
# computes two values: the first value is the number of times
# the first dice wins (out of all possible 36 choices),
# the second value is the number of times the second dice wins.
# We say that a dice wins if the number on it is greater than the
# number on the other dice.
#
# To debug your implementation, use the following test cases:
#
# Sample 1
#
# Input: dice1 = [1, 2, 3, 4, 5, 6], dice2 = [1, 2, 3, 4, 5, 6]
#
# Output: (15, 15)
#
# Sample 2
#
# Input: dice1 = [1, 1, 6, 6, 8, 8], dice2 = [2, 2, 4, 4, 9, 9]
#
# Output: (16, 20)

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins +=1
            elif j > i:
                dice2_wins +=1

    return (dice1_wins, dice2_wins)
#
# Now, your goal is to check whether among the three given dices
# there is one that is better than the remaining two dices.
#
# Implement a function that takes a list of dices and checks
#  whether there is dice (in this list) that is better than all
#  other dices. We say that a dice is better than another one,
#  if it wins more frequently (that is, out of all 36
#  possibilities, it wins in aa cases, while the second one
#  wins in bb cases, and a>ba>b). If there is such a dice,
#  return its (0-based) index. Otherwise, return -1.
#
# Use the following datasets for debugging:
#
# Sample 1
#
# Input: [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
#
# Output: -1
#
# Sample 2
#
# Input: [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
#
# Output: 2
#
# Sample 3
#
# Input: [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
#
# Output: -1

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    dice_names = {}
    wins = {}
    for i in range(len(dices)):
        dice_names[i] = dices[i]
        wins[i] = 0


    perms = list(itertools.combinations(dice_names,2))


    for i in perms:
        if count_wins(a[i[0]], a[i[1]])[0] > count_wins(a[i[0]], a[i[1]])[1]:
            wins[i[0]] += 1
        elif count_wins(a[i[0]], a[i[1]])[1] > count_wins(a[i[0]], a[i[1]])[0]:
            wins[i[1]] += 1
        else:
            pass


    if max(wins) == len(dices):
        return max(wins, key=wins.get)
    else:
        return -1

# You are now ready to play!
# Implement a function that takes a list of dices
# (possibly more than three) and returns a strategy. The
# strategy is a dictionary:
#
# If, after analyzing the given list of dices, you decide
# to choose a dice first, set strategy["choose_first"] to
# True and set strategy["first_dice"] to be the (0-based)
# index of the dice you would like to choose
#
# If you would like to be the second one to choose a dice,
# set strategy["choose_first"] to False. Then, specify,
# for each dice that your opponent may take, the dice that you
# would take in return. Namely, for each i from 0 to
# len(dices)-1, set strategy[i] to an index j of the dice
# that you would take if the opponent takes the i-th dice
# first.
#
# Use the following datasets for debugging:
#
# Sample 1
#
# Input: [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
#
# Output: {'choose_first': False, 0: 1, 1: 2, 2: 0}
#
# Sample 2
#
# Input: [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
#
# Output: {'choose_first': True, 'first_dice': 1}
#
# Note that your answers do not have to coincide with the
# answers above. First, the order of elements does not
# matter in the dictionary. Second, the dictionary might
# contain extra information that is not required in the
# statement of the problem. For example, {0: 3, 'first_dice': 1,
# 'choose_first': True} is also a correct output in Sample 2.

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)

    # write your code here

    return strategy
