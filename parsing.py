with open('C:/Users/hp/Downloads/sample_logs.txt') as file:
    for i in file:
        if 'ERROR' in i:
            print(i)