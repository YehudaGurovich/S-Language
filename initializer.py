from macros import MACRO_HANDLERS


def initialize_program(FILE_NAME) -> list[str]:

    with open(FILE_NAME, "r") as f:
        s_program = f.readlines()

    for line in range(len(s_program)):
        s_program[line] = s_program[line].strip()

    s_program = [line for line in s_program if line != ""]

    vars_to_init = initialize_variables(s_program)
    s_program = add_initialized_variables(s_program, vars_to_init)

    s_program = expand_macros(s_program)

    print(s_program)

    return s_program


def initialize_variables(s_program) -> list[int]:

    init_vars = []

    # Uncomment the following lines to allow user input for variable initialization
    # var = ''
    # while var != -1:
    #     var = int(input("Enter variable number to initialize (or -1 to stop): "))
    #     if var != -1:
    #         init_vars.append(var)

    return init_vars


def add_initialized_variables(s_program, init_vars) -> list[str]:

    for i, var in enumerate(init_vars):
        print(f"Initializing variable X{i + 1} with value {var}")

        for _ in range(var):
            s_program.insert(0, f"X{i + 1}<-X{i + 1}+1")

    return s_program


def expand_macros(s_program) -> list[str]:

    expanded = []
    for line in s_program:
        applied = False
        for pattern, func in MACRO_HANDLERS.items():
            # ERROR HERE
            new_lines = func(line)
            if new_lines != [line]:
                expanded.extend(new_lines)
                applied = True
                break
        if not applied:
            expanded.append(line)
    return expanded
