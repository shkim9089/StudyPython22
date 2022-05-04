# 주소록 프로그램 v1.1
# 작성일 : 2022-05-04
# 작성자 : SH KIM
# 설  명 : 낼쉼

# 연락처 클래스
import os


class Contact:
    name = ''; phone_num =''; e_mail=''; addr=''

    def __init__(self,name,phone_num,e_mail,addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'==============================')
        return str_val           

def run():
    lst_contact = [] # 빈 리스트 생성
    clearconsole()
    while True:
        sel_menu =get_menu()
        if sel_menu == 1:
            clearconsole()
            contact = set_contact()
            lst_contact.append(contact)
            input()         #아무값도 없이 엔터 대기
            clearconsole() 
        elif sel_menu == 2: #연락처 출력
            clearconsole()
            get_contact(lst_contact)
            input()          #엔터대기
            clearconsole()
        elif sel_menu == 3: #연락처 출력
            clearconsole()
            name = input('삭제할 이름 입력 >')
            del_contact(lst_contact,name)
            input()          #엔터대기
            clearconsole()
        elif sel_menu == 4:
            break
        else:
            clearconsole()



# 주소록 입력함수
def set_contact():
    name,phone_num,e_mail,addr = \
    input('정보입력(이름,핸드폰,이메일,주소(구분자 /)) >').split('/')
    contact = Contact(phone_num=phone_num, e_mail=e_mail,name=name,addr=addr)
    return contact


# 주소록 전체출력
def get_contact(lst_contact):
    for contact in lst_contact:
        print(contact)

#주소록 삭제
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]


#메뉴 입력
def get_menu():
    str_menu = ('--주소록 프로그램v1.1--\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    menu = input('메뉴입력 : ')
    return int(menu)




def clearconsole():
    command = 'clear' ##mac,unix 리눅스 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows,dos 화면 클리어 명령어
    os.system(command)

if __name__ == '__main__':
    run()
