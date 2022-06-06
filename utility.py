class Product:

    def __init__(self, prod_id: int, category: str, price: float, name: str, quantity: int):
        self.prod_id = prod_id
        self.category = category
        self.price = price
        self.name = name
        self.quantity = quantity


class ProductInfo:
    def __init__(self, prod_id: int, category: str, sub_category: str, photo_link: str, sold: int, rating: float,
                 buy_rate: int):
        self.prod_id = prod_id
        self.category = category
        self.sub_category = sub_category
        self.photo_link = photo_link
        self.sold = sold
        self.rating = rating
        self.buy_rate = buy_rate


class User:
    user_id: int
    lastname: str
    firstname: str
    email: str
    contact: str
    address = "615 V. Abad Tormis Ext., Sambag II, Urgello, Cebu City 6000, Philippines"


def parseCatLocation(category: str):
    if category == 'Bath':
        return 'bath'
    if category == 'Bedding':
        return 'bedding'
    if category == 'Furniture':
        return 'furniture'
    if category == 'Storage and Organization':
        return 'storage'
    if category == 'Laundry and Cleaning Equipment':
        return 'laundry_cleaning'
    return "#"


def parseSubCatLocation(prod_id: int):
    ID: int = 0
    for X in range(1200):
        X *= 100
        if int(prod_id) >= int(X):
            ID = int(X)
    return f"{ID + 1}...{ID + 6}"
