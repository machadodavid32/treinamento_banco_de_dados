import mysql.connector

# instalar > pip install mysql-connector-python

# Conectar-se a um banco de dados ou criá-lo
conexao = mysql.connector.connect(
    user='root', 
    password='senhaForte123',
    host='localhost',
    database='academia'
)

# Criar uma tabela
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cargo VARCHAR(255) NOT NULL,
        dataContratacao DATE NOT NULL
    );
''')
conexao.commit()

# # Inserir dados na tabela com base na entrada do usuário
# id1 = input("Digite o ID para o primeiro funcionário: ")
# nome1 = input("Digite o nome para o primeiro funcionário: ")
# cargo1 = input("Digite o cargo para o primeiro funcionário: ")
# dataContratacao1 = input("Digite a data de contratação para o primeiro funcionário (AAAA-MM-DD): ")

# query = "INSERT INTO Funcionarios VALUES (%s, %s, %s, %s)"
# valores1 = (id1, nome1, cargo1, dataContratacao1)

# cursor.execute(query, valores1)
# conexao.commit()

# Listar todos os dados da tabela após a atualização
cursor.execute("SELECT * FROM Funcionarios")
funcionarios = cursor.fetchall()
print(funcionarios)

# Atualizar dados na tabela
query = "UPDATE Funcionarios SET cargo = %s WHERE id = %s"
valores = ('Desenvolvedor Sênior',1)
cursor.execute(query, valores)
conexao.commit()


# Deletar dados da tabela
cursor.execute("DELETE FROM Funcionarios WHERE id = %s", (1,))
conexao.commit()