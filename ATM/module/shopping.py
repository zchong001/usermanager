# author: Random
# date: 2018/3/15
#实现购物商城,买东西加入购物车,调用信用接口结账
#1.商品列表
#2.购物车
#3.信用卡结账
import json
#定义函数显示商品列表
def shopping_products():
    with open ('../conf/products','r') as products_file:
        products = json.load(products_file)
        for index,product in enumerate(products,1):
            print('%-3s%-12s: %-8s'%(index,product,products[product]))#左对齐


#定义函数购物车
def shopping_car():
    pass


if __name__ == '__main__':
    # with open ('../conf/products','w') as products:
    #     a={
    #         'mac book pro':12000,
    #         'iphone':6000,
    #         'cup':80,
    #         'pen':120,
    #         'computer':5600,
    #         'paper':30,
    #         'TV':4200,
    #         'flowers':126,
    #         'car':180000,
    #         'bike':3600
    #     }
    #     json.dump(a,products)
    shopping_products()