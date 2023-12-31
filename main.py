from utils.cli import execute_factorization, execute_graphs

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
