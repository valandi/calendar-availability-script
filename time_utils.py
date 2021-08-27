import datetime

def convert_time_string_to_id(time_str):
    time_arr = time_str.split(':')
    return int(int(time_arr[0]) * 4 + int(time_arr[1]) / 15)

def convert_id_to_time_string(fifteen_minute_id):
    hours = int(fifteen_minute_id / 4)
    minutes = int(fifteen_minute_id % 4) * 15
    return str(hours) + ":" + str(minutes).zfill(2)

def get_next_x_work_dates(x):
    next_five_work_dates = []
    today = datetime.date.today()

    curr = today
    while len(next_five_work_dates) < x:
        if curr.weekday() < 5:
            next_five_work_dates.append(str(curr))
        curr = curr + datetime.timedelta(days=1)
    return next_five_work_dates