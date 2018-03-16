# author: Random
# date: 2018/3/15
#实现购物商城,买东西加入购物车,调用信用接口结账
#1.商品列表
#2.购物车 1)选择商品 2)核定价格与总价
#3.信用卡结账
import json

path_products = '../conf/products' #产品路径

#定义函数 显示商品列表 传入产品编号,返回商品名称 商品价格
def shopping_products(product_number=0):
    with open (path_products,'r') as products_file:
        products = json.load(products_file)
        print('商品列表'.center(40,'-'))
        print('%-8s%-12s%-16s' %('商品编号','商品名称','商品价格'))
        #显示商品列表
        for index,product in enumerate(products,1):
            print('%-11s%-16s%-16s'%(index,product,products[product]))#左对齐
        print(''.center(40, '-'))
        # 返回商品列表
        for index, product in enumerate(products, 1):
           if index == product_number:
                return product,products[product]

#定义函数 购物车: 计算商品价格,数量,总价????
def shopping_car(product_name,product_price):
    #使用列表进行存储
    aggregate_amount = []  # 用于购物车商品金额
    amount = 0  # 购物车商品金额
    aggregate_amount[product_name] = product_price
    for i in aggregate_amount:
        amount+=aggregate_amount[i]
    return amount

if __name__ == '__main__':
    shopping_car('pen',80)
    shopping_car('pen', 120)
    print(amount)
