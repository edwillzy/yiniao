import datetime

def isLeapYear(year):
    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return 1
    else:
        return 0

def calTimeGap(formerTime):
    daysMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    currTime = datetime.datetime.now()
    currTimeYear = currTime.year
    currTimeMonth = currTime.month
    currTimeDay = currTime.day
    
    formerTimeList = formerTime.split('-')
    formerTimeYear = int(formerTimeList[0])
    formerTimeMonth = int(formerTimeList[1])
    formerTimeDay = int(formerTimeList[2])
    
    timeGap = 0
    # =
    if(currTimeYear == formerTimeYear):
        if(currTimeMonth == formerTimeMonth):
            timeGap = formerTimeDay - currTimeDay
        else:
            # 对于不同月的日期，先算出两个端点的散天数
            if(formerTimeMonth == 2 and isLeapYear(formerTimeYear)):
                timeGap = (daysMonth[-1] - formerTimeDay) + currTimeDay
            elif(formerTimeMonth == 2 and not isLeapYear(formerTimeYear)):
                timeGap = (daysMonth[2] - formerTimeDay) + currTimeDay
            else:
                timeGap = (daysMonth[formerTimeMonth] - formerTimeDay) + currTimeDay
            # 然后计算除两个端点内的整天数
            for month in range(formerTimeMonth + 1, currTimeMonth):
                if(month == 2 and isLeapYear(formerTimeYear)):
                    timeGap += daysMonth[-1]
                elif(month == 2 and not isLeapYear(formerTimeYear)):
                    timeGap += daysMonth[2]
                else:
                    timeGap += daysMonth[month]
    #--and-...-    
    else:       
        if(formerTimeMonth == 2 and isLeapYear(formerTimeYear)):
            timeGap = (daysMonth[-1] - formerTimeDay) + currTimeDay
        elif(formerTimeMonth == 2 and not isLeapYear(formerTimeYear)):
            timeGap = (daysMonth[2] - formerTimeDay) + currTimeDay
        else:
            timeGap = (daysMonth[formerTimeMonth] - formerTimeDay) + currTimeDay

        for month in range(formerTimeMonth + 1, 13):
            if(month == 2 and isLeapYear(formerTimeYear)):
                timeGap += daysMonth[-1]
            elif(month == 2 and not isLeapYear(formerTimeYear)):
                timeGap += daysMonth[2]
            else:
                timeGap += daysMonth[month]
        
        for month in range(1, currTimeMonth):
            if(month == 2 and isLeapYear(currTimeYear)):
                timeGap += daysMonth[-1]
            elif(month == 2 and not isLeapYear(currTimeYear)):
                timeGap += daysMonth[2]
            else:
                timeGap += daysMonth[month]

        for year in range(formerTimeYear + 1, currTimeYear):
            if(isLeapYear(year)):
                timeGap += 366
            else:
                timeGap += 365
    return timeGap

print(str(calTimeGap('2021-01-02')) + '天')
