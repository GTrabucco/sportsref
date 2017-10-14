# flake8: noqa

SITE_ABBREV = {
    'http://www.pro-football-reference.com': 'pfr',
    'http://www.basketball-reference.com': 'bkref',
    'http://www.sports-reference.com/cfb': 'ncaaf',
    'http://www.sports-reference.com/cbb': 'ncaab',
}

from sportsref import decorators, utils, nfl, nba

__all__ = ['decorators', 'utils', 'nfl', 'nba', 'SITE_ABBREV']
