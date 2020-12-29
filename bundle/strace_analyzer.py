input_file = open("log","r")
syscalls = []
for line in input_file:
    if line.find("(") != -1:
        syscall = line[line.find(" ")+1:line.find("(")]
        if syscall[0] != "<" and syscall not in syscalls:
            syscalls.append(syscall)
syscalls = sorted(syscalls)
for syscall in syscalls:
    print("\"" + syscall + "\",")
