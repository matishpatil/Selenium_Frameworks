#!/usr/bin/python    
import configparser
import db6

def init_balance():
    config=configparser.RawConfigParser()
    config.read("ConfigFile.ini")

    id = config.get("CustomerInfo","cust.id")

    q = "select account_balance from onlinebanking.savings_account where id = {};".format(id)
    f = db6.query(q)
    p = str(f).split()
    print("f value is {}".format(p[1]))
    config.set("CustomerInfo","cust.init_balance",p[1])
    initial_balance = float(config.get("CustomerInfo","cust.init_balance"))

    config.set('CustomerInfo','cust.init_balance',initial_balance)
    with open('ConfigFile.ini','w') as conf:
        config.write(conf)
    return initial_balance

if __name__ == "__main__":
    init_balance()