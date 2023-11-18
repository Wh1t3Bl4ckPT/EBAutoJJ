import time
import keyboard

strings_to_type = ["UM!", "DOIS!", "TRÊS!", "QUATRO!", "CINCO!", "SEIS!", "SETE!", "OITO!", "NOVE!", "DEZ!",
                   "ONZE!", "DOZE!", "TREZE!", "CATORZE!", "QUINZE!", "DEZESSEIS!", "DEZESSETE!", "DEZOITO!",
                   "DEZENOVE!", "VINTE!", "VINTE E UM!", "VINTE E DOIS!", "VINTE E TRÊS!", "VINTE E QUATRO!",
                   "VINTE E CINCO!", "VINTE E SEIS!", "VINTE E SETE!", "VINTE E OITO!", "VINTE E NOVE!", "TRINTA!",
                   "TRINTA E UM!", "TRINTA E DOIS!", "TRINTA E TRÊS!", "TRINTA E QUATRO!", "TRINTA E CINCO!",
                   "TRINTA E SEIS!", "TRINTA E SETE!", "TRINTA E OITO!", "TRINTA E NOVE!", "QUARENTA!", "QUARENTA E UM!",
                   "QUARENTA E DOIS!", "QUARENTA E TRÊS!", "QUARENTA E QUATRO!", "QUARENTA E CINCO!",
                   "QUARENTA E SEIS!", "QUARENTA E SETE!", "QUARENTA E OITO!", "QUARENTA E NOVE!", "CINQUENTA!"]


def type_strings():
    print("Aperte F5 para começar a contar!")
    keyboard.wait('F5')

    for string in strings_to_type:
        keyboard.write('/')
        time.sleep(0.3)
        keyboard.write(string)
        time.sleep(0.9)
        keyboard.send('enter')
        time.sleep(1)

type_strings()