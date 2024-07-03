from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO:
    @staticmethod
    def getAllLocalizations():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct c.Localization as l
                from classification c 
                """
        cursor.execute(query)
        for row in cursor:
            result.append(row['l'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnections():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select c1.Localization as l1, c2.Localization as l2, i.GeneID1 as g1, i.GeneID2 as g2, i.`Type` as t, count(distinct i.`Type`) as peso 
                from classification c1, classification c2, interactions i
                where c1.GeneID = i.GeneID1 and c2.GeneID = i.GeneID2
                and c1.Localization != c2.Localization
                group by c1.Localization, c2.Localization
                """
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result

