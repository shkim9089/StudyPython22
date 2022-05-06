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
    load_contact(lst_contact)  #파일 DB 읽어오기
    clearconsole()
    while True:
        sel_menu =get_menu()
        if sel_menu == 1:  #연락처 입력
            clearconsole()
            contact = set_contact()
            if contact is None: 
                input("계속하려면 엔터를 누르세요")
                clearconsole()
                continue #contact가 비었다면 리스트추가 불가
            lst_contact.append(contact)
            input(input("연락 추가 성공\n계속하려면 엔터를 누르세요"))         #아무값도 없이 엔터 대기
            clearconsole() 
        elif sel_menu == 2: #연락처 출력
            clearconsole()
            get_contact(lst_contact)
            input(input("계속하려면 엔터를 누르세요"))          #엔터대기
            clearconsole()
        elif sel_menu == 3: #연락처 삭제
            clearconsole()
            name = input('연락처 삭제성공 \n삭제할 이름 입력 >')
            del_contact(lst_contact,name)
            input(input("계속하려면 엔터를 누르세요"))          #엔터대기
            clearconsole()
        elif sel_menu == 4:    # 종료
            save_contact(lst_contact)   #파일 DB저장ㅇ
            break
        else:
            clearconsole()



# 주소록 입력함수
def set_contact():
    contact = None
    try:  #아무입력없이 엔터, 갯수 틀리면 생기는 예외처리
        name,phone_num,e_mail,addr = \
        input('정보입력(이름,핸드폰,이메일,주소(구분자 /)) >').split('/')
        contact = Contact(phone_num=phone_num, e_mail=e_mail,name=name,addr=addr)
    except Exception as e:
        print('입력회수 확인(이름/핸드폰/이메일/주소')
    finally:
        return contact #잘못되면 None리턴 , contact 객체 리턴



# 주소록 전체출력
def get_contact(lst_contact):
    for contact in lst_contact:
        print(contact)



#주소록 삭제
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]


#주소록 파일DB 작성 저장
def save_contact(lst_contact:list):
    f = open('./advanced/db_contact.txt', mode='w', encoding='utf-8')
    for contact in lst_contact:
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')

    f.close()

#주소록 파일DB 로드
def load_contact(lst_contact:list):
    f = open('./advanced/db_contact.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: break

        lines = line.rstrip('\n').split('/')   #\n제거하고 /로 나누고 리스트화
        if len(lines) !=4: continue  #220506 11:11 엔터로 생기는 예외처리
        contact = Contact(lines[0],lines[1],lines[2],lines[3]) 
        lst_contact.append(contact)

    f.close()



#메뉴 출력 및 선택
def get_menu():
    str_menu = ('--주소록 프로그램v1.1--\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    #0~9숫자 외에는 value erro 발생
    menu = 0 # 초기화
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        print(e)
    finally:    
        return menu




def clearconsole():
    command = 'clear' ##mac,unix 리눅스 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows,dos 화면 클리어 명령어
    os.system(command)

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print('ctrl+c 종료')

    
