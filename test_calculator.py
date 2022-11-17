from calculator import calculations, input_num

def main():
    test_calc

def test_calc():
    assert calculations(1.0, "+", 2.0) == 3.0
    assert calculations(4.0, "-", 2.0) == 2.0
    assert calculations(5.0, "-", 5.0) is not -0
    assert calculations(10.0, "*", 10.0) == 100.0
    assert calculations(-10.0, "*", -10.0) == 100.0
    assert calculations(-10.0, "*", 10.0) == -100.0
    assert calculations(4.0, "/", 2.0) == 2.0
    #assert calculations(4.0, "/", 0) == "Can't divide by Zero"
















"""""
from calc import addition, subtraction, divison, multiplication

def main():
    test_additon()
    test_subtraction()
    test_multiplication()

def test_additon():
    assert addition(1.0, "+", 2.0) == 3.0

def test_subtraction():
    assert subtraction(4.0, "-", 2.0) == 2.0
    assert subtraction(5.0, "-", 5.0) is not -0

def test_multiplication():
    assert multiplication(10.0, "*", 10.0) == 100.0
    assert multiplication(-10.0, "*", -10.0) == 100.0
    assert multiplication(-10.0, "*", 10.0) == -100.0

def test_division():
    assert divison(4.0, "/", 2.0) == 2.0
    assert divison(4.0, "/", 0) == "Can't divide by Zero"
    assert divison(9.3, "/", 4.8) == 



"""""
if __name__ == "__main__":
    main()