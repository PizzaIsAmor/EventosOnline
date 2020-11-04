import MySQLdb


class Dao:
    def __init__(self, nome_tabela: str):
        self.__db = MySQLdb.connect(user='root', passwd='admin', host='localhost', port=3306)
        self.__tabela = InstrucaoSql(Dao.decifra_tabela(nome_tabela))

    @property
    def tabela(self):
        return str(self)

    @tabela.setter
    def tabela(self, nome_tabela):
        self.__tabela = InstrucaoSql(Dao.decifra_tabela(nome_tabela))

    @staticmethod
    def decifra_tabela(index: str):
        tabelas: dict = {'cliente': 'tb_cliente', 'estabelecimento': 'tb_estabelecimento'}
        return tabelas[index.lower()]

    def salvar(self, elemento: dict) -> bool:
        cursor = self.__db.cursor()

        if 'id' not in elemento or elemento['id'] == None:
            atributos = []
            for campo, valor in elemento.items():
                atributos.append(valor)
            print("Atributos: " + str(tuple(atributos)))
            cursor.execute(self.__tabela.adiciona(elemento), tuple(atributos))
        else:
            cursor.execute(self.__tabela.atualiza(elemento), tuple(atribulos))
        self.__db.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def deleta(self, elemento_id: int) -> bool:
        self.__db.cursor().execute(self.__tabela.deleta(elemento_id))
        self.__db.commit()

    def busca(self, campo: str, valor: str) -> tuple:
        cursor = self.__db.cursor()
        cursor.execute(self.__tabela.busca(campo), (valor,))
        elemento = cursor.fetchone()

        return elemento

    def busca_todos(self) -> list:
        cursor = self.__db.cursor()
        cursor.execute(self.__tabela.busca_todos())

        return cursor.fetchall()

    def criar_backup(self):
        criar_tabelas = '''SET NAMES utf8;
            CREATE DATABASE IF NOT EXISTS `eventosonline` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
            USE `eventosonline`;
            CREATE TABLE IF NOT EXISTS `tb_cliente` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `email` varchar(50) COLLATE utf8_bin NOT NULL UNIQUE,
              `senha` varchar(50) COLLATE utf8_bin NOT NULL,
              `nome` varchar(50) COLLATE utf8_bin NOT NULL,
              `cidade` varchar(50) COLLATE utf8_bin NOT NULL,
              `privilegio` bit(1) NOT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
            CREATE TABLE IF NOT EXISTS `tb_estabelecimento` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `email` varchar(50) COLLATE utf8_bin NOT NULL UNIQUE,
              `senha` varchar(50) COLLATE utf8_bin NOT NULL,
              `nome` varchar(50) COLLATE utf8_bin NOT NULL,
              `cidade` varchar(50) COLLATE utf8_bin NOT NULL,
              `cnpj` varchar(50) COLLATE utf8_bin NOT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

        self.__db.cursor().execute(criar_tabelas)

        # inserindo usuarios
        cursor = self.__db.cursor()
        cursor.executemany(
            'INSERT INTO eventosonline.tb_cliente (email, senha, nome, cidade, privilegio) VALUES (%s, %s, %s, %s, %s)',
            [
                ('marcos.pereira@outlook.com', 'admin', 'Marcos Pereira', 'Porto Alegre', int(False)),
                ('lucas.silva@outlook.com', 'admin', 'Lucas Silva', 'Porto Alegre', int(False)),
                ('diego.lunelli@outlook.com', 'admin', 'Diego Lunelli', 'Porto Alegre', int(False)),
                ('camila.santos@outlook.com', 'admin', 'Camila Santos', 'Porto Alegre', int(False)),
                ('debora.antunes@outlook.com', 'admin', 'Debora Antunes', 'Porto Alegre', int(False)),
                ('maria.das.dores@outlook.com', 'admin', 'Maria das Dores', 'Porto Alegre', int(False)),
                ('carlos.silva@outlook.com', 'admin', 'Carlos Roberto Silva', 'Porto Alegre', int(False)),
                ('isa.b@outlook.com', 'admin', 'Isabela Borges', 'Porto Alegre', int(False)),
                ('admin@outlook.com', 'admin', 'Rafael Lunelli', 'Porto Alegre', int(True))
            ])

        cursor.execute('select * from eventosonline.tb_cliente')

        # inserindo estabelecimentos
        cursor.executemany(
            'INSERT INTO eventosonline.tb_estabelecimento (email, senha, nome, cidade, cnpj) VALUES (%s, %s, %s, %s, %s)',
            [
                ('opiniao@outlook.com', 'admin', 'Opiniao', 'Porto Alegre', '0000000001'),
                ('bar.do.gomes@outlook.com', 'admin', 'Bar do Gomes', 'Porto Alegre', '0000000002'),
                ('roister@outlook.com', 'admin', 'Roister', 'Porto Alegre', '0000000003'),
                ('pinacoteca.bar@outlook.com', 'admin', 'Pinacoteca Bar', 'Porto Alegre', '0000000004'),
                ('al.coala@outlook.com', 'admin', 'Al Coala', 'Porto Alegre', '0000000005'),
            ])

        cursor.execute('select * from eventosonline.tb_estabelecimento')

        self.__db.commit()
        cursor.close()

class InstrucaoSql:
    def __init__(self, tabela: str):
        self.__tabela: str = tabela

    def __str__(self):
        return self.__tabela

    def adiciona(self, elemento: dict) -> tuple:
        query = f'INSERT into eventosonline.{self.__tabela} ('
        query_2 = ') values ('
        for coluna, valor in elemento.items():
            query += f'{coluna}, '
            query_2 += '%s, '
        query = str(query[:-2]) + str(query_2[:-2]) + ')'
        print("Query: " + str(query))
        return query

    def atualiza(self, elemento: dict) -> tuple:
        query = f'UPDATE eventosonline.{self.__tabela} SET '
        for coluna, valor in elemento.items():
            query += f'{coluna} = %s, '
        query = query[:-2] + ' where id = %s'

        print(query)
        return query

    def deleta(self, elemento_id: int) -> tuple:
        pass

    def busca(self, campo: str) -> str:
        return f'SELECT * from eventosonline.{self.__tabela} WHERE {campo} = %s'

    def busca_todos(self) -> tuple:
        return f'SELECT * from eventosonline.{self.__tabela}'


if __name__ == '__main__':
    Dao('cliente').criar_backup()