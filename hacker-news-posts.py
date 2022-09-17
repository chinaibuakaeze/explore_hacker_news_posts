from csv import reader
import os
import sys
import datetime as dt

#function to read file 
def read_file(filename = "HN_posts.csv"):
    with open(os.path.join(sys.path[0], filename)) as opened_file:
        hacker_news = reader(opened_file)
        hacker_news = list(hacker_news)
    return hacker_news

hn = read_file()

#remove header from the list of lists
hacker = hn[1:]

#remove the rows without comment
dataset= []
for row in hacker:
    if row[4] != "0":
        dataset.append(row)

#filter posts to get only posts that begin with Ask HN or Show HN
ask_posts = []
show_posts = []
other_posts = []

for row in dataset:
    title = row[1]
    title = title.lower()
    if title.startswith('ask hn'):
        ask_posts.append(row)
    elif title.startswith('show hn'):
        show_posts.append(row)
    else:
        show_posts.append(row)

#Determine if asks posts or show posts receive more comments on average 
total_ask_comments = 0
for row in ask_posts:
    num_comments = int(row[4])
    total_ask_comments += num_comments
avg_ask_comments = total_ask_comments/(len(ask_posts))

total_show_comments = 0
for row in show_posts:
    total_show_comments += int(row[4])
avg_show_comments = total_show_comments/len(show_posts)

#Focus remaining analysis on show posts since they're likely to receive more comments

#Calculate the number of show posts created in each hour of the day
result_list = []
counts_by_hour = {}
comments_by_hour = {}

for row in show_posts:
    created_at = row[6]
    num_comments = int(row[4])
    result_list.append([created_at, num_comments])

for row in result_list:
    date = row[0]
    date = dt.datetime.strptime(date, "%m/%d/%Y %H:%M")
    hour = dt.datetime.strftime(date, "%H")
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = row[1]
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += row[1]

#Calculate the average number of comments per post for posts created during each hour of the day
avg_by_hour = []
for row in comments_by_hour:
    avg_by_hour.append([row, comments_by_hour[row]/counts_by_hour[row]])

#Sort the list of average hours
swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
sorted_swap = sorted(swap_avg_by_hour, reverse = True)
print("Top 5 hours for Show comments: ")
print("\n")
for comment in sorted_swap[:5]:
    time = dt.datetime.strptime(comment[1], "%H")
    time = dt.datetime.strftime(time, "%H:%M")
    print(f"{time}: {comment[0]:.2f} comments per post.")
