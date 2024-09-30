import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("bancoE")
cursor = conexao.cursor()

# ID do usuário e exemplar que serão usados no empréstimo
usuario_id = 1
exemplar_id = 1

# Verificar se o exemplar está disponível
cursor.execute(
    "SELECT disponivel FROM Exemplares WHERE exemplar_id = ?", (exemplar_id,)
)
exemplar_disponivel = cursor.fetchone()

if exemplar_disponivel and exemplar_disponivel[0] == 1:
    # Registrar o empréstimo
    cursor.execute(
        """
        INSERT INTO Emprestimos (usuario_id, exemplar_id, data_emprestimo, data_devolucao, estado, renovacoes)
        VALUES (?, ?, DATE('now'), DATE('now', '+7 day'), 'Pendente', 0)
        """,
        (usuario_id, exemplar_id),
    )

    # Atualizar a disponibilidade do exemplar
#     cursor.execute(
#         "UPDATE Exemplares SET disponivel = 0 WHERE exemplar_id = ?", (exemplar_id,)
#     )

#     # Confirmar transações
#     conn.commit()

#     print("Livro emprestado com sucesso!")
# else:
#     print("Exemplar não está disponível para empréstimo.")

# Fechar a conexão
conexao.commit()
conexao.close
