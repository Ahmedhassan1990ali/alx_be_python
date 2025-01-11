from datetime import datetime, timedelta

def display_current_datetime():
    current_date_f = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date_f)
    return current_date_f
    
display_current_datetime()
integer =int(input("Enter the numer  of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.now() + timedelta(days=integer)
    future_date_f = future_date.strftime("%Y-%m-%d")
    print (future_date_f)
    return future_date_f
calculate_future_date()