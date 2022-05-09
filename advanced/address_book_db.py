# 주소록 프로그램 v1.5
# 작성일 : 2022-05-09
# 작성자 : SH KIM
# 설  명 : 월요일 파일db에서 오라클로 변경

# 연락처 클래스
import cx_Oracle as ora
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

def initDB():
    dsn = ora.makedsn('localhost',1521,service_name='orcl')
    conn = ora.connect(user='scott',password='tiger',dsn =dsn,encoding='utf-8')
    return conn


def run():
    conn = initDB()  # 오라클 연결해서 연결객체 생성
    clearconsole()
    while True:
        sel_menu =get_menu()
        if sel_menu == 1:  #연락처 입력
            clearconsole()
            isval = set_contact(conn)
            if isval:
                input("연락 추가 성공\n계속하려면 엔터를 누르세요")        #아무값도 없이 엔터 대기
            else:
                input("오류발생! 관리자에게 연락바람")
            clearconsole() 
        elif sel_menu == 2: #연락처 출력
            clearconsole()
            get_contact(conn)
            input("계속하려면 엔터를 누르세요")         #엔터대기
            clearconsole()
        elif sel_menu == 3: #연락처 삭제
            clearconsole()
            name = input('연락처 삭제성공 \n삭제할 이름 입력 >')
            del_contact(conn,name)
            input("계속하려면 엔터를 누르세요")          #엔터대기
            clearconsole()
        elif sel_menu == 4:    # 종료
            conn.close()
            break
        else:
            clearconsole()



# 주소록 입력함수
def set_contact(conn):
    contact = None
    isSucceed = False  #입력성공여부
    try:  #아무입력없이 엔터, 갯수 틀리면 생기는 예외처리
        name,phone_num,e_mail,addr = \
        input('정보입력(이름,핸드폰,이메일,주소(구분자 /)) >').split('/')
        contact = Contact(phone_num=phone_num, e_mail=e_mail,name=name,addr=addr)
        # DB처리
        cur = conn.cursor()
        query = ('INSERT INTO ADDRESSBOOK '  #공백없으면 예외발생, 없이 순서동일
                 'VALUES (SEQ_ADDREBOOK.nextval, :1,:2,:3,:4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSuceed = True
    except Exception as e:
        print('입력회수 확인(이름/핸드폰/이메일/주소')
        isSuceed = False
    finally:
        return isSuceed # True면 DB입력 성공

# 주소록 전체출력
def get_contact(conn):
    cur = conn.cursor()
    query = 'SELECT name,phone_num,e_mail,addr FROM ADDRESSBOOK'
    
    for row in cur.execute(query):
        contact = Contact(row[0],row[1],row[2],row[3])
        print(contact)
    
    cur.close()


#주소록 삭제
def del_contact(conn, name):
    cur = conn.cursor()
    query = f"DELETE FROM ADDRESSBOOK WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()


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

    
