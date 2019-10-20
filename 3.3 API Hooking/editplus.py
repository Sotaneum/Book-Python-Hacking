"""
https://github.com/Sotaneum/Book-Python-Hacking
LEE DONG GUN 2015-06-13
"""
# Support Python 2
import utils, sys
from pydbg import *
from pydbg.defines import *

dbg=pydbg()
isProcess =False

orgPattern="love"
repPattern="hate"
processName="editplus.exe"

def replaceString(dbg,args):
    buffer = dbg.read_process_memory(args[1],args[2])

    if orgPattern in buffer:
        print "[APIHooking] Befor : %s" % buffer
        buffer = buffer.replace(orgPattern,repPattern)
        replace = dbg.write_process_memory(args[1],buffer)
        print "[APIHokking] After : %s" % dbg.read_process_memory(args[1],args[2])
    return DBG_CONTINUE

for(pid,name) in dbg.enumerate_processes():
    if name.lower() == processName:
        isProcess = True
        hooks=utils.hook_container()

        dbg.attach(pid)
        print "Saves a process handle in self.h_process of pid[%d]" % pid
        hookAddress = dbg.func_resolve_debuggee("kernel32.dll","WriteFile")

        if hookAddress:
            hooks.add(dbg, hookAddress, 5, replaceString, None)
            print "sets a breakpoint at the designated address: 0x%08x" % hookAddress
            break
        else :
            print "[Error] : couldn't resolve hook addree"
            sys.exit(-1)
if isProcess:
    print "waiting for occuring debugger event"
    dbg.run()
else:
    print "[Error] : There in no process [%s]" % processName
    sys.exit(-1)
