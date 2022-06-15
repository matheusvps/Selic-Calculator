# giant_internship
Selic Calculator Program 
I started by interpreting the database, noting that the Selic rate was not updated on weekends and holidays (which makes sense).

From that I created functions:
getDate (which splits the json into columns and rearranges the dates), getRate (which retrieves the Selic rate value of the day), existData ( which checks if the corresponding date exists )

With these functions, I built the financial calculator by accumulating the daily values ​​​​in the starting capital, with due knowledge of compound interest.

From there, I went to solve the technical challenge. In my head, the reasoning is simple: create a loop between 0 and len(json) . Within this loop, I would put at the end of a list the respective gains, with intervals between 500 and 500 days.

From there, the answer would be simple: use the max function and return the highest gain, and retrieve the value of the indices from the loop to see what the date range was.

I've been trying to solve the loop problem since Monday.
I tried what I could between classes and work and dedicated myself to solving the problem. I chose not to upload it completely so you can see what I tried.
