players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer",
}

second_base = players['2b']
designated_hitter = players['DH']

print(designated_hitter)


teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
print(teams['angels'])
print(teams['yankees'])

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Betts']

print(teams)

# see below second argument of get is a fallback or default value that will get returned if there is no key matching the first argument

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')

print(featured_team)

# see below the dictionary view object for values() keys() and items() how to turn them into a list make a copy and keep them thread safe or keep them from changing dynamically so to speak 

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

player_names = list(players.copy().values())

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1][1][0])


teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)