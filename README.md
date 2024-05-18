# JobSearchParser
Search specific company websites for a 'career' page, search open positions for a specific job title, and outputs a summary of the job description.

This is a work in progress and is in no way guaranteed to work for your specific needs. Especially considering that I am not a developer.

Basic Functionality:  
Enter a single URL or a list of URLs to parse  
Search for the job opening page (typically searching visable URLs for 'career')  
Search the returned URL for open positions  
Summarize the requirements of the open position  
Provide a link to apply for the position  

Dreams for v2  
Add AI abilities to prioritize requirements to customize your resume  
Auto apply to position  

Completed as of 20240518:  
Starts with a csv file of urls of the target companies  
Built a csv to json converter to make it easier for my brain to work with. So far this is just a manual step, but easy enough to automate, and it was good practice.  
Parse the json file for urls  
scan the url for links that contain the word/phrase "career", "join the team", etc.  
scan THOSE urls for my preferred job titles "project manager", "director pmo", etc.  
IF it contains the above, it captures the section of the page containing the search strings, and logs it to an object  
finally it outputs the object to a json file  

It ain't exactly pretty, and my entire thought process is laid out in the repository, but by god it works.  