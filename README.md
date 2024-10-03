# Banco_Test
Testando Banco com DBeaver realizando Pesquisa

## Buscando dados e otimizando pesquisa implementando Prazo_entrega
![Captura de tela 2024-10-03 162303](https://github.com/user-attachments/assets/4f17081d-2814-4195-8408-68bb1bcafb69)

## Buscando dados e otimizando pesquisa implementando Prazo_entrega

```python

SELECT 
    Emprestimos.emprestimo_id,  -- Seleciona o ID do empréstimo da tabela 'Emprestimos'
    Emprestimos.estado,         -- Seleciona o estado do empréstimo (por exemplo, 'Pendente', 'Concluído')
    Emprestimos.data_emprestimo,  -- Seleciona a data em que o empréstimo foi realizado
    DATE(Emprestimos.data_emprestimo, '+5 days') AS prazo_entrega,  -- Calcula a data de entrega somando 5 dias à data do empréstimo
    Usuarios.nome AS nome_usuario,  -- Seleciona o nome do usuário que fez o empréstimo, renomeando a coluna como 'nome_usuario'
    Livros.titulo,                 -- Seleciona o título do livro que foi emprestado
    Livros.valor AS valor_unitario,  -- Seleciona o valor do livro, renomeando a coluna como 'valor_unitario'
    Livros.quantidade AS quantidade_livro,  -- Seleciona a quantidade de exemplares do livro, renomeando como 'quantidade_livro'
    (Livros.valor * Livros.quantidade) AS total_valor  -- Calcula o valor total (valor do livro multiplicado pela quantidade)
FROM 
    Livros  -- Tabela de livros que contém os detalhes dos livros emprestados
JOIN 
    Emprestimos ON Livros.livro_id = Emprestimos.usuario_id  -- Realiza uma junção entre a tabela 'Livros' e 'Emprestimos' com base em 'livro_id' (esta linha parece ter um erro, deveria ser `Emprestimos.livro_id`)
JOIN 
    Usuarios ON Emprestimos.usuario_id = Usuarios.usuario_id  -- Realiza uma junção entre 'Emprestimos' e 'Usuarios' para obter os dados do usuário que fez o empréstimo
WHERE 
    Emprestimos.estado = 'Pendente'  -- Filtra os empréstimos que estão no estado 'Pendente'
ORDER BY 
    Emprestimos.emprestimo_id;  -- Ordena os resultados com base no ID do empréstimo em ordem crescente


```



```python
import sqlite3

conexao = sqlite3.connect("bancoE")
cursor = conexao.cursor()

# Criando Tabela Autores
# cursor.execute(
# """
# CREATE TABLE Autores(
# autor_id INT,
# nome VARCHAR(100),
#  nacionalidade VARCHAR(50));
#   """
# )

# Inserindo Autores
# cursor.execute(
#    """
#   INSERT INTO Autores (autor_id, nome, nacionalidade)
#   VALUES
#   (1, 'Caíque Cardoso', 'Brasileiro'),
#   (2, 'Simon Collison', 'Americano'),
#  (3, 'Machado de Assis', 'Brasileiro'),
#  (4, 'Clarice Líspecto', 'Brasileiro');
#  """
# )

# Criando Tabela Editoras
# cursor.execute(
#     """
#     CREATE TABLE Editoras(
#     editora_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(100) NOT NULL);
#     """
# )

# Inserindo Editoras
# cursor.execute(
#     """
#     INSERT INTO Editoras (editora_id, nome)
#     VALUES
#     (1, 'Editora Ciência Moderna'),
#     (2, 'Alta Books'),
#     (3, 'Editora Saraiva'),
#     (4, 'Penguin Books');
#     """
# )

# Criando Tabela de Livro
# cursor.execute(
#     """
#     CREATE TABLE Livros (
#         livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         titulo TEXT NOT NULL,
#         editora_id INTEGER NOT NULL,
#         max_renovacoes INTEGER,
#         FOREIGN KEY (editora_id) REFERENCES Editoras(editora_id)
#     );
#     """
# )

# #Inserindo Livro
# cursor.execute(
#     """
#     INSERT INTO Livros (livro_id, titulo,  editora_id, max_renovacoes)
#     VALUES
#     (1, 'Orientação a Objetos na Prática', 1, 3),
#     (2, 'Desenvolvendo CSS na Web', 2, 1),
#     (3, 'Dom Casmurro', 3, 4),
#     (4, 'A Hora da Estrela', 2, 3);
#     """
# )

# Criando a Tabela Exemplares
# cursor.execute(
#     """
#     CREATE TABLE Exemplares (
#     exemplar_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     livro_id INTEGER,
#     codigo VARCHAR(50),
#     disponivel BOOLEAN DEFAULT 1,
#     FOREIGN KEY (livro_id) REFERENCES Livros(livro_id));
#     """
# )
# cursor.execute(
#     """
# ALTER TABLE Exemplares ADD COLUMN  estado VARCHAR(25);
# """
# )

# Criando a tabela Usuarios
# cursor.execute(
#     """
#     CREATE TABLE Usuarios (
#     usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(100) NOT NULL,
#     telefone VARCHAR(15),
#     nacionalidade VARCHAR(50));
#     """
# )

# Criando a tabela Emprestimos
# cursor.execute(
#     """
# CREATE TABLE Emprestimos (
#     emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     usuario_id INTEGER,
#     exemplar_id INTEGER,
#     data_emprestimo DATE,
#     data_devolucao DATE,
#     estado VARCHAR(25),
#     renovacoes INTEGER DEFAULT 0,
#     FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
#     FOREIGN KEY (exemplar_id) REFERENCES Exemplares(exemplar_id)
# );
# """
# )
#

# Adicionando a coluna 'valor' à tabela 'Livros'
# cursor.execute("""
#     ALTER TABLE Livros
#     ADD COLUMN valor DECIMAL(10, 2);
# """)

# Atualizando os valores dos livros no banco de dados
# cursor.execute("""
#     UPDATE Livros
#     SET valor = 89.90
#     WHERE livro_id = 4;
# """)

# (Repita para os outros valores...)


# Adicionando a coluna 'Quantidade' à tabela 'Livros'
# cursor.execute("""
#     ALTER TABLE Livros
#     ADD COLUMN quantidade DECIMAL(10, 2);
# """)

# Atualizando os quantidade dos livros no banco de dados
# cursor.execute("""
#     UPDATE Livros
#     SET quantidade = 5
#     WHERE livro_id = 4;
# """)

# (Repita para os outros valores...)


# #Inserindo Livro Pendentes
# cursor.execute(
#     """
#     INSERT INTO Emprestimos (usuario_id, exemplar_id, data_emprestimo, data_devolucao, estado )
#     VALUES
#     (1, 1, '2024-09-01', '2024-09-15', 'Pendente'),
#     (2, 2, '2024-09-05', '2024-09-20', 'Pendente'),
#     (3, 3, '2024-09-10', '2024-09-25', 'Devolvido'),
#     (4, 4, '2024-09-12', '2024-09-28', 'Pendente');
#     """
# )


# #Inserindo Lista Usuarios
# cursor.execute(
#     """
#     INSERT INTO Usuarios (usuario_id, nome, telefone, nacionalidade )
#     VALUES
#     (4, 'Frank', '20172017', 'Brasil'),
#     (5, 'Daniela', '1984231984', 'Brasil'),
#     (6, 'João', '20172017', 'Brasil');
#     """
# )

# Inserindo Livro
# cursor.execute(
#     """
#     INSERT INTO Livros (livro_id, titulo,  editora_id, max_renovacoes)
#     VALUES
#     (1, 'Orientação a Objetos na Prática', 1, 3),
#     (2, 'Desenvolvendo CSS na Web', 2, 1),
#     (3, 'Dom Casmurro', 3, 4),
#     (4, 'A Hora da Estrela', 2, 3);
#     """
# )


# Criando tabela Livro e Autores
# cursor.execute(
#     """
# CREATE TABLE Livro_Autores (
#     livro_id INTEGER,
#     autor_id INTEGER,
#     PRIMARY KEY (livro_id, autor_id),
#     FOREIGN KEY (livro_id) REFERENCES Livros(livro_id),
#     FOREIGN KEY (autor_id) REFERENCES Autores(autor_id)
# );
#  """
# )

# Inserindo Livro e Autores
# cursor.execute(
#     """
#     INSERT INTO Livro_Autores (livro_id, autor_id)
#     VALUES
#     (1, 1),
#     (2, 2),
#     (3, 3),
#     (4, 4);
#     """
# )

# Inserindo Exemplares
# cursor.execute(
#     """
#     INSERT INTO Exemplares (exemplar_id, livro_id,  codigo, disponivel)
#     VALUES
#     (1, 1, 'OOP001', 1),
#     (2, 1, 'OOP002', 1),
#     (3, 2, 'DCW001', 1),
#     (4, 3, 'DC001', 0),
#     (5, 4, 'HE001', 2);
#     """
# )

# ----------------------- Consulta------------------------------
# ==================> todos os livros disponivel <================
# dado = cursor.execute(
#     """
# ==================> CAPIAR ESTA PARTE <========================
# SELECT Livros.titulo, Exemplares.codigo
# FROM Livros
# JOIN Exemplares ON Livros.livro_id = Exemplares.livro_id
# WHERE Exemplares.disponivel = 1;
# ===============================================================
#     """
# )

# Encontrar todos os livros emprestados
# dado = cursor.execute(
#     """
# ==================> CAPIAR ESTA PARTE <========================
# SELECT Livros.titulo, Exemplares.codigo
# FROM Emprestimos
# JOIN Exemplares ON Emprestimos.exemplar_id = Exemplares.exemplar_id
# JOIN Livros ON Exemplares.livro_id = Livros.livro_id
# WHERE Emprestimos.estado = 'Pendente'
# ===============================================================
#     """
# )

# VAI CONTAR QUANTOS NOMES TEM NO USUARIOS
# ==================> CAPIAR ESTA PARTE <========================
# SELECT nome, COUNT(*) AS total
# FROM Usuarios
# GROUP BY nome
# HAVING COUNT(*) > 1;
# ===============================================================

# VAI SOMAR QUANTIDADE X VALOR TRAZENDO TOTAL
# ==================> CAPIAR ESTA PARTE <========================
# SELECT
#     Livros.titulo, Livros.valor, Livros.quantidade,
#     (Livros.valor * Livros.quantidade) AS total_valor
# FROM
#     Livros
# ===============================================================

# VAI BUSCAR LISTA DE EMPRESTIMOS SE PENDENTE OU DEVOLVIDO
# ==================> CAPIAR ESTA PARTE <========================

# SELECT
#     Livros.titulo,
#     Exempl
