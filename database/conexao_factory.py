import psycopg2


class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(
            host = 'berry.db.elephantsql.com',
            database = 'sdxiltor',
            user = 'sdxiltor',
            password = 'hPK7ZYe9cTtgAzWz2ieL7BPoovTqFy-c'
            )

conexao.close()