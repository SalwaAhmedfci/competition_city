import csv

import array

# function to find if
# given point lies inside
# a given rectangle or not.
import csv




def checking_Points(x,y,x1,y1,x2,y2,cityName):
    result = []
    res = ["None"]
    if ((x >= x1 and x <= x2) or (x <= x1 and x >= x2)):
        inside_x = True
    else:
        inside_x = False
    if ((y >= y1 and y <= y2) or (y <= y1 and y >= y2)):
        inside_y = True
    else:
        inside_y = False

    if (inside_x == True and inside_y == True) :
        return True
    else:
        return False









if __name__ == "__main__":
    # initializing_lists
    cities_List = [];
    pointList = [];
    result = [];
    # reading from files

    with open('points.csv', 'r') as point_file:
        points = csv.reader(point_file)
        for row in points:
            pointList.append(row)
        points2check = pointList[1:]



    with open('cities.csv', 'r') as cities_file:
        cities = csv.reader(cities_file)
        for row in cities:
            cities_List.append(row)
        cities = cities_List[1:]





    listofcities = []

    for point in points2check:
        cityNameFinal = "None"

        x = int(point[1])
        y = int(point[2])

        for city in cities:
            cityName = city[0]
            x1 = int(city[1])
            y1 = int(city[2])
            x2 = int(city[3])
            y2 = int(city[4])
            if (checking_Points(x, y, x1, y1, x2, y2, cityName)==True):
                cityNameFinal = cityName;
                break

        result.append(checking_Points(x, y, x1, y1, x2, y2, cityNameFinal))
        print(cityNameFinal)
