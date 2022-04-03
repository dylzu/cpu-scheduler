# Name: Dylan Corbari
# Student Number: 20341171
# I acknowledge all terms of DCU's Academic Integrity Policy

import sys
from driver import drive

def main():
    turn = 0
    wait = 0

    total_turn = 0
    total_wait = 0

    for n in sorted(drive(), key=lambda x:x[1][1]):
        burst = int(n[1][1])
        turn = turn + burst
        
        total_wait = total_wait + wait
        
        print("Running task [ {} {} {} ] turn around time [ {} ] waiting time [ {} ]".format(n[0], n[1][0], n[1][1], turn, wait))
        
        wait = wait + burst
        
        total_turn = total_turn + turn
        
    print("Average Turnaround Time:", total_turn/len(drive()))
    print("Average Waiting Time:", total_wait/len(drive()))

if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("no file found, ensure you have the input file in the same directory as this script and that its called properly in command line")
    except IndexError:
        print("no index found, check values are filled out")
    except ValueError:
        print("no value found, make sure values are integers")
