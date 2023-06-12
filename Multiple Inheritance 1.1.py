# multiple inheritance
class bank:

    def transaction(self):
        print("total transaction value ")
    def account_opening(self):
        print("Your account open status ")
    def deposit(self):
        print("your deposit amount is ")
    def test(self):
        print("this is a test methord from bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show all the transaction processed from hdfc to icici ")
    def test(self):
        print("this is a test methord from HDFC_bank class")

class SBI:
    def account_status_icici(self):
        print("Print account status of icici bank through SBI")

class icici(HDFC_bank,bank,SBI):   #if methord or varible names are same in multiple classes then by default it will process function/method from the class which is called in first please i.e. class icici(HDFC_bank,bank) OR class icici(bank, HDFC_bank):
    pass

i = icici()
i.account_opening()
i.transaction()
i.deposit()
i.hdfc_to_icici()
i.test()
i.account_status_icici()