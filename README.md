# Path Finding of Maze

> Author : Ya Chen<br>
> Date : 2021 / 4 / 5<br>
> List :
>
> > <a href = "#description">Description</a><br>
> > <a href = "#algorithms">Algorithms</a><br>
> > <a href = "#exercise">Exercise Essentials</a><br>
> > <a href = "#reference">Reference</a>

---

<br>
<div id = "description">

## Description

First of all, suppose there is a ( H + 2 ) x ( W + 2 ) maze with an outer wall, the grid content of `*` <b>is the wall and cannot be walked into</b>. The grid content `0 ~ 9` indicates the height of the grid, which can be walked into, but if you walk from a grid with height c to the next grid with height d, it costs the robot <b>10 + (c-d)<sup>2</sup></b> in power cost.<br>
The robot starts from the top left corner and can move to any of the four adjacent spaces. If it finally reaches the end point in the lower right corner, the task is completed.<br>
<b>Of course, it would be great to find the best solution that costs the least total power!</b>

</div>
<br>
<br>
<div id = "algorithms">

## Algorithms

I will use the following three algorithms to perform the exercise:

1. Uniform-cost search ( An algorithm likes Dijkstra's single-source-shortest-path algorithm )
2. Iterative Deeping Depth-First Search ( IDS or IDDFS )
3. Iterative Deeping A* ( IDA* )

</div>
<br>
<br>
<div id = "exercise">

## Exercise Essentials

- How to display the output plate?
- How the route should be generated?
- How to implement <b>Frontier</b>?
- What informations to store at the node?
- How to distinguish repetition?
- Will there be infinite loops?
- Will the memory explode?
- Will the result be the best solution?
- Which heuristic result is better to use?
- How to estimate the Time complexity and Space complexity?

</div>
<br>
<br>
<div id = "reference">

## Reference

1. <a href = "https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php">DIJKSTRA'S SHORTEST PATH ALGORITHM</a>
2. <a href = "https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search">Iterative deepening depth-first search</a>
