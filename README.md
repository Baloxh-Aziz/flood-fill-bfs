# Flood Fill Algorithm (BFS)

Implementation of the **Flood Fill** algorithm using **Breadth-First Search (BFS)** in Python.

## What is Flood Fill?
Flood Fill is an algorithm that fills a connected region of a grid with a new value — similar to the "paint bucket" tool in image editors.

## How it works
1. Start at a given cell `(x, y)`
2. Check if it matches the `old_color`
3. Change it to `new_color`
4. Use a queue (BFS) to visit all 4 neighboring cells (up, down, left, right)
5. Repeat until no more connected cells with `old_color` remain

## Example
```
Before Flood Fill:        After Flood Fill:
[1, 1, 0, 0]             [2, 2, 0, 0]
[1, 0, 0, 1]             [2, 0, 0, 1]
[1, 1, 1, 0]    →        [2, 2, 2, 0]
[0, 0, 1, 1]             [0, 0, 1, 1]
```
Starting at `(0,0)`, all connected `1`s are replaced with `2`.

## How to run
```bash
pip install -r requirements.txt
python floodfillassignment.py
```

## Author
Azizullah Asad 
