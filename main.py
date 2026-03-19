from initializer import initialize_program
from parser import run_s_program


if __name__ == "__main__":
    FILE_NAME = "testing/IF_EQ_ZERO.sl"

    s_program = initialize_program(FILE_NAME)
    run_s_program(s_program)
