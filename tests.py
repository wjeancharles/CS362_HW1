"""
Wesley Jean-Charles
Last Updated: 1/28/23
HW 1
"""
import unittest
from credit_card_validator import credit_card_validator


class TestCCV(unittest.TestCase):

    """
    This series of tests will complete tests for VISA credit cards
    """
    # Card length is 0
    def test_v1(self):
        num = ""
        self.assertFalse(credit_card_validator(num))
        # return True

    # Card starts with 0 with length 15
    def test_v2(self):
        num = "068783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 3 with length 15
    def test_v3(self):
        num = "3687836885785856"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 4 with length 15
    def test_v4(self):
        num = "468783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 5 with length 15
    def test_v5(self):
        num = "568783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'a' with length 15
    def test_v5a(self):
        num = "a68783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 15
    def test_v5b(self):
        num = "abcdefghijklmno"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/' symbol with length 15
    def test_v5c(self):
        num = "/68783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 15
    def test_v5d(self):
        num = "/*-+...-===+-*/"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 0 with length 16
    def test_v6(self):
        num = "0687836885785856"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 3 with length 16
    def test_v7(self):
        num = "3687836885785856"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 4 with length 16
    def test_v8(self):
        num = "46878368857858567"
        self.assertTrue(credit_card_validator(num))

    # Card starts with 4 with length 16 but has letters
    def test_v8a(self):
        num = "4687836885a858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 4 with length 16 but has symbol
    def test_v8b(self):
        num = "4687836885+858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 4 with length 16 but has letters and symbols
    def test_v8c(self):
        num = "4s+f-er-0m,lo9-p"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 5 with length 16
    def test_v9(self):
        num = "56878368857858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'a' with length 16
    def test_v9a(self):
        num = "a687836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 16
    def test_v9b(self):
        num = "abcdefghijklmnop"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/' symbol with length 16
    def test_v9c(self):
        num = "/687836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 16
    def test_v9d(self):
        num = "/*-+...-===+-*/+"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 0 with length 17
    def test_v10(self):
        num = "046878368857858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 3 with length 17
    def test_v11(self):
        num = "346878368857858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 4 with length 17
    def test_v12(self):
        num = "468783688578585670"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 5 with length 17
    def test_v13(self):
        num = "546878368857858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'a' with length 17
    def test_v14(self):
        num = "a6878368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 17
    def test_v15(self):
        num = "abcdefghijklmnopq"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/' symbol with length 17
    def test_v17(self):
        num = "/6878368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 17
    def test_v18(self):
        num = "/*-+...-===+-*/++"
        self.assertFalse(credit_card_validator(num))

    """
    This series of tests will complete tests for AMEX credit cards
    """
    # Card length is 0
    def test_a1(self):
        num = ""
        self.assertFalse(credit_card_validator(num))

    # Card length is 14 starts with 0
    def test_a2(self):
        num = "08059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 14 starts with 33
    def test_a3(self):
        num = "33059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 14 starts with 34
    def test_a4(self):
        num = "34059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 14 starts with 37
    def test_a5(self):
        num = "37059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 14 starts with 38
    def test_a6(self):
        num = "38059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'a' with length 14
    def test_a6a(self):
        num = "aa878368857858"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 14
    def test_a6b(self):
        num = "abcdefghijklmn"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/+' symbol with length 14
    def test_a6c(self):
        num = "/+878368857858"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 14
    def test_a6d(self):
        num = "/*-+...-===+-*"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 0
    def test_a7(self):
        num = "008059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 33
    def test_a8(self):
        num = "338059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 34
    def test_a9(self):
        num = "348059402380403"
        self.assertTrue(credit_card_validator(num))

    # Card length is 15 starts with 37
    def test_a10(self):
        num = "378059402380403"
        self.assertTrue(credit_card_validator(num))

    # Card length is 15 starts with 34 but has letter
    def test_a10a(self):
        num = "348059402380a03"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 34 but has symbol
    def test_a10b(self):
        num = "348059402+80403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 34 but has letters and symbols
    def test_a10c(self):
        num = "34+65fr+-*/8r43"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 37 but has letter
    def test_a10d(self):
        num = "378059402380a03"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 37 but has symbol
    def test_a10e(self):
        num = "378059402+80403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 37 but has letters and symbols
    def test_a10f(self):
        num = "37+65fr+-*/8r43"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 38
    def test_a11(self):
        num = "388059402380403"
        self.assertFalse(credit_card_validator(num))

        # Card starts with 'a' with length 15
    def test_a11a(self):
        num = "a68783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 15
    def test_a11b(self):
        num = "abcdefghijklmno"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/' symbol with length 15
    def test_a11c(self):
        num = "/68783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 15
    def test_a11d(self):
        num = "/*-+...-===+-*/"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 0
    def test_a12(self):
        num = "0128059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 33
    def test_a13(self):
        num = "3308059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 34
    def test_a14(self):
        num = "3408059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 37
    def test_a15(self):
        num = "3708059402380403"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 38
    def test_a16(self):
        num = "3808059402380403"
        self.assertFalse(credit_card_validator(num))

        # Card starts with 'a' with length 16
    def test_a17(self):
        num = "a687836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 16
    def test_a18(self):
        num = "abcdefghijklmnop"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/' symbol with length 16
    def test_a19(self):
        num = "/687836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 16
    def test_a20(self):
        num = "/*-+...-===+-*/+"
        self.assertFalse(credit_card_validator(num))

    """
    This series of tests will complete tests for MasterCard credit cards
    """
    # Card length is 0
    def test_m1(self):
        num = ""
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 0
    def test_m2(self):
        num = "011296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 50
    def test_m3(self):
        num = "501296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 51
    def test_m4(self):
        num = "511296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 55
    def test_m5(self):
        num = "551296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 56
    def test_m6(self):
        num = "561296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 2220
    def test_m7(self):
        num = "222060438728760"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 2221
    def test_m8(self):
        num = "222160438728760"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 2720
    def test_m9(self):
        num = "272060438728760"
        self.assertFalse(credit_card_validator(num))

    # Card length is 15 starts with 2721
    def test_m10(self):
        num = "272160438728760"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aa' with length 15
    def test_m10a(self):
        num = "aa8783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aaaa' with length 15
    def test_m10aa(self):
        num = "aaaa83688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 15
    def test_m10b(self):
        num = "abcdefghijklmno"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/+' symbol with length 15
    def test_m10c(self):
        num = "/+8783688578585"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 15
    def test_m10d(self):
        num = "/*-+...-===+-*/"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 0
    def test_m11(self):
        num = "0011296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 50
    def test_m12(self):
        num = "5011296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 51
    def test_m13(self):
        num = "5111296043872876"
        self.assertTrue(credit_card_validator(num))

    # Card starts with 51 with length 16 but has letters
    def test_m13a(self):
        num = "5187836885a858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 51 with length 16 but has symbol
    def test_m13b(self):
        num = "5187836885+858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 51 with length 16 but has letters and symbols
    def test_m13c(self):
        num = "51+f-er-0m,lo9-p"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 55
    def test_m14(self):
        num = "5511296043872876"
        self.assertTrue(credit_card_validator(num))

    # Card starts with 55 with length 16 but has letters
    def test_m14a(self):
        num = "5587836885a858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 55 with length 16 but has symbol
    def test_m14b(self):
        num = "5587836885+858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 55 with length 16 but has letters and symbols
    def test_m14c(self):
        num = "55+f-er-0m,lo9-p"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 56
    def test_m15(self):
        num = "5611296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 2220
    def test_m16(self):
        num = "2220296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 2221
    def test_m17(self):
        num = "2221296043872876"
        self.assertTrue(credit_card_validator(num))

    # Card starts with 2221 with length 16 but has letters
    def test_m17a(self):
        num = "2221836885a858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 2221 with length 16 but has symbol
    def test_m17b(self):
        num = "2221836885+858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 2221 with length 16 but has letters and symbols
    def test_m17c(self):
        num = "2221-er-0m,lo9-p"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 2720
    def test_m18(self):
        num = "2720296043872876"
        self.assertTrue(credit_card_validator(num))

    # Card starts with 2720 with length 16 but has letters
    def test_m18a(self):
        num = "2720836885a858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 2720 with length 16 but has symbol
    def test_m18b(self):
        num = "2720836885+858567"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 2720 with length 16 but has letters and symbols
    def test_m18c(self):
        num = "2720-er-0m,lo9-p"
        self.assertFalse(credit_card_validator(num))

    # Card length is 16 starts with 2721
    def test_m19(self):
        num = "2721296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aa' with length 16
    def test_m19a(self):
        num = "aa87836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aaaa' with length 16
    def test_m19aa(self):
        num = "aaaa836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 16
    def test_m19b(self):
        num = "abcdefghijklmnop"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/-' symbol with length 16
    def test_m19c(self):
        num = "/-87836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/-+-' symbol with length 16
    def test_m19cc(self):
        num = "/-+-836885785855"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 16
    def test_m19d(self):
        num = "/*-+...-===+-*/+"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 0
    def test_m20(self):
        num = "02221296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 50
    def test_m21(self):
        num = "50221296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 51
    def test_m22(self):
        num = "51221296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 55
    def test_m23(self):
        num = "55221296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 56
    def test_m24(self):
        num = "56221296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 2220
    def test_m25(self):
        num = "22201296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 2221
    def test_m26(self):
        num = "22211296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 2720
    def test_m27(self):
        num = "27201296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card length is 17 starts with 2721
    def test_m28(self):
        num = "27211296043872876"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aa' with length 17
    def test_m29(self):
        num = "aa878368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card starts with 'aaaa' with length 17
    def test_m29a(self):
        num = "aaaa8368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card has all letters with length 17
    def test_m30(self):
        num = "abcdefghijklmnopq"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/+' symbol with length 17
    def test_m31(self):
        num = "/+878368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card starts with '/++-' symbol with length 17
    def test_m31a(self):
        num = "/++-8368857858555"
        self.assertFalse(credit_card_validator(num))

    # Card has all symbols with length 17
    def test_m32(self):
        num = "/*-+...-===+-*/++"
        self.assertFalse(credit_card_validator(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
