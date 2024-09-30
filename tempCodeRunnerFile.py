
# Atualizando os valores dos livros no banco de dados
cursor.execute("""
    UPDATE Livros
    SET valor = 59.90
    WHERE livro_id = 1;
""")

cursor.execute("""
    UPDATE Livros
    SET valor = 45.00
    WHERE livro_id = 2;
""")

cursor.execute("""
    UPDATE Livros
    SET valor = 34.99
    WHERE livro_id = 3;
""")

cursor.execute("""
    UPDATE Livros
    SET valor = 29.90
    WHERE livro_id = 4;
""")

