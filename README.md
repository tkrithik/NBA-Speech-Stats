**Inspiration:**
The debates in the basketball world seem to be never-ending, and there have been numerous controversies surrounding the rankings of NBA players for a particular season. Being huge basketball enthusiasts ourselves, we know how big of a role statistics plays when it comes to comparing two or more players. Most websites today, although they provide a wide range of statistics, but little to no website addresses the blind. We believe the blind should have access to stats just as easily as everybody else. Thus, we made our stats website almost entirely navigable and useable by voice. meaning statistics of every current NBA player at the tip of everyone's fingertips, or rather, at the tip of their tongues.

**Function:**
Our program takes in one of two possible inputs: a certain statistic of a particular player, or those of a specific team. Our program gives the user the option of displaying a certain type of statistic (for example, points or rebounds), or displaying it all at the same time. This is true for both one particular player and a team. Furthermore, our code also gets from the file the user uploaded, and then creates a copy of the file in a local repository. This file will later be converted to text, to determine what stats the user wants, and then an audio file will be posted that responds to the user telling them their stats.

**How We Built It:**
The first thing that we did to create this program was to web scrape information from a particular basketball-related API. After storing this information, we then proceeded to separate the important words of the sentence (that the user would speak out) from the unimportant ones, and stored them in specific global variables. We then built our program such that it would be able to recognize whether the user was inquiring about a player or a team and whether they wanted to see all statistics at once or just one particular statistic. We then created a dictionary in our program, where we assigned keys to certain statistics for them to be displayed when called upon. The only thing remaining was to then convert the speech to an audio file, and vice versa once it had been processed. The way we did this was using a google web speech to text api. This api allowed us to convert the user's input, or their spoken command, into text, which python could then process. After converting it to text using this api, we determined the stat the user asked for, and then returned a string, which was converted into sound using gtts. This sound file was then available for the user to download and listen to their stats on.

**Challenges We Ran Into:**
One major challenge we ran into was the fact that the various teams in the NBA had different numbers of words in them. For example, when we initially structured our program, we noticed that the code only seemed to work for teams with two words (like the Miami Heat, or the Boston Celtics). The code would not work for teams with three words (like the Golden State Warriors, or the Los Angeles Lakers). As a result, we were forced to create a more generalized algorithm that was able to recognize the words that were important regardless of the number of words a team had. The same problem occurred with a couple of metrics too. Although we initially assumed that each metric was one-word, we quickly realized that this was not the case as “Three Pointers” and “Field Goals” were made up of more than one word. Another aspect we found challenging while creating this program was designing the HTML page since neither of much had much experience with it. It took us watching a lot of Youtube tutorials and articles online, but we were able to make our site more visually appealing. Another challenge we ran into regarding the speech to text was Flask not properly retrieving files the user downloaded. However, by adding post and get arguments, as well as storing the received file in a dedicated folder, we were able to retrieve the user's audio file. We also had trouble regarding the use of the google api. However, after documentation and research we were able to create a function that in took the audio and returned string for python to process.

**Accomplishments That We’re Proud Of:**
One thing that we are extremely proud about was being able to concise all the various statistics into one dictionary and using just one print statement to display any particular statistic (or all statistics) for any player or team. As mentioned above, this was one aspect of the program that we found especially challenging, so it felt really good to get over that hump. Another thing we are extremely proud of is the lack of experience and the ability we were able to perform at. For half of our team, this was their 1st hackathon, and for the other half, their 2nd. Furthermore, we also had used Flask and google speech to text api very minimalistically in the past, and through research and documentation, we were able to over come this challenge.

**What We Learned:**
As neither one of us was familiar with Flask before this, this was something that we learned over the course of creating this program. We found this to be an extremely useful skill for the future because we can use it to develop lots more web applications for other hackathons. Another thing that we learned while creating this program was how to effectively web scrape because we realized just how effective this process is and how much time we can save and dedicate to other aspects of programs. Lastly, the use of the google speech to text api helped us learn a new method to achieving a goal. originally, we planned to use AWS, as our team had past experience working with it, but to manage cost efficiently, we researched alternate solutions, greatly aiding us in our code.

**Next Steps for our Program:**
We wanted to create a server for this program, where would input a live audio feed. However, we were not able to do it this time because we did not have the necessary resources to do so. One additional add-on that we would like to make to this program includes a wider range of statistics that the user can choose to ask from. This could be achieved by possibly combining information from two or more APIs, which gives us more parameters for the arguments. Furthermore, we also wanted to make our code more hands free, including the audio playing back to the user, not by downloading. We also want to implement a server, given the proper resources, so our project can truly help the blind people in need out in the world interested in sports.
