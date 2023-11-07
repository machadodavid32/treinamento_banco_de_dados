import sqlite3

"""Atenção, o código abaixo deverá ser organizado em funções, já que existem mudanças 
toda a vez que for colocar o código pra funcionar. Exemplo: Toda vez que for rodar este codigo, 
teremos que cadastrar novamente os dados na tabela. Não precisa se colocar em funções."""

# Conectar a um banco de dados
conexao = sqlite3.connect('funcionarios.db') # caso não haja um banco com este nome, ele vai criar um.

# Criar uma tabela
cursor = conexao.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Funcionarios (
                   id INTERGER PRIMARY KEY,
                   nome TEXT NOT NULL,
                   cargo TEXT NOT NULL,
                   dataContratacao TEXT NOT NULL 
               );
               ''')
conexao.commit()


# Inserir dados em uma tabela
nome = input('Digite o nome: ')
cargo = input('Digite o cargo: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')

cursor.execute("INSERT INTO Funcionarios VALUES (?,?,?,?)", (3, nome, cargo, data))
conexao.commit()

nome = input('Digite o nome: ')
cargo = input('Digite o cargo: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')

cursor.execute("INSERT INTO Funcionarios VALUES (?,?,?,?)", (4, nome, cargo, data))
conexao.commit()

# Obs: os 4 ? são as 4 colunas, o numeros 1 e 2 representam o id, primeira coluna


# listar todos os dados de uma tabela
cursor.execute("SELECT * FROM Funcionarios")
funcionarios = cursor.fetchall()
print(funcionarios)
  
  
# Alterar dados de uma tabela
cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id = ?", ('desenvolvedor senior', 2))
conexao.commit()
  
# Excluir dados de uma tabela
cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (1,)) # Aqui deletando id 1. 
# obs: A virgula depois do 1 é obrigatoria. Caso haja um segundo id pra deletar, a virgular depois..
# ..do segundo id ñ existe.

# Obrigatorio, no caso do sqlite, fechar a conexão após finalizar as operações
conexao.close()
  