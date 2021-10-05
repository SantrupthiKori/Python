import unittest
from validate import validateUP

class Validtest(unittest.Testcase):
    def testval1(self):
        self.asserEqual(validateUP('Santrupthi', 'San@1999'), True)

    def testval2(self):
        self.asserEqual(validateUP('S', 'San@1999'), False)

    def testval3(self):
        self.asserEqual(validateUP('Santr', 'San19'), False)

    def testval4(self):
        self.asserEqual(validateUP('Santr1','S'), False)

    def testval5(self):
        self.asserEqual(validateUP(9809,'San@1999'), False)

    def testval6(self):
        self.asserEqual(validateUP('Santrupthi', 54199), False)

    def setUp(self):
            print("setup")

    def teardown(self):
            print("Teardown")

    @classmethod
    def setUpClass(self)-> print("setup class"):
        pass