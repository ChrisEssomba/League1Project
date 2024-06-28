import scrapy

class Rankingspider(scrapy.Spider):
    name = 'ranker'
    start_urls = ['https://www.premierleague.com/tables?co=1&se=578&ha=-1&team=FIRST']
    
    def parse(self, response):
        
        #1 We store the table in a variable
        table = response.css('table')

        #2 We store the rows in a variable
        rows = table.css('tbody tr:not(.league-table__expandable.expandable)')
        rows = rows[0:20] #we only want the first 20
        
        #3 We loop over each row
        for row in rows:
            # Extract data from each cell
            Ranking = row.css('td > span.league-table__value.value::text').get()
            Teams = row.css('td > a > span.league-table__team-name.league-table__team-name--long.long::text').get()
            Played = row.css('td:nth-child(3)::text').get()
            Won = row.css('td:nth-child(4)::text').get()
            Drawn = row.css('td:nth-child(5)::text').get()
            Lost =row.css('td:nth-child(6)::text').get()
            Points = row.css('td:nth-child(10)::text').get()
            
            #4 We Yield the result
            yield {
                'Position': Ranking,
                'Club': Teams,
                'Played': Played,
                'Won': Won,
                'Drawn': Drawn,
                'Lost': Lost,
                'Points': Points
            }
