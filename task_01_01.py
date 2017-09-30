#!/usr/bin/python3.5

print('Введите площадь садового участка (в сотках)')
ploshad_uchastka_v_sotkah = float(input())
if ploshad_uchastka_v_sotkah < 0:
    print('Введены некорректные данные!')
else:
    ploshad_1_gryadki = 15 * 25
    print('Площадь 1й грядки =', ploshad_1_gryadki, ' квадратных метров')
    ploshad_uchastka_v_mkv = ploshad_uchastka_v_sotkah * 100
    print('Площадь учатска =', ploshad_uchastka_v_mkv, 'квадратных метров')
    gryadok_na_uchastke = int(ploshad_uchastka_v_mkv / ploshad_1_gryadki)
    print('На участке поместится грядок:', gryadok_na_uchastke)
    neispolzovannie_metry = ploshad_uchastka_v_mkv - ploshad_1_gryadki * gryadok_na_uchastke
    print('Осталось не занято', int(neispolzovannie_metry), 'квадратных метров')
