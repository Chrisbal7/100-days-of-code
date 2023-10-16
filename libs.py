logo = r'''
 _
| |
| |__   __ _ _ __   __ _ _ __ __    __ _ _ _
| '_ \ / _ `| '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/                    
'''


cipher = r"""
                                  88
                                  88
     ,adPPYba,   88  8b,dPPYba,   88,dPPYba,  ,adPPYba,,  8b,dPPYba,
    a8"      ""  88  88P'    "8a  88P'   "8a  a8_______8  88P'   "Y8
    8b           88  88       d8  88      88  8PP"        88
    "8a,    ,aa  88  88b,   ,a8"  88      88  "8b,        88
     `"Ybbd8"'   88  88`YbbdP"'   88      88   `"Ybd8b8a  88
                     88
                     88   
"""

caesar = r"""
   ,adPPYba,   ,adPPYYba,  ,adPPYba,,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,
  a8"      ""  ""     `Y8  a8______88  I8[        ""     `Y8  88P'   "Y8
  8b           ,adPPPPP88  8PP"          `Y8ba    ,adPPPPP88  88
  "8a,    ,aa  88,    ,88  "8b,        aa    ]8I  88,    ,88  88
   `"Ybbd8"'   `"8bbdP"Y8   `"Ybd8b8a   `YbbdP    `"8bbdP"Y8  88
"""

figure = r"""
        +----+
        |    |
             |
             |
             |
             |
    ==================
"""

figure = list(figure)
hangs = {39: '0',
         54: '|',
         53: '/',
         55: '\\',
         68: '/',
         70: '\\'}

index_list = list(hangs.keys())


def hang_the_man():
    index = index_list[0]
    figure[index] = hangs[index]
    index_list.remove(index)


def display_figure():
    print(''.join(figure))


word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'justice',
    'journey',
    'step',
    'miracle',
    'oracle',
    'share',
    'minute',
    'second',
    'first',
    'audio',
    'video',
    'play',
    'joke',
    'swim',
    'tackle',
    'disappear',
    'forgive',
    'forget',
    'remember',
    'raise'
    'rain',
    'love',
    'code',
    'thanks',
    'yes',
    'no',
    'okay',
    'virtual',
    'assistant',
    'life',
    'easy',
    'difficult',
    'strange',
    'strong',
    'wagon',
    'khaki',
    'orange',
    'mess',
    'clean',
    'storage',
    'dry',
    'cool',
    'hot',
    'warm',
    'temperature',
    'wedding',
    'family',
    'accountability',
    'responsible',
    'rely',
    'trust',
    'trustworthy',
    'confidence',
    'shy',
    'faith',
    'truth',
    'forgiveness',
    'happiness',
    'fulfilment',
    'wealth',
    'health',
    'electrical',
    'fatal',
    'good',
    'service',
    'matter',
    'what',
    'happen',
    'zigzag',
    'out',
    'open',
    'close',
    'remain',
    'all',
    'intelligence',
    'brain',
    'consistency',
    'care',
    'ability',
    'competence',
    'expert',
    'jesus',
    'update',
    'viral',
    'call',
    'wash',
    'support',
    'write',
    'read',
    'think',
    'different',
    'try',
    'education',
    'network',
    'business',
    'build',
    'fruit',
    'spirit',
    'power',
    'glory',
    'ocean',
    'mountain',
    'cow',
    'sheep',
    'goat',
    'horse',
    'lion',
    'leopard',
    'elephant',
    'tiger',
    'wolf',
    'cat',
    'dog',
    'penguin',
    'crocodile',
    'greet',
    'ready',
    'courage',
    'east',
    'north',
    'south',
    'west',
    'earth',
    'world',
]
