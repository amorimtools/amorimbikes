from criarbanco import criar_banco
from menu import exibir_menu, exibir_produtos

def main():
    criar_banco()
    while True:
        exibir_menu()
        opcao = input("Amorim Bikes - Catálogo ")

        if opcao == '1':
            exibir_produtos('Bikes')
        elif opcao == '2':
            exibir_produtos('Pneus')
        elif opcao == '3':
            exibir_produtos('Manoplas')
        elif opcao == '4':
            exibir_produtos('Aros')
        elif opcao == '5':
            exibir_produtos('Suspensoes')
        elif opcao == '6':
            exibir_produtos('Freios')
        elif opcao == '7':
            print("Amorim Bikes agradece seu interesse, até a próxima !")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
