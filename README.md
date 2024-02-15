# SalesAI
Sales enhancement through AI for finding treatment clinics

## Notes from 1st Meeting
Choose a treatment, e.g. Emsculpt

Find clinics which offer the treatment, usually choose clinics which offer expensive versions of the treatment as these clinics are most likely to pay for the service Sam provides. 
Check the clinic websites, the two main criteria used to determine whether the clinics qualify are:
1.	The quality of the website, i.e., whether the website is made professionally or not, can be checked by verifying the domain name and checking if it contains a web builder’s name, like wix.
2.	Check if the clinic has a team.
 
He usually contacts 60 customers a day, where 20 customers are contacted in an hour, and the conversion rate of potential customers to actual clients is 3 a day. 

**The most time-consuming aspect of his day is the actual finding of the customers.** 

Therefore, the steps are:
1.	Build a simple webcrawler using BeautifulSoup, that obtains all websites of clinics that offer the treatment in question.
2.	Build an LLM empowered webscraper that goes through the obtained websites and qualifies them.
3.	Upload all the relevant data from the qualified websites into an excel file.
4.	Wrap this in a nice UI using streamlit or similar libraries.
5.	Deploy.
Other technical aspects and work split will be discussed later.
Obviously, this shouldn’t be “that” time consuming, but we will pitch a 2-month project for a currently defined price of about £6000. 
Need to get in touch with Sam’s brother. 

