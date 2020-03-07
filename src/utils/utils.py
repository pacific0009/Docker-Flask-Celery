import datetime
def date_to_str(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")
def str_to_date(date_str):
    return datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")