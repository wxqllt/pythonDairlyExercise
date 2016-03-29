from math import sqrt

critics = {'Lisa Rose':{'Lady in the Water':2.5,'snakes on a Plane':3.5,'just my luck':3.0,'superman returns':3.5,'you,me and dupress':2.5,'the night listener':3.0},
           'Gene Seymour':{'Lady in the Water':3.0,'snakes on a Plane':3.5,'just my luck':1.5,'superman returns':5.0,'you,me and dupress':3.5,'the night listener':3.0},
           'Michael Phillips':{'Lady in the Water':2.5,'snakes on a Plane':3.0,'just my luck':3.5,'the night listener':4.0},
           'Claudia Puig':{'snakes on a Plane':3.5,'just my luck':3.0,'superman returns':4.0,'the night listener':4.0,'you,me and dupress':2.5},
           'Mick LaSalle':{'Lady in the Water':3.0,'snakes on a Plane':4.0,'just my luck':2.0,'superman returns':3.0,'you,me and dupress':2.0,'the night listener':3.0},
           'Jack Matthnew':{'Lady in the Water':3.0,'snakes on a Plane':4.0,'just my luck':3.0,'superman returns':5.0,'you,me and dupress':3.5,'the night listener':3.0},
           'Toby':{'snakes on a Plane':4.5,'superman returns':4.0,'you,me and dupress':1.0,}
           }

#欧几里德距离
def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    #如果没有相同 返回0
    if len(si) == 0: return 0
    #求所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return  1/(1+sqrt(sum_of_squares))