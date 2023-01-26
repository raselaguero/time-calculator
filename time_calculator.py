def func_hours(dura_h, hours, ini_h):
    if dura_h >= 24:
        div = dura_h / 24
        if str(div).__contains__('.'):
            decima = str(div).partition('.')[2][:2]
            decima = (int(decima) * 0.01) * 24
            h, m = str(decima).partition('.')[0], str(decima).partition('.')[2]
            hours += int(h)
            if int(m) > 59:
                hours += 1
        else:
            hours += div
    else:
        hours = ini_h + dura_h
    return hours

def func_minutes(minutes, hours):
     if minutes > 59:
        minutes -= 60
        if len(str(minutes)) == 1:
            minutes = '0{}'.format(minutes)
        hours += 1
     return minutes, hours

def func_cant_days(cant, merid, meridian, days, d):
    if cant < 1 and ((merid == 'PM') and merid != meridian):
        days = '(next day)'
        d = 1
    if cant == 1:
        days = '(next day)'
        d = 1
    if cant > 1 and str(cant).__contains__('.'):
        cant = str(cant).partition('.')[0]
        d = int(cant)+1
        days = '({} days later)'.format(d)
    return days, d

def func_meridian(hours, meridian):
    change = hours // 12
    if change % 2 != 0:
        if meridian == 'AM':
            meridian = 'PM'
        else:
            meridian = 'AM'
    return meridian

def func_week_day(day, week, d):
    if day != '':
        for w in range(1, len(week)):
            if week[w] == day:
                suma = d + w
                if suma > 7:
                    day = week[suma - 7]
                else:
                    day = week[suma]
                break
    return day

def add_time(inicio, duracion, day=''):
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    dura_h, dura_m = int(duracion.partition(':')[0]), int(duracion.partition(':')[2])
    time, meridian = inicio.partition(' ')[0], inicio.partition(' ')[2]
    ini_h, ini_m = int(time.partition(':')[0]), int(time.partition(':')[2])
    day = day.lower().title()
    hours = ini_h
    minutes = ini_m + dura_m
    cant = (ini_h + dura_h) / 24
    days = ''
    d = 0
    merid = meridian

    hours = func_hours(dura_h, hours, ini_h)
    minutes, hours = func_minutes(minutes, hours)
    meridian = func_meridian(hours, meridian)
    days, d = func_cant_days(cant, merid, meridian, days, d)
    day = func_week_day(day, week, d)

    if 12 < hours <= 24:
        hours -= 12
    if hours > 24:
        hours -= 24

    if day != '':
        print('{}:{} {}, {} {}'.format(hours, minutes, meridian, day, days))
    else:
        print('{}:{} {} {}'.format(hours, minutes, meridian, days))