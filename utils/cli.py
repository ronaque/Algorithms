from encryption_decryption.rc5 import rc5_encryption_algorithm, rc5_entry
from factorization.pollard_rho import pollard_rho_factorization
from graphs.hamiltonian_cycle import get_first_cycle_backtracking


def execute_pollard_rho():
    composite_number = int(input("Enter the number to be factorized: "))
    first_factor = pollard_rho_factorization(composite_number)
    if first_factor:
        second_factor = int(composite_number / first_factor)
        print(f"{composite_number} = {first_factor} * {second_factor}")
    else:
        print(f"The algorithm could not factorize {composite_number} in sqrt({composite_number}) iterations.")


def execute_encryption_decryption():
    command = int(input("Choose what you want to execute:"
                        "\n0 - Exit"
                        "\n1 - RC5"
                        "\n"))

    match command:
        case 0:
            return
        case 1:
            rc5_entry()

    return

def execute_factorization():
    command = int(input("Choose what you want to execute:"
                        "\n0 - Exit"
                        "\n1 - Pollard's Rho Factorization"
                        "\n"))

    match command:
        case 0:
            return
        case 1:
            execute_pollard_rho()
        case _:
            print("Invalid command")

    return


def execute_graphs():
    command = int(input("Choose what you want to execute:"
                        "\n0 - Exit"
                        "\n1 - Hamiltonian Cycle backtracking"
                        "\n"))

    match command:
        case 0:
            return
        case 1:
            get_first_cycle_backtracking()

    return
