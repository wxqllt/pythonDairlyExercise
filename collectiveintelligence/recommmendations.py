#!/usr/bin/python
# -*-coding: utf-8 -*-
from math import sqrt

critics = {'Lisa Rose':{'Lady in the Water':2.5,'snakes on a Plane':3.5,'just my luck':3.0,'superman returns':3.5,'you,me and dupress':2.5,'the night listener':3.0},
           'Gene Seymour':{'Lady in the Water':3.0,'snakes on a Plane':3.5,'just my luck':1.5,'superman returns':5.0,'you,me and dupress':3.5,'the night listener':3.0},
           'Michael Phillips':{'Lady in the Water':2.5,'snakes on a Plane':3.0,'just my luck':3.5,'the night listener':4.0},
           'Claudia Puig':{'snakes on a Plane':3.5,'just my luck':3.0,'superman returns':4.0,'the night listener':4.0,'you,me and dupress':2.5},
           'Mick LaSalle':{'Lady in the Water':3.0,'snakes on a Plane':4.0,'just my luck':2.0,'superman returns':3.0,'you,me and dupress':2.0,'the night listener':3.0},
           'Jack Matthnew':{'Lady in the Water':3.0,'snakes on a Plane':4.0,'just my luck':3.0,'superman returns':5.0,'you,me and dupress':3.5,'the night listener':3.0},
           'Toby':{'snakes on a Plane':4.5,'superman returns':4.0,'you,me and dupress':1.0,}
           }


# 欧几里德距离
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    # 如果没有相同 返回0
    if len(si) == 0: return 0
    # 求所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return  1/(1+sqrt(sum_of_squares))


# 皮尔逊相关系数
def sim_pearson(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:si[item] = 1
    # 如果没有相关返回0
    n = len(si)
    if len(si) == 0: return  0

    # 对所有偏好求和
    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    # 求平方和
    sumsq1 = pow([prefs[person1][item] for item in si], 2)
    sumsq2 = pow([prefs[person2][item] for item in si], 2)

    # 求乘积和
    pSum = sum(prefs[person1][item]*prefs[person2][item] for item in si)

    # 求pearson coefficent
    num = pSum - (sum1*sum2/n)
    den = sqrt((sumsq1-pow(sum1, 2)/n)*(sumsq2-pow(sum2,2)/n))
    if den == 0:
        return 0
    r = num/den
    return r


# 从反映偏好的字典中返回最佳匹配者,返回结果的个数和相似度函数均为可选参数
# 返回值越接近1匹配度越高
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# 利用所有他人评论价值的加权平均作为评分,为某人提供意见
def getRecommendations(prefs, person, similarity=sim_pearson):
    # 相似度与评分乘积之和
    totals = {}
    # 相似度之和
    simSums = {}
    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue
        # 对自己没有看过的电影进行评价
        for item in prefs[person]:
            if prefs[person][item] == 0 or item not in prefs[person]:
                # 相似度*评分
                totals.setdefault(item, 0)
                totals[item] += sim*prefs[other][item]
                # 相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # 归一化列表
    rankings = [(total/simSums[item], item) for item, total in totals.items()]

    # 返回经过排序的列表
    rankings.sort()
    rankings.reverse()
    return rankings


# 把critics转换成电影为key每个人的评分为value的字典
def transformPrefs(prefs):
    result = {}
    for name in prefs:
        for item in prefs[name]:
            result.setdefault(item, {})
            result[item][name] = prefs[name][item]
    return result







