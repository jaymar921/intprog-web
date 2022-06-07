from mysql import connector
import hashlib
import utility


def Database():
    return connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="intprog_haus"
    )


def register_account(acc_id: int, lastname: str, firstname: str, email: str, contact: str, password: str):
    sql: str = f"INSERT INTO `users` (`id`,`lastname`,`firstname`,`email`,`contact`,`password`) values ('{acc_id}','{lastname}','{firstname}','{email}','{contact}','{password}')"
    db = Database()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def getAccount(email: str, password: str) -> bool:
    sql: str = f"SELECT * FROM `users` WHERE `email`=%s AND `password`=%s;"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql, (email, password))
    DATA: list = cursor.fetchall()
    db.close()
    return len(DATA) > 0


def getAccountByEmail(email: str):
    sql: str = f"SELECT * FROM `users` WHERE `email`='{email}'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    db.close()
    if len(DATA) > 0:
        user: utility.User = utility.User
        user.user_id = DATA[0]['id']
        user.lastname = DATA[0]['lastname']
        user.firstname = DATA[0]['firstname']
        user.email = DATA[0]['email']
        user.contact = DATA[0]['contact']
        return user
    return None


def getAccountById(id_: str):
    sql: str = f"SELECT * FROM `users` WHERE `id`='{id_}'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    db.close()
    if len(DATA) > 0:
        user: utility.User = utility.User
        user.user_id = DATA[0]['id']
        user.lastname = DATA[0]['lastname']
        user.firstname = DATA[0]['firstname']
        user.email = DATA[0]['email']
        user.contact = DATA[0]['contact']
        return user
    return None


def hashString(string: str) -> str:
    data: str = hashlib.md5(string.encode()).hexdigest()
    return str(data)[0:32]


def getProduct(prod_id: int):
    sql: str = f"SELECT * FROM `product` where prod_id = '{prod_id}'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return utility.Product(DATA[0]['PROD_ID'], DATA[0]['PROD_CATEGORY'], DATA[0]['PROD_PRICE'], DATA[0]['PROD_NAME'],
                           DATA[0]['PROD_QUANTITY'])


def getProductInfo(prod_id: int):
    sql: str = f"SELECT * FROM `product_info` where product_id='{prod_id}'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return utility.ProductInfo(DATA[0]['PRODUCT_ID'], DATA[0]['PRODUCT_CATEGORY'], DATA[0]['SUB_CATEGORY'],
                               DATA[0]['PICTURE_LINK'], DATA[0]['SOLD'], DATA[0]['RATING'], DATA[0]['BUY_RATE'])


def getProductBySearch(search: str):
    sql: str = f"SELECT * FROM `product` where prod_name like '%{search}%'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return DATA


def updateProductRating(prod_id: int, rating: float):
    sql: str = f"UPDATE `product_info` SET rating={rating},BUY_RATE=BUY_RATE+1 WHERE PRODUCT_ID={prod_id}"
    db = Database()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def addRating(prod_id: int, comment: str, user_id: int, rating: float):
    sql: str = f"INSERT INTO COMMENT(PROD_ID,COMMENT,CUSTOMER_ID,RATING) values (%s,%s,%s,%s)"
    db = Database()
    cursor = db.cursor()
    cursor.execute(sql, (prod_id, comment, user_id, rating))
    db.commit()
    cursor.close()
    db.close()


def getComment(prod_id: int):
    sql: str = f"SELECT * FROM COMMENT where PROD_ID={prod_id}"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return DATA


def getProductByName(search: str):
    sql: str = f"SELECT * FROM `product` where prod_name='{search}'"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return DATA


def addToCart(email: str, prod_id: int):
    sql: str = f"INSERT INTO `cart`(`CUSTOMER_ID`,`PROD_ID`) VALUES ('{getAccountByEmail(email).user_id}', '{prod_id}')"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def getCart(user_id: int):
    sql: str = f"SELECT * FROM `cart` where CUSTOMER_ID={user_id} group by(PROD_ID) "
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return DATA


def removeCart(user_id: int, prod_id: int):
    sql: str = f"DELETE FROM `cart` where CUSTOMER_ID={user_id} AND PROD_ID={prod_id}"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def getPurchases(user_id: int):
    sql: str = f"SELECT * FROM `purchase` where CUSTOMER_ID={user_id} group by(PROD_ID) "
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    DATA: list = cursor.fetchall()
    cursor.close()
    db.close()
    return DATA


def addToPurchase(email: str, prod_id: int):
    sql: str = f"INSERT INTO `purchase`(`CUSTOMER_ID`,`PROD_ID`) VALUES ('{getAccountByEmail(email).user_id}', '{prod_id}')"
    db = Database()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def deleteCart(user_id: int):
    sql: str = f"DELETE FROM `cart` WHERE CUSTOMER_ID = {user_id}"
    db = Database()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
