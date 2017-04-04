import sys
print('使用sys.exit退出程序')
while True:
    print('Type(打字) exit to exit.')
    response = input()
    if response =='exit':
        print('You typed '+response+'.')
        sys.exit()

