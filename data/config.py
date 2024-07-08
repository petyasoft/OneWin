# api id, hash
API_ID = 1111
API_HASH = 'api_hash'

USE_TG_BOT = False # True if you want use tg, else False
BOT_TOKEN = '283993:kdmioieiweikiokeocki4okew' # API TOKEN get in @BotFather
CHAT_ID = '22803822' # Your telegram id

# задержка между подключениями к аккаунтам
ACC_DELAY = [5, 15]

# тип прокси
PROXY_TYPE = "socks5" # http/socks5

# папка с сессиями (не менять)
WORKDIR = "sessions/"

# использование прокси
USE_PROXY = True # True/False

# до какого уровня прокачивать
UPGRADE_LEVEL = 5

hello ='''              _                               __  _        
 _ __    ___ | |_  _   _   __ _  ___   ___   / _|| |_  ___ 
| '_ \  / _ \| __|| | | | / _` |/ __| / _ \ | |_ | __|/ __|
| |_) ||  __/| |_ | |_| || (_| |\__ \| (_) ||  _|| |_ \__ \\
| .__/  \___| \__| \__, | \__,_||___/ \___/ |_|   \__||___/
|_|                |___/        

'''

TOOLS = {'Mines', 'Bombucks', 'LuckyJet', 'coinflip', 'BrawlPirates', 'Tower', 'AnubisPlinko', 'RocketQueen', 'LuckyLoot', 'SpeednCash', 'RoyalMines', 'RocketX', 'Double'}
REQUIRED = {'coinflip': None, 'Mines': None, 'Bombucks': None, 'Tower': None,'Double': 'coinflip10', 'RoyalMines': 'Mines10', 'LuckyLoot': 'Bombucks10', 'BrawlPirates': 'Tower10', 'AnubisPlinko': 'Double5', 'RocketX': 'RoyalMines5', 'SpeednCash': 'AnubisPlinko5', 'RocketQueen': 'SpeednCash11', 'LuckyJet': 'SpeednCash5'}
PRICES = {'coinflip1': 150, 'coinflip2': 188, 'coinflip3': 234, 'coinflip4': 293, 'coinflip5': 366, 'coinflip6': 458, 'coinflip7': 572, 'coinflip8': 715, 'coinflip9': 894, 'coinflip10': 1118, 'coinflip11': 1397, 'coinflip12': 1746, 'coinflip13': 2183, 'coinflip14': 2728, 'coinflip15': 3411, 'coinflip16': 4263, 'coinflip17': 5329, 'coinflip18': 6661, 'coinflip19': 8327, 'coinflip20': 10408, 'Mines1': 340, 'Mines2': 425, 'Mines3': 531, 'Mines4': 664, 'Mines5': 830, 'Mines6': 1038, 'Mines7': 1297, 'Mines8': 1621, 'Mines9': 2027, 'Mines10': 2533, 'Mines11': 3166, 'Mines12': 3958, 'Mines13': 4948, 'Mines14': 6185, 'Mines15': 7731, 'Mines16': 9663, 'Mines17': 12079, 'Mines18': 15100, 'Mines19': 18874, 'Mines20': 23592, 'Bombucks1': 444, 'Bombucks2': 577, 'Bombucks3': 750, 'Bombucks4': 975, 'Bombucks5': 1268, 'Bombucks6': 1649, 'Bombucks7': 2143, 'Bombucks8': 2786, 'Bombucks9': 3622, 'Bombucks10': 4708, 'Bombucks11': 6121, 'Bombucks12': 7957, 'Bombucks13': 10344, 'Bombucks14': 13448, 'Bombucks15': 17482, 'Bombucks16': 22727, 'Bombucks17': 29544, 'Bombucks18': 38408, 'Bombucks19': 49930, 'Bombucks20': 64909, 'Tower1': 500, 'Tower2': 615, 'Tower3': 757, 'Tower4': 930, 'Tower5': 1144, 'Tower6': 1408, 'Tower7': 1731, 'Tower8': 2130, 'Tower9': 2619, 'Tower10': 3222, 'Tower11': 3963, 'Tower12': 4874, 'Tower13': 5996, 'Tower14': 7375, 'Tower15': 9071, "poshalko" : 228,'Tower16': 11157, 'Tower17': 13723, 'Tower18': 16879, 'Tower19': 20762, 'Tower20': 25537, 'Double1': 1200, 'Double2': 1440, 'Double3': 1728, 'Double4': 2074, 'Double5': 2488, 'Double6': 2986, 'Double7': 3583, 'Double8': 4300, 'Double9': 5160, 'Double10': 6192, 'Double11': 7430, 'Double12': 8916, 'Double13': 10699, 'Double14': 12839, 'Double15': 15407, 'Double16': 18488, 'Double17': 22186, 'Double18': 26623, 'Double19': 31948, 'Double20': 38338, 'RoyalMines1': 1500, 'RoyalMines2': 2100, 'RoyalMines3': 2940, 'RoyalMines4': 4116, 'RoyalMines5': 5762, 'RoyalMines6': 8067, 'RoyalMines7': 11294, 'RoyalMines8': 15812, 'RoyalMines9': 22137, 'RoyalMines10': 30992, 'RoyalMines11': 43388, 'RoyalMines12': 60743, 'RoyalMines13': 85041, 'RoyalMines14': 119057, 'RoyalMines15': 166680, 'RoyalMines16': 233352, 'RoyalMines17': 326693, 'RoyalMines18': 457370, 'RoyalMines19': 640318, 'RoyalMines20': 896446, 'LuckyLoot1': 2200, 'LuckyLoot2': 3300, 'LuckyLoot3': 4950, 'LuckyLoot4': 7425, 'LuckyLoot5': 11138, 'LuckyLoot6': 16706, 'LuckyLoot7': 25059, 'LuckyLoot8': 37589, 'LuckyLoot9': 56384, 'LuckyLoot10': 84575, 'LuckyLoot11': 126863, 'LuckyLoot12': 190295, 'LuckyLoot13': 285442, 'LuckyLoot14': 428163, 'LuckyLoot15': 642244, 'LuckyLoot16': 963367, 'LuckyLoot17': 1445050, 'LuckyLoot18': 2167575, 'LuckyLoot19': 3251362, 'LuckyLoot20': 4877043, 'BrawlPirates1': 3500, 'BrawlPirates2': 4200, 'BrawlPirates3': 5040, 'BrawlPirates4': 6048, 'BrawlPirates5': 7258, 'BrawlPirates6': 8709, 'BrawlPirates7': 10451, 'BrawlPirates8': 12541, 'BrawlPirates9': 15049, 'BrawlPirates10': 18059, 'BrawlPirates11': 21671, 'BrawlPirates12': 26005, 'BrawlPirates13': 31206, 'BrawlPirates14': 37448, 'BrawlPirates15': 44937, 'BrawlPirates16': 53925, 'BrawlPirates17': 64709, 'BrawlPirates18': 77651, 'BrawlPirates19': 93182, 'BrawlPirates20': 111818, 'AnubisPlinko1': 4000.0, 'AnubisPlinko2': 5600, 'AnubisPlinko3': 7840, 'AnubisPlinko4': 10976, 'AnubisPlinko5': 15366, 'AnubisPlinko6': 21513, 'AnubisPlinko7': 30118, 'AnubisPlinko8': 42165, 'AnubisPlinko9': 59032, 'AnubisPlinko10': 82644, 'AnubisPlinko11': 115702, 'AnubisPlinko12': 161983, 'AnubisPlinko13': 226776, 'AnubisPlinko14': 317486, 'AnubisPlinko15': 444480, 'AnubisPlinko16': 622272, 'AnubisPlinko17': 871181, 'AnubisPlinko18': 1219654, 'AnubisPlinko19': 1707515, 'AnubisPlinko20': 2390522, 'RocketX1': 5000.0, 'RocketX2': 7750, 'RocketX3': 12012, 'RocketX4': 18619, 'RocketX5': 28860, 'RocketX6': 44733, 'RocketX7': 69336, 'RocketX8': 107471, 'RocketX9': 166580, 'RocketX10': 258199, 'RocketX11': 400209, 'RocketX12': 620324, 'RocketX13': 961502, 'RocketX14': 1490329, 'RocketX15': 2310010, 'RocketX16': 3580515, 'RocketX17': 5549798, 'RocketX18': 8602187, 'RocketX19': 13333390, 'RocketX20': 20666754, 'SpeednCash1': 20000.0, 'SpeednCash2': 30400, 'SpeednCash3': 46208, 'SpeednCash4': 70236, 'SpeednCash5': 106759, 'SpeednCash6': 162274, 'SpeednCash7': 246656, 'SpeednCash8': 374917, 'SpeednCash9': 569874, 'SpeednCash10': 866208, 'SpeednCash11': 1316636, 'SpeednCash12': 2001287, 'SpeednCash13': 3041957, 'SpeednCash14': 4623774, 'SpeednCash15': 7028137, 'SpeednCash16': 10682768, 'SpeednCash17': 16237808, 'SpeednCash18': 24681468, 'SpeednCash19': 37515832, 'SpeednCash20': 57024064, 'RocketQueen1': 100000.0, 'RocketQueen2': 145000.0, 'RocketQueen3': 210250, 'RocketQueen4': 304863, 'RocketQueen5': 442051, 'RocketQueen6': 640973, 'RocketQueen7': 929411, 'RocketQueen8': 1347647, 'RocketQueen9': 1954088, 'RocketQueen10': 2598936, 'RocketQueen11': 3456585, 'RocketQueen12': 4597259, 'RocketQueen13': 6114354, 'RocketQueen14': 8132091, 'RocketQueen15': 10815681, 'RocketQueen16': 14384856, 'RocketQueen17': 19131858, 'RocketQueen18': 25445371, 'RocketQueen19': 33842343, 'RocketQueen20': 45010317, 'LuckyJet1': 750000.0, 'LuckyJet2': 1031250, 'LuckyJet3': 1417969, 'LuckyJet4': 1949707, 'LuckyJet5': 32680847, 'LuckyJet6': 3686165, 'LuckyJet7': 5068477, 'LuckyJet8': 6969155, 'LuckyJet9': 9582589, 'LuckyJet10': 13176059, 'LuckyJet11': 18117082, 'LuckyJet12': 24910987, 'LuckyJet13': 34252608, 'LuckyJet14': 47097336, 'LuckyJet15': 64758837, 'LuckyJet16': 89043400, 'LuckyJet17': 122434675, 'LuckyJet18': 168347679, 'LuckyJet19': 231478058, 'LuckyJet20': 318282330}
