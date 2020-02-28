import datetime
import holidays



def conv_str_to_date(dateday_str):
    dateday = datetime.datetime.strptime(dateday_str, '%d/%m/%Y')
    return dateday

def check_if_not_holiday(dateday):
    pt_holidays = holidays.PT()
    is_holyday = dateday not in pt_holidays

    return is_holyday



dateday_beg = '01/01/2020' #input('Informe primeira data (dd/mm/yyyy): ')
dateday_end = '30/04/2020' #input('Informe última data (dd/mm/yyyy): ')

dateday_beg = conv_str_to_date(dateday_beg)
dateday_end = conv_str_to_date(dateday_end)


day = datetime.timedelta(days=1)

while dateday_beg <= dateday_end:
    if (check_if_not_holiday(dateday_beg) and dateday_beg.weekday() not in (5, 6)):
        print(str(dateday_beg)+ ' is not an workday.')
    else:
        print(str(dateday_beg) + ' is an holiday or weekend.')
    
    dateday_beg += day




# pt_holidays = holidays.PT()
# is_holyday = '25/12/2020' in pt_holidays

# dateday_list = daterange(dateday_beg, dateday_end)


# def daterange(start_date, end_date):
#     dateday_list = []
#     for n in range(int ((end_date - start_date).days)):
#         dateday_list.append(yield start_date + timedelta(n))
    
#     return dateday_list

# print(is_holyday)

# dateday_obj = conv_str_to_date(dateday)

# print(dateday_obj.weekday())

# dateday_str = datetime.datetime.strftime(dateday_obj, '%d/%m/%Y')

# print(dateday_str)