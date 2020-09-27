restart = ('y')

while restart == 'y':
    print("Welcome, Print any Special Pattern \n")
    print("\nChoose Your Pattern Shape")
    print("\nPress 1 for Binary Triangle")
    print("Press 2 for Pascal Triangle")
    print("Press 3 for Hour Glass")
    print("Press 4 for K-shape Pattern\n")

    option = int(input("Enter Your Choice : "))

    if option == 1:
        def binary(n):
            k = 2 * n - 2
            for i in range(0, n):
                for j in range(0, k):
                    print(end=" ")
                k = k - 1
                for j in range(0, i + 1):
                    print('10', end="")
                print("\r")

        if __name__ == '__main__':
            n = int(input("Enter the number of rows : "))
            print(binary(n))
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

    elif option == 2:
        def pascal(n):
            for i in range(0, n):
                for j in range(0, i + 1):
                    print(function(i, j), " ", end=" ")
                print()

        def function(n, k):
            result = 1
            if (k > n - k):
                k = n - k
            for i in range(0, k):
                result = result * (n - i)
                result = result // (i + 1)
            return result

        if __name__ == '__main__':
            n = int(input("Enter the number of rows : "))
            print(pascal(n))
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

    elif option == 3:
        def hour_glass(n):
            k = n - 2
            for i in range(n, -1, -1):
                for j in range(k, 0, -1):
                    print(end=" ")
                k = k + 1
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")
            k = 2 * n - 2
            for i in range(0, n + 1):
                for j in range(0, k):
                    print(end=" ")
                k = k - 1
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")

        if __name__ == '__main__':
            n = int(input("Enter the number of rows : "))
            print(hour_glass(n))
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

    elif option == 4:
        for i in range(7):
            for j in range(7):
                if j == 0 or i - j == 3 or i + j == 3:
                    print("*", end="")
                else:
                    print(end=" ")
            print()

        restart = input("\nPress y to restart : ").lower()
        print("\n")
        if restart != 'y':
            print("Thank you!!!")
            break

    else:
        print("Invalid Option \n")
        restart = ('y')

else:
    print("Invalid Option \n")
    restart = ('y')