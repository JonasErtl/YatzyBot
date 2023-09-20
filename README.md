## Yatzy Solver
This is a program that will try to find the optimal moves in a game of Scandinavian Yatzy.  

## Initial Idea
- You get an input -> you check which combinations are already satisfied. 
- The probability to achieve each outcome is calculated. 
- A choice needs to be made based on the probabilities. 

## The Evaluation
- I have just begun working on the actual function that will decide the best move. So far to me it feels very inelegant and klunky, might have to choose some better approach. 
- Now the eval function has the ability to detect favorable combinations in a dice roll. However it is not able to decide which dice to keep and which to reroll if there wasn't found a matching combination in the first roll. 
- If no duplicates are found in the roll, all the dice should be rerolled. This is not optimal, but easy to implement. If a duplicate of numbers not yet taken is found, they are kept, the rest is rerolled. Should the subsequent 
rolls lead to a better outcome like FH, LS etc. these are kept. Otherwise the duplicate is noted down. 
