import pandas as pd

# Homework 2
df = pd.read_csv('task\\stackoverflow_qa.csv')

#homework2 task1
ts1=df[df['creationdate']<'2024-01-01']
print(ts1)
#homework2 task2
ts2=df[df['score']>50]
print(ts2)
#homework2 task3
ts3=df[(df['score']>=50)&(df['score']<=100)]
print(ts3)
#homework2 task4
ts4=df[(df['ans_name']=='Scott Boston')]
print(ts4)
#homework2 task5
ts5=df[df['answercount']==5]
print(ts5)
#homework2 task6
ts6=df[(df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31') & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)]
print(ts6)
#homework2 task7
ts7=df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print(ts7)
#homework2 task8
ts8=df[df['ans_name'] != 'Scott Boston']
print(ts8)

# Homework 3
titanic_df = pd.read_csv("task\\titanic.csv")

#homework3 task1
ts1=titanic_df[(titanic_df['Sex']=='female')&(titanic_df['Pclass']==1)&(titanic_df['Age']>=20)&(titanic_df['Age']<=30)]
print(ts1)

#homework3 task2
ts2=titanic_df[ titanic_df['Fare']>100  ]
print(ts2)

#homework3 task3
ts3=titanic_df[ (titanic_df['Survived'] == 1) & (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)  ]
print(ts3)

#homework3 task4
ts4=titanic_df[ (titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50) ]
print(ts4)

#homework3 task5
ts5=titanic_df[ (titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)  ]
print(ts5)

#homework3 task6
ts6=titanic_df[ (titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)  ]
print(ts6)

#homework3 task7
ts7=titanic_df[ titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)  ]
print(ts7)

#homework3 task8
ts8=titanic_df[ titanic_df['PassengerId'] % 2 == 1]
print(ts8)

#homework3 task9
ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
ts9 = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print(ts9)

#homework3 task1
ts10=titanic_df[ titanic_df['Name'].str.contains('Miss') & (titanic_df['Pclass'] == 1)  ]
print(ts10)

