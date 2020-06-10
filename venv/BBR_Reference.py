import pprint
from bs4 import BeautifulSoup
import requests


class BBRScraper(object):

    def __init__(self, playerFirstName, playerLastName):
        self.playerFirstName = playerFirstName.lower()
        self.playerLastName = playerLastName.lower()
        URL = 'https://www.basketball-reference.com/players/' + playerLastName[0] + '/' + playerLastName[
                                                                                          0:5] + playerFirstName[
                                                                                                 0:2] + '01.html'
        self.page = requests.get(URL)

    def singleYearStats(self, year):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        year = soup.find(id='per_game.' + str(year))
        # id = "per_game.1985"

        statsTable = soup.find(id='per_game')
        statTableHead = statsTable.find("thead")
        statTableBody = statsTable.find("tbody")

        yearStats = year.find_all('td')
        for tableBody in statTableBody.find_all('th'):
            print(tableBody.text.strip())

        """for stat in yearStats:
            print(stat.text.strip())"""

    def getAllPerGameStats(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        perGameStatsTable = soup.find(id='per_game')

        statTableHead = perGameStatsTable.find("thead")
        statTableBody = perGameStatsTable.find("tbody")

        statsColumnLabel = (statTableHead.text.strip()).split("\n")
        statsRowLabel = (statTableBody.text.strip()).split("\n")
        # careerPerGameData = perGameStatsTable.find_all('tr')
        # print(perGameStatsTable)

        perGameCareerStats = dict()
        for row in statTableBody.find_all('th'):
            perGameCareerStats[row.text] = []
            for col in statsColumnLabel:
                perGameCareerStats[row.text].append(col)

        # print(perGameCareerStats)

    # print(year1Pos)
    """def seasonStats(self, seasonStatsType):
        soup2 = BeautifulSoup(self.page.content, 'html.parser')
        careerData = soup2.find(id=seasonStatsType)
        careerStats = careerData.find_all('tr')
        for years in careerStats:
            print(years.text.strip())


        id = "div_per_game"
        id = "div_totals"
        id = "all_per_minute"
        id = "all_per_poss"
        id = "all_advaced"
        id = "all_shooting"
        id = "all_pbp"   
        id = "all_year-and-career-highs"
        id = "all_playoffs_per_game"
        id = "all_playoffs_totals"
        id = "all_playoffs_per_minute"
        id = "all_playoffs_per_poss"
        id = "all_playoffs_advanced"
        id = "all_playoffs_shooting"
        id = "all_playoffs_php"
        id = "all_all_star" # can count this to figure out number of all star years
        """


scraper = BBRScraper("michael", "jordan")
scraper.getAllPerGameStats()


class tableFormat(object):
    def __init__(self, statType, playerFirstName, playerLastName):
        self.statType = statType
        self.playerFirstName = playerFirstName.lower()
        self.playerLastName = playerLastName.lower()
        URL = 'https://www.basketball-reference.com/players/' + self.playerLastName[0] + '/' + self.playerLastName[
                                                                                               0:5] + self.playerFirstName[
                                                                                                      0:2] + '01.html'
        self.page = requests.get(URL)

    def getTableFormat(self):
        """returns a formatted table based on the the player name and the statType so it can be used in the seasons class"""
        soup = BeautifulSoup(self.page.content, 'html.parser')
        statsTable = soup.find(id='per_game')
        statTableHead = statsTable.find("thead")
        statTableBody = statsTable.find("tbody")
        statsColumnLabel = (statTableHead.text.strip()).split("\n")
        statsRowLabel = (statTableBody.text.strip()).split("\n")
        formattedTable = dict()
        for row in statTableBody.find_all('th'):
            formattedTable[row.text] = []
            for col in statsColumnLabel:
                formattedTable[row.text].append(col)
        return formattedTable


class season(object):
    def __init__(self, playerFirstName, playerLastName, year):
        """
        :param playerFirstName: player's First Name
        :param playerLastName: player's Last Name
        :param year: stats year

        uses the inputed information to get the basketball reference URL
        """
        self.playerFirstName = playerFirstName.lower()
        self.playerLastName = playerLastName.lower()
        self.year = year
        self.URL = 'https://www.basketball-reference.com/players/' + self.playerLastName[0] + '/' + self.playerLastName[
                                                                                                    0:5] + self.playerFirstName[
                                                                                                           0:2] + '01.html'
        self.page = requests.get(self.URL)

    def getStats(self, type):
        """
        :param type: stat type based on basketball reference classification, ie. per_game
        :return: returns the stats for that year in a list format
        """
        soup = BeautifulSoup(self.page.content, 'html.parser')
        year = soup.find(id=type + "." + str(self.year))
        # id = "per_game.1985"

        yearStats = year.find_all('td')
        tableFormat1 = tableFormat(type, self.playerFirstName, self.playerLastName)
        statsTableFormat = tableFormat1.getTableFormat()
        season1 = str(self.year)
        season2 = str(self.year + 1)
        seasonID = season1 + "-" + season2[-2] + season2[-1]
        seasonTableFormat = statsTableFormat[seasonID]

        stats = dict()
        stats[seasonTableFormat[0]] = seasonID
        for i in range(1, len(seasonTableFormat)):
            stats[seasonTableFormat[i]] = yearStats[i - 1].text

        return stats

        # print(statsTableFormat[season1+"-"+season2[-2]+season2[-1]])
        """for tableBody in statTableBody.find_all('th'):
            print(tableBody.text.strip())"""

        """for stat in yearStats:
            print(stat.text.strip())"""


    def testSeason(self):
        testSeason = season("Michael", "Jordan", 1995)
        x = testSeason.getStats("per_game")
        print(x)


