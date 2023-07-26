from termcolor import colored, cprint
from os import name, system
from time import sleep
import sys


def clear():
	system('cls') if name == 'nt' else system('clear')
		

def title_style(title):
    clear()
    cprint('=' * 25, 'yellow')
    cprint(title, 'magenta')
    cprint('=' * 25 + "\n", 'yellow')


def options(number, actions):
	for i in range(0, len(number)):
		print(colored(f"{number[i]} ", 'magenta') + colored(f"{actions[i]}", 'yellow'))


def menu_internal():
	numbers = ['[1]', '[2]']
	actions = ['ɴᴏᴠᴀ ᴏᴘᴇʀᴀᴄᴀᴏ', 'sᴀɪʀ']
	options(numbers, actions)
	match input(colored( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' )):
		case '1':
			menu_operations()
		case '2':
			clear()
			sys.exit()

def menu_operations():
	title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
	numbers = [ '[1]', '[2]', '[3]', '[4]', '\n[5]']
	actions = [ 'ᴀᴅɪᴄᴀᴏ', 'sᴜʙᴛʀᴀᴄᴀᴏ', 'ᴍᴜʟᴛɪᴘʟɪᴄᴀᴄᴀᴏ', 'ᴅɪᴠɪsᴀᴏ' , 'ᴠᴏʟᴛᴀʀ' ]
	options(numbers, actions)
	operations()


def operations():
    type = input(colored( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' ))
    if type == '5':
        menu_main()
    title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
    match type:
        case '1':
            n1 = int(input(colored('1° valor: ', 'yellow')))
            n2 = int(input(colored('2° valor: ', 'yellow')))
            a = n1 + n2
            b = '+'
        case '2':
            n1 = int(input(colored('1° valor: ', 'yellow')))
            n2 = int(input(colored('2° valor: ', 'yellow')))
            a = n1 - n2
            b = '-'
        case '3':
            n1 = int(input(colored('1° valor: ', 'yellow')))
            n2 = int(input(colored('2° valor: ', 'yellow')))
            a = n1 * n2
            b = '*'
        case '4':
            n1 = int(input(colored('1° valor: ', 'yellow')))
            n2 = int(input(colored('2° valor: ', 'yellow')))
            a = n1 / n2
            b = '/'
        case '5':
            menu_operations()
        case _:
            clear()
            print('ᴏᴘᴄᴀᴏ ɪɴᴠᴀʟɪᴅᴀ')
            sleep(0.90)
            menu_operations()
    title_style('        ᴏᴘᴇʀᴀᴄᴏᴇs')
    print(f"{n1} {b} {n2} = {a}\n")
    menu_internal()
    


def menu_main():
    title_style('          ᴍᴇɴᴜ')
    numbers = [ '[1]', '[2]', '\n[3]' ]
    actions = [ 'ᴏᴘᴇʀᴀᴄᴏᴇs', 'ᴄʀᴇᴅɪᴛᴏs', 'sᴀɪʀ' ]
    options(numbers, actions)
    text = colored( '\n\nᴅɪɢɪᴛᴇ ᴀǫᴜɪ: ', 'blue' )
    match input(text):
        case '1':
            menu_operations()
        case '2':
            clear()
            print('sᴇʀᴠɪᴄᴏ ɪɴᴅɪsᴘᴏɴɪᴠᴇʟ !')
            sleep(0.90)
            menu_main()
        case '3':
            clear()
            sys.exit()
    





# started
menu_main()
