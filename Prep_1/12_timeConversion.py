def timeConversion(s):
    parts = s.strip().split(':')
    hour, minute, second = parts[0], parts[1], parts[2][:2]
    period = parts[2][2:]  # Extract AM/PM

    # Convert hour from 12-hour to 24-hour format
    if period == 'PM' and hour != '12':
        hour = str(int(hour) + 12)
    elif period == 'AM' and hour == '12':
        hour = '00'

    # Format the hour to ensure it is two digits
    if len(hour) < 2:
        hour = '0' + hour

    result = ':'.join([hour, minute, second])
    return result

timeConversion('10:05:45PM')