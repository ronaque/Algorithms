from graphs.hamiltonian_cycle import executar_backtracking_unico_ciclo


def executar_grafos():
    comando = int(input("Seleciona o que deseja executar:"
                        "\n0 - Voltar"
                        "\n1 - Backtracking para encontrar Ciclo Hamiltoniano em grafo não direcionado"
                        "\n"))

    match comando:
        case 0:
            return
        case 1:
            executar_backtracking_unico_ciclo()

    return


if __name__ == '__main__':
    comando = int(input("Seleciona o que deseja executar:"
                        "\n0 - Sair"
                        "\n1 - Algorithms em graphs"
                        "\n"))

    while comando != 0:
        match comando:
            case 1:
                executar_grafos()

        comando = int(input("Seleciona o que deseja executar:"
                            "\n0 - Sair"
                            "\n1 - Algorithms em graphs"
                            "\n"))

    print("Fim da execução")
