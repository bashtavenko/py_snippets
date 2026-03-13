import unittest

from misc.ica.bank import Bank


class BankTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.bank = Bank()

    def test_create_account(self):
        self.assertEqual(self.bank.create_account(1, "acc1"), True)
        self.assertEqual(self.bank.create_account(2, "acc1"), False)
        self.assertEqual(self.bank.create_account(3, "acc2"), True)

    def test_deposit(self):
        self.assertEqual(self.bank.create_account(1, "acc1"), True)
        self.assertEqual(self.bank.deposit(2, "acc1", 500), 500)
        self.assertEqual(self.bank.deposit(3, "acc1", 300), 800)
        self.assertEqual(self.bank.deposit(4, "non_existent", 100), None)

    def test_transfer(self):
        self.assertEqual(self.bank.create_account(1, "acc1"), True)
        self.assertEqual(self.bank.create_account(2, "acc2"), True)
        self.assertEqual(self.bank.deposit(3, "acc1", 1000), 1000)
        self.assertEqual(self.bank.transfer(4, "acc1", "acc2", 300), 700)
        # Insufficient funds
        self.assertEqual(self.bank.transfer(5, "acc1", "acc2", 800), None)
        # Non-existent account
        self.assertEqual(self.bank.transfer(6, "acc1", "non_existent", 100), None)
        # Transfer to self
        self.assertEqual(self.bank.transfer(7, "acc1", "acc1", 100), None)
    #
    # def test_1(self):
    #     self.assertEqual( self.bank.create_account(1, "account1") == True
    #     self.assertEqual( self.bank.create_account(2, "account1") == False
    #     self.assertEqual( self.bank.create_account(3, "account2") == True
    #     self.assertEqual( self.bank.deposit(4, "non_existent", 100) == None
    #     self.assertEqual( self.bank.deposit(5, "account1", 2700) == 2700
    #     self.assertEqual( self.bank.transfer(6, "account1", "account2", 2701) == None
    #     self.assertEqual( self.bank.transfer(7, "account1", "account2", 200) == 2500
    #
    # def test_2(self):
    #     self.assertEqual( self.bank.create_account(1, "A") == True
    #     self.assertEqual( self.bank.create_account(2, "B") == True
    #     self.assertEqual( self.bank.deposit(3, "A", 500) == 500
    #     self.assertEqual( self.bank.transfer(4, "A", "B", 300) == 200
    #     self.assertEqual( self.bank.deposit(5, "B", 200) == 500
    #     self.assertEqual( self.bank.transfer(6, "B", "A", 600) == None
    #     self.assertEqual( self.bank.transfer(7, "B", "A", 400) == 100
    #
    # def test_3(self):
    #     self.assertEqual( self.bank.create_account(1, "X") == True
    #     self.assertEqual( self.bank.deposit(2, "X", 1000) == 1000
    #     self.assertEqual( self.bank.create_account(3, "Y") == True
    #     self.assertEqual( self.bank.transfer(4, "X", "Y", 500) == 500
    #     self.assertEqual( self.bank.transfer(5, "Y", "X", 600) == None
    #     self.assertEqual( self.bank.deposit(6, "Y", 300) == 800
    #     self.assertEqual( self.bank.transfer(7, "Y", "X", 400) == 400
    #
    #


if __name__ == "__main__":
    unittest.main()