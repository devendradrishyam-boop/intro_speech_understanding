def next_birthday(date, birthdays):
    '''
    Find the next birthday after the given date.

    @param:
    date - a tuple of two integers specifying (month, day)
    birthdays - a dict mapping from date tuples to lists of names, for example,
      birthdays[(1,10)] = list of all people with birthdays on January 10.

    @return:
    birthday - the next day, after given date, on which somebody has a birthday
    list_of_names - list of all people with birthdays on that date
    '''
    if not birthdays:
        return None, []

    # Sort all keys (dates) chronologically
    sorted_dates = sorted(birthdays.keys())

    # Find the first date strictly greater than the given date
    next_date = None
    for d in sorted_dates:
        if d > date:
            next_date = d
            break

    # If no date is found after the given date, wrap around to the beginning of the year
    if next_date is None:
        next_date = sorted_dates[0]

    return next_date, birthdays[next_date]
    
