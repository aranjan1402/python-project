import unittest
import account as AccountClass

class Test(unittest.TestCase):
    accInfo = AccountClass.account()
    def test_check_password_length(self):
        print("checking possible passssword\n")
        passwordList = ['hbvkvbwvvvfs','hgfergebvibihbrv','gveirvbkrvbivbrv' ]

        for passwd in passwordList:
            print("Ckecking password" + passwd + "\n")
            passInfo = self.accInfo.check_password_length(passwd)
            self.assertTrue(passInfo)
if __name__ == '__main__':
    unittest.main()
