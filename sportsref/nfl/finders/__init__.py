# Fill in PlayerSeasonFinder docstring
import PSF

IOD = PSF.getInputsOptionsDefaults()

paramStr = '\n'.join(
    ':param {}: default="{}"'.format(
        name,
        ','.join(dct['value'])
    )
    for name, dct in sorted(IOD.iteritems()))
optsStr = '\n'.join(
    '{}: {}'.format(
        name,
        ','.join('"{}"'.format(opt) for opt in dct['options'])
    )
    if len(dct['options']) <= 10 else
    '{}: {}...{}'.format(
        name,
        ','.join('"{}"'.format(opt) for opt in dct['options'][:10]),
        ','.join('"{}"'.format(opt) for opt in dct['options'][-2:])
    )
    for name, dct in sorted(IOD.iteritems()))


PSF.PlayerSeasonFinder.__doc__ = """
Finds player-seasons that match criteria supplied by keyword arguments.

Can use tm or team for team_id.
Can use yr, year, yrs, or years for year_min, year_max.
Can use [draft_]pos, [draft_]position, [draft_]positions for a shortcut for [draft_]positions.

Options for inputs:
{}

{}
:returns: list of matching player-season tuples
:rtype: [(player ID, season year)]

""".format(paramStr, optsStr)

# clean up namespace
del IOD, paramStr, optsStr


# Fill in GamePlayFinder docstring
import GPF

IOD = GPF.getInputsOptionsDefaults()

paramStr = '\n'.join(
    ':param {}: default="{}"'.format(
        name,
        ','.join(dct['value'])
    )
    for name, dct in sorted(IOD.iteritems())
)

optsStr = '\n'.join(
    '{}: {}'.format(
        name,
        ','.join('"{}"'.format(opt) for opt in dct['options'])
    )
    if len(dct['options']) <= 10 else
    '{}: {}...{}'.format(
        name,
        ','.join('"{}"'.format(opt) for opt in dct['options'][:10]),
        ','.join('"{}"'.format(opt) for opt in dct['options'][-2:])
    )
    for name, dct in sorted(IOD.iteritems())
)

GPF.GamePlayFinder.__doc__ = """
Finds plays that match criteria supplied by keyword arguments.

Can use tm or team instead of team_id.
Can use yr, year, yrs, or years instead of year_min, year_max.
For multi-valued options (like down or rush direction), separate values with commas or use a list.
For options that are yes/no/either or yes/no/any, -1 is either/any, 0 is no, 1 is yes.

Options for the inputs:
{}

{}
:returns: Pandas dataframe of plays
:rtype: pd.DataFrame
""".format(paramStr, optsStr)

# clean up namespace
del IOD, paramStr, optsStr

from PSF import PlayerSeasonFinder
from GPF import GamePlayFinder

PSF_URL = ('http://www.pro-football-reference.com/'
                     'play-index/psl_finder.cgi')

PSF_CONSTANTS_FILENAME = 'PSFConstants.json'

GPF_URL = ('http://www.pro-football-reference.com/'
           'play-index/play_finder.cgi')

GPF_CONSTANTS_FILENAME = 'GPFConstants.json'

# modules/variables to expose
__all__ = [
    'PlayerSeasonFinder',
    'GamePlayFinder',
    'PSF_URL',
    'PSF_CONSTANTS_FILENAME',
    'GPF_URL',
    'GPF_CONSTANTS_FILENAME',
]
