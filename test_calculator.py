from calculator import calculations

def main():
    test_num()

def test_num():
    assert calculations(1.0, "+", 2.0) == 3.0
    #assert calculations() == "Choose Operator:(+, -, *, /)"

if __name__ == "__main__":
    main()



#Rarely test nput