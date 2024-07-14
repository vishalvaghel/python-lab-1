
EMPNAME =

def add_employee(name):
    EMPNAME.append(name)
    print(f"Added {name} to EMPNAME.")
    print(f"Current list of employees: {EMPNAME}\n")

def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Removed {name} from EMPNAME.")
    else:
        print(f"{name} is not found in EMPNAME.")
    print(f"Current list of employees: {EMPNAME}\n")

def append_employee(name):
    EMPNAME.append(name)
    print(f"Appended {name} to EMPNAME.")
    print(f"Current list of employees: {EMPNAME}\n")

if __name__ == "__main__":
    add_employee("John")
    add_employee("Jane")
    append_employee("Alice")
    remove_employee("John")
    remove_employee("Bob") 
