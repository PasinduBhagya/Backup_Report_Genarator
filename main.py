import datetime

non_weekly = ['18h00m-daily','21h00m-daily','00h00m-daily','03h00m-daily','06h00m-daily','09h00m-daily','12h00m-daily','15h00m-daily',]
weekly = ['18h00m-daily','21h00m-daily','00h00m-weekly','03h00m-weekly','06h00m-weekly','09h00m-weekly','12h00m-weekly','15h00m-weekly',]

today_date = datetime.date.today()
yesterday_date = today_date - datetime.timedelta(days=1)
if today_date.weekday() == 6:
    folder_list = weekly
else:
    print(non_weekly)
    folder_list = non_weekly
    
for index_value, folder_name in enumerate(folder_list):
    if index_value < 2:
        folder_path = str(yesterday_date) + "-" + folder_name
    else:
        folder_path = str(today_date) + "-" + folder_name

    # folder_path 