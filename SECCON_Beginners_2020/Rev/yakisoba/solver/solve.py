# -*- coding: utf-8 -*-
import angr, claripy

p = angr.Project("./yakisoba")
state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)

simgr.explore(find=lambda s: b"Correct!" in s.posix.dumps(1), avoid=lambda s: b"Wrong!" in s.posix.dumps(1))
print(simgr.found[0].posix.dumps(0))
print(simgr.found[0].posix.dumps(1))
