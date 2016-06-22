import sqlite3

class UseBd:
    def __init__(self):
        self.__conexao = sqlite3.connect("bd_Virus.db")

    def create(self):
        cursor = self.__conexao.cursor()
        #cursor.execute('''drop table if exists Virus''')
        cursor.execute('''create table if not exists Virus
                        (id int, vida int, dinheiro int, unlockPuloDuplo int, unlockSuperPeso int, unlockPlanar int, score int) ''')
        cursor.execute('''insert into Virus values (1, 1, 0, 0, 0, 0, 0)''')

        cursor.close()
        self.__conexao.commit()
        #self.__conexao.close()

    def insert(self, virus):
        cursor = self.__conexao.cursor()
        id = 1
        vida = int(virus.vidaBase)
        dinheiro = int(virus.dinheiro)
        unlockPuloDuplo = virus.unlockPuloDuplo
        unlockSuperPeso = virus.unlockSuperPeso
        unlockPlanar = virus.unlockPlanar
        score = int(virus.score)
        cursor.execute('''insert into Virus values (?, ?, ?, ?, ?, ?, ?)''',
        	[id, vida, dinheiro, unlockPuloDuplo, unlockSuperPeso, unlockPlanar, score])
        cursor.close()
        self.__conexao.commit()

    def selectVida(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select vida from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def selectDinheiro(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select dinheiro from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def selectUnlockPuloDuplo(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select unlockPuloDuplo from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def selectUnlockSuperPeso(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select unlockSuperPeso from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def selectUnlockPlanar(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select unlockPlanar from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def selectScore(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select score from Virus''')
        for row in res:
            return row[0]
        cursor.close()
        self.__conexao.commit()
        #return res

    def imprime(self):
        cursor = self.__conexao.cursor()
        res = cursor.execute('''select * from Virus''')
        for row in res:
            print((row))
        cursor.close()
        self.__conexao.commit()
        return res

    def update(self, virus):
        cursor = self.__conexao.cursor()
        id = 1
        vida = virus.vidaBase
        dinheiro = int(virus.dinheiro)
        unlockPuloDuplo = virus.unlockPuloDuplo
        unlockSuperPeso = virus.unlockSuperPeso
        unlockPlanar = virus.unlockPlanar
        score = int(virus.Hscore)
        self.delete()
        cursor.execute('''insert into Virus values (?, ?, ?, ?, ?, ?, ?)''',
                       [id, vida, dinheiro, unlockPuloDuplo, unlockSuperPeso, unlockPlanar, score])
        cursor.close()
        self.__conexao.commit()


    def delete(self):
        cursor = self.__conexao.cursor()
        id = 1

        cursor.execute('''DELETE FROM Virus
        WHERE id = ?''', [id])

        cursor.close()
        self.__conexao.commit()