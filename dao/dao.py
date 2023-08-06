import mysql.connector


# Abre a conexão com o banco de dados dado os parametros necessários
def OpenConnection():
    try:
        # Configuração da conexão com o banco de dados
        connection = mysql.connector.connect(
            host='localhost',      # Endereço do servidor do banco de dados
            user='coredumped',    # Nome de usuário do banco de dados
            password='coredumped',  # Senha do usuário do banco de dados
            database='mydb', # Nome do banco de dados a ser utilizado
        )
        # Verifica se a conexão foi bem-sucedida
        if connection.is_connected():
            # Imprime uma mensagem de sucesso caso a conexão tenha sido bem-sucedida
            print('Conexão bem-sucedida!')
            return connection
        else:
            return None
    except mysql.connector.Error as e:
        # Imprime uma mensagem de erro caso a conexão tenha sido mal-sucedida
        print('Erro ao conectar-se ao banco de dados:', e)
        return None
    
