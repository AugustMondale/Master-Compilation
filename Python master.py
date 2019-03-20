while True:
    try:
        def print_result():
            print('\nAnswer is: ' )
            print(result)
            print ('\n')
        import earth
        earth.earth()
        print("Hello")
        print("Choose an option to begin, or type 'quit' to exit\n")
        print("'calc' - Calculator")
        print("     - Basic Scientific Calculator\n")
        print("'pythag' - Pythagorean Thoerem")
        print("     - Right Triangle Hyoptenuse Calculator\n")
        print "'hang' - Hangman"
        print "     - Hangman Game with Random words\n"
        user_input = raw_input("Which option would you like to choose?: ")
        if user_input == "calc":
            while True:
                import calcimg
                ops = ['*' , '+' , '-' , '/' , '^' ]
                print("\nWelcome to the Calculator" )
                calcimg.img()
                print("\n Enter a number, an operator, and another number" )
                print("For python 2.7, you will require quotes around the operator")
                print("Or enter 'quit' to exit")
                print(" '*' , '+' , '-' , '/' , '^' ")
                try:
                    entry = raw_input("type 's' to begin, or type quit to leave: ")
                    if entry == 's':
                         num1 = float(input("Enter a Number: "))
                         op_inp = raw_input("Operator: ")
                         num2 = float(input("Enter another Number: "))
                         if  ops[0] == op_inp:
                             result = str(num1 * num2)
                             print_result()
                         elif ops[1] == op_inp:
                             result = str(num1 + num2)
                             print_result()
                         elif ops[2] == op_inp:
                             result = str(num1 - num2)
                             print_result()
                         elif ops[3] == op_inp:
                             result = str(num1 / num2)
                             print_result()
                         elif ops[4] == op_inp:
                             result = str(num1 ** num2)
                             print_result()
                    elif entry == "quit":
                        print("Goodbye")
                        print ('\n')
                        break
                except NameError:
                    print("\nNameError: Invalid Input")
                    print("Try again")
                except OverflowError:
                    print("\nOverflowError: Result is too large, try again")
            else:
                print("unknown error")

        elif user_input == "pythag":
            while True:
                import math
                print("\nWelcome to the Pythagorean Theorem Calculator")
                print("Enter Lengths of Sides A and B of a Right Triangle to Calculate C\n")
                print('   |\ ')
                print('   | \ ' )
                print('   |  \ ')
                print(' A |   \ C')
                print('   |    \ ')
                print('   |     \ ')
                print('   |______\ ')
                print('      B   ')
                try:
                     entry = raw_input(" Type s to begin, or type quit to leave: ")
                     if entry == "s":
                            A = float(input("Enter A: "))
                            B = float(input("Enter B: "))
                            C = math.sqrt((A**2)+(B**2))
                            print "The Value of C is: "
                            print(C)
                            print "\n"
                     elif entry == "quit":
                        print("Goodbye \n")
                        break
                     else:
                        print("Invalid Input \n")
                except NameError:
                    print("Error Occurred: Invalid Input \n")
                    print("Try again")
        elif user_input == 'hang':
            import Hangman
            Hangman.hangman()

        elif user_input == 'quit':
            break
        else:
            print("Invalid Option \n")
    except NameError:
        print("NameError: Invalid input \n")
        print("Try again")
