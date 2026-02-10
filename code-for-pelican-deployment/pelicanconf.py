AUTHOR = 'rechelon'
SITENAME = 'ZineLibrary'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'En'

THEME = 'themes/edtheme'

SITELOGO = 'images/zinelibrary.jpg'

PLUGINS = [
    'tag_cloud',
]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PUBLISHERS = (
    ("AK Press", "https://akpress.org/"),
    ("PM Press", "https://pmpress.org/"),
    ("Black Rose Books", "https://blackrosebooks.com"),
    ("Black Mosquito", "https://black-mosquito.org/en/"),
    ("Freedom Press", "https://freedompress.org.uk/"),
    ("C4SS", "https://store.c4ss.org"),
    ("Crimethinc", "https://crimethinc.com"),
    ("Dog Section Press", "https://www.dogsection.org/"),
    ("Active Distribution", "https://activedistribution.org/"),
    ("Detritus", "https://detritusbooks.com/"),
    ("Eberhardt", "https://eberhardtpress.bigcartel.com/"),
    ("See Sharp", "https://seesharppress.com/books1.html"),
)

DISTROS = (
    ("Scrappy Capy", "https://en.scrappycapydistro.info/zines"),
    ("No Trace Project", "https://www.notrace.how/"),
    ("Sprout", "https://www.sproutdistro.com/"),
    ("1312 Press", "https://1312press.noblogs.org/"),
    ("A Zine Library", "https://azinelibrary.org/"),
    ("Sherwood Forest Zine Library", "https://www.sherwoodforestzinelibrary.org/virtual-zine-library-recently-added/anarchism"),
    ("South Chicago ABC", "https://www.southchicagoabc.org/zine-library/"),
    ("Filler", "https://fillerpgh.wordpress.com/archive/"),
    ("Haters Cafe", "https://haters.noblogs.org/zines/"),
    ("Prole.info", "https://www.prole.info/"),
    ("Power To The People", "https://msha.ke/powertothepeople/"),
    ("C4SS", "https://zinelibrary.c4ss.org"),
    ("LittleMouse.fun", "https://www.littlemouse.fun/zines.html"),
    ("Invisible Molotov", "https://invisiblemolotov.wordpress.com/"),
    ("It's Going Down Library", "https://itsgoingdown.org/library/"),
    ("Final Straw Radio", "https://thefinalstrawradio.noblogs.org/zines/"),
    ("Tolerated Individuality", "https://toleratedindividuality.wordpress.com/zine-library/"),
    ("Crimethinc", "https://crimethinc.com"),
    ("Ill Will", "https://illwill.com/print"),
    ("Brown Recluse", "https://www.brownreclusezinedistro.com/"),
    ("True Apple Press", "https://trueleappress.wordpress.com/2020/02/18/2020-distro-catalog/"),
    ("Warzone", "https://warzonedistro.noblogs.org/"),
)

DEFAULT_PAGINATION = 1000

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = "random"
TAG_CLOUD_BADGE = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
