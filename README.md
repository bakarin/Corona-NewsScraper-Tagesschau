# Corona-NewsScraper-Tagesschau
## Project Motivation
In Germany, the first case of Corona virus was reported at the end of January 2020. It was an employee at the Webasto company, who had gotten infected by a Chinese colleague. The news started to cover more and more about the Corona virus as the number of cases rose, both nationally and internationally. By 9th March there were more than 1,000 people infected in Germany and the Health Minister asked to cancel any large events. 

On that day I decided to track news articles about the topic featured on Germany's biggest news portal [Tagesschau](https://www.tagesschau.de/). I try to track once per day between 6 and 7 pm before the popular 15 minute live airing of the Tagesschau news on the public TV station ARD at 8 pm.

| Date | Description | Number of Cases |
| :--- | :--- | ---: |
| 27 Jan 2020 | first reported case of Corona virus in Germany | 1 |
| 09 Mar 2020 | cancellation of any events with more than 1,000 participants by the Health Minister | 1,000+ |
| 16 Mar 2020 | churches, sports clubs, schools across the country remain closed in most federal states | 7,000+ |
| 22 Mar 2020 | announcement of a national "contact ban" by chancellor Angela Merkel | 29,000+ |


## Technical Details
The program parses the starting page of [Tagesschau](https://www.tagesschau.de/) for titles or abstracts that contain the word _corona_ or _covid_. It then extracts the full text articles and saves them to a csv in the /data folder together with a timestamp and the news category it was posted in.

![Alt text](/images/tagesschau_screenshot.png?raw=true "Title")

## Installations
* Python version 3
* Beautiful Soup
* Pandas

## Coming Soon...
* Planning to run the script automatically at a scheduled time
* Planning on doing some Natural Language Processing on the data to gain some insights on how official communication is evolving over time


