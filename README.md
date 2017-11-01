# Problem Title: Project File Dependencies
Project managers, such as the UNIX utility make, are used to maintain large software projects made up
from many components. Users write a project file specifying which components (called tasks) depend on
others and the project manager can automatically update the components in the correct order.
Write a program that reads a project file from stdin and writes to stdout the order in which the tasks
should be performed.

## Input format
The first line of input specifies the number of N tasks and the number of M rules.
The rest of the input consists of M rules, one in each line, specifying dependencies using the following
syntax: T0 k T1 T2 ... Tk

## Output format
The task order

### Notes
- Solved using Kahn's Algorithm that solves the problem in linear time
- A heap was used as data structure to hold the next nodes to evaluate
- Developed using python 2.7.12
- Usage: python main.py <input-file>

João Ramalho (ramalho.vfc@gmail.com)