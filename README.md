# maze_solver
A guided project from [boot.dev](https://www.boot.dev/courses/build-maze-solver-python)


## Ideas for Extending the Project

- Add other solving algorithms, like breadth-first search or A*
- Make the visuals prettier, change the colors, etc
- Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
- Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
- Make much larger mazes to solve
- Make it a game where the user chooses directions
- If you made it a game, allow the user to race an algorithm
- Make it 3 dimensional
- Time the various algorithms and see which ones are the fastest

## Added extensions
- a random solver: picks its next direction at random, while the depth-first solver always tries directions in the order of [right, bottom, left, top]
- added a sleep_time argument to Maze._animate so that the animation speed could be varied depending on which part of the code calls the method. At the moment, maze building is faster than maze solving.