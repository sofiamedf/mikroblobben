import pathlib
import wordcloud
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

path = pathlib.Path.cwd() /  'blog_bu_irl.txt'
print(path)

mask = np.array(Image.open("3.png"))
plt.imshow(mask)

text = path.read_text()
stopwords = ['aderton', 'adertonde', 'adjö', 'aldrig', 'alla', 'allas', 'allt',
    'alltid', 'alltså', 'andra', 'andras', 'annan', 'annat', 'arton', 'artonde',
    'att', 'av', 'bakom', 'bara', 'behöva', 'behövas', 'behövde', 'behövt',
    'beslut', 'beslutat', 'beslutit', 'bland', 'blev', 'bli', 'blir', 'blivit',
    'bort', 'borta', 'bra', 'bäst', 'bättre', 'båda', 'bådas', 'dag', 'dagar',
    'dagarna', 'dagen', 'de', 'del', 'delen', 'dem', 'den', 'deras', 'dess',
    'det', 'detta', 'dig', 'din', 'dina', 'dit', 'ditt', 'dock', 'du', 'där',
    'därför', 'då', 'efter', 'eftersom', 'elfte', 'eller', 'elva', 'en', 'enkel',
    'enkelt', 'enkla', 'enligt', 'er', 'era', 'ert', 'ett', 'ettusen', 'fanns',
    'fem', 'femte', 'femtio', 'femtionde', 'femton', 'femtonde', 'fick', 'fin',
    'finnas', 'finns', 'fjorton', 'fjortonde', 'fjärde', 'fler', 'flera',
    'flesta', 'fram', 'framför', 'från', 'fyra', 'fyrtio', 'fyrtionde', 'få',
    'får', 'fått', 'följande', 'för', 'före', 'förlåt', 'förra', 'första',
    'genast', 'genom', 'gick', 'gjorde', 'gjort', 'god', 'goda', 'godare',
    'godast', 'gott', 'gälla', 'gäller', 'gällt', 'gärna', 'gå', 'går', 'gått',
    'gör', 'göra', 'ha', 'hade', 'haft', 'han', 'hans', 'har', 'heller',
    'hellre', 'helst', 'helt', 'henne', 'hennes', 'hit', 'hon', 'honom',
    'hundra', 'hundraen', 'hundraett', 'hur', 'här', 'hög', 'höger', 'högre',
    'högst', 'i', 'ibland', 'idag', 'igen', 'igår', 'imorgon', 'in', 'inför',
    'inga', 'ingen', 'ingenting', 'inget', 'innan', 'inne', 'inom', 'inte',
    'inuti', 'ja', 'jag', 'jämfört', 'kan', 'kanske', 'knappast', 'kom', 'komma',
    'kommer', 'kommit', 'kr', 'kunde', 'kunna', 'kunnat', 'kvar', 'legat',
    'ligga', 'ligger', 'lika', 'likställd', 'likställda', 'lilla', 'lite',
    'liten', 'litet', 'länge', 'längre', 'längst', 'lätt', 'lättare', 'lättast',
    'långsam', 'långsammare', 'långsammast', 'långsamt', 'långt', 'man', 'med',
    'mellan', 'men', 'mer', 'mera', 'mest', 'mig', 'min', 'mina', 'mindre',
    'minst', 'mitt', 'mittemot', 'mot', 'mycket', 'många', 'måste', 'möjlig',
    'möjligen', 'möjligt', 'möjligtvis', 'ned', 'nederst', 'nedersta', 'nedre',
    'nej', 'ner', 'ni', 'nio', 'nionde', 'nittio', 'nittionde', 'nitton',
    'nittonde', 'nog', 'noll', 'nr', 'nu', 'nummer', 'när', 'nästa', 'någon',
    'någonting', 'något', 'några', 'nödvändig', 'nödvändiga', 'nödvändigt',
    'nödvändigtvis', 'och', 'också', 'ofta', 'oftast', 'olika', 'olikt', 'om',
    'oss', 'på', 'rakt', 'redan', 'rätt', 'sade', 'sagt', 'samma', 'se', 'sedan',
    'senare', 'senast', 'sent', 'sex', 'sextio', 'sextionde', 'sexton',
    'sextonde', 'sig', 'sin', 'sina', 'sist', 'sista', 'siste', 'sitt', 'sju',
    'sjunde', 'sjuttio', 'sjuttionde', 'sjutton', 'sjuttonde', 'sjätte', 'ska',
    'skall', 'skulle', 'slutligen', 'små', 'smått', 'snart', 'som', 'stor',
    'stora', 'stort', 'större', 'störst', 'säga', 'säger', 'sämre', 'sämst',
    'så', 'tack', 'tidig', 'tidigare', 'tidigast', 'tidigt', 'till', 'tills',
    'tillsammans', 'tio', 'tionde', 'tjugo', 'tjugoen', 'tjugoett', 'tjugonde',
    'tjugotre', 'tjugotvå', 'tjungo', 'tolfte', 'tolv', 'tre', 'tredje',
    'trettio', 'trettionde', 'tretton', 'trettonde', 'två', 'tvåhundra',
    'under', 'upp', 'ur', 'ursäkt', 'ut', 'utan', 'utanför', 'ute', 'vad', 'var',
    'vara', 'varför', 'varifrån', 'varit', 'varken', 'varsågod', 'vart', 'vem',
    'vems', 'verkligen', 'vi', 'vid', 'vidare', 'viktig', 'viktigare',
    'viktigast', 'viktigt', 'vilka', 'vilken', 'vilket', 'vill', 'vänster',
    'vänstra', 'värre', 'vår', 'våra', 'vårt', 'än', 'ännu', 'är', 'även',
    'åtminstone', 'åtta', 'åttio', 'åttionde', 'åttonde', 'över', 'övermorgon',
    'överst', 'övre']

wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA").generate(text)

image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[8,8])
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

plt.savefig("blog_irl_cloud.png", dpi = 600, facecolor = 'w', format = 'png')
plt.show()
