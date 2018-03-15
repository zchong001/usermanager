import json
import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
path_new = 'data'
path = os.path.join(path,path_new)
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
    acc_name = os.path.join(path,acc_name)
    with open(acc_name,'w') as file:
        json.dump(account,file)

#修改账户并保存
def accout_save(acc_name,**kwargs):
    acc_name = os.path.join(path, acc_name)
    with open(acc_name,'r') as file:
        acc_info=json.load(file)
        #打印账户信息
        # for index in acc_info:
        #     print('%s : %s'%(index,acc_info[index]))
        # print('------------------------------------')
        #打印传入信息,并修改账户信息
        if acc_info['frozen_credit_card_flag'] == '0':
            for index in kwargs:
                acc_info[index]=kwargs[index]
            #保存修改信息
            with open(acc_name,'w') as new_file:
                # print(acc_info)
                json.dump(acc_info, new_file)
        elif acc_info['frozen_credit_card_flag'] == '1':
            print('信用卡已被冻结')



if __name__ == '__main__':
    # account_creat('tom')
    accout_save('tom', credit_limit=10000, amount_money=10000,frozen_credit_card_flag=1)
    # path = os.path.dirname(os.path.dirname(__file__))
    # path_new = 'data'
    # path = os.path.join(path,path_new)
    # print(path)
    # account_creat('john',password='john')
