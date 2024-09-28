import sqlite3

def exibir_menu():
    print("\nSelecione uma categoria para ver os produtos:")
    print("1. Bikes")
    print("2. Pneus")
    print("3. Manoplas")
    print("4. Aros")
    print("5. Suspensoes")
    print("6. Freios")
    print("7. Sair")

def obter_produtos_por_categoria(categoria):
    conexao = sqlite3.connect('amorimbikes.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT modelo, preco FROM produtos WHERE categoria = ?', (categoria,))
    produtos = cursor.fetchall()

    conexao.close()
    return produtos

def exibir_produtos(categoria):
    produtos = obter_produtos_por_categoria(categoria)
    if produtos:
        print(f"\nProdutos disponíveis na categoria '{categoria}':")
        for modelo, preco in produtos:
            print(f"Modelo: {modelo}, Preço: R$ {preco:.2f}")
    else:
        print(f"\nNenhum produto encontrado na categoria '{categoria}'.")
