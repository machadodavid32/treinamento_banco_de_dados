import psycopg2

# instalar > pip install psycopg2-binary
# Lembrar de fazer funções

# Conectar ao banco de dados
# Os dados a seguir PRECISAM ser substituídos com os dados do SEU banco de dados
conexao = psycopg2.connect(
    dbname='railway', 
    user='postgres', 
    password='Y4EVahgoeOcJHhyEsi2m',
    port='7126',
    host='containers-us-west-32.railway.app'
)

# Criar tabela Funcionarios
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cargo VARCHAR(255) NOT NULL,
        datacontratacao DATE NOT NULL
    );
''')
conexao.commit()

# Pedir ao usuário para inserir dados do funcionário
nome = input("Informe o nome do funcionário: ")
cargo = input("Informe o cargo do funcionário: ")
datacontratacao = input("Informe a data de contratação (AAAA-MM-DD): ")

# Inserir dados do funcionário no banco de dados
cursor.execute("INSERT INTO Funcionarios (nome, cargo, datacontratacao) VALUES (%s, %s, %s)",(nome, cargo, datacontratacao))
conexao.commit()

# Atualizar dados do funcionário
id_atualizar = input("Informe o ID do funcionário que você deseja atualizar: ")
novo_cargo = input("Informe o novo cargo para este funcionário: ")
cursor.execute(
    "UPDATE Funcionarios SET cargo = %s WHERE id = %s",
    (novo_cargo, id_atualizar)
)
conexao.commit()


# Selecionar e exibir todos os funcionários
cursor.execute("SELECT * FROM Funcionarios")
funcionarios = cursor.fetchall()
print(funcionarios)


# Deletar dados do funcionário
id_deletar = input("Informe o ID do funcionário que você deseja deletar: ")
cursor.execute(
    "DELETE FROM Funcionarios WHERE id = %s",
    (id_deletar,)
)
conexao.commit()