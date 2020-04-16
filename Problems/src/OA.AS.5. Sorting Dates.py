import datetime as dt


def sortDates(dates):
    # Write your code here

    aux = sorted([(dt.datetime.strptime(d, '%d %b %Y'), d) for d in dates])
    return [d[1] for d in aux]


print(sortDates(['01 Jan 2020', '02 Feb 2019', '05 Dec 1999', '30 Jun 2000']))
