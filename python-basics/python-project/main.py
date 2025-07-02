import requests
from IDdict import warehouseIDs
from URLdict import URLs
import time

class WBAPI:
    def __init__(self) -> None:
        print("Привет!\nЭто приложение для работы с WB API. С помощью него можно\n"
            "отследить значение коэффициентов приемки различных складов\n"
            "вайлдбериз и собрать по ним статистику, чтобы в дальнейшем понимать,\n"
            "в какое время стоит выслеживать наиболее выгодный коэффициент\n"
            "для поставки.\n"
            "Для начала работы введите 'start'\n"
            "Для навигации по работе программы введите 'info'\n"
            "Для выхода из программы введите 'stop'\n"
            "--------------------------------------------")
    
    _auth = False

    def start(self) -> None:
        print("Для авторизации и дальнейшей работы введите специальный токен\n"
              "--------------------------------------------")
        token = str(input())
        if token == "exit":
            print("Завершение сессии. Для навигации по приложению введите 'info'\n"
            "--------------------------------------------")
            return
        self.HEADER = {'Authorization' : token}
        check = requests.get(URLs["test"], headers=self.HEADER)
        while check.reason != "OK":
            print("Упс, плохой токен. Попробуйте еще раз\n"
                  "--------------------------------------------")
            token = input()
            if token == "exit":
                print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                "--------------------------------------------")
                return
            self.HEADER = {'Authorization' : token}
            check = requests.get(URLs["test"], headers=self.HEADER)
        print(check.reason)
        print("--------------------------------------------")
        self._auth = True
    
    def check(self) -> bool:
        if not self._auth:
            print("Вы не авторизовались!")
            self.start()
        return self._auth

    def aboutID(self) -> None: # доделать
        print("Введите наименования склада\n"
              "--------------------------------------------")
        name = str(input())
        if name == "exit":
            print("Завершение сессии. Для навигации по приложению введите 'info'\n"
            "--------------------------------------------")
            return
        whget = requests.get(URLs["warehouses"], headers=self.HEADER)
        whlist = whget.json()
        length = len(whlist)
        while(True):
            for i in range(length):
                if whlist[i]['name'] == name:
                    print(whlist[i])
                    return
                if i == length - 1:
                    print("Кажется, такого склада не существует. Попробуйте снова\n"
                        "--------------------------------------------")
                    name = str(input())
                    if name == "exit":
                        print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                        "--------------------------------------------")
                        return
                    
    def getinfo(self) -> None:
        print("start:       Начало работы программы\n"
              "about:       Получить информацию о складе\n"
              "info:        Навигация по программе\n"
              "statistic:   Собрать статистику по складу\n"
              "exit:        Закончить сессию\n"
              "--------------------------------------------")
        
    def getstatistic(self) -> None:
        print("Статистика собирается на протяжение суток. По истечению этого\n"
              "времени программа остановится и вы попадете в главное меню.\n"
              "--------------------------------------------")
        print("Введите наименования склада\n"
              "--------------------------------------------")
        whname = str(input())
        if whname == "exit":
            print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                  "--------------------------------------------")
            return
        while whname not in warehouseIDs:
            print("Кажется, такого склада не существует. Попробуйте снова\n"
                  "--------------------------------------------")
            whname = str(input())
            if whname == "exit":
                print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                      "--------------------------------------------")
                return
        print("Введите тип упаковки\n"
              "2 - Короба\n"
              "5 - Монопалеты\n"
              "6 - Суперсейф\n"
              "--------------------------------------------")
        boxtype = int(input())
        if boxtype == "exit":
            print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                  "--------------------------------------------")
            return
        while not (boxtype != 2 or boxtype != 5 or boxtype != 6):
            print("Неверный тип упаковки\n"
                  "--------------------------------------------")
            boxtype = int(input())
            if boxtype == "exit":
                print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                      "--------------------------------------------")
                return
        print("Введите желаемый коэффициент [-1, 20]\n"
              "--------------------------------------------")
        coef = int(input())
        if coef == "exit":
            print("Завершение сессии. Для навигации по приложению введите 'info'\n"
            "--------------------------------------------")
            return
        while coef < -1 or coef > 20:
            print("Неверное значение коэффициента\n"
                  "--------------------------------------------")
            coef = int(input())
            if coef == "exit":
                print("Завершение сессии. Для навигации по приложению введите 'info'\n"
                      "--------------------------------------------")
                return
        wh_id = warehouseIDs[whname]
        getid = requests.get(URLs["koeficient"], headers=self.HEADER, params=f"warehouseIDs={wh_id}")
        idlist = getid.json()
        length = len(idlist)
        count = 0
        while(True):
            print(f"Поиск склада #{count}")
            for i in range(length):
                if idlist[i]['boxTypeID'] == boxtype and idlist[i]['coefficient'] == coef:
                    print(idlist[i])
                    print()
            count += 1
            if count == 288: # 288 * 300 (секунд) = 24 часа
                return
            time.sleep(300)
            



# token: eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQxMTE4djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTc0Nzc5MzI2MywiaWQiOiIwMTkzNDRjMC0yNDdjLTdjMDEtOWY2MS1hMmViNjJiMmMwMWQiLCJpaWQiOjEyNTMwMzM5Nywib2lkIjo0MTY1MjYxLCJzIjoxMDQwLCJzaWQiOiJlNDJjZmQ5MS1kODNkLTRlNDMtYTQ0OS1iMjUxZWM0YjBkNWQiLCJ0IjpmYWxzZSwidWlkIjoxMjUzMDMzOTd9.Z9-JkdQR_Lynca2IvFPMK-d3fS-0ZE3Ks3uVGNBiwbRC27N-XuMphKQjMoRNE1QBizCybjEI01fWfgUlPG-eWw

STATE = True

session = WBAPI()

while STATE:
    inp = input()

    if inp == "start":
        session.start()
    elif inp == "about":
        if not session.check():
            continue
        session.aboutID()
    elif inp == "info":
        session.getinfo()
    elif inp == "statistic":
        if not session.check():
            continue
        session.getstatistic()
    elif inp == "stop":
        STATE = False
        continue
    else:
        print("Неизвестное значение на входе, попробуйте снова")
        continue
