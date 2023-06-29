# 10.4 Конструкция match/case
""""""

"""
Общий синтаксис конструкции match/case:

match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
        
        
Оператор match принимает выражение subject и сравнивает его значение с последовательными шаблонами, 
заданными как один или несколько блоков case. 
В частности, сопоставление с образцом работает следующим образом:

* использование данных с типом и формой (subject);
* оценка subject в заявлении match;
* сравнение subject с каждым шаблоном в заявлении case сверху вниз, пока совпадение не будет подтверждено.
* выполнение действия action, связанного с шаблоном подтвержденного совпадения;
* если точное совпадение не подтверждено, то в качестве совпадающего случая
  будет использоваться последний case c подстановочным знаком '_', если он указан. 
  Если точное совпадение не подтверждено и case _: - не существует, то весь блок match не выполняется.
"""
command = 'right'
match command:
    case 'top':  # аналог оператора if
        print('Команда вверх')
    case var:  # var = command  # аналог оператора else,  т.к. сработает всегда
        print(f'Команда {var}')
# Команда right


command = 'top'
match command:
    case 'top':  # аналог оператора if
        print('Команда вверх')
    case _:  #  case _: "wildcard"  вариант оператора else, т.к. сработает всегда
        print('Неизвестная команда ')
# Команда вверх


command = 'stop'
match command:
    case str() as cmd:  # cmd = command
        print(f'Строковая команда {cmd}')
    case _:  # wildcard
        print('Неизвестная команда ')
# Строковая команда stop


# сопоставление с более структурированным шаблоном  | * | * |
def go(direction):
    match direction:
        case "North" | "East" | "South" | "West":
            return "Хорошо, я пошел!"
        case _:
            return "Неизвестное направление..."

go("North")  # Хорошо, я пошел!
go("Stop")  # Неизвестное направление...


#  логика обработки переменной “direction” вложена в более сложное:
def act(command):
    match command.split():
        case "Cook", "breakfast":
            return "Я люблю завтракать."
        case "Cook", *arg:
            return "Что то готовится..."
        case "Go", "North" | "East" | "South" | "West":
            return "Хорошо, я пошел!"
        case "Go", *arg:
            return "Неизвестное направление..."
        case _:
            return "Я не могу этого сделать..."

act("Go North")  # Хорошо, я пошел!
act("Go way")  # Неизвестное направление...
act("Cook breakfast")  # Я люблю завтракать.
act("Cook anything")  # Что то готовится...
act("Drive")  # Я не могу этого сделать...


#
#  *   *   *   *   *   TASK    *   *   *   *   *
#


# 01
"""
https://stepik.org/lesson/988826/step/6?unit=996311
Input:  BOTTOM
Output: Команда bottom
"""
cmd = input()

match cmd:
    case 'top' | 'Top' | 'TOP':
        print("Команда top")
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print("Команда bottom")
    case 'right' | 'Right' | 'RIGHT':
        print("Команда right")
    case 'left' | 'Left' | 'LEFT':
        print("Команда left")
    case _:
        print("Неверная команда")


# Короче
cmd = input().lower()
match cmd:
    case 'top' | 'bottom' | 'right' | 'left':
        print(f'Команда {cmd}')
    case _:
        print('Неверная команда')


# 02
"""
https://stepik.org/lesson/988826/step/7?unit=996311
В функцию get_data() передается параметр value:
def get_data(value):
    match value:
        # здесь продолжайте программу   
    return None
Необходимо дописать оператор match/case в этой функции так,
чтобы для каждого типа данных (int, float и str) формировалась переменная со значением value 
и возвращалась функцией (непосредственно из блока case).
"""

def get_data(value):
    match value:
        case int() as data:
            return data
        case float() as data:
            return data
        case str() as data:
            return data
    return None

# Короче
def get_data(value):
    match value:
        case bool():
            return None
        case int() | float() | str() as data:
            return data
    return None

# print(get_data(True))

# print(get_data(9.2))

# 03
"""
https://stepik.org/lesson/988826/step/8?unit=996311
В функцию get_data() передается параметр value:
def get_data(value):
    match value:
        # здесь продолжайте программу    
    return None
Необходимо дописать оператор match/case со следующими шаблонами:
если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
если переменная value имеет тип str, то просто вернуть ее значение.
"""


def get_data(value):
    match value:
        case bool():
            return None
        case int() as data if data > 0:
            return data
        case float() as data if -100 <= data <= 100:
            return data
        case str() as data:
            return data
    return None

# print(get_data(True))
