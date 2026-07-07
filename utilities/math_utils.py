def calculate_fine(overdue_days:int,fine_per_day:float=5.0)->float:
    if overdue_days<=0:
        return 0.0
    return overdue_days*fine_per_day