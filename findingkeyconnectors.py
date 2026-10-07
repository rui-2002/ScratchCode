from __future__ import division
from collections import Counter
from collections import defaultdict

users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# add list of friends for each users

for user in users:
    user["friends"]=[]

for i , j in friendships:
    users[i]["friends"].append(users[j]) # add i as friend of j
    users[j]["friends"].append(users[i]) # add j as friend of i


def number_of_friends(user):
    """how many friends user have"""
    return len(user["friends"])


total_connection=sum(number_of_friends(user) for user in users)

print(f"Total no. of connections : {total_connection}")


# total no . of avg connections
num_users=len(users)
avg_connections=total_connection/num_users

print(f"avg connections : {avg_connections}")

# number of friends by id 
num_friends_by_id=[(user["id"],number_of_friends(user))for user in users]

print(num_friends_by_id)


# sorting

sorted_num_friends_by_id=sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)

print(sorted_num_friends_by_id)


def friend_of_friend(user_id):
    friends=[]
    for friend in user_id["friends"]:
        for friend_of_friend in friend["friends"]:
            friends.append(friend_of_friend["id"])

    return friends


print("friend of friend")
print(friend_of_friend(users[0]))

print([friend["id"] for friend in users[0]["friends"]])
print([friend["id"] for friend in users[1]["friends"]])
print([friend["id"] for friend in users[2]["friends"]])


# Another way of finding friend of friend :

def not_the_same(user,other_user):
    """two users are not same if their id differs"""
    return user["id"]!=other_user["id"]


def not_friend(user, another_user):
    for friend in user["friends"]:
        if friend["id"] == another_user["id"]:
            return False

    return True

print("Are they friends :")
print(not_friend(users[0],users[3]))


def friends_of_friends_ids(user):
    fof_ids = []

    for friend in user["friends"]:
        for fof in friend["friends"]:
            if fof != user and fof not in user["friends"]:
                fof_ids.append(fof["id"])

    return fof_ids
        

print(Counter(friends_of_friends_ids(users[3])))


interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# find user with certain interest 

def find_user_interest(interest):
    ids=[]
    for id in interests:
        if id[1]==interest:
            ids.append(id[0])
    return ids

print(f"User id with interest : {find_user_interest('probability')}")


# for large dict , we should make mapping from interest to user ids

user_ids_by_interest=defaultdict(list)

# keys are interests , values are list of user_ids with that interest
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)


print(user_ids_by_interest)


def most_common_interest():
    common = 0

    for interest in user_ids_by_interest:
        count = 0

        for user in user_ids_by_interest[interest]:
            count += 1

        common = max(common, count)

    return common

print(most_common_interest())


salaries_and_tenures = [
(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]


salary_by_year=defaultdict(list)

for salary , year in salaries_and_tenures :
    salary_by_year[year].append(salary)

print(salary_by_year)

# average salary by tenure
average_salary_by_tenure={
    year : sum(salary)/len(salary)
    for year , salary in salary_by_year.items()
}

print(average_salary_by_tenure)