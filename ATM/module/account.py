import json
import os
import sys

#获取绝对路径
# path = os.path.dirname(os.path.dirname(__file__))
# path_new = r'data\account'
# path = os.path.join(path,path_new)

#相对路径  需要把项目绝对路径增加到sys.path中
path = '../data/account'
#创建账户  使用缺省参数
def account_creat(acc_name,password=123456,credit_limit=15000,amount_money=2000,credit_limit_spending=0,
                 amount_money_spending=0,money_in=0,money_out=0,
                 credit_limit_cash=0,credit_limit_repayment=0,frozen_credit_card_flag=0):
    account = {
        'name': acc_name,
        'password': password,
        'credit_limit': credit_limit,
        'amount_money': amount_money,
        'credit_limit_spending': credit_limit_spending,
        'amount_money_spending': amount_money_spending,
        'money_in': money_in,
        'money_out': money_out,
        'credit_limit_cash': credit_limit_cash,
        'credit_limit_repayment': credit_limit_repayment,
        'frozen_credit_card_flag':frozen_credit_card_flag
    }
    acc_name = os.path.join(path_test,acc_name)
    with open(acc_name,'w') as file:
        json.dump(account,file)

#修改账户并保存
def accout_save(acc_name,**kwargs):
    acc_name = os.path.join(path, acc_name)
    with open(acc_name,'r') as file:
        acc_info=json.load(file)
        #判断信用卡是否冻结
        if acc_info['frozen_credit_card_flag'] == 0:
            for index in kwargs:
                acc_info[index]=kwargs[index]
            #保存修改信息
            with open(acc_name,'w') as new_file:
                json.dump(acc_info, new_file)
        elif acc_info['frozen_credit_card_flag'] == 1:
            print('信用卡已被冻结')


if __name__ == '__main__':
    account_creat('tom111')
    # accout_save('tom', credit_limit=222)
    # accout_save('tom')
    # path = os.path.dirname(os.path.dirname(__file__))
    # path_new = 'data'
    # path = os.path.join(path,path_new)
    # print(path)
    # account_creat('john',password='john')
