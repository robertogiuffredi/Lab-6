# Roberto Giuffredi
def encode(string):
    list = []
    for i in string:
        list.append(int(i))
    encoded_list = ''
    for idx, j in enumerate(list):
        list[idx] = str(j + 3)
        encoded_list += list[idx]
    return encoded_list

def decode(string): #decoder function
    list = []
    for i in string:
        list.append(int(i))
    encoded_list = ' '
    for idx, j in enumerate(list):
        list[idx] = str(j - 3)
        encoded_list += list[idx]
    return encoded_list

def menu():
    return print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

if __name__ == '__main__':
    while True:
        menu()
        option = input('Please enter an option: ')
        if option == '1':
            string = input('Please enter your password to encode: ')
            encoded_password = encode(string)
            print('Your password has been encoded and stored!')
        elif option == '2': # prints the encoded password and the decoded password (original)
            string = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {string}.')
        elif option == '3':
            break
