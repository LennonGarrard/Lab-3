def question1():
    print("which data type is most appropriate to store gps coordinates")
    user_input1 = input("Answer:")
    if user_input1 == "Float":
        print("Correct!")
    elif user_input1 == "float":
        print("Correct!")
    else:
        print("Incorrect")
        question1()

question1()