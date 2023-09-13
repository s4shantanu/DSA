#Pattern Examples 

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("1", end=" ")
        print("\r")

pattern(5)


def pattern2(n):
    for i in range(n):
        for j in range(n-i):
            print("1", end=" ")
        print("\r")

pattern2(5)