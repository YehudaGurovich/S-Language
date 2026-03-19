from collections import defaultdict


VARIABLES = defaultdict(int)
LABEL_TABLE = {}


def clean_data(s_program) -> list[str]:
    return [line.replace(" ", "") for line in s_program if line != ""]


def create_label_table(s_program):
    for i, line in enumerate(s_program):
        label_name = line[:-1]
        if ':' in line and LABEL_TABLE.get(label_name) is None:
            LABEL_TABLE[label_name] = i
            print(f"Label {label_name} found at line {i}")


def run_s_program(s_program):
    s_program = clean_data(s_program)
    create_label_table(s_program)

    print(s_program)

    PC = 0

    while PC < len(s_program):
        line = s_program[PC]
        PC += 1


        # ERROR HERE IN THE WHOLE IF BLOCK
        if line.startswith("#"):  # Skip comments
            continue
        # Skip labels
        elif ':' in line:
            label(line)
        elif line.endswith('+1'):
            add(line)
        elif line.endswith('-1'):
            sub(line)
        elif '=' in line:
            PC = jump(line, PC - 1)
        else:
            noop(line)

    print(VARIABLES)


def jump(line, PC) -> int:
    print(f"JUMP {line}")
    # ifvar1!=0GOTOlabel
    _, label = line.split('GOTO')
    var, _ = line.split('!=')
    var = var[2:]  # Remove the 'IF' prefix
    return LABEL_TABLE[label] if VARIABLES[var] != 0 else PC + 1


def noop(line) -> None:
    print(f"NOOP {line}")
    VARIABLES[line] = VARIABLES[line]  # Initialize variable


def sub(line) -> None:
    print(f"SUB {line}")
    var = line.split('<-')[0]
    if VARIABLES[var] > 0:
        VARIABLES[var] -= 1


def add(line) -> None:
    print(f"ADD {line}")
    var = line.split('<-')[0]
    VARIABLES[var] += 1


def label(line) -> None:
    print(f"LABEL {line}")
