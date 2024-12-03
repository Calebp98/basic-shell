import sys
import os
import subprocess
import shlex

def main():
    valid_commands = {"echo", "exit", "type", "pwd", "cd"} 

    def check_path(arg):
        path = os.environ.get('PATH', '') 
        path = path.split(":")
        for dir in path:
            try:
                if arg in set(os.listdir(dir)):
                    return os.path.join(dir, arg)
            except (FileNotFoundError, PermissionError): 
                continue
        return False

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush() 
        try:
            received_input = shlex.split(input())
            if not received_input:  
                continue

            
            command = received_input[0]
            args = received_input[1:]
                
            if command == "exit" or command == "exit 0":  
                sys.exit(0)
            elif command == "echo":
                print(" ".join(args))
            elif command == "type":
                arg = args[0]
                if arg in valid_commands:
                    print(f"{arg} is a shell builtin")
                else:
                    file_path = check_path(arg)
                    if file_path:
                        print(f"{arg} is {file_path}")
                    else:
                        print(f"{arg}: not found")
            elif command == "pwd":
                print(os.getcwd())
            elif command == "cd":
                if args[0] == "~":
                    os.chdir(os.path.expanduser("~"))
                else:
                    try:
                        os.chdir(args[0])
                    except FileNotFoundError:
                        print(f"cd: {args[0]}: No such file or directory")
            else:
                file_path = check_path(command)
                if file_path:
                    temp = subprocess.run([file_path] + args) #just assigning to suppress some subprocess func output
                else:   
                    print(f"{command}: command not found")
        except KeyboardInterrupt: 
            print()
            continue


if __name__ == "__main__":
    main()
