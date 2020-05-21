f = open("weather.txt", "r", encoding='utf8')
weather = []
lines = f.readlines()
for i in range(len(lines)):
    weather.append(lines[i].strip().split(','))
weather = weather[1:]

# Province,City,Year,Month,Day,Weather,Max Temperature (℃),Min Temperature (℃),Rainfall (mm),Snowfall (cm)
Province = []
City = []
Date = []
for i in weather:
    if i[0] not in Province:
        Province.append(i[0])
    if i[1] not in City:
        City.append(i[1])
    if (i[2], i[3], i[4]) not in Date:
        Date.append((i[2], i[3], i[4]))

# 1. province 별 평균 강수량 구하기
Province_rain = [0] * len(Province)
Province_dates = [0] * len(Province)
for i in weather:
    for p in range(len(Province)):
        if i[0] == Province[p]:
            Province_rain[p] += float(i[8])
            Province_dates[p] += 1

print("Province, average rain fall")
for i in range(len(Province)):
    print(Province[i] + ",", Province_rain[i] / Province_dates[i])

# 2. City 별 눈이 가장 많이 온 날 구하기
City_snow_day = [[-1, (0, 0, 0)] for i in City]
for i in weather:
    for c in range(len(City)):
        if i[1] == City[c]:
            if float(i[9]) > City_snow_day[c][0]:
                City_snow_day[c][0] = float(i[9])
                City_snow_day[c][1] = (i[2], i[3], i[4])

print("\nCity, max snow day")
for i in range(len(City)):
    print(City[i] + ",", City_snow_day[i][1])

# 3. 전국 단위 비가 가장 많이 온 Year+Month+Day 구하기
Date_rain = [[0, date] for date in Date]
for i in weather:
    for d in range(len(Date)):
        if (i[2], i[3], i[4]) == Date[d]:
            Date_rain[d][0] += float(i[8])
            Date_rain[d][1] = Date[d]
Date_rain.sort(reverse=True)
print("\nmaximum rain in", Date_rain[0][1])

# 4-1. 날짜 별 가장 낮은 최저 기온을 갖는 city 구하기
Date_low = [[1000, "city", date] for date in Date]
for i in weather:
    for d in range(len(Date)):
        if (i[2], i[3], i[4]) == Date[d]:
            if float(i[7]) < Date_low[d][0]:
                Date_low[d][0] = float(i[7])
                Date_low[d][1] = i[1]
                Date_low[d][2] = Date[d]
print("\nDate, City with lowest min temperature")
for i in range(len(Date)):
    print(str(Date[i]) + ",", Date_low[i][1])

# 4-2. 4-1의 city 빈도에 따라 정렬하기
City_low = [[0, city] for city in City]
for c in range(len(City_low)):
    City_low[c][1] = City[c]
for i in range(len(Date)):
    for c in range(len(City)):
        if Date_low[i][1] == City_low[c][1]:
            City_low[c][0] += 1
City_low.sort(reverse=True)
print("\nnumber, City")
for i in City_low:
    print(i)
