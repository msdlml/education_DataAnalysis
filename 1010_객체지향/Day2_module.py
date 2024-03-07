

addr_list = []

def get_menu_num():
    print("메인메뉴)","1.입력","2.출력","3.검색","4.종료", sep="\n\t")
    num = int(input("번호 입력하세요 : "))
    return num

def input_list():
    while True:
        name = input("이름:")
        age = input("나이:")
        addr = input("주소:")
        addr_list.append({"name":name, "age":age, "addr":addr})
        keep_going = input("계속 하시겠습니까(y/n)?")
        if keep_going == "n":
            break
    
def print_list():
    print("-"*40)
    print("\t이름\t나이\t주소")
    print("-"*40)
    for n in addr_list:
        print("\t%(name)s\t%(age)s\t%(addr)s"%n)
    
def search_name():
    name = input("이름을 입력하세요 :")
    for n in addr_list:
        if n["name"] == name:
            print("-"*40)
            print("\t이름\t나이\t주소")
            print("-"*40)
            print("\t%(name)s\t%(age)s\t%(addr)s"%n)
            break
