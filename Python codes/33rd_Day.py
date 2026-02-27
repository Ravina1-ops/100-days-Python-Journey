# Finally keyword

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        # This will print even though the function returned 1 or 0 above!
        print("I am always executed")

x = func1()
print(x)