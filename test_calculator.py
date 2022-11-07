from calculator import input_num

def main():
    test_num()

def test_num():
    assert input_num("A") == False
    assert input_num("5") == True

if __name__ == "__main__":
    main()