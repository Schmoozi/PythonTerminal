# Mohammed Dahri
# Terminal Program - January 2022

# Instance Variables
name = 0
cmd1 = 0
cmd2 = 0
cmd3 = 0
cmd4 = 0
command = 0
hist = []


##############################################################################################################
# CORE FUNCTION:
def core():
    global command
    while command != "terminate":
        if command == "info.log":
            loginhist()
            hist.append(command)
            command = input("\n> ")
        elif command == "info.terminal":  # Reveals information about the terminal
            infoterminal()
            hist.append(command)
            command = input("\n> ")
        elif command == "info.command":  # Reveals command history
            infocommand()
            hist.append(command)
            command = input("\n> ")
        elif command == "hist.cmd":  # Reveals all history
            histcmd()
            hist.append(command)
            command = input("\n> ")
        else:
            print("command does not exist -- no action was taken.")
            hist.append("'" + command + "' not")
            command = input("\n> ")


##############################################################################################################

# COMMAND STORAGE
# Prints log-in record
def loginhist():
    print("Logged in as " + name + " on (null)")


cmd1 = 1


# Prints information about the terminal
def infoterminal():
    print("\nTerminal: \nVersion: 0.1\nJanuary 2022")


cmd2 = 1


# Prints a select command history when called
def infocommand():
    if cmd1 == 1:
        print("Command 1 'info.log' loaded on (null) at (null) by " + name)
    if cmd2 == 1:
        print("Command 2 'info.terminal' loaded on (null) at (null) by " + name)
    if cmd3 == 1:
        print("Command 3 'info.command' loaded on (null) at (null) by " + name)


cmd3 = 1


# The shutdown process
def shutdown():
    noshutdown = []
    retry = 0
    confirm1 = 0
    confirm2 = 0
    cmd1 = 0
    if cmd1 == 0:
        print("Command 1 'info.log' disabled on (null) at (null) by " + name)
    elif cmd1 != 0:
        noshutdown.append("Command 1")
    cmd2 = 0
    if cmd2 == 0:
        print("Command 2 'info.terminal' disabled on (null) at (null) by " + name)
    elif cmd2 != 0:
        noshutdown.append("Command 2")
    cmd3 = 0
    if cmd3 == 0:
        print("Command 3 'info.command' disabled on (null) at (null) by " + name)
    elif cmd3 != 0:
        noshutdown.append("Command 3")
    if cmd4 == 0:
        print("Command 4 'hist.cmd' disabled on (null) at (null) by " + name)
    elif cmd4 != 0:
        noshutdown.append("Command 4")
    while len(noshutdown) != 0:
        for i in range(0, (len(noshutdown))):
            print("Termination of " + noshutdown[i] + " failed.")
        print("\nERROR 2: Termination cannot be completed without all commands being disabled.")
        while retry != "N":
            retry = input("Retry? (Y/N): ")
        if retry == "N":
            print("\nForce-qutting terminal may be dangerous, please confirm.")
            confirm2 = input("Please enter the password for " + name + ": ")
            while confirm2 != "1234":
                print("Incorrect passcode. Please try again.")
                confirm2 = input("Please enter the password for " + name + ": ")
            print("\nForce quitting terminal")
            exit("TERMINAL FORCEFULLY TERMINATED.")
    if len(noshutdown) == 0:
        print("All commands successfully disabled.")
        print(noshutdown)


# prints history
def histcmd():
    global hist
    for i in range(0, len(hist)):
        print(hist[i] + " ran by " + name + " on (null)")
        i = i + 1
    print("hist.cmd ran by " + name + " on (null)")


cmd4 = 1

##############################################################################################################

# LOG IN PROCESS
name = input("Please enter the administrator username: ")
while name != "Admin":  # The Administrator username
    print("'" + name + "' is not a valid user for this machine. Please try again.\n")
    name = input("Please enter the administrator username: ")
password = (input("Please enter the administrator password: "))
while password != "1234":  # The Administrator password
    print("Incorrect password. Please try again.\n")
    name = input("Please enter the administrator password: ")
print("\nTerminal\n" + "UNKNOWN SYSTEM > " + name + " > SYSTEM TERMINAL:")
command = input("> ")

while command != "terminate":
    core()

if command == "terminate":
    confirm = input("Terminate and close Terminal? (Y/N): ")
    if confirm == "N":
        core()
    elif confirm == "Y":
        print("SHUTTING DOWN COMMANDS")
        shutdown()
        print("\n TERMINAL SUCCESSFULY TERMINATED.")
        exit(0)
