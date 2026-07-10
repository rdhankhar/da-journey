class account:
    
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount ,"was credited")
        print("total balnace = ", acc1.balance)
        
    def debit(self,amount):
        self.balance  -= amount
        print("Rs.",amount ,"was debited")
        print("total balnace = ", acc1.balance)
    
    
acc1 = account(10000,12345)
print(acc1.balance,acc1.account_no)
acc1.debit(9000)
acc1.credit(40000)
acc1.debit(5000)