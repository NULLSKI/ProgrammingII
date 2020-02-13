import random
import time
die1=0
die2=0
turn_count=1
total=0

while total !=7:
     play_again = 1
     die1 = random.randint(1,6)
     die2 = random.randint(1,6)
     print 'Die one is: {}'.format(die1)
     time.sleep(.25)
     print 'Die two is: {}'.format(die2)
     time.sleep(.5)
     total = die1 + die2
     if total == 7:
      if turn_count > 2 and turn_count < 10:
       print "You rolled a 7 in only {} turns! You win!".format(turn_count)
      else:
        if turn_count >= 10:
          print('Sorry it took you {} turns to roll a 7, you lose.').format(turn_count)
        else:
          print ("You rolled a 7 on your first try! You win!")
     else:
      turn_count = turn_count + 1
      print 'No dice, your total was {}'.format(total)
     time.sleep(.5)
  

