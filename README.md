# monty_hall_simulation
Simulates the Monty Hall problem with 3 doors

The Monty Hall problem is a very (to me at least) counter-intuitive probability mind experiment which
contorts my brain and fascinates me at the same time. I can just about understand the
probabilistic arguments, but I still find it confusing.  This program is an experimental
simulator to see what numbers we get when the player decides to stick or switch.

If you are having problems understanding the outcome, I find it helps to imagine that there
are a million doors rather than 3.  After you choose your door (1/1,000,000 chance of hiding the car)
Monty opens up 999,998 doors that hide goats to leave one door still closed.  Now which door do you think
is most likely to hide the car? The one you choose, or the one that Monty avoided opening while
he opened all 999,998 other doors?!  It seems obvious to me that the other door that Monty left un opened
has a massively higher chance of hiding the door than the original choice!  As N reduces to 3 this
obviousness reduces greatly however!

Summary:
--------

There are 3 doors, behind one lies a car, while behind the other two are goats.
A player chooses a door at random.  Monty then opens one of the other doors to show that
there is no car behind it.  Monty asks the player if they would like to stick with their
door or switch to the other un-opened door.

If the player sticks with their door then their chance of winning the car should be 1/3
If the player switches door then their chances of winning the car increases to 2/3!!!

For more info: https://en.wikipedia.org/wiki/Monty_Hall_problem
