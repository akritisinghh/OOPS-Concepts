# multiple inheritance
class bank:

    def transaction(self):
        print("total transaction value ")
    def account_opening(self):
        print("Your account open status ")
    def deposit(self):
        print("your deposit amount is ")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show all the transaction processed from hdfc to icici ")

class icici(bank, HDFC_bank):   #mutiple inheritance
    pass

i = icici()
i.account_opening()
i.transaction()
i.deposit()
i.hdfc_to_icici()