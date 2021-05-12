# angr


## What Can Do
angr is a python framework of binary analysis.  
In order to find the input arguments that meet the specific conditions, angr analyzes the assembly structure and the memory address.  
Unlike blute force attack, the performance of angr is faster.

## Environment
python 3

## How to Use
angr installs through pip command.  
```$ pip install angr```

We provide a sample code as below.

## Code
[solve.py](solve.py)
```python solve.py
# -*- coding: utf-8 -*-
import angr

elf = input("Input File Name: ")
p = angr.Project("./" + elf)
state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)

# Change the following comments which are "Correct!" and "Wrong!" as needed
simgr.explore(find=lambda s: b"Correct!" in s.posix.dumps(1), avoid=lambda s: b"Wrong!" in s.posix.dumps(1))
print(simgr.found[0].posix.dumps(0))
print(simgr.found[0].posix.dumps(1))
```
