from mysql import connector
import hashlib

database = connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="intprog_haus"
)


def register_account(acc_id: int, lastname: str, firstname: str, email: str, contact: str, password: str):
    sql: str = f"INSERT INTO `users` (`id`,`lastname`,`firstname`,`email`,`contact`,`password`) values ('{acc_id}','{lastname}','{firstname}','{email}','{contact}','{password}')"
    cursor = database.cursor()
    cursor.execute(sql)
    database.commit()
    cursor.close()


def getAccount(email: str, password: str)->bool:
    sql: str = f"SELECT * FROM `users` WHERE `email`='{email}' AND `password`='{password}';"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    return len(DATA) > 0


def hashString(string: str) -> str:
    data:str = hashlib.md5(string.encode()).hexdigest()
    return str(data)[0:32]