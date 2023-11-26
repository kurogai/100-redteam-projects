import string

def translator():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shift = 13

    shift_lowercase = lowercase[shift:] + lowercase[:shift]
    shift_uppercase = uppercase[shift:] + uppercase[:shift]

    translate = str.maketrans(lowercase +uppercase, shift_lowercase + shift_uppercase)
    return translate

def rot13(message):
    table = translator()
    return message.translate(table)

def main():
    user_input = input("yout input : ")

    encripted_message = rot13(user_input)
    print(f"Encripted Message {encripted_message}")

    decripted_message = rot13(encripted_message)
    print(f"Decripted Message: {decripted_message}")

main()