# Exploring hacker news posts

This project explores a dataset of submissions to popular technology site Hacker News. Hacker news is a site similar to reddit where user-submitted stories are voted and commented upon. The dataset can be found [here](https://www.kaggle.com/datasets/hacker-news/hacker-news-posts). The dataset contains approximately 300,000 rows. 

### Column Description

Here are the descriptions of the columns:
* id: The unique identifier from hacker news for the post
* title: The title of the post 
* url: The url that the post links to, if it has a url
* num_points: The number of points the post acquired. (Total number of upvotes - total number of downvotes)
* num_comments:The number of comments that were made on the post 
* author: The username of the person who submitted the post
* created_at: The date and time at which the post was submitted

I'll compare two types of posts `Ask HN` and `Show HN`. Users submit Ask HN posts to ask the hacker news community a specific question. Similarly, users submit Shown HN posts to show the hacker news community a project, a product, or generally anything interesting. I'll compare these posts to determine:
* Do `Ask HN` or `Show HN` receive more comments on average?
* Do posts created at a certain time receive more comments on average?

**Below is a sample dataset that I'll explore for this project:**

[['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at'],
 ['12579008',
  'You have two days to comment if you want stem cells to be classified as '
  'your own',
  'http://www.regulations.gov/document?D=FDA-2015-D-3719-0018',
  '1',
  '0',
  'altstar',
  '9/26/2016 3:26'],
 ['12579005',
  'SQLAR  the SQLite Archiver',
  'https://www.sqlite.org/sqlar/doc/trunk/README.md',
  '1',
  '0',
  'blacksqr',
  '9/26/2016 3:24'],
 ['12578997',
  'What if we just printed a flatscreen television on the side of our boxes?',
  'https://medium.com/vanmoof/our-secrets-out-f21c1f03fdc8#.ietxmez43',
  '1',
  '0',
  'pavel_lishin',
  '9/26/2016 3:19'],
 ['12578989',
  'algorithmic music',
  'http://cacm.acm.org/magazines/2011/7/109891-algorithmic-composition/fulltext',
  '1',
  '0',
  'poindontcare',
  '9/26/2016 3:16']]
  
  ### Analysis Steps
**For analyzing this data, I did the following:**
* I cleaned the data and removed the rows without any commments since the focus is on analyzing the number of comments. This reduced the number of rows for the data from approximately 300,000 to about 80,401 rows.
* I removed the header and analyzed the rest of the data
* I filtered the data to get only posts that begin with Ask HN or Shown HN
* I determined that show posts(posts begining with Show HN) have higher comments on average
* I focused the remaining analysis on show posts since they're likely to receive more comments
* I calculated the number of show posts created in each hour of the day, then calculated the average number of comments per post for posts created during each hour of the day and finally determined if posts created at a certain time receive more comments on average.


## Conclusion

I determined that `Show HN` posts received more comments on average. The average number of comments received by `Ask HN` posts was 13.74 while `Show HN` posts received 24.73 comments.
Also, posts created at a certain time receive more comments on average. Posts created at `13:00` received an average of 27.73 comments per post. This was the highest average comments of any Show HN posts. Since the dataset was collected in eastern time, the best time to post on hacker news for more engagement is at `1:00 PM EST`.
