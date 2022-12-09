"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hours = 0 , commission = 0, number = 0):
        self.name = name
        self.pay = pay
        self.hours = hours 
        self.commission = commission
        self.number = number

    def get_pay(self):
        if self.hours > 0:
            pay = self.get_hourly_pay()
            if self.commission > 0:
                if self.number > 0:
                    pay += self.get_contract_commission()
                else:
                    pay += self.get_bonus_commission()
        else:
            pay = self.get_monthly_pay()
            if self.commission > 0:
                if self.number > 0:
                    pay += self.get_contract_commission()
                else:
                    pay += self.get_bonus_commission()
        return pay

    def __str__(self):
        exp = f'{self.name}'
        if self.hours > 0:
            exp += f' works on a contract of {self.hours} hours at {self.pay}/hour'
        else:
            exp += f' works on a monthly salary of {self.pay}'
        if self.commission > 0:
            if self.number > 0:
                exp += f' and receives a commission for {self.number} contract(s) at {self.commission}/contract'
            else:
                exp += f' and receives a bonus commission of {self.commission}'

        exp += f'.  Their total pay is {self.get_pay()}.'  

        return exp

    def get_hourly_pay(self):
        pay = self.pay
        if self.hours > 0:
            pay *= self.hours
        return pay
        
    def get_monthly_pay(self):
        pay = self.pay
        return pay

    def get_bonus_commission(self):
        commission = self.commission
        return commission

    def get_contract_commission(self):
        commission = self.commission
        if self.number > 0:
            number = self.number
            commission *= number
        return commission

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', pay=4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', pay=25, hours=100)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', pay=3000, commission=200, number=4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', pay=25, hours=150, number=3, commission=220)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', pay=2000, commission=1500)



# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', pay=30, hours=120, commission=600)
