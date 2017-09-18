# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The process of constraint propagation includes a set of constraints and a set of all possible values. When eliminating the possibilities, we need to first examine the number of posibilities of one specific cell. If two of the cells, naked twins, in its row, column, square or diagonal line have same possibilities, we can eliminate one possibility from another cell in the neibourhood. For instance, if in row E, two cells (F1, F2) have possibilities of "2" and "3", and another cell (E1) in the column corresbonding to F1 has "3" and "9", we can then eliminate the "3" from E1 and F1. Then, due to the elimination, the possibility for the three cells are now clear, which is F1-2, F2-3 and E1-9. During the process of reducing possible values of cells other than naked twins, we change the constraints of the cells in the neighbourhood then deduce the value that is only possible for the specific cell.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: First, we add the diagonal cells to the neighbourhood of all the relevant cells. By adding these diagonal units, we increased the constraints of the game. If we want to use the "naked twins" strategy to solve this problem, the increased constraint will eliminate more possibilities and make the game easier.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

