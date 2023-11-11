from graphs.hamiltonian_cycle import executar_backtracking_unico_ciclo
from utils.cli import execute_pollard_rho


def execute_graphs():
    command = int(input("Seleciona o que deseja executar:"
                        "\n0 - Voltar"
                        "\n1 - Backtracking para encontrar Ciclo Hamiltoniano em grafo não direcionado"
                        "\n"))

    match command:
        case 0:
            return
        case 1:
            executar_backtracking_unico_ciclo()

    return

def execute_factorization():
    command = int(input("Choose what you want to execute:"
                        "\n0 - Voltar"
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


if __name__ == '__main__':
    command = int(input("Choose what you want to execute:"
                        "\n0 - Exit"
                        "\n1 - Graph Algorithms"
                        "\n2 - Factorization Algoriths"
                        "\n"))

    while command != 0:
        match command:
            case 1:
                execute_graphs()
            case 2:
                execute_factorization()

        command = int(input("Choose what you want to execute:"
                            "\n0 - Exit"
                            "\n1 - Graph Algorithms"
                            "\n2 - Factorization Algoriths"
                            "\n"))

    print("Fim da execução")
