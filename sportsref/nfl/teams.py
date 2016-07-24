import datetime
import re
import urlparse

import requests
import numpy as np
import pandas as pd
from pyquery import PyQuery as pq

import sportsref

__all__ = [
    'teamNames',
    'teamIDs',
    'listTeams',
    'Team',
]

@sportsref.decorators.memoized
def teamNames():
    doc = pq(sportsref.utils.getHTML(sportsref.nfl.BASE_URL + '/teams/'))
    table = doc('table#teams_active')
    df = sportsref.utils.parseTable(table)
    df = df.loc[~df['hasClass_partial_table']]
    ids = df.team_name.str[:3].values
    teamNames = [tr('th a') for tr in table('tr').items()]
    teamNames = filter(None, teamNames)
    teamNames = [lst[0].text_content() for lst in teamNames]
    d = dict(zip(ids, teamNames))
    return d

@sportsref.decorators.memoized
def teamIDs():
    names = teamNames()
    ids = {v: k for k, v in names.iteritems()}
    return ids

@sportsref.decorators.memoized
def listTeams():
    return teamNames().keys()

@sportsref.decorators.memoized
class Team:

    def __init__(self, teamID):
        self.teamID = teamID

    def __eq__(self, other):
        return (self.teamID == other.teamID)

    def __hash__(self):
        return hash(self.teamID)

    @sportsref.decorators.memoized
    def teamYearURL(self, yr_str):
        return (sportsref.nfl.BASE_URL +
                '/teams/{}/{}.htm'.format(self.teamID, yr_str))

    @sportsref.decorators.memoized
    def getMainDoc(self):
        relURL = '/teams/{}'.format(self.teamID)
        teamURL = sportsref.nfl.BASE_URL + relURL
        mainDoc = pq(sportsref.utils.getHTML(teamURL))
        return mainDoc

    @sportsref.decorators.memoized
    def getYearDoc(self, yr_str):
        return pq(sportsref.utils.getHTML(self.teamYearURL(yr_str)))

    @sportsref.decorators.memoized
    def name(self):
        """Returns the real name of the franchise given the team ID.

        Examples:
        'nwe' -> 'New England Patriots'
        'sea' -> 'Seattle Seahawks'

        :returns: A string corresponding to the team's full name.
        """
        doc = self.getMainDoc()
        headerwords = doc('div#meta h1')[0].text_content().split()
        lastIdx = headerwords.index('Franchise')
        teamwords = headerwords[:lastIdx]
        return ' '.join(teamwords)

    @sportsref.decorators.memoized
    def roster(self, year):
        """Returns the roster table for the given year.

        :year: The year for which we want the roster; defaults to current year.
        :returns: A DataFrame containing roster information for that year.
        """
        raise "not yet implemented"

    @sportsref.decorators.memoized
    def boxscores(self, year):
        """Gets list of BoxScore objects corresponding to the box scores from
        that year.

        :year: The year for which we want the boxscores; defaults to current
        year.
        :returns: np.array of strings representing boxscore IDs.
        """
        doc = self.getYearDoc(year)
        table = doc('table#games')
        df = sportsref.utils.parseTable(table)
        if df.empty:
            return np.array([])
        return df.boxscore_word.dropna().values

    @sportsref.decorators.memoized
    def passing(self, year):
        # TODO: WHY WON'T THIS WORK??
        print 'ERROR: THIS FUNCTION IS BROKEN'
        doc = self.getYearDoc(year)
        table = doc('table#passing')
        df = sportsref.utils.parseTable(table)
        return df

    @sportsref.decorators.memoized
    def rushingAndReceiving(self, year):
        # TODO: WHY WON'T THIS WORK??
        print 'ERROR: THIS FUNCTION IS BROKEN'
        doc = self.getYearDoc(year)
        table = doc('#rushing_and_receiving')
        df = sportsref.utils.parseTable(table)
        return df

    # TODO: add functions for HC, OC, DC, SRS, SOS, PF, PA, W-L, etc.