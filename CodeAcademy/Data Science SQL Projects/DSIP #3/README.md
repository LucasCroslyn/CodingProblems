# Introduction
This project is hosted on the CodeAcademy forums as an independant project to gain further understanding of working with fairly basic SQL.
Link: https://discuss.codecademy.com/t/data-science-independent-project-3-education-census-data/419947

# Database
The database is the example database downloaded through the project link above.

The database has information about high school education 

We are not provided a entity relationship diagram as there are only 2 tables. We are also not provided a description of columns but an investigation will be done to see what they are in the work.

# Questions
## Basic Questions
1. How many public high schools are in each zip code? in each state?
2. The locale_code column in the high school data corresponds to various levels of urbanization as listed below. Use the CASE statement to display the corresponding locale_text and locale_size in your query result.
   | locale_text | locale_code (locale_size)              |
   | ----------- | -------------------------------------- |
   | City        | 11 (Large), 12 (Midsize), 13 (Small)   |
   | Suburb      | 21 (Large), 22 (Midsize), 23 (Small)   |
   | Town        | 31 (Fringe), 32 (Distant), 33 (Remote) |
   | Rural       | 41 (Fringe), 42 (Distant), 43 (Remote) |

3. What is the minimum, maximum, and average median_household_income of the nation? for each state?
4. Do characteristics of the zip-code area, such as median household income, influence students’ performance in high school?
## Intermediate Questions
5. On average, do students perform better on the math or reading exam? Find the number of states where students do better on the math exam, and vice versa
## Advanced Challenge
6.  What is the average proficiency on state assessment exams for each zip code, and how do they compare to other zip codes in the same state?