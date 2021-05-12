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
