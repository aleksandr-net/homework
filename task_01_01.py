#!/usr/bin/python3.5

print('Введите площадь садового участка (в сотках)')
ploshad_uchastka_v_sotkah = float(input())
if ploshad_uchastka_v_sotkah < 0:
    print('Введены некорректные данные!')
else:
    ploshad_1_gryadki = 15 * 25
    ploshad_uchastka_v_mkv = ploshad_uchastka_v_sotkah * 100
    gryadok_na_uchastke = int(ploshad_uchastka_v_mkv / ploshad_1_gryadki)
    neispolzovannie_metry = ploshad_uchastka_v_mkv - ploshad_1_gryadki * gryadok_na_uchastke
    print(int(neispolzovannie_metry))
