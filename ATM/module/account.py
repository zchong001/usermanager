import json

account = {
            "name":"first",
            "password":"first",
            "credit_limit":15000,
            "amount_money":2000,
            "credit_limit_spending":0,
            "amount_money_spending":0,
            "money_in":0,
            "money_out":0,
            "credit_limit_cash":0,
            "credit_limit_repayment":0
          }

#创建账户保存函数  关键字参数怎么修改函数里面的字典值
def account_save(acc_name,**kwargs):
    account = {
        'name': acc_name,
        'password': kwargs,
        'credit_limit': 15000,
        'amount_money': 2000,
        'credit_limit_spending': 0,
        'amount_money_spending': 0,
        'money_in': 0,
        'money_out': 0,
        'credit_limit_cash': 0,
        'credit_limit_repayment': 0
    }
    with open(acc_name,'w') as file:
        json.dump(account,file)





if __name__ == '__main__':
    def test(name, **kwargs):
        print(name, kwargs['hello'])
    account_save('test',password=1)
