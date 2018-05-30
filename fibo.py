# -*- coding: utf-8 -*-

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

class BankCustomer:
    '''A customer of a bank with a checking account.
    
    Attributes:
        name: name of the customer (string)
        balance: amount of money in the account (float)
    
    Credit: this class is adapted from an excellent example from Jeff Knupp: 
        https://jeffknupp.com/
    '''
    
    def __init__(self,name,balance=0.0):
        self.name    = name
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            print('Overdraft alert! Amount requested greater than available balance.')
        self.balance -= amount
        return self.balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance