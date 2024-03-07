from Day2_module import *

def main():
    process_menu = {1:input_list, 2:print_list, 3:search_name}
    while True:
        menu_num = get_menu_num()
        if menu_num == 4:
            break
        process_menu[menu_num]()

if __name__ == '__main__':
    main()        