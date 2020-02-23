while True:
    try:
        a = input()
        if type(int(a)) == int:
            print('It is an Int')
            continue
        else:
            print('Bye')
            break
    except:
        try:
            if type(float(a)) == float:
                print('It is a float')
                break
            else:
                print('Bye')
        except:
            print(a + " that's nice")
            break
