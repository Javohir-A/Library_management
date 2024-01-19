import datetime 
from random import randint,sample
class bankAccount:
    def __init__(self, balance: float, account_holder: str, account_id = str(randint(10000,99999))) -> None:
        self.__balance = balance
        self.__account_holder = account_holder
        self.__account_id = account_id
        self.__transaction_history = {'deposits': [], 'withdrawals': [], 'transfers': []}
        self.current_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def get_balance(self):
        return self.__balance
    def get_account_holder_name(self):
        return self.__account_holder
    def get_account_id(self):
        return self.__account_id
    def get_transaction_history(self):
        return self.__transaction_history
    
    def deposit(self, amount: float):
        id_transaction = randint(1000,9999)
        self.__balance += amount
        bill = {
            str(id_transaction) : {
                'time': self.current_time,
                'amount' : amount,
                'balance' : self.__balance
            }
        }
        self.__transaction_history['deposits'].append(bill)
        return f"""***Deposite***\nId : {id_transaction}
Time : {self.current_time}
Amount : {amount}
Balance : {self.__balance}
"""

    def get_deposit_history(self):
        deps_info = "****Deposit history****\n"
        for items in self.__transaction_history['deposits']:
            for item in items.items():
                dep_info = ''.join(f"""
    Id : {item[0]}
    Time : {item[1]['time']}
    Amount: {item[1]['amount']}
    balance: {item[1]['balance']}
""")    
            deps_info += dep_info

        return deps_info
    
    def get_transfers_history(self):
        deps_info = "****Transfer history****\n"
        for items in self.__transaction_history['transfers']:
            for item in items.values():
                from_ = next(iter(item.keys()), 'N/A')

                dep_info = ''.join(f"""
    {from_.capitalize()}: {item[from_]}
    Time: {item['time']}
    Amount: {item['amount']}
    Balance: {item['balance']}
""")
                deps_info += dep_info
        return deps_info
    
    def transfer(self, reciever: "bankAccount", amount: float):
        self.__balance-=amount
        reciever.__balance+=amount
        id = randint(1000,9999)
        bill_sender = {str(id):{
            'reciever' : reciever.get_account_holder_name(),
            'time' : self.current_time,
            'amount' : amount,
            'balance' : self.__balance
        }}
        bill_reciever = {str(id):{
            'sender' : self.__account_holder,
            'time' : self.current_time,
            'amount' : amount,
            'balance' : reciever.get_balance()
        }}        
        # insert information about transfer to recievers history
        self.__transaction_history['transfers'].append(bill_sender)
        
        #insert information about transfer to senders history
        reciever.__transaction_history['transfers'].append(bill_reciever)
        
        return f"""***Transfer***\n
    Id : {id}
    Reciever :  {reciever.get_account_holder_name()}
    Time :      {self.current_time}
    Amount :    {amount}
    Balance :   {self.__balance}
"""
    def withdraw_money(self, amount: float):
        assert self.__balance - amount > 0, f'Insufficient funds {amount}'
        self.__balance -= amount
        id = randint(1000,9999)
        bill_withdrawal = {str(id):{
            'time' : self.current_time,
            'amount' : amount,
            'balance' : self.__balance
        }}  
        self.__transaction_history['withdrawals'].append(bill_withdrawal)
        return  f"""***Withdrawal***\n
    Id : {id}
    Time :      {self.current_time}
    Amount :    -{amount}
    Balance :   {self.__balance}
"""
    def get_account_info(self):
        return f"""
    Account ID:         {self.__account_id}
    Account holder:     {self.__account_holder}
    Account balance:    {self.__balance}
"""

account = bankAccount(0,"Javohir")
account2 = bankAccount(0, "Shavkat", '656')
account3 = bankAccount(0, "Dilshod", '6516')
account.deposit(250_000)
account.deposit(2_000_000)
account.deposit(140000)
print(account.transfer(account3,2_500))
print(account.transfer(account2, 150_000))
account2.deposit(150_000)
print(account.withdraw_money(2000))
print(account2.transfer(account, 55_000))
# print(account.get_deposit_history())
# print(account.get_account_info())
# print(account.get_transaction_history(), '\n')
# print(account2.get_transaction_history())
print(account.get_transfers_history())
print(account2.get_transfers_history())

#%%
