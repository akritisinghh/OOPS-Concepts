# multilevel inheritance
class bank:

    def transaction(self):
        print("total transaction value ")
    def account_opening(self):
        print("Your account open status ")
    def deposit(self):
        print("your deposit amount is ")


class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show all the transaction processed from hdfc to icici ")

class icici(HDFC_bank):
    pass
i = icici()
i.hdfc_to_icici()
i.deposit()
i.transaction()
i.account_opening()
