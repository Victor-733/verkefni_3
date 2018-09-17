from sys import argv
from bottle import *

@route("/")
def index():
    return """
    <h2>Verkefni 3</h2>
    <p><a href="/a">Liður A</a></p>
    <p><a href="/b">Liður B</a></p>
    """

# a liður -----------------------

@route("/a")
def index():
    return template("temp-A.tpl")

@route("/sida/<kt>")
def page(kt):
    return template("temp-kt.tpl", kt=kt)

# b liður -----------------------

@route("/b")
def index():
    return template("temp-B.tpl", frettir=frettir)

@route("/static/<skra>")
def static(skra):
    return static_file(skra, root="./static")

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.jpg", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpg", "dsg@frettir.is"]]


@route("/frett/<id:int>")
def index(id):
    return template("frett.tpl", frett=frettir[id], nr=id)

run(host="0.0.0.0", port=argv[1], debug=True, reloader=True)

# villuboð ----------------------

@error(404)
def villa(error):
    return "<h2 'style=color:blue'>Error 404: See, I pulled a lil sneaky on ya</h2>"
