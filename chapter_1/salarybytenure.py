
from collections import defaultdict


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

def tenure_bucket(tenure):
    if tenure <2 :
        return "less than two"
    elif tenure <5 :
        return "between two and five"
    else :
        return "more than five"
    
# grouping salary acc. to tenure bucket
salary_by_tenure_bucket=defaultdict(list)


for salary , tenure in salaries_and_tenures:
    bucket=tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

print(salary_by_tenure_bucket)


# computing salary of each group 
average_salary_by_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
}
        
        

