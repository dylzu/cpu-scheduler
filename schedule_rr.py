# Name: Dylan Corbari
# Student Number: 20341171
# I acknowledge all terms of DCU's Academic Integrity Policy

import sys
from driver import drive

def add_list(bursts):
    sum = 0
    for i in bursts:
        sum = sum + i
    return sum

def rr(bursts, dict, num):
    i = 0
    total_turn = 0
    turn = 0
    while sum(bursts) != 0 and i < len(bursts):
        total_turn = total_turn + turn
        if bursts[i] == 0:
            pass
        elif bursts[i] < 10:
            print("Running task [ {} {} {} ] => [ {} ]".format(dict[i][0], dict[i][1][0], bursts[i], bursts[i]))
            bursts[i] = 0
            turn =  turn + 5
            #print(turn)
        elif bursts[i] >= 10 and num == 0:
            print("Running task [ {} {} {} ] => [ 10 ]".format(dict[i][0], dict[i][1][0], bursts[i]))
            bursts[i] = bursts[i] - 10
            turn = turn + 10
            #print(turn)
        elif bursts[i] >= 10 and num == 1:
            print("Running task [ {} {} {} ] => [ 10 ]".format(dict[i][0], dict[i][1][0], bursts[i]))
            bursts[i] = bursts[i] - 10
            turn = turn + 10
            #print(turn)
        i = i + 1    

    print("Total turn around time =",total_turn)


def main():
    bursts = []

    for n in drive():
        slice = n[1][1]
        bursts.append(slice)

    rr(bursts, sorted(drive()), 0)
    while sum(bursts) != 0:
        rr(bursts, sorted(drive()), 1)
        
if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("no file found, ensure you have the input file in the same directory as this script and that its called properly in command line")
    except IndexError:
        print("no index found, check values are filled out")
    except ValueError:
        print("no value found, make sure values are integers")
