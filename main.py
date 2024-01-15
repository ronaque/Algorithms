from utils.cli import execute_factorization, execute_graphs, execute_encryption_decryption

def command():
    return int(input("Choose what you want to execute:"
                        "\n0 - Exit"
                        "\n1 - Graph Algorithms"
                        "\n2 - Factorization Algoriths"
                        "\n3 - Encryption and Decryption Algorithms"
                        "\n"))

if __name__ == '__main__':
    execute = command()

    while execute != 0:
        match execute:
            case 1:
                execute_graphs()
            case 2:
                execute_factorization()
            case 3:
                execute_encryption_decryption()

        execute = command()

    print("End of Execution")
