from factorization.pollard_rho import pollard_rho_factorization


def execute_pollard_rho():
    composite_number = int(input("Enter the number to be factorized: "))
    first_factor = pollard_rho_factorization(composite_number)
    if first_factor:
        second_factor = int(composite_number / first_factor)
        print(f"{composite_number} = {first_factor} * {second_factor}")
    else:
        print(f"The algorithm could not factorize {composite_number} in sqrt({composite_number}) iterations.")
