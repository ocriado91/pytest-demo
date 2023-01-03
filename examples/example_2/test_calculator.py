'''
Unit test for Calculator
'''

from calculator import Calculator

def test_add():
    ''' Test to check add method '''
    assert Calculator().add(10,4) == 14

def test_substract():
    ''' Test to check substract method '''
    assert Calculator().substract(10,4) == 6

def test_multiplication():
    ''' Test to check multiplication method '''
    assert Calculator().multiplication(10,4) == 40

def test_division():
    ''' Test to check division method '''
    assert Calculator().division(10,4) == 2.5
