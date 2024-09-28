import sqlite3

def criar_banco():
    conexao = sqlite3.connect('amorimbikes.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            modelo TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    produtos = [
        ('Bikes', 'GTI Aro 29 21v', 1200.00),
        ('Bikes', 'Oggi 7.0 24v', 2300.00),
        ('Pneus', 'Pneu Levorin Praeiro', 80.00),
        ('Pneus', 'Pneu Chaoyang Victory', 120.00),
        ('Aros', 'Vzan Extreme', 80.00),
        ('Aros', 'Vmmax', 120.00),
        ('Manoplas', 'Manopla Absolute', 35.00),
        ('Manoplas', 'Manopla Yamada', 30.00),
        ('Suspensoes', 'Suspensao Absolute', 300.00),
        ('Suspensoes', 'Suspensao Rockshox', 1200.00),
        ('Freios', 'Freio Mecanico Absolute', 80.00),
        ('Freios', 'Freio Hidraulico Shimano', 350.00)
    ]

    cursor.executemany('INSERT INTO produtos (categoria, modelo, preco) VALUES (?, ?, ?)', produtos)

    conexao.commit()
    conexao.close()
