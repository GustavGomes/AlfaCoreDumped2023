import mysql.connector


def OpenConnection():
    try:
        # Configuração da conexão com o banco de dados
        connection = mysql.connector.connect(
            host='localhost',      # Endereço do servidor do banco de dados
            user='coredumped',    # Nome de usuário do banco de dados
            password='coredumped',  # Senha do usuário do banco de dados
            database='mydb', # Nome do banco de dados a ser utilizado
        )

        if connection.is_connected():
            print('Conexão bem-sucedida!')
            return connection
        else:
            return None
    except mysql.connector.Error as e:
        print('Erro ao conectar-se ao banco de dados:', e)
        return None
    
