'''
Jesus Macias

This program looks at 10000 tweets and determines the percentage of tweets
that begin with RT (retweet).
'''
import tweepy
import keys

# accessing the twitter account
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# initializing api
api = tweepy.API(auth, wait_on_rate_limit=True)

# search term and date
search_words = "#covid"
date_since = "2021-11-1"

tweets = []
retweetList = []
notRT_list = []
for tweet in tweepy.Cursor(api.search, q=search_words, tweet_mode='extended').items(1000):
    # tweeter name
    tweettext = str(tweet.full_text.lower())
    tweets.append(tweettext)
    tweetID = tweet.id
    # print tweet text
    print("Tweet:"+str(tweettext))
    print("Tweet ID:"+str(tweetID))
    if tweettext.startswith("rt") == True:
        retweetList.append(tweettext)
        print("This is a Retweet\n")
    else:
        notRT_list.append(tweettext)
        print("This is not a Retweet\n")

numbRetweets = len(retweetList)
numbNonRT = len(notRT_list)
print("Tweets that are Retweets:",numbRetweets)
print("Tweets that are Not Retweets:",numbNonRT)
print("Percentage of Retweets:", format((numbRetweets/len(tweets) *100), ".2f")+"%")

'''*************************************************************************************************************************************
Sample Output:

Tweet:rt @mojahedineng: over 473,700 people have died of #covid in 547 cities checkered across all of #iran’s 31 provinces, according to reports…
Tweet ID:1458611289891115016
This is a Retweet

Tweet:rt @clayandbuck: is it safe? dr. makary on the vax for kids
"the child may be more likely to die in a car accident driving to the pediatric…
Tweet ID:1458611224451682315
This is a Retweet

Tweet:rt @veteranspartync: then get rid of all covid restrictions. the pandemic is over, #covid is endemic.
#ncpol
Tweet ID:1458611217564581889
This is a Retweet

Tweet:rt @telesurtv: las medidas impuestas por las autoridades chinas 🇨🇳 para contener el #coronav  irus también afectan a la limpieza de las calle…
Tweet ID:1458611165819457546
This is a Retweet

Tweet:📷 would love to be poolside in bali right now 🏖 📸:@sophiacatley . https://t.co/awt0exdejn .  . #bali #weding #geriabali #beach #surfing #ibiza #cliff #balivillas #villainbali #covid #holidays... https://t.co/jrpiziomp8
Tweet ID:1458611163969773568
This is not a Retweet

Tweet:our #fairtrade colleagues at @blossomproducts blog about traveling to peru during the #covid pandemic. that is challenging. https://t.co/8xfizhuwyj
Tweet ID:1458611153349742593
This is not a Retweet

Tweet:rt @teacircleoxford: the burmese version of pan nu zaw’s article from 2020 is now available! in this essay, pan nu zaw discusses the elusiv…
Tweet ID:1458611118885195783
This is a Retweet

Tweet:rt @beingrichard: weird logic.

"number of deaths following covid jab has risen to 94 ... while numbers sound alarming, an #nz vaccinologis…
Tweet ID:1458611087943811072
This is a Retweet

Tweet:rt @mojahedineng: over 473,700 people have died of #covid in 547 cities checkered across all of #iran’s 31 provinces, according to reports…
Tweet ID:1458610995841179653
This is a Retweet

Tweet:rt @amateelsalvador: durante el periodo de mayor crisis por la pandemia de #covid-19, las personas #lgbtiq nos vimos mayormente afectadxs e…
Tweet ID:1458610994318659590
This is a Retweet

Tweet:rt @sillymickel: “*dave:*  “okay, so stay tuned &amp; uh we’ll letcha know as more developments in the big reveal...um, uh...(smack)...”

““peo…
Tweet ID:1458610993794207744
This is a Retweet

Tweet:@jrockair @glennbeck glenn the governments response to #covid was injecting bleach
Tweet ID:1458610942779006982
This is not a Retweet

Tweet:rt @conflitsfrance: 🇫🇷 flash | selon une étude, les #étudiants sont plus concernés par des t  roubles anxieux et #dépressifs que le reste de…
Tweet ID:1458610913645408260
This is a Retweet

Tweet:the #covid vaccine is still experimental and therefore cannot be forced on the military or any other business or educational establishments.  the big lie is that it has been approved by the #fda.
Tweet ID:1458610896008138752
This is not a Retweet

Tweet:la secretaría de salud federal reportó que en las últimas 24 horas #méxico sumó 264 muertos por #covid-19 y 3 mil 556 contagios por el virus del sars-cov2.

https://t.co/swxyscs1f7
Tweet ID:1458610842895732739
This is not a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458610663853633536
This is a Retweet

Tweet:rt @ucsf: u.s. teens doubled non-school screen time to 7.7 hours a day during the #covid-19 pandemic, @jamapediatrics study led by @ucsf pe…
Tweet ID:1458610640629551104
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458610637253316613
This is a Retweet

Tweet:rt @suselymorfag: inicia hoy iii proceso de rendición de cuenta de los delegados a sus electores. el cual tendrá lugar en el ámbito de la c…
Tweet ID:1458610625685467144
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458610551014187008
This is a Retweet

Tweet:#pandemia del #covid|19 deja subregistro de casos de #vih en #veracruz | #salud #coronavirus #xalapa #formatosiete https://t.co/sbcfnbnmbt
Tweet ID:1458610499583680512
This is not a Retweet

Tweet:rt @beingrichard: #india, #bangladesh, #pakistan,  #indonesia collectively have 2 billion people + low access to 'advanced' (mrna/rna) vacc…
Tweet ID:1458610495947083777
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458610434836209668
This is a Retweet

Tweet:chic zebra stripes pink roses trendy pattern premium face mask  https://t.co/vmp3bd8a6w #covid #facemasks #covid19 #coronavirus #socialdistancing
Tweet ID:1458610431908536323
This is not a Retweet

Tweet:in russia, 83% of covid hospital beds are filled amid surge - abc news

#health #humanityatstake #humanhealth #covid #covid19 #deltavariant #deltaplus #pandemic
 https://t.co/rnugqggmwk
Tweet ID:1458610427479293952
This is not a Retweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458610316154224641
This is a Retweet

Tweet:rt @iaim_ve: #bioseguridadenmaiquetía || estimado usuario el uso de la mascarilla es obligatorio para que le sea permitido el acceso al aer…
Tweet ID:1458610245354369026
This is a Retweet

Tweet:rt @virgintradergal: um another #gop candidate retweeting @enzolytics (collaborating with #intel &amp; #samsung for #ai &amp; production) fully hum…
Tweet ID:1458610131906686978
This is a Retweet

Tweet:@peteraktiv @semanthis leider. wenn schon bei #covid-krise, bei der es noch vergleichbar einfach wäre, sie zu bewältigen, derartig versagt wird,sehe ich schwarz für die jungen. sorry kids, wir haben verkackt. aber als krone der schöpfung feiern. erdgeschichtlich gesehen, werden wir eine fußnote sein.
Tweet ID:1458610102378901510
This is not a Retweet

Tweet:jösses, stämmer verkligen detta?!! "bordell i wien erbjuder 30 minuters gratis sex för dem som tar vaccin".

#covid #corona #vaccin https://t.co/63n7fbemyv
Tweet ID:1458609945356779522
This is not a Retweet

Tweet:"#covid body" https://t.co/vntxwozcuk
Tweet ID:1458609893804429316
This is not a Retweet

Tweet:rt @greenjennyjones: i am intolerant of people who use public transport without a mask. it's selfish and stupid, when 1,160 people have die…
Tweet ID:1458609880965726208
This is a Retweet

Tweet:rt @lalobarose: #blachier est en train de dire qu'on nous aurait menti et que la gestion de la #crisesanitaire a été calamiteuse
en 2020, l…
Tweet ID:1458609876100390914
This is a Retweet

Tweet:rt @myherbfoods: germany issues dire warning about moderna jab https://t.co/jqi43xxdzi #covid-19vaccine #germany #moderna
Tweet ID:1458609874775031809
This is a Retweet

Tweet:rt @m_t_franz: ich werd jetzt grantig mit dieser völlig falschen #covid politik!! https://t.co/cjlue0q7u9
Tweet ID:1458609869032992773
This is a Retweet

Tweet:rt @yomimiyo1: @cooperativa supongo que la autoridad sanitaria hará algo con esa indígena incivilizada. #ministeriodesalud #chile #paris #c…
Tweet ID:1458609789311746059
This is a Retweet

Tweet:whet me is the republican plan to combat #covid? ohhh! 😲 https://t.co/r5xijb5yr0
Tweet ID:1458609743472250880
This is not a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458609683212681216
This is a Retweet

Tweet:emergence of sars-cov-2 immune escape variants in an immunocompromised patient https://t.co/p3g61idh04 #sars #sarscov2 #coronavirus #covid @naturecomms @unifreiburg @unibern https://t.co/oxoajtq9fl
Tweet ID:1458609671984582659
This is not a Retweet

Tweet:one reason for neverending #covid:

condition us to treat fellow human beings as biohazards until (but never) proven innocent

get ready for #climate #lockdowns, restrictions, bs, etc.
Tweet ID:1458609599825661958
This is not a Retweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458609588224372741
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458609556444131334
This is a Retweet

Tweet:rt @realamvoice: dr. peter mccullough joins @jfradioshow to explain the risks associated with the #covid vaccines.

watch the full conversa…
Tweet ID:1458609497945956354
This is a Retweet

Tweet:rt @matigrje: #covid #fjb #letsgobrandon #joebiden #democrats #osha #cdc #wakeupamerica #vaccine #mandate #walkout https://t.co/diphlup9un
Tweet ID:1458609481248501760
This is a Retweet

Tweet:est ce que le gouvernement va nous expliquer un jour pourquoi la vaccination avec #pfizer contre le #covid est privilégiée par rapport aux autres #laboratoires. impossible de prendre un rdv hors vaccins #pfizer https://t.co/06hno27jyz https://t.co/ind1l5zlvn
Tweet ID:1458609398897647617
This is not a Retweet

Tweet:this is why we have motherfucking vaccine mandates. it’s to save lives, and protect those who can’t be vaccinated. this isn’t a fucking game, and it isn’t fucking politics.

#getvaccinated #covid19 #covid https://t.co/k528f5mmg2 https://t.co/egvbqky0aw
Tweet ID:1458609389581922309
This is not a Retweet

Tweet:rt @thirumahanevera: அவதூறு வழக்குகள் ரத்து

#evks #evkselangovan #thirumahaneveraa #periyar #inc #inctamilnadu #rahulgandhi #soniagandhi #…
Tweet ID:1458609358531559425
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458609334619942912
This is a Retweet

Tweet:rt @mohfw_india: #unite2fightcorona #covidsafefestivities

here's a beautiful madhubani painting depicting the famous #chhathpuja . this fe…
Tweet ID:1458609312276770817
This is a Retweet

Tweet:loosing a patient to covid is still hard. seeing someone die alone in the hospital is still hard. especially since now death due to covid is considered preventable by taking a vaccine that was approved 10 months 27 days ago. #covidvaccine #taketheshot #covid
Tweet ID:1458609312004284425
This is not a Retweet

Tweet:crude #oil and #petroleum prices have increased from 2020 lows, marking their highest levels since 2014. during the #covid-19 pandemic, #crudeoil and petroleum demand declined, inventories increased, and prices fell. #usa #energy
https://t.co/za2e8uv1vk
Tweet ID:1458609263417470978
This is not a Retweet

Tweet:um another #gop candidate retweeting @enzolytics (collaborating with #intel &amp; #samsung for #ai &amp; production) fully human mabs that cure #covid &amp; #hiv
yes! @thedemocrats catch up! @govrondesantis #florida $enzc https://t.co/6iwv0f1vko
Tweet ID:1458609197155819520
This is not a Retweet

Tweet:rt @singhrowdysingh: #laxmmi #bellbottom &amp; now #sooryavanshi  it's hattrick of success for @akshaykumar sir  #covid #pandemic one &amp; only su…
Tweet ID:1458609186770546688
This is a Retweet

Tweet:#economia | com mais 280 óbitos em 24 horas, o #brasil superou a marca de #610milmortes em decorrência de complicações associadas à #covid-19.

#notícia #osudoestegoiano #osg #regiãosudoeste #sudoestegoiano #goiás https://t.co/vktuwmlitz
Tweet ID:1458609180722479104
This is not a Retweet

Tweet:as #covid infections and hospitalizations climb in #michigan lots of patients who’ve deferred care are coming out of the woodwork. one @umichmedicine er doc on the intense pressure in hospital care: https://t.co/sgsjonstli https://t.co/1pmm25qrn6
Tweet ID:1458609169179631618
This is not a Retweet

Tweet:mantap, 200 juta dosis vaksin covid disuntikkan ke masyarakat

#vaksin #vaksinasi #vaksinasinasional #corona #coronavirus #covid19 #covid #rakyatmerdeka #rmid

https://t.co/7vy6nbktwf
Tweet ID:1458609169171464194
This is not a Retweet

Tweet:rt @emeimarkus: #sileri alla #donato sulla pubblicazione scientifica in inglese: "ma ha capito quello che ha letto?"

"certo, se vuole glie…
Tweet ID:1458609159922982913
This is a Retweet

Tweet:#francoparisi  #covid #positivo #covidpositivo
#igualteapoyo #vota7
#parisipresidente #parisiregresa https://t.co/5p92fgwbrd
Tweet ID:1458609143015694340
This is not a Retweet

Tweet:@cooperativa supongo que la autoridad sanitaria hará algo con esa indígena incivilizada. #ministeriodesalud #chile #paris #covid
Tweet ID:1458609123465986050
This is not a Retweet

Tweet:rt @beingrichard: weird logic.

"number of deaths following covid jab has risen to 94 ... while numbers sound alarming, an #nz vaccinologis…
Tweet ID:1458609116260167684
This is a Retweet

Tweet:rt @vaevictis: come funziona il test rt-pcr (il cosiddetto «tampone») e perché è essenziale il numero di cicli cₜ; nelle immagini del tweet…
Tweet ID:1458609113290752005
This is a Retweet

Tweet:rt @proudindian_uva: sir now even maharastra psc followed gpsc, opsc, icai, indian army by provide extra attempt to #covid affected aspiran…
Tweet ID:1458609087898284032
This is a Retweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458608976409600006
This is a Retweet

Tweet:rt @covidnewsbymib: #coronafacts:

📍can thermal scanners detect #covid19 infected people❓❓

↗️no, thermal scanners don't detect #covid infe…
Tweet ID:1458608897342672897
This is a Retweet

Tweet:rt @christi29161044: dr. vladimir zelenko joins dr. gina to discuss the incredible results from early treatment of #covid and the many live…
Tweet ID:1458608889801285633
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458608880141930499
This is a Retweet

Tweet:rt @nitrox82: el "peak" que ya "pasó" esta a plena vista.
osea.. peak en el ojo
xd
#covid
@covid19cl https://t.co/wtyltjypkb
Tweet ID:1458608873254932480
This is a Retweet

Tweet:rt @iaim_ve: #venezueladecidiócuidarse✈️|| desde el #iaim velamos por el cumplimiento de las medidas sanitarias durante su estadía por el p…
Tweet ID:1458608869547167751
This is a Retweet

Tweet:rt @nofilterhayley: #florida #covid #health #summit https://t.co/gzrolwcsfq
Tweet ID:1458608862836187136
This is a Retweet

Tweet:rt @roslemusmartin: en tan solo unos días ya hay más de 1 millón de niños  vacunados contra #covid: !los niños ponen el ejemplo a los adult…
Tweet ID:1458608859958947842
This is a Retweet

Tweet:rt @statsjamie: 🚨🚨 labour politician in wales debating #vaccinepassports.

"people on the lowest incomes are not able to go to the matches…
Tweet ID:1458608856431538181
This is a Retweet

Tweet:rt @ucsfhospitals: healthcare workers "are feeling very nervous as we head into the holidays," @lekshmimd says of a recent uptick on #covid…
Tweet ID:1458608847703134208
This is a Retweet

Tweet:health minister: #france experiencing start of fifth wave of #covid epidemic #worldnews https://t.co/axnibkvue6
Tweet ID:1458608799703388162
This is not a Retweet

Tweet:rt @b52malmet: death by #covid is a brutal way to go, your lungs fill with so much fluid you drown yourself. that so many  republicans choo…
Tweet ID:1458608796884877321
This is a Retweet

Tweet:dr. vladimir zelenko joins dr. gina to discuss the incredible results from early treatment of #covid and the many lives that could have been saved last year.
https://t.co/pd2m876ih1
Tweet ID:1458608684007784449
This is not a Retweet

Tweet:la vacunación masiva contra el virus #sars-cov-2 que, de forma oportuna y ordenada, se ha llevado a cabo en méxico ha pasado de ser una esperanza para disminuir los contagios y sobre todo los casos agudos de #covid-19 a una realidad latente.

https://t.co/surpkhc44p
Tweet ID:1458608665913663488
This is not a Retweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458608665317953543
This is a Retweet

Tweet:#jabicide

#resistuniteorganize

#bible #godfirst #jesussaves #pray #maga #lsu #louisiana #batonrouge lsu #covid19 #covid #coronavirus covid-19 #nola #faithoverfear #maga #gobr #fightforfreedom baton rouge #scalesofjustice #love #laplace new orleans https://t.co/javqo71bcr
Tweet ID:1458608577011228673
This is not a Retweet

Tweet:@foxnews you made have a fatal error about your #covid #news coverage!
Tweet ID:1458608547260940289
This is not a Retweet

Tweet:rt @mojahedineng: over 473,700 people have died of #covid in 547 cities checkered across all of #iran’s 31 provinces, according to reports…
Tweet ID:1458608546354970627
This is a Retweet

Tweet:rt @la_resistensia_: 🟥⚠️esta mascarilla no filtra aerosoles infectivos #covid⚠️🟥
por favor no la use. rechácela. protéjase y proteja a los…
Tweet ID:1458608545218314241
This is a Retweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458608541586051079
This is a Retweet

Tweet:rt @lalobarose: #blachier est en train de dire qu'on nous aurait menti et que la gestion de la #crisesanitaire a été calamiteuse
en 2020, l…
Tweet ID:1458608526994153477
This is a Retweet

Tweet:rt @boghuma: wasn't november when we were told to expect widely available &amp; cheaper rapid diagnostic #covid tests in the us?
i made stops a…
Tweet ID:1458608519427596291
This is a Retweet

Tweet:rt @suselymorfag: inicia hoy iii proceso de rendición de cuenta de los delegados a sus electores. el cual tendrá lugar en el ámbito de la c…
Tweet ID:1458608512901201929
This is a Retweet

Tweet:rt @hibiscuits1: for whose benefit? brilliant @chpithinktank looks at the @nhsengland contract with the private hospital sector in the firs…
Tweet ID:1458608504839839748
This is a Retweet

Tweet:#méxico reporta tres mil 556 nuevos
contagios de #covid-19 en 24 horas

el país acumula 290 mil 374 defunciones, así como tres millones 834 mil 815 casos confirmados

https://t.co/pr3chy6b0u https://t.co/gvl7ji3ebv
Tweet ID:1458608444995510274
This is not a Retweet

Tweet:rt @aloa5: #covid in deutschland, #endgame #tag1

es wird ganz, ganz böse. nicht vielleicht, sondern sicher.  nicht sicher bin ich, wie ich…
Tweet ID:1458608392516292608
This is a Retweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458608378553552900
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458608375458054145
This is a Retweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458608374736728068
This is a Retweet

Tweet:rt @usmortality: the pandemic is moving north!

#covid #covid19 #corona #coronavirus https://t.co/1bs1namrve
Tweet ID:1458608347364667392
This is a Retweet

Tweet:rt @iaim_ve: #laprevensióneslaclave || conoce el uso adecuado de la mascarilla como medida de prevención y contención para aislar el virus…
Tweet ID:1458608329987702789
This is a Retweet

Tweet:rt @sputnikvaccine: one of sputnik v key creators alexander #gintsburg turns 70🎂

dr gintsburg &amp; his gamaleya center team created safe &amp; ef…
Tweet ID:1458608292800999427
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾 
also catch us at times…
Tweet ID:1458608289848217601
This is a Retweet

Tweet:rt @gnb_antidrogas1: #9nov protégete de la #covid-19 🦠y cuídate de esta pandemia, no bajes la s medidas de bioseguridad #pueblodignoysoberan…
Tweet ID:1458608286060720129
This is a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458608265156255749
This is a Retweet

Tweet:@pulseitnews just published an opinion piece of mine about how we can support covid-19 patients in the home when care for mild cases is transferred to gps. i think home monitoring supported by telehealth is key.
https://t.co/rtbswcsqhz

#covid #thenewnormal #gp #rpm #telehealth
Tweet ID:1458608174802472961
This is not a Retweet

Tweet:los casos de covid19 se mantienen sin sobresaltos en la ciudad
#laplata-2 #covid-2 #vacunas
https://t.co/syvmdfzrug
Tweet ID:1458608163238854663
This is not a Retweet

Tweet:rt @pacfan613: germany issues dire warning about moderna jab https://t.co/lk8jypkzgq #covid-19vaccine #germany #moderna
Tweet ID:1458608156616110084
This is a Retweet

Tweet:new covid-19 infections in southeast asia: what the numbers looked like today. #covid #southeastasia #erudite https://t.co/djnelloyda https://t.co/vfzkixiabw
Tweet ID:1458608154971971586
This is not a Retweet

Tweet:rt @telearagua: #infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás…
Tweet ID:1458608015360278529
This is a Retweet

Tweet:https://t.co/s96wlosmqe

@medsurgnurses
#msnw21 #nurses #nurselife #covid #nursing #healthcare #rn #lvn #medical #nursesrock #registerednurse #health #coronavirus #thankyou #thankyounurses #thankyoumedsurgnurses https://t.co/e7k3vd8xub
Tweet ID:1458607993088524290
This is not a Retweet

Tweet:rt @sandralopezleon: 🦠🧠 #covid #neuro
https://t.co/j3rbj3vwh3
síntomas y neuro-patofisiología de covid https://t.co/b4x9lx1yqy
Tweet ID:1458607981382225921
This is a Retweet

Tweet:rt @vaccinologist: 609 days since the #covid #pandemic was officially declared, we are still nowhere near the end because of this and all t…
Tweet ID:1458607969679990785
This is a Retweet

Tweet:rt @davidkoubbi: pourquoi le #president a t’il changé de voix ? est-ce un sosie ? est-il enrhumé ? a t’il le #covid ? est-ce la 5g ? nous a…
Tweet ID:1458607966857351171
This is a Retweet

Tweet:listen | https://t.co/iljspigtzc | from 2020 #fromthearchives #listenagain #peoplefirstradio #14years #communityradio #parenting #covid19 #covid #personalstory #children #child #summer #neighbourhood #friendship #growingup #parent #mother https://t.co/kpacwlpyto
Tweet ID:1458607954756833286
This is not a Retweet

Tweet:rt @johnbasham: analysis: the @cdc apparently manipulated studies in order to prop up the official #covid narrative. two studies published…
Tweet ID:1458607916014092296
This is a Retweet

Tweet:national education day...

education imparted by heart can bring revolution in the society.

#education #learning #school #motivation #students #study #student #covid #science #children #india #knowledge #college #teacher #learn

#royceramics #600x600 #morbi #gvt #pgvt https://t.co/4t4rcrsxfa
Tweet ID:1458607913082052608
This is not a Retweet

Tweet:#infórmate📢| prevenir el #covid-19 es tarea de todos. si sales, toma en cuenta esta serie de recomendaciones y así evitarás el contagio. recuerda que tu salud y la de los tuyos es lo más importante.

#músicosdelapatria https://t.co/p0womxvfn2
Tweet ID:1458607912679395328
This is not a Retweet

Tweet:in part 1 of our latest #gettinginpodcast q&amp;a, we answer questions about submitting test scores in a #testoptional world and reporting disability and #covid relief payments on the #fafsa. check it out! @voiceamvariety https://t.co/jhyeu9zwpy
Tweet ID:1458607910108504067
This is not a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458607900352471043
This is a Retweet

Tweet:rt @iaim_ve: #venezueladecidiócuidarse✈️|| ¡la prevención es la clave! el gobierno bolivariano decidió cuidar al pueblo de venezuela y desd…
Tweet ID:1458607841699377153
This is a Retweet

Tweet:rt @ciudadanodoe: el riesgo de las #vacunas es mayor que el del #covid? #plandemia #covid19 #españa
Tweet ID:1458607803728281605
This is a Retweet

Tweet:rt @yukon_strong: we’re at peak yukon #covid hysteria.

i’d like watchers to google antigenic sin. how do you feel about the risks to your…
Tweet ID:1458607780122836994
This is a Retweet

Tweet:rt @mojahedineng: over 473,700 people have died of #covid in 547 cities checkered across all of #iran’s 31 provinces, according to reports…
Tweet ID:1458607728876732416
This is a Retweet

Tweet:rt @suselymorfag: inicia hoy iii proceso de rendición de cuenta de los delegados a sus electores. el cual tendrá lugar en el ámbito de la c…
Tweet ID:1458607688091328519
This is a Retweet

Tweet:rt @iaim_ve: #bioseguridadenmaiquetía || estimado pasajero antes de ingresar a los terminales aéreos del principal aeropuerto de venezuela,…
Tweet ID:1458607648287477764
This is a Retweet

Tweet:#covid-19 | 2.461 nuevos casos este miércoles en colombia https://t.co/uacqnonvia
Tweet ID:1458607574614425600
This is not a Retweet

Tweet:rt @georgemonks11: it’s a real head scratcher on how oklahoma has the only dedicated pandemic center in the us whose core mission is to do…
Tweet ID:1458607424605204483
This is a Retweet

Tweet:rt @iaim_ve: #iaim_esbioseguridad || los pasajeros que transitan por el terminal nacional del aeropuerto “simón bolívar” de maiquetía, al i…
Tweet ID:1458607394594951169
This is a Retweet

Tweet:#covid has isolated mentally ill folks even worse now.  this is very concerning, we must not let them be isolated.  find means for virtual group meetings via @zoom, other such tech.  that online chat rooms are more essential than ever to connect!  @disabilitychat @actordougjones
Tweet ID:1458607379117916161
This is not a Retweet

Tweet:rt @wladimirfco: ahora resulta que parisi tiene covid? 😂😂
lo que faltaba...que weón mas chanta.
sin duda alguna parisi pasará a la histori…
Tweet ID:1458607253364170758
This is a Retweet

Tweet:rt @healthyamerica1: tfah applauds the report of the biden administration’s health equity task force released today. the investments recomm…
Tweet ID:1458607195424239619
This is a Retweet

Tweet:rt @ecoactu_ma: [assurances]
🔔 rendez vous sur https://t.co/l6lhsucbwq pour plus de précisions.
#ecoactu #vaccins #covid19 #maroc #news #…
Tweet ID:1458607194371510273
This is a Retweet

Tweet:rt @wladimirfco: ahora resulta que parisi tiene covid? 😂😂
lo que faltaba...que weón mas chanta.
sin duda alguna parisi pasará a la histori…
Tweet ID:1458607190546083842
This is a Retweet

Tweet:rt @iaim_ve: #laprevensióneslaclave || conoce el uso adecuado de la mascarilla como medida de prevención y contención para aislar el virus…
Tweet ID:1458607190298742789
This is a Retweet

Tweet:#blachier est en train de dire qu'on nous aurait menti et que la gestion de la #crisesanitaire a été calamiteuse
en 2020, les patients #covid représentaient 5% dans les services de réanimation et 2% de l'ensemble des hospitalisations coût 200 milliards, deux #confinements https://t.co/usxzdlctt8
Tweet ID:1458607147617554436
This is not a Retweet

Tweet:rt @nitrox82: el "peak" que ya "pasó" esta a plena vista.
osea.. peak en el ojo
xd
#covid
@covid19cl https://t.co/wtyltjypkb
Tweet ID:1458607110359433218
This is a Retweet

Tweet:shout out to the gal with the sinus infection that came into my work today saying not to worry it wasn't #covid ...like damn, it doesn't matter what it is, if you're sick you should be at home not spreading that shit. people who don't think about others are the worst...
Tweet ID:1458606986350710785
This is not a Retweet

Tweet:#pfizer ceo bourla: people who spread #misinformation on #covid #vaccines are ‘criminals’ https://t.co/vmvyzyivfs via @breitbartnews
Tweet ID:1458606949784764419
This is not a Retweet

Tweet:shout out to @askuhc @uhc for denying covid-19 testing although it explicitly states in the plan that it is covered! #covid #fraud #united #uhc
Tweet ID:1458606945020043268
This is not a Retweet

Tweet:rt @wladimirfco: ahora resulta que parisi tiene covid? 😂😂
lo que faltaba...que weón mas chanta.
sin duda alguna parisi pasará a la histori…
Tweet ID:1458606937155596290
This is a Retweet

Tweet:rt @virgintradergal: oh nice! now i got retweeted by the next governor of #ny !
ny’ers - this is huge
cure for #covid and eventual end to…
Tweet ID:1458606880297832456
This is a Retweet

Tweet:rt @amateelsalvador: durante el periodo de mayor crisis por la pandemia de #covid-19, las personas #lgbtiq nos vimos mayormente afectadxs e…
Tweet ID:1458606846361624580
This is a Retweet

Tweet:rt @avoiceforchoice: .@joebiden's plan to make unvaccinated workers pay for #covid testing could backfire.
#vaccinemandates #withoutus
htt…
Tweet ID:1458606843308089346
This is a Retweet

Tweet:rt @emeimarkus: #sileri alla #donato sulla pubblicazione scientifica in inglese: "ma ha capito quello che ha letto?"

"certo, se vuole glie…
Tweet ID:1458606807862161414
This is a Retweet

Tweet:@shantiiiiiiiigm @patrice_0311 c est déjà fait l effet kiss cool du #covid
Tweet ID:1458606797795827715
This is not a Retweet

Tweet:@ozraeliavi excellent news..

well done to all authorities involved...

#springst #covid #exemption #health #vaccination #australia
Tweet ID:1458606785581907969
This is not a Retweet

Tweet:rt @lerouxarthur10: le #covid est sans doute la plus grande expérience sociale de foutage de gueule des populations, à l'échelle d'une plan…
Tweet ID:1458606762534133764
This is a Retweet

Tweet:#kenya #gdp rebounds strongly in q2, helped by relaxed #covid curbs | ⁦⁦@reuters⁩ #newskenya #economy #recovery  https://t.co/zqucrwrefs
Tweet ID:1458606759103377418
This is not a Retweet

Tweet:el "peak" que ya "pasó" esta a plena vista.
osea.. peak en el ojo
xd
#covid
@covid19cl https://t.co/wtyltjypkb
Tweet ID:1458606742636568578
This is not a Retweet

Tweet:blue sea glitter mermaid fish scales pattern premium face mask  https://t.co/e9fotp9q7q #mermaids #fantasy #glitter #glam #covid #facemasks #covid19 #coronavirus #socialdistancing        
Tweet ID:1458606657294974976
This is not a Retweet

Tweet:"educators have to be open to change. understanding with...#covid, the strains that have been placed on the education system+students' learning."

new @starkvillesd school calendar has more breaks for students/teachers, more options for different learning needs: https://t.co/tdr7oloivy
Tweet ID:1458606633198755842
This is not a Retweet

Tweet:rt @dazed420gaming: specialist #pzgd #daznout #daz3d #dazedgaming #ps4share #ps5share #nba #nishadahiya #inflation #covid19 #covidvaccine #…
Tweet ID:1458606578509103104
This is a Retweet

Tweet:rt @mediasettgcom24: covid, rinviato il congresso del ppe a rotterdam  #covid https://t.co/fxqvt9txzx https://t.co/gbdpdtlo6a
Tweet ID:1458606435688923139
This is a Retweet

Tweet:"a family says after their mother beat #covid-19, they found maggots in her nose and mouth while she remained hospitalized. they are holding staff at santa ana’s south coast global medical center responsible for the death of their mother."

#california
https://t.co/kq2yozuyun
Tweet ID:1458606399504666634
This is not a Retweet

Tweet:rt @cadenasurtv: miércoles 10 de noviembre: se registraron 15 nuevos casos de #coronavirus #covid-19 en #morelos, y 3 fallecimientos más. y…
Tweet ID:1458606393666281474
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458606376964567042
This is a Retweet

Tweet:ahora resulta que parisi tiene covid? 😂😂
lo que faltaba...que weón mas chanta.
sin duda alguna parisi pasará a la historia como el candidato presidencial más nefasto.
#parisi #covid #boricpresidente #vota1 https://t.co/dxciyzrdsc
Tweet ID:1458606340943728644
This is not a Retweet

Tweet:covid screening questions (black text). available on over 80 products! #stickers #tshirts #pillows #mugs #masks https://t.co/descykp3ua
#covid-19 #giftideas
Tweet ID:1458606330302894084
This is not a Retweet

Tweet:rt @docbrandenburg: „müssen #jugendliche vor der politik schützen, nicht vor #covid“. korrekt! danke, herr kollege 🙏 👇 https://t.co/b01nit2…
Tweet ID:1458606264775233543
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458606256571265030
This is a Retweet

Tweet:finally a movie i really want to see, so i check the #covid protocols at my local @amctheatres 
sorry. no. #vaccines not required. #masks “recommended” only when not eating 😉 #really do you want people to come back to your theaters? 🤷🏻‍♀️
Tweet ID:1458606175835074563
This is not a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458606168213962755
This is a Retweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458606112387837959
This is a Retweet

Tweet:tren covid-19 di jawa kembali naik, ini instruksi prof wiku adisasmito kepada gubernur https://t.co/zzgtwegpiu #covid-19 #profwikuadisasmito #trencovid-19
Tweet ID:1458606105446076416
This is not a Retweet

Tweet:rt @uhn: it's #mrtweek! whether easing a claustrophobic patient's fear of the #mri process or performing portable x-rays on #covid patients…
Tweet ID:1458606071715704835
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾 
also catch us at times…
Tweet ID:1458606069824081923
This is a Retweet

Tweet:rt @publichealthaz: new ⁦@publichealthaz⁩ data brief:

arizona is the only state in the u.s. where #covid has been the leading cause of de…
Tweet ID:1458606049707974661
This is a Retweet

Tweet:rt @iaim_ve: #laprevensióneslaclave || conoce el uso adecuado de la mascarilla como medida de prevención y contención para aislar el virus…
Tweet ID:1458606025653854211
This is a Retweet

Tweet:miércoles 10 de noviembre: se registraron 15 nuevos casos de #coronavirus #covid-19 en #morelos, y 3 fallecimientos más. ya son 50 mil 096 casos acumulados y 4,821 decesos en total       

https://t.co/sbwt1sykwk https://t.co/qiigujssm6
Tweet ID:1458606013121134593
This is not a Retweet

Tweet:rt @sputnikvaccine: one of sputnik v key creators alexander #gintsburg turns 70🎂

dr gintsburg &amp; his gamaleya center team created safe &amp; ef…
Tweet ID:1458606012668207112
This is a Retweet

Tweet:#beasiswa #mahasiswaindonesia #dirumahaja #s #mahasiswi #skripsi #pendidikan #mahasiswabaru #viral #sekolah #snmptn #infokampus #kamp #m #niversitesi #jakarta #utbk #covid #masukptn #anakkuliah
https://t.co/wceokihvok https://t.co/zhzgcmhnok
Tweet ID:1458606010176708609
This is not a Retweet

Tweet:rt @iaim_ve: #venezueladecidiócuidarse✈️|| desde el #iaim velamos por el cumplimiento de las medidas sanitarias durante su estadía por el p…
Tweet ID:1458605951402057729
This is a Retweet

Tweet:rt @vaevictis: come funziona il test rt-pcr (il cosiddetto «tampone») e perché è essenziale il numero di cicli cₜ; nelle immagini del tweet…
Tweet ID:1458605900713893894
This is a Retweet

Tweet:rt @clayandbuck: is it safe? dr. makary on the vax for kids
"the child may be more likely to die in a car accident driving to the pediatric…
Tweet ID:1458605883332730880
This is a Retweet

Tweet:#there #isa #covid #case #in #your #house. #whatdoyou #do? - #abcnews via @abc - https://t.co/syknh7atvk
Tweet ID:1458605880929251330
This is not a Retweet

Tweet:rt @iaim_ve: #bioseguridadenmaiquetía || estimado usuario el uso de la mascarilla es obligatorio para que le sea permitido el acceso al aer…
Tweet ID:1458605846590590982
This is a Retweet

Tweet:rt @simonbankshb: the false narrative perpetrated by @scottmorrisonmp on #covid-19 success is obvious:
* he opposed the national cabinet le…
Tweet ID:1458605832342425602
This is a Retweet

Tweet:rt @vaevictis: come funziona il test rt-pcr (il cosiddetto «tampone») e perché è essenziale il numero di cicli cₜ; nelle immagini di questo…
Tweet ID:1458605826852233219
This is a Retweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458605772527517701
This is a Retweet

Tweet:rt @webstergtarpley: https://t.co/yfex952u92
#beijing's suppression of #covid origins through this latest crime against humanity should rem…
Tweet ID:1458605767775248389
This is a Retweet

Tweet:rt @retireddent: when are you dumbasses going to learn how to wear your masks properly?
i mean it’s almost been two years!

wear it tightl…
Tweet ID:1458605752923402244
This is a Retweet

Tweet:rt @kahisse68: mais quel foutage de gueule...cela dépasse l'entendement.doit on supposer des lors que soit les chiffres des décès #covid so…
Tweet ID:1458605683977465857
This is a Retweet

Tweet:rt @lcp: "le fait que la #covid cible plus les gens ayant des comorbidités, veut dire que quand il y aura une immunité suffisante dans la p…
Tweet ID:1458605610258292742
This is a Retweet

Tweet:rt @lerouxarthur10: le #covid est sans doute la plus grande expérience sociale de foutage de gueule des populations, à l'échelle d'une plan…
Tweet ID:1458605534538575874
This is a Retweet

Tweet:continúa constante recuperación de zacatecanos que enfrentaron al #covid-19 @gobiernozac

https://t.co/q8dxgyzwgb
Tweet ID:1458605435456528384
This is not a Retweet

Tweet:rt @telesurtv: las medidas impuestas por las autoridades chinas 🇨🇳 para contener el #coronav  irus también afectan a la limpieza de las calle…
Tweet ID:1458605423364354057
This is a Retweet

Tweet:remarkable changes during #covid that are specific regionally. #sf's hotels and restaurants really took a hit https://t.co/rgqx0nuw8v
Tweet ID:1458605408965181444
This is not a Retweet

Tweet:top news koran rakyat merdeka

stok vaksin makin banyak
kemenkes siapin jurus kejar target vaksinasi

#kemenkes #vaksin #vaksinasi #vaksinasinasional #corona #coronavirus #covid19 #covid_19 #covid #rakyatmerdeka #rmid

https://t.co/1coa9gki0g
Tweet ID:1458605394213806086
This is not a Retweet

Tweet:rt @yukon_strong: we’re at peak yukon #covid hysteria.

i’d like watchers to google antigenic sin. how do you feel about the risks to your…
Tweet ID:1458605369794703367
This is a Retweet

Tweet:rt @brighttodayth: โควิดวันนี้ (11พ.ย.64)
ติดเชื้อรวม 7,496 ราย จำแนกเป็น
ผู้ป่วยในเรือนจำ 240 ราย
ผู้ป่วยมาจากต่างประเทศ 12 ราย
ผู้ป่วยสะส…
Tweet ID:1458605273069744129
This is a Retweet

Tweet:rt @rosemarybayer: i’m #vaccinated  and i’m boosted. 🎉

i’m doing everything i can to prevent spreading #covid to those who cannot be vacci…
Tweet ID:1458605236625547267
This is a Retweet

Tweet:rt @matigrje: #covid #fjb #letsgobrandon #joebiden #democrats #osha #cdc #wakeupamerica #vaccine #mandate #walkout https://t.co/diphlup9un
Tweet ID:1458605228379361285
This is a Retweet

Tweet:rt @amking0321: #covid treasonous acts🆘👇 https://t.co/dfwwvmkbfw
Tweet ID:1458605211749171201
This is a Retweet

Tweet:rt @amateelsalvador: durante el periodo de mayor crisis por la pandemia de #covid-19, las personas #lgbtiq nos vimos mayormente afectadxs e…
Tweet ID:1458605196393824259
This is a Retweet

Tweet:@medrxivpreprint risk of severe covid-19 is rare among fully vaccinated individuals in england https://t.co/0dfrxcz30k @medrxivpreprint @uniofoxford  @lshtm @bristoluni #coronavirus #efficacy #healthcare #sarscov2 #vaccine #covid #coronavirus
Tweet ID:1458605169550053379
This is not a Retweet

Tweet:rt @mizzimanews: #myanmar orders 2 million to stay home as #covid-19 cases spike | mizzima myanmar news and insight https://t.co/du4jjs44dr…
Tweet ID:1458605168564527105
This is a Retweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458605158292721670
This is a Retweet

Tweet:rt @matigrje: #covid #fjb #letsgobrandon #joebiden #democrats #osha #cdc #wakeupamerica #vaccine #mandate #walkout https://t.co/diphlup9un
Tweet ID:1458605141813309440
This is a Retweet

Tweet:rt @realtalkscsu: if you haven’t already, join jamil and kc as they talk with @scsutopowl in last week's episode about how @scsu is address…
Tweet ID:1458605104597291010
This is a Retweet

Tweet:rt @amking0321: #covid treasonous acts🆘👇 https://t.co/dfwwvmkbfw
Tweet ID:1458605047827341318
This is a Retweet

Tweet:risk of severe covid-19 is rare among fully vaccinated individuals in england https://t.co/0dfrxdgeou @medrxivpreprint @uniofoxford  @lshtm @bristoluni #coronavirus #efficacy #healthcare 
#sarscov2 #vaccine #covid #coronavirus https://t.co/lx5pyxhxqs
Tweet ID:1458605005674622983
This is not a Retweet

Tweet:rt @matty_otc: listen up #america this is the only #governor /candidate #nationwide that is talking about a #cure for #covid. @gibson4nys w…
Tweet ID:1458604981733539841
This is a Retweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458604915513724928
This is a Retweet

Tweet:#negazionista

“#covid, a #trieste il picco più alto di sempre”.

 “trieste non esiste”.

#maurobiani #biani #greenpass
#covid19

@maurobiani @repubblica https://t.co/tpf2ojbhuz
Tweet ID:1458604914888822794
This is not a Retweet

Tweet:rt @lcp: "le fait que la #covid cible plus les gens ayant des comorbidités, veut dire que quand il y aura une immunité suffisante dans la p…
Tweet ID:1458604860761419777
This is a Retweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458604844684652547
This is a Retweet

Tweet:rt @unclebillymoney: .@gibson4nys in it to win it

supporting real #cures

more will follow

big pharm vax don't work as advertised

@enzol…
Tweet ID:1458604835486453762
This is a Retweet

Tweets that are Retweets: 664
Tweets that are Not Retweets: 336
Percentage of Retweets: 66.40%
'''


