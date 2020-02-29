import datetime
import holidays



def conv_str_to_date(dateday_str):
    dateday = datetime.datetime.strptime(dateday_str, '%d/%m/%Y')
    return dateday

def check_if_not_holiday(dateday):
    pt_holidays = holidays.PT()
    is_holyday = dateday not in pt_holidays

    return is_holyday
