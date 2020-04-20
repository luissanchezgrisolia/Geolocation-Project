# Geolocation-Project
3rd project for Ironhack bootcamp


**_I am supposted to recently created a new company in the `GAMING industry`. Where should I locate the office?_**

#imagen

### RESUME🎮👨🏻‍💻

As the introduction said, I just created a new company (just imagine).I must decide where to locate the office according to my employees’ preferences, which are the following ones (sorted by my decision criteria):

*Decision criteria: we are all the same in the company so majority preferences are first

- Everyone: near to pubs. 🍸
- 30% of the company: near to kindergarten. 👶🏼
- 20 Designers:  near companies that also do design. 👩🏼‍🎨
- 20 Developers: near successful tech startups (raised at least $ 1M). 💰
- 20 Account managers: near airport. 🛩
- 10 Executives: like Starbucks. ☕️
- 1 CEO: is vegan. 🥦

PS*You can find a detailed explanation of decision making in the WORK DEVELOPMENT section

### WORK PROCESS 💻 ⚙️

In "Input" folder you will find the initial CSV from which I have worked.
I have clean it, and from it I have developed the main.ipynb file in which I have been looking for the perfect place to locate the office.
The whole code I wrote is in SRC folder.

  - Python 3 
  - Mongodb
  - Modules pandas, numpy and regex. 
  - Request module in order to get some information through some APIs
  - Tableau
  - Visual Studio Code


### WORK DEVELOPMENT 👾🗺

*We are all the same in the company so majority preferences are first* 

The two first preferences (pubs & kindergarten) are supplied in almost every city, so next preferences I had to fulfill were "Design companies", "successful tech startups" and "Airports" all of them with the same number of interested people.

1) I started working with "companies CSV" (input folder) and I transformed it, working with Pandas and Mongodb, in order to get the best location near both design and startups companies. Importing that new info to Tableu I finally get a possible location for my office. 👩🏼‍🎨 💰 ✅

2) After that, I checked if that location could fulfill the AM preferences ("Airports"), so I imported airports json file (input folder) with some airports information and again with Mongodb geoquery I found an airport really close. That location was starting to be perfect. 🛩✅ 

(I crossed my fingers so that location will not be in the middle of nowhere and had some activity.)

3) Time to find some pubs near the office. I worked with Foursquare's API and bingo! I found some of them really close. 🍸✅

4) Parents, you have not been forgotten. I located throught Foursquare's API a close kindergarten for your children.👶🏼✅

5) Cooffe for everyone! A Starbucks was found throught Foursquare's API at only 0.5 meters. ☕️✅


I gathered all the information and represented in a map using tableau. You can find the link in the 










Hope you like it.

LSG
