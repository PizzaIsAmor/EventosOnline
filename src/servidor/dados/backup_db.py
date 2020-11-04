import MySQLdb


def criar_backup():
    conn = MySQLdb.connect(user='root', passwd='admin', host='localhost', port=3306)

    # Descomente se quiser desfazer o banco...
    # conn.cursor().execute("DROP DATABASE `jogoteca`;")
    # conn.commit()
    criar_tabelas = '''SET NAMES utf8;
        CREATE DATABASE IF NOT EXISTS `eventosonline` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
        USE `eventosonline`;
        CREATE TABLE IF NOT EXISTS `tb_cliente` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `email` varchar(50) COLLATE utf8_bin NOT NULL,
          `senha` varchar(50) COLLATE utf8_bin NOT NULL,
          `nome` varchar(50) COLLATE utf8_bin NOT NULL,
          `cidade` varchar(50) COLLATE utf8_bin NOT NULL,
          `privilegio` bit(1) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
        CREATE TABLE IF NOT EXISTS `tb_estabelecimento` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `email` varchar(50) COLLATE utf8_bin NOT NULL,
          `senha` varchar(50) COLLATE utf8_bin NOT NULL,
          `nome` varchar(50) COLLATE utf8_bin NOT NULL,
          `cidade` varchar(50) COLLATE utf8_bin NOT NULL,
          `cnpj` varchar(50) COLLATE utf8_bin NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

    conn.cursor().execute(criar_tabelas)

    # inserindo usuarios
    cursor = conn.cursor()
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
    print(' -------------  Clientes:  -------------')
    for user in cursor.fetchall():
        print(str(user[0]) + " - " + str(user[1]) + "  |  " + str(user[3]))

    # inserindo jogos
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
    print(' --------  Estabelecimentos:  --------')
    for jogo in cursor.fetchall():
        print(jogo[1])

    conn.commit()
    cursor.close()

if __name__ == '__main__':
    criar_backup()