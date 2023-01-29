# CS362_HW1
HW 1 Writing Black Box Tests

Apply black box testing techniques

Description
For this assignment, you will be writing unit tests based on the following specifications/requirements.

You will write a series of unit tests to test a function called credit_card_validator (written for you) that is passed a sequence of digits as a string that represents a credit card number. This function will return True if it is a valid credit card number, otherwise, it will return False.

Depending on the credit card issuer, the length of a credit card number can range between 10 and 19 digits. The first few digits of the number are the issuer prefix. Each credit card issuer has an assigned range of numbers. For example, only Visa credit card numbers may begin with 4, while American Express card numbers must begin with either a 34 or 37. Sometimes, credit card providers are assigned multiple ranges. For example, MasterCard card numbers must start with the numbers between 51 through 55 or 2221 through 2720 (both ranges are inclusive). 

The last digit of the number is referred to as the check digit and acts as a checksum. Most credit cards calculate this check digit using the Luhn algorithm (see resources below for how this is calculated).

In order to limit the scope of this assignment, we are going to limit the number of credit card issuers to 3: Visa, MasterCard, and American Express. Each has its own prefixes and length requirements.

Visa
Prefix(es): 4
Length: 16
MasterCard
Prefix(es): 51 through 55 and 2221 through 2720 
Length: 16
American Express
Prefix(es): 34 and 37
Length: 15
Your task is to create a series of tests that attempt to reveal bugs in the implementation. As this is black box testing, you will not have access to the source so you must use what you have learned this week to generate test cases.

You will be submitting your code to Gradescope, which will auto grade your tests. In order to get full credit on the assignment, you will need to locate all 10 bugs in the code (refer to the rubric for full details). Some are easier than others. Bug 5 is easy to miss without using Partition Testing and Bug 6 requires using what you know about common errors to design your tests.
