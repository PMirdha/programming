from decimal import Decimal


class Product(object):
    def __init__(self):
        self.unit_price = {
            "A": Decimal(50),
            "B": Decimal(30),
            "C": Decimal(20),
            "D": Decimal(15)
        }
        self.specific_price = {
            "A": {
                "unit": 3,
                "price": Decimal(130)
            },
            "B": {
                "unit": 2,
                "price": Decimal(45)
            }
        }

    def get_discount_details(self, product):
        data = self.specific_price.get(product)
        return (data["unit"], data["price"]) if data else (None, None)

    def get_unite_price(self, product):
        return self.unit_price.get(product)

    def is_valid_product(self, product):
        
        return True if self.unit_price.get(product) else False


product_obj = Product()


def validate_product(fn):

    def wrapper(cl_obj, product=None, *args, **kwargs):
        if product:
            if not product_obj.is_valid_product(product):
                raise Exception("Invalid Product - %s" % product)
        return fn(cl_obj, product, *args, **kwargs)

    return wrapper


class Kart(object):

    def __init__(self, pdt_list=()):
        self.product_count = {}
        self.user = None
        self.insert_product_list(pdt_list)

    def insert_product_list(self, products):
        for pdt in products:
            if not product_obj.is_valid_product(pdt):
                raise Exception(
                    "Invalid Product - {}, being inserted in Kart".format(
                        pdt))
            self.product_count[pdt] = self.product_count.get(pdt, 0) + 1

    def change_product_count(self, product, count=1):
        self.product_count[product] = (
            0 if self.product_count.get(product, 0) + count < 0 else
            self.product_count.get(product, 0) + count)

    @validate_product
    def add_product(self, product, count=1):
        self.change_product_count(product, count)

    @validate_product
    def remove_product(self, product, count=1):
        if not self.product_count.get(product):
            raise Exception("Product - %s not in Kart" % product)
        count = count * -1
        self.change_product_count(product, count=count)

    def total_cost(self):
        cost = 0
        for product in self.product_count.keys():
            cost += self.product_cost(product)
        return cost

    def product_cost(self, product):
        cost = 0
        count = self.product_count.get(product, 0)
        discount_unit, discount_price = product_obj.get_discount_details(
            product)
        unit_price = product_obj.get_unite_price(product) or 0
        if discount_unit and discount_price:
            cost += (int(count/discount_unit) * discount_price)
            count = count % discount_unit

        cost += count * unit_price
        return cost


if __name__ == "__main__":
    purchased_pdts = input()
    kart = Kart(purchased_pdts)
    print(kart.total_cost())
