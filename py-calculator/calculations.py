import GUI

calculation = ""


def sayHello():
    GUI.result.delete(1.0, 'end')
    GUI.result.insert(1.0, 'Hello! Start your calculations! :)')


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    GUI.result.delete(1.0, 'end')
    GUI.result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        GUI.result.delete(1.0, 'end')
        GUI.result.insert(1.0, calculation)
    except:
        clear_field()
        GUI.result.insert(1.0, 'Error')


def clear_field():
    global calculation
    calculation = ''
    GUI.result.delete(1.0, 'end')
