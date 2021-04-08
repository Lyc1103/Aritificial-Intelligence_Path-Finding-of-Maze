# Path Finding of Maze

> Author : Ya Chen<br>
> Date : 2021 / 4 / 5<br>
> List :
>
> > <a href = "#description">Description</a><br><a href = "#algorithms">Algorithms</a><br><a href = "#exercise">Exercise Essentials</a><br><a href = "#reference">Reference</a><br><a href = "#execute">How to Execute</a>

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
<div id = "execute">

## How to Execute

## If you have the `make` commend :

If your device supports the `make` command, this will be much easier ( because my file name is very long... ).<br>
You can type `make` in Terminal to see the output of all Python files directly.<br>
You can also type in :<br>

> <p>>>>make<br>
> // Output all the execution results</p>

> <p>>>>make p1 <br>
> // Output the execution result of P1_UCS </p>

> <p>>>>make p2 <br>
> // Output the execution result of P2_IDS </p>

> <p>>>>make p3 <br>
> // Output the execution result of P3_IDASTAR </p>

<br>

## If you <font color = "red">do not</font> have the `make` commend :

If your device <b><font color = "red">does not</font></b> supports the `make` command, there will be a little inconvenience ( because my file name is very long... ).<br>
You can type in :<br>

> <p>>>>python mazeMaker.py <br>
> // If you want to random the looks of maze in input.txt</p>

> <p>>>>python P1_UCS.py <br>
> // Output the execution result of P1_UCS </p>

> <p>>>>python P2_IDS.py <br>
> // Output the execution result of P2_IDS </p>

> <p>>>>python P3_IDSSTAR.py <br>
> // Output the execution result of P3_IDASTAR </p>

</div>
<br>
<br>
<div id = "reference">

## Reference

1. <a href = "https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php">DIJKSTRA'S SHORTEST PATH ALGORITHM</a>
2. <a href = "https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search">Iterative deepening depth-first search</a>

</div>
