from mysql import connector
import hashlib
import utility

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


def getAccount(email: str, password: str) -> bool:
    sql: str = f"SELECT * FROM `users` WHERE `email`='{email}' AND `password`='{password}';"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    return len(DATA) > 0


def hashString(string: str) -> str:
    data: str = hashlib.md5(string.encode()).hexdigest()
    return str(data)[0:32]


def getProduct(prod_id: int):
    sql: str = f"SELECT * FROM `product` where prod_id = '{prod_id}'"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    return utility.Product(DATA[0]['PROD_ID'], DATA[0]['PROD_CATEGORY'], DATA[0]['PROD_PRICE'], DATA[0]['PROD_NAME'],
                           DATA[0]['PROD_QUANTITY'])


def getProductInfo(prod_id: int):
    sql: str = f"SELECT * FROM `product_info` where product_id='{prod_id}'"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    return utility.ProductInfo(DATA[0]['PRODUCT_ID'], DATA[0]['PRODUCT_CATEGORY'], DATA[0]['SUB_CATEGORY'],
                               DATA[0]['PICTURE_LINK'], DATA[0]['SOLD'], DATA[0]['RATING'], DATA[0]['BUY_RATE'])


def getProductBySearch(search: str):
    sql: str = f"SELECT * FROM `product` where prod_name like '%{search}%'"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    return DATA
