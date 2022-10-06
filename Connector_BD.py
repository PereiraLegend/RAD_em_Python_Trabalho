# from RAD_em_Python_Trabalho import Trabalho_RAD_em_Python
import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'Cliente'
username = 'postgres'
pwd = '12345'
port = 5432
conn = None
conecta = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = 12345,
        port = port
    )
except:
    print("ERRO ao conectar no banco de dados!")

conecta = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conecta.execute('DROP TABLE IF EXISTS TABELACLIENTE')
create_script = """ CREATE TABELA IF NOT EXISTS CLIENTE (
                        CPF varchar(15) PRIMARY KEY,
                        Nome varchar(50) NOT NULL,
                        Sobrenome varchar(50) NOT NULL,
                        Idade varchar(2) NOT NULL,
                        Conta varchar(30) NOT NULL )"""
conecta.execute(create_script)
conecta = conn.cursor()
conecta.execute('DROP TABLE IF EXISTS TABELACLIENTE')
create_script = """CREATE TABELA IF NOT EXISTS DADOS (
                        Agencia varchar(50) NOT NULL,
                        Numero varchar(50) NOT NULL,
                        Saldo varchar(50) NOT NULL,
                        Gerente varchar(50) FOREIGN KEY(Gerente) REFERENCES CLIENTE(CPF) NOT NULL,
                        Titular varchar(50) NOT NULL FOREIGN KEY(Titular) REFERENCES CLIENTE(CPF),)"""
conecta.execute(create_script)
conecta = conn.cursor()
conn.commit()

# Criando a tabela

insert_table = 'INSERT INTO CLIENTE (CPF, Nome, Sobrenome, Idade, Conta) VALUES ( %s, %s, %s, %s, %s)'
insert_tablev = (cpf_bd, nome_bd, sobrenome_bd, idade_bd, conta_bd)
for record in insert_table:
    conecta.execute(insert_tablev, record)
insert_table = 'INSERT INTO DADOS (Agencia, Numero, Saldo, Gerente, Titular) VALUES ( %s, %s, %s, %s, %s)'
insert_tablev = (agencia_bd, numero_bd, saldo_bd, gerente_bd, titular_bd)
for record in insert_table:
    conecta.execute(insert_tablev, record)

# Atualizando a tabela

update_table = 'UPDATE DADOS SET (Agencia, Numero, Saldo, Gerente, Titular) VALUES ( %s, %s, %s, %s, %s)'
insert_tablev = (agencia_bd, numero_bd, saldo_bd, gerente_bd, titular_bd)
conecta.execute(update_table)
update_table = 'UPDATE CLIENTE SET (CPF, Nome, Sobrenome, Idade, Conta) VALUES ( %s, %s, %s, %s, %s)'
insert_tablev = (cpf_bd, nome_bd, sobrenome_bd, idade_bd, conta_bd)
conecta.execute(update_table)

# deletando a tabela

delete_table = 'DELETE_FROM CLIENTE WHERE Nome = %s'
delete_tablev = ('Maria')
conecta.execute(delete_table, delete_tablev)
delete_table = 'DELETE_FROM DADOS WHERE Nome = %s'
delete_tablev = ('Carlos,')
conecta.execute(delete_table, delete_tablev)

# Selecionando a tabela

conecta.execute('SELECT * CLIENTE')
for table in conecta.fetchall():
    print(record[Saldo])
conecta.execute('SELECT * DADOS')
for table in conecta.fetchall():
    print(record[Sobrenome])
conn.commit()

except Exception as error:
    print("error")
finally:
    if conecta is not None:
        conecta.close()
    if conn is not None:
        conn.close()