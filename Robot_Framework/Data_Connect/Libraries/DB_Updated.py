#!/usr/bin/python    
import configparser
import db6

def final_balance():
    config=configparser.RawConfigParser()
    config.read("ConfigFile.ini")

    id = config.get("CustomerInfo","cust.id")

    q = "select account_balance from onlinebanking.savings_account where id = {};".format(id)
    f = db6.query(q)
    p = str(f).split()
    print("f value is {}".format(p[1]))
    config.set("CustomerInfo","cust.updated_balance",p[1])
    final_balance = float(config.get("CustomerInfo","cust.updated_balance"))

    config.set('CustomerInfo', 'cust.updated_balance', final_balance)
    with open('ConfigFile.ini', 'w') as conf:
        config.write(conf)
    return final_balance

if __name__ == "__main__":
    final_balance()