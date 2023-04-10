import json
import time
class Orders:
    def __init__(self, product, prod_num, order_time):
        self.product = product
        self.prod_num = prod_num
        self.order_time = order_time
    def __str__(self):
        return f'Product Name: {self.product}, Order Number: {self.order_no} Time: {self.time}'
    def toJSON(product, prod_num, order_time):
        order_dic = {
            "order": [
                {"Item": product, "Item No": prod_num, "Time": order_time}
            ]
        }
        with open("Order.json", "a") as fp:
            fp.write(",\n")
            json.dump(order_dic, fp)