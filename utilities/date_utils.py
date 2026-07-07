from datetime import datetime
def get_current_datetime()->datetime:
    return datetime.now()
def calculate_days_difference(start_date:datetime,end_date:datetime)->int:
    difference=end_date-start_date
    return difference.days
