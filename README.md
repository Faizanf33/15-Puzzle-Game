## 15-Puzzle-Game (Greedy Approach)
_______________________________

- *Accidental implementation* (Expected was heuristic approach)
- Simple logic/no big deal.

> How it works:
> 1. Given an array(1-D) as initial state **(Must be of len=16)**.
> 2. Check whether goal state is reachable.
> 3. Find the position of empty **None** block.
> 4. Enlist possible moves.
> 5. Find the cost of each move.
> 6. Apply move with the minimum cost.
> 7. Repeat 4,5,6 until goal state is found.

### Why algorithm fails for fairly complicated/large problems.
- Algorithm moves on the basis of current possible moves (no track/record).
- Moves with no/same minimum cost ends to repetition.
- Repetition is somehow solved using randomness but complicates the problem.
