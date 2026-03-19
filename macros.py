MACRO_HANDLERS = {}
LABEL_COUNTER = 0
VARIABLES_COUNTER = 0


def new_label() -> str:
    new_label_name = f"DYNAMIC_LABEL_{LABEL_COUNTER:= LABEL_COUNTER + 1}"
    return new_label_name


def new_variable() -> str:
    new_var_name = f"Z_DYNAMIC_VAR_{VARIABLES_COUNTER:= VARIABLES_COUNTER + 1}"
    return new_var_name


def macro(pattern):
    """Decorator to register a macro handler."""
    def decorator(func):
        MACRO_HANDLERS[pattern] = func
        return func
    return decorator


# def expand_assign_value_to_variable(line):
#     # X1<-5
#     if


@macro("IF_EQ_ZERO")
def expand_if_equal_zero(line):
    # implement expansion
    if line.startswith("GOTO"):
        label = line[4:]
        new_variable = new_variable()
        return [
            f"{new_variable}<-{new_variable}+1",
            f"IF{new_variable}!=0GOTO{label}",
        ]
    return [line]


# @macro("CLEAR")
# def expand_clear_variable(line):
#     # Z_DYNAMIC_VAR_1<-0
#     pass
