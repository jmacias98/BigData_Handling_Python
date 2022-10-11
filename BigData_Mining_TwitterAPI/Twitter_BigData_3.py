'''
Jesus Macias

This program looks at 10000 tweets and determines which are extended tweets.
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

# empty lists
extendedList = []
notExtendedList = []
tweets = []
for tweet in tweepy.Cursor(api.search, q=search_words, tweet_mode='extended').items(1000):
    # tweeter name
    tweettext = str(tweet.full_text.lower())
    tweets.append(tweettext)
    tweetID = tweet.id
    # print tweet text
    print("Tweet:"+str(tweettext))
    print("Tweet ID:"+str(tweetID))
    if tweettext.startswith("@") == True:
        extendedList.append(tweettext)
        print("This is an Extended Tweet\n")
    else:
        notExtendedList.append(tweettext)
        print("This is not an Extended Tweet\n")

numbExtended = len(extendedList)
numbNotExtended = len(notExtendedList)
print("Tweets that are Extended:",numbExtended)
print("Tweets that are Not Extended:",numbNotExtended)
print("Percentage of Extended Tweets:", format(numbExtended/len(tweets) *100, ".2f")+"%")

'''
Sample Output:

“#covid, a #trieste il picco più alto di sempre”.

 “trieste non esiste”.

#maurobiani #biani #greenpass
#covid19

@maurobiani @repubblica https://t.co/tpf2ojbhuz
Tweet ID:1458604914888822794
This is not an Extended Tweet

Tweet:rt @lcp: "le fait que la #covid cible plus les gens ayant des comorbidités, veut dire que quand il y aura une immunité suffisante dans la p…
Tweet ID:1458604860761419777
This is not an Extended Tweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458604844684652547
This is not an Extended Tweet

Tweet:rt @unclebillymoney: .@gibson4nys in it to win it

supporting real #cures

more will follow

big pharm vax don't work as advertised

@enzol…
Tweet ID:1458604835486453762
This is not an Extended Tweet

Tweet:@cognitive_19 @thenewsoncnbc @kaylatausche much worse than just the #covid stimulus. never dealt w/ the 2008 financial crisis. qe continued since then. only way to deal with the massive 
debt is to devalue $usd so the debt is pennies on the dollar. it is unbelievable. $rub #russian central bank is awesome. holding no $usd.
Tweet ID:1458604797205139458
This is an Extended Tweet

Tweet:rt @govkathyhochul: #covid update:

-153,396 test results reported
-5,138 positives
-3.35% positive
-1,881 hospitalizations (+3)
-29 new de…
Tweet ID:1458604695912652813
This is not an Extended Tweet

Tweet:rt @publichealthaz: new ⁦@publichealthaz⁩ data brief:

arizona is the only state in the u.s. where #covid has been the leading cause of de…
Tweet ID:1458604693706313729
This is not an Extended Tweet

Tweet:rt @publichealthaz: new ⁦@publichealthaz⁩ data brief:

arizona is the only state in the u.s. where #covid has been the leading cause of de…
Tweet ID:1458604688677376002
This is not an Extended Tweet

Tweet:rt @yodl17: $enzc #monoclonalantibodies #covid #hiv 🔥💪👀
Tweet ID:1458604672676159493
This is not an Extended Tweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458604665189191682
This is not an Extended Tweet

Tweet:csm...al #covid le dio #parisi
Tweet ID:1458604604480884736
This is not an Extended Tweet

Tweet:rt @kahisse68: mais quel foutage de gueule...cela dépasse l'entendement.doit on supposer des lors que soit les chiffres des décès #covid so…
Tweet ID:1458604595245158400
This is not an Extended Tweet

Tweet:โควิดวันนี้ (11พ.ย.64)
ติดเชื้อรวม 7,496 ราย จำแนกเป็น
ผู้ป่วยในเรือนจำ 240 ราย
ผู้ป่วยมาจากต่างประเทศ 12 ราย
ผู้ป่วยสะสม 1,968,106 ราย (ตั้งแต่ 1 เมษายน)
หายป่วยกลับบ้าน 7,452 ราย
หายป่วยสะสม 1,853,210 ราย (ตั้งแต่ 1 เมษายน)
เสียชีวิต 57 ราย

#covid #โควิด19 #โควิด https://t.co/jzoblls9x3
Tweet ID:1458604565192839168
This is not an Extended Tweet

Tweet:#covid #salud #gralguido

🔴reporte gral guido, 37 dias libre de covid

salió un nuevo reporte en el distrito vecino, a cargo de daniel brestolli, secretario de salud y bienestar social.

lee esta nota y más 👇
https://t.co/rygoumjclp https://t.co/zy9vxzex5v
Tweet ID:1458604547144888325
This is not an Extended Tweet

Tweet:#entératecubano / 70% de la población cubana inmunizada vs la #covid y con vacunas propias, rápido descenso del número de contagios en el país y mortalidad casi nula. #notemetasconcuba https://t.co/37sp1kzosn
Tweet ID:1458604522427801611
This is not an Extended Tweet

Tweet:rt @publichealthaz: new ⁦@publichealthaz⁩ data brief:

arizona is the only state in the u.s. where #covid has been the leading cause of de…
Tweet ID:1458604498570465285
This is not an Extended Tweet

Tweet:rt @ciudadanodoe: el riesgo de las #vacunas es mayor que el del #covid? #plandemia #covid19 #españa
Tweet ID:1458604469063602176
This is not an Extended Tweet

Tweet:rt @rayrayny2022: @manof4truth @disclosetv #coronavirus #covid #covid19 #darkwinter dark winter omega exercise evergrande #evergrande https…
Tweet ID:1458604364080328709
This is not an Extended Tweet

Tweet:в россии разрабатывают подавляющее размножение  #covid-19 лекарство https://t.co/hho9d5tuxn
Tweet ID:1458604300079357957
This is not an Extended Tweet

Tweet:rt @lcp: "le fait que la #covid cible plus les gens ayant des comorbidités, veut dire que quand il y aura une immunité suffisante dans la p…
Tweet ID:1458604299655725056
This is not an Extended Tweet

Tweet:rt @jeha2019: tägl. gibt es neue erkenntnisse zur #covid-#impfung; nicht selten sind es negative.
für unter 30jährige gibt es nunmehr nur n…
Tweet ID:1458604294517702657
This is not an Extended Tweet

Tweet:#mosen #antivaxxers missouri is at 567.3 #covid day case doubling. please, get vaccinated. https://t.co/jbvoqun2vu
Tweet ID:1458604293343358986
This is not an Extended Tweet

Tweet:rt @freedomworks: unvaccinated teenagers have a lower #covid risk than fully vaccinated 30-year-olds!

unmask schools asap.

let children r…
Tweet ID:1458604265375686662
This is not an Extended Tweet

Tweet:rt @verhaeghe: c'est moi ou, vous aussi, vous avez eu l'impression que #macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Tweet ID:1458604195154694147
This is not an Extended Tweet

Tweet:hello @rafat flew back from france last night via #lisbon got my #covid test monday in #angers .was asked for it both in #paris and #lisbon, at #ewr not even a mention, even though @cdcgov rules require a negative test to enter us, even from fully vaccinated us citizens like me.
Tweet ID:1458604146874011656
This is not an Extended Tweet

Tweet:rt @diariesofjessie: if the vaccine is as great as #democrats claim dems wouldn’t have to force or bribe people to take the jab. speaks vol…
Tweet ID:1458604117245444098
This is not an Extended Tweet

Tweet:rt @mind_spin: ⛑️eindelijk... staat de #zorg op tegen @hugodejonge en @minpres

dit interview moét viraal, want dit is zó belangrijk. dit i…
Tweet ID:1458604094004862977
This is not an Extended Tweet

Tweet:rt @jeroensmeets76: het is zover. alle bijeenkomsten voor huisartsen fysiek geannuleerd. bijna 15% vd huisartsen covid pos. zorg continuïte…
Tweet ID:1458604036123508739
This is not an Extended Tweet

Tweet:@dajiyuan epoch times
[famous column] infection mortality rate rises under high vaccination rate
the chief clinical officer of ireland, dr. henry, believes that the original #covid virus herd immunity requires 60% of the population # to be vaccinated, but due to the delta variant,        
Tweet ID:1458604001205927942
This is an Extended Tweet

Tweet:🔴 último minuto  🔴

franco parisi da positivo a covid-19

#parisi #francoparisi #covid https://t.co/bkrohp86ra
Tweet ID:1458603967051702278
This is not an Extended Tweet

Tweet:cane positivo al covid nel regno unito, si sospetta contagio dai padroni #cane #positivo #covid #regno #unito #sospetta #contagio #padroni  https://t.co/uwskmklytm
Tweet ID:1458603826433478660
This is not an Extended Tweet

Tweet:is this a bad thing ??? #covid #vaccine #pfizer
Tweet ID:1458603777456492547
This is not an Extended Tweet

Tweet:rt @aleteiaes: no perdía la fe y la esperanza, aunque estaba muriendo de #covid. el testimonio de este enfermero aún nos conmueve https://t…
Tweet ID:1458603749543489541
This is not an Extended Tweet

Tweet:this should be sent to every politician in your state and dc.
demand justice from #covid
and the #vaccinesideeffects 👇 https://t.co/emikobkd2y
Tweet ID:1458603721202577409
This is not an Extended Tweet

Tweet:pfizer/gov: vaccine "misinformation" makes you a threat to public health and a criminal. #covid #vaccine #nwo

https://t.co/ebb7mdhfii
Tweet ID:1458603648590700550
This is not an Extended Tweet

Tweet:@eliowa @philiplederer vaccinated ppl are in our gyms and bars, spreading covid into the community. viral load in sewage is twice the value it was this time last year. vaccine mandates and vaccine passports give a false sense of security. #covid #bospoli #bps #vaccinemandate
Tweet ID:1458603602377908233
This is an Extended Tweet

Tweet:rt @paz4u: we expected/expect so much fm #presidentbiden i think the reason his poll numbers are lower right now is because he has lost con…
Tweet ID:1458603548585963523
This is not an Extended Tweet

Tweet:rt @val_bernasconi: même si la pandémie semble moins préoccupante, 1 cas de #covid dans une prison pourrait encore avoir des conséquences c…
Tweet ID:1458603539706613762
This is not an Extended Tweet

Tweet:pandemic keeps on keeping on. #vancouverisland sees 88 new #covid cases today, though the number of @vanislandhealth active cases is down to 598 today (from 613 yesterday &amp; 615 mon). overall, current #hospitalizations (62) a bit lower than last week. but 3 more deaths today. https://t.co/3ycujdn636
Tweet ID:1458603537848410117
This is not an Extended Tweet

Tweet:rt @quandomccoy: we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times…
Tweet ID:1458603478822137858
This is not an Extended Tweet

Tweet:rt @publichealthaz: new ⁦@publichealthaz⁩ data brief:

arizona is the only state in the u.s. where #covid has been the leading cause of de…
Tweet ID:1458603462170607621
This is not an Extended Tweet

Tweet:rt @theresadenverco: right now @mayorhancock @cityofdenver joining metro mayors to talk regional collaboration during #covid pandemic @uofd…
Tweet ID:1458603459616198661
This is not an Extended Tweet

Tweet:rt @conflitsfrance: 🇫🇷 flash | selon une étude, les #étudiants sont plus concernés par des t  roubles anxieux et #dépressifs que le reste de…
Tweet ID:1458603444978257920
This is not an Extended Tweet

Tweet:rt @retireddent: when are you dumbasses going to learn how to wear your masks properly? 
i mean it’s almost been two years!

wear it tightl…
Tweet ID:1458603393241554948
This is not an Extended Tweet

Tweet:rt @banesaddiction: vax passports:
🚫air travel: don't care, i live in the best country
🚫restaurants: good, don't need that seed oil, wheat…
Tweet ID:1458603384957816834
This is not an Extended Tweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458603384408317952
This is not an Extended Tweet

Tweet:.@joebiden's plan to make unvaccinated workers pay for #covid testing could backfire.
#vaccinemandates #withoutus
https://t.co/bqmwiuboqp via @yahoonews
Tweet ID:1458603380977422339
This is not an Extended Tweet

Tweet:rt @lerouxarthur10: le #covid est sans doute la plus grande expérience sociale de foutage de gueule des populations, à l'échelle d'une plan…
Tweet ID:1458603378578178048
This is not an Extended Tweet

Tweet:a little over 2 weeks until thanksgiving.  get your booster asap so you have maximal protection for the holiday.

#getvaccinatedsavelives #getvaxxed #covid19 #covidiot #covid #corona #coronavirus #vaccinated #pureblood #unvaccinated
Tweet ID:1458603351466147843
This is not an Extended Tweet

Tweet:rt @boghuma: wasn't november when we were told to expect widely available &amp; cheaper rapid diagnostic #covid tests in the us?
i made stops a…
Tweet ID:1458603309837737992
This is not an Extended Tweet

Tweet:rt @medimusicus: so, unsere #covid-its ist bis auf 2 betten voll belegt. 2/3 der patienten sind nicht geimpft. der jüngste von ihnen ist 22…
Tweet ID:1458603302564904962
This is not an Extended Tweet

Tweet:rt @la_resistensia_: 🟥⚠️esta mascarilla no filtra aerosoles infectivos #covid⚠️🟥
por favor no la use. rechácela. protéjase y proteja a los…
Tweet ID:1458603295023321098
This is not an Extended Tweet

Tweet:lancaster county covid numbers (11/10/21):

total deaths: 1,359
deaths reported today: 9
total cases: 73,439
cases reported today: 179
mortality rate: 1.85% (pa= 2.00%, natl= 1.62%)
new case metric: 424.0 #covid
Tweet ID:1458603249745940480
This is not an Extended Tweet

Tweet:rt @nonsonpago1: “#negazione”

“#covid, a #trieste il #picco più alto di sempre”

 “trieste non esiste”

fantastico, geniale mauro, graz…
Tweet ID:1458603138009735170
This is not an Extended Tweet

Tweet:rt @aloa5: #covid in deutschland, #endgame #tag1

es wird ganz, ganz böse. nicht vielleicht, sondern sicher.  nicht sicher bin ich, wie ich…
Tweet ID:1458603108481867778
This is not an Extended Tweet

Tweet:rt @conflitsfrance: 🇫🇷 flash | selon une étude, les #étudiants sont plus concernés par des t  roubles anxieux et #dépressifs que le reste de…
Tweet ID:1458603104312700933
This is not an Extended Tweet

Tweet:rt @chiefsforchange: with tn all corps, @tnedu, led by @schwinnteach, is partnering with districts and investing $200 million in #covid aid…
Tweet ID:1458602998276530177
This is not an Extended Tweet

Tweet:#гинцбург рассказал о работе над подавляющим размножение #covid лекарстве https://t.co/bmxnobowve https://t.co/slhc7y3jya
Tweet ID:1458602959269416965
This is not an Extended Tweet

Tweet:@fr_parisi está pa serie de tv, pero de esas malas y que posponen mil veces. ahora #covid positivo!! anda aaaaa, tengo recuerdos de que era amigo del pelao garay o estoy equivocada?
Tweet ID:1458602883293724679
This is an Extended Tweet

Tweet:【名家专栏】高疫苗接种率下感染死亡率攀升

爱尔兰首席临床官亨利博士认为，原始 #covid 病毒的群体免疫需要60%的人口 #接种疫苗，但由于delta变种，他声称，“估计数字已经高达85%～90%”。而且，他所指的是爱尔兰总人口，这意味着爱尔兰的年幼儿童也必
须接种疫苗。

https://t.co/onkbecubuy
Tweet ID:1458602880106172425
This is not an Extended Tweet

Tweet:rt @yukon_strong: we’re at peak yukon #covid hysteria.

i’d like watchers to google antigenic sin. how do you feel about the risks to your…
Tweet ID:1458602830495846404
This is not an Extended Tweet

Tweet:rt @wonderwoman4usa: the #protest for freedom &amp; personal liberty is universal: it belies country, state, party &amp; vax status. "when governme…
Tweet ID:1458602699663060994
This is not an Extended Tweet

Tweet:rt @laissonslespre1: contrat #pfizer #europe
#covid19 #covid #covid #vaccination #business #passanitaire #3emedose #biontech #conflitsdinté…
Tweet ID:1458602680486617088
This is not an Extended Tweet

Tweet:rt @giovaquez: a berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. i tamponi non saranno più sufficienti #covid
Tweet ID:1458602678427127811
This is not an Extended Tweet

Tweet:rt @silviamarquez24: #rusia
récord de casos de #covid y #putin no compró la cantidad de test q había prometido.
-
los amigos y las mismas c…
Tweet ID:1458602643299909635
This is not an Extended Tweet

Tweet:@seanhannity now do #desantis #covid deaths shawn #deathdesantis #hannity
Tweet ID:1458602641601310725
This is an Extended Tweet

Tweet:rt @fredhutch: “we can confidently say that the virus will be endemic for the foreseeable future.. projecting how severe it will be will be…
Tweet ID:1458602608331931649
This is not an Extended Tweet

Tweet:rt @sadicomic: jacques attuali 1981, consigliere di mitterrand, si stava già discutendo il colpo.
non avete paura del #covid  ma di chi lo…
Tweet ID:1458602582331564039
This is not an Extended Tweet

Tweet:too bad kids have to be fully vaccinated to attend (considering they just allowed kids to get it &amp; it takes 2 weeks to be fully vaccinated 🤔)… thought masks were supposed to protect &amp; save lives #covid #disappointed #novaccinemandates #comicon #choice https://t.co/zlehpagxah
Tweet ID:1458602555689295875
This is not an Extended Tweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458602534902370306
This is not an Extended Tweet

Tweet:rt @billpostmus: fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458602518104006659
This is not an Extended Tweet

Tweet:#china another #covid outbreak? https://t.co/oabdmmslx1
Tweet ID:1458602499284344832
This is not an Extended Tweet

Tweet:@eliowa @philiplederer many are vaccinated. vaccination does not prevent carrier state. viral loads are identical (for all practical purposes) between unvaxxed and vaxxed individuals. vaccines don't prevent transmission #covid #bospoli #bps #vaccinemandate mask and test is the only way.
Tweet ID:1458602466849787908
This is an Extended Tweet

Tweet:https://t.co/axkmms5hww

#getvaccinatedsavelives #getvaxxed #covid19 #covidiot #covid #corona #coronavirus #vaccinated #pureblood #unvaccinated #winning
Tweet ID:1458602463771041795
This is not an Extended Tweet

Tweet:rt @ajplus: u.s. consumer prices surged by 6.2% in the last year — a record increase since 1990.

food banks are struggling to meet demands…
Tweet ID:1458602441490894854
This is not an Extended Tweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458602398130319365
This is not an Extended Tweet

Tweet:rt @paz4u: we expected/expect so much fm #presidentbiden i think the reason his poll numbers are lower right now is because he has lost con…
Tweet ID:1458602363585843201
This is not an Extended Tweet

Tweet:rt @amateelsalvador: durante el periodo de mayor crisis por la pandemia de #covid-19, las personas #lgbtiq nos vimos mayormente afectadxs e…
Tweet ID:1458602314118447105
This is not an Extended Tweet

Tweet:rt @tiago_tasa: poderiam embutir o icms dos combustíveis no preço da cerveja e refrigerantes, acredito que resolveria muita coisa! @reguffe…
Tweet ID:1458602306015014913
This is not an Extended Tweet

Tweet:rt @katherinfrs: #ultimahora #10nov vacúnate contra el covid sin costo, sin hacer cola y sin registro previo. conoce los centros de vacunac…
Tweet ID:1458602275098800131
This is not an Extended Tweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458602232618930184
This is not an Extended Tweet

Tweet:rt @debunkjunction: @meidastouch trump’s minions lie. that’s all they do. here’s a whopper from kayleigh about #covid in late february 2020…
Tweet ID:1458602124284248070
This is not an Extended Tweet

Tweet:rt @unidosxisrael: los funcionarios de #israel eliminan las restricciones de #covid al aire libre...
https://t.co/rrgylxag7a
Tweet ID:1458602064263712771
This is not an Extended Tweet

Tweet:suma morelos 4 mil 821 defunciones por #covid-19 https://t.co/5alx1vbrxf
Tweet ID:1458602034840616964
This is not an Extended Tweet

Tweet:rt @clayandbuck: the government’s kid-covid strategy has been indefensible
"all of these people who have tried to convince you that your ki…
Tweet ID:1458602030264692739
This is not an Extended Tweet

Tweet:rt @adriennefrantz: so proud of my baby girl! she is 5 and got her vaccine yesterday! she was so excited! one step closer to normal! we did…
Tweet ID:1458601890556612616
This is not an Extended Tweet

Tweet:rt @mexnewz: las personas que creen en #teoríasconspirativas sobre #covid19 tienen más probabilidades de contraer el virus: #estudio | #cie…
Tweet ID:1458601789721391107
This is not an Extended Tweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458601773162192896
This is not an Extended Tweet

Tweet:rt @lerouxarthur10: le #covid est sans doute la plus grande expérience sociale de foutage de gueule des populations, à l'échelle d'une plan…
Tweet ID:1458601754220765192
This is not an Extended Tweet

Tweet:rt @iaim_ve: #bioseguridadenmaiquetía || estimado usuario el uso de la mascarilla es obligatorio para que le sea permitido el acceso al aer…
Tweet ID:1458601745135947778
This is not an Extended Tweet

Tweet:mais quel foutage de gueule...cela dépasse l'entendement.doit on supposer des lors que soit les chiffres des décès #covid sont totalement bidonnés,soit qu'il y a eu un véritable génocide dans les ephad?je sais ou penche ma raison...#resistance #noussavons
https://t.co/clltjkbwlq https://t.co/unyvl4cvps
Tweet ID:1458601713976455168
This is not an Extended Tweet

Tweet:uggh - #covid seems endless. "after weeks of declines, u.s. covid cases have stalled at a high level: 'the ers are packed'" https://t.co/nqkacnr7xq
Tweet ID:1458601661568487425
This is not an Extended Tweet

Tweet:mild #covid not linked to long-term cardiac damage: https://t.co/ph7u0gmkej

subscribe to tulane outbreak, a curated wrap-up of the most relevant news focused on emerging infectious diseases, like #covid19: https://t.co/oazq0ww4qe https://t.co/acuzimjwgu
Tweet ID:1458601636067168257
This is not an Extended Tweet

Tweet:#meganoticias #colima  🔴 ✝️
defunciones por #covid en los municipios de colima

la información  📲https://t.co/jeypipjaag
descarga la app ▶ https://t.co/scmudyqwmf

@meganoticiasmx
@kary_solano1
@aledatasoy
@manuel_posos
@dinorahaguirre3
@ross_venancio
@vichug3 https://t.co/va49bhimbq
Tweet ID:1458601619801575427
This is not an Extended Tweet

Tweet:rt @breaking_247: act health has reported nine new cases of #covid-19 - the same as yesterday. there are currently no people in act hospita…
Tweet ID:1458601605490790406
This is not an Extended Tweet

Tweet:rt @virgintradergal: oh nice! now i got retweeted by the next governor of #ny !
ny’ers - this is huge
cure for #covid and eventual end to…
Tweet ID:1458601580559745025
This is not an Extended Tweet

Tweet:act health has reported nine new cases of #covid-19 - the same as yesterday. there are currently no people in act hospitals with covid https://t.co/has2um0w4v https://t.co/wqlkb18w2c    
Tweet ID:1458601569738444802
This is not an Extended Tweet

Tweet:rt @davidkoubbi: pourquoi le #president a t’il changé de voix ? est-ce un sosie ? est-il enrhumé ? a t’il le #covid ? est-ce la 5g ? nous a…
Tweet ID:1458601493985169409
This is not an Extended Tweet

Tweet:sigue latente. veo a mucha con exceso de confianza.( sin cubre bocas, restaurantes con más de 60 % de capacidad ) no bajemos la guardia . 😷 #covid https://t.co/8peb8un8v2
Tweet ID:1458601444324564995
This is not an Extended Tweet

Tweet:rt @conflitsfrance: 🇫🇷 flash | selon une étude, les #étudiants sont plus concernés par des t  roubles anxieux et #dépressifs que le reste de…
Tweet ID:1458601437349490689
This is not an Extended Tweet

Tweet:rt @oko_press: przeczytaj więcej: https://t.co/2j46v16z6m

#koronawirus #pandemia #epidemia #covid-19 #polska #białoruś #okopress https://t…
Tweet ID:1458601425630597122
This is not an Extended Tweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458601373579284480
This is not an Extended Tweet

Tweet:*160,000 #covid deaths,no issue
* #brexit economic and political damage, no issue
*breaking laws, mps code continually, no issue
*ppe fraud and cronyism, no issue.

highlighting second jobs and lobbying - whoa hold on that’s too much for #torys

#conservatives
#torycorruption https://t.co/vd83ocdzdh
Tweet ID:1458601232994643969
This is not an Extended Tweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458601179898916864
This is not an Extended Tweet

Tweet:rt @mexnewz: crece la #cuartaola de #covid en #alemania: #nuevorécord de casos y más de 200 muertes en un día | #salud #internacional #covi…
Tweet ID:1458601128183144451
This is not an Extended Tweet

Tweet:rt @meganoticiasco: #meganoticias #colima  📈  🛑
situación actual de #covid-19 en el estado de colima

la información  📲https://t.co/jeypiq…
Tweet ID:1458601098302865410
This is not an Extended Tweet

Tweet:rt @icwgroup: our hr ondemand partner, mineral, surveyed over 1,200 small and midsize businesses and found staffing shortages, retention, a…
Tweet ID:1458601089025118209
This is not an Extended Tweet

Tweet:rt @melissalmrogers: just a reminder that 0.06% of covid deaths in canada were among those aged 19 and under

#canada #ontario #quebec #co…
Tweet ID:1458601076655988736
This is not an Extended Tweet

Tweet:rt @meganoticiasco: #meganoticias #colima  📊 🔍
casos activos de #covid por municipios de colima

la información  📲https://t.co/jeypipjaag
d…
Tweet ID:1458601049879678976
This is not an Extended Tweet

Tweet:cifras #covid de @salud_ec (10 de noviembre)

▶️ 520.296 casos confirmados desde el 29 de febrero 2020.

▶️ 102.641 casos probables.

▶️ 7.891 fallecidos confirmados por covid y 1.329 probables (total 9.208) en el 2021.

#ecuador
#usacubrebocas https://t.co/5gcpubeqhf
Tweet ID:1458601012261011461
This is not an Extended Tweet

Tweet:rt @m_t_franz: ich werd jetzt grantig mit dieser völlig falschen #covid politik!! https://t.co/cjlue0q7u9
Tweet ID:1458600937526902785
This is not an Extended Tweet

Tweet:rt @rmanifiesto: #vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciar…
Tweet ID:1458600897353859072
This is not an Extended Tweet

Tweet:rt @emeimarkus: francesca #donato a #sileri: "si faccia spiegare dai sui colleghi di harvard che cos'è l'immunità da guarigione e quanto du…
Tweet ID:1458600874524225539
This is not an Extended Tweet

Tweet:rt @mariabartiromo: more people died bc of #fentanyl. serious q- why are we allowing china &amp; mexican cartels to push so many killer drugs i…
Tweet ID:1458600833227046918
This is not an Extended Tweet

Tweet:rt @telesurtv: las medidas impuestas por las autoridades chinas 🇨🇳 para contener el #coronav  irus también afectan a la limpieza de las calle…
Tweet ID:1458600797739134982
This is not an Extended Tweet

Tweet:rt @boghuma: wasn't november when we were told to expect widely available &amp; cheaper rapid diagnostic #covid tests in the us?
i made stops a…
Tweet ID:1458600790352924679
This is not an Extended Tweet

Tweet:rt @teacircleoxford: the burmese version of pan nu zaw’s article from 2020 is now available! in this essay, pan nu zaw discusses the elusiv…
Tweet ID:1458600783252008962
This is not an Extended Tweet

Tweet:rt @teacircleoxford: the burmese version of pan nu zaw’s article from 2020 is now available! in this essay, pan nu zaw discusses the elusiv…
Tweet ID:1458600747852083205
This is not an Extended Tweet

Tweet:nfl fines aaron rodgers $15,000 over covid-19 shot situation https://t.co/mfg8p80xg7 #nfl #covid #vaccinemandates #aaronrodgers #adamlazard https://t.co/oe86ncustp
Tweet ID:1458600745780006913
This is not an Extended Tweet

Tweet:rt @tisliving: @nasolutions @tkdgrlkg @kathyfisher10 actually prior to #covid i as a primary care provider could sign papers after reviewin…
Tweet ID:1458600725026590720
This is not an Extended Tweet

Tweet:rt @sadicomic: jacques attuali 1981, consigliere di mitterrand, si stava già discutendo il colpo.
non avete paura del #covid  ma di chi lo…
Tweet ID:1458600693938499584
This is not an Extended Tweet

Tweet:our hr ondemand partner, mineral, surveyed over 1,200 small and midsize businesses and found staffing shortages, retention, and #covid remain primary stressors. see the full study and learn more about hr ondemand. https://t.co/4avblumdco

#workcompconnect #blog #hr
Tweet ID:1458600641803268100
This is not an Extended Tweet

Tweet:rt @teacircleoxford: တွေ့ရခဲသော လူငယ်တို့၏ရာသီဥတုပြောင်းလဲခြင်းဆိုင်ရာ တက်ကြွလှုပ်ရှား မှု့နှင့် အရွေ့တစ်ခု စတင်ရန်အတွက် လှမ်းသင့်သောခြေလှ…
Tweet ID:1458600621096030210
This is not an Extended Tweet

Tweet:rt @_apeterson_: children 5-11 are now eligible for #covid #vaccination.

but what about younger children?

should pediatricians offer covi…
Tweet ID:1458600610027159554
This is not an Extended Tweet

Tweet:minnesota's #covid stats in
book club invitation convo: https://t.co/xw5czcveuq
Tweet ID:1458600603081392137
This is not an Extended Tweet

Tweet:rt @phlegmfighter: can you eat and drink on #hfnc #highflowo2 #highflow?  we tried it and nobody thought it was much of a problem at all. #…
Tweet ID:1458600585813540864
This is not an Extended Tweet

Tweet:rt @suselymorfag: inicia hoy iii proceso de rendición de cuenta de los delegados a sus electores. el cual tendrá lugar en el ámbito de la c…
Tweet ID:1458600566586753027
This is not an Extended Tweet

Tweet:rt @statsjamie: discussing #vaccinepassports in #wales with @iromg

▪️had 2 vaccines so eligible for pass &amp; just tested +ve for #covid (no…
Tweet ID:1458600538103234563
This is not an Extended Tweet

Tweet:daily brief: #covid hospitalizations are on the rise in areas with low #vaccination rates. more in the daily brief...

https://t.co/vdbkcqndtu https://t.co/9axhc6d0dw
Tweet ID:1458600496772653058
This is not an Extended Tweet

Tweet:rt @platon38900187: #covid la grande frousse est bien istallée. a paris, comme en suisse, le nombre de personnes se balladant dans la rue a…
Tweet ID:1458600480742035456
This is not an Extended Tweet

Tweet:rt @m_t_franz: ich werd jetzt grantig mit dieser völlig falschen #covid politik!! https://t.co/cjlue0q7u9
Tweet ID:1458600476111482886
This is not an Extended Tweet

Tweet:oh nice! now i got retweeted by the next governor of #ny !
ny’ers - this is huge
cure for #covid and eventual end to #covid in sight with @enzolytics
(also #hiv &amp; many more viral illnesses in humans &amp; animals)! $enzc @bowzachary https://t.co/zekdflwul7
Tweet ID:1458600448198328320
This is not an Extended Tweet

Tweet:#covid checa aquí cómo puedes descargar tu certificado vía whatsapp

https://t.co/t5c0ynebhs
Tweet ID:1458600367286067200
This is not an Extended Tweet

Tweet:los funcionarios de #israel eliminan las restricciones de #covid al aire libre...
https://t.co/rrgylxag7a
Tweet ID:1458600367134896133
This is not an Extended Tweet

Tweet:တွေ့ရခဲသော လူငယ်တို့၏ရာသီဥတုပြောင်းလဲခြင်းဆိုင်ရာ တက်ကြွလှုပ်ရှား မှု့နှင့် အရွေ့တစ်ခု စတင်ရန်အတွက် လှမ်းသင့်သောခြေလှမ်းများအကြောင်းကို ပန်းနုဇော်မှ  ဆွေးနွေးထားပါသည်။

#climatechange #burma #myanmar #covid-19

https://t.co/nwcrkouwtv https://t.co/8cfvgguhb2
Tweet ID:1458600365578883076
This is not an Extended Tweet

Tweet:the burmese version of pan nu zaw’s article from 2020 is now available! in this essay, pan nu zaw discusses the elusiveness of youth climate change activism and proposes steps to start a movement.

#climatechange #burma #myanmar #covid-19

https://t.co/nwcrkom8i5 https://t.co/4lwaektxry
Tweet ID:1458600364626911237
This is not an Extended Tweet

Tweet:many conversations i have with patients focus on determining differences between correlation &amp; causation.

i can state with 100% confidence that every single person who receives a #covid vaccine will die (eventually).

that is very different than saying they cause death. https://t.co/5xk6rjuxhr
Tweet ID:1458600363821469698
This is not an Extended Tweet

Tweet:#hk #covid-19
hong kong raised the covid-19 risk level for new zealand to medium from low with effect from nov 17 as infections surged in the pacific nation, according to a government statement.

full story:
https://t.co/0fdxapnjcj https://t.co/tyuygsrvcc
Tweet ID:1458600363234234370
This is not an Extended Tweet

Tweet:i would say aaron rodgers is now qualified to work for the biden administration. #covid-19 #joebiden
Tweet ID:1458600286025564169
This is not an Extended Tweet

Tweet:we can thank #doctors, #hospital directors, and #covid #bureaucrats everywhere who--much like #lutchmedial--have watered the tree of #tyranny with their aptitude to blindly "#trustthescience", abuse power, and impose their will on others

i hope to water his grave myself, one day https://t.co/4e2xaefkea
Tweet ID:1458600266995953666
This is not an Extended Tweet

Tweet:@thereidout @jeffdsachs is this the #bigpharmatyranny getting rich off #covid or the @dnc stock holders ?
Tweet ID:1458600239703764999
This is an Extended Tweet

Tweet:rt @ellesm: if there was a deadly pandemic, the top 1% would protect themselves by wfh,masks&amp;would bunker down, letting us plebs carry on a…
Tweet ID:1458600217884909570
This is not an Extended Tweet

Tweet:looks like #aaronrodgers got the #rodgersrate from the nfl...$14,650, for putting his team in danger of #covid...hope this doesn’t send him to the poor house...
Tweet ID:1458600130651856899
This is not an Extended Tweet

Tweet:#vacunandonospuebloquevence| ministerio de salud de #nicaragua, a partir del día de mañana jueves 11 de noviembre, iniciaría la jornada de vacunación voluntaria contra la #covid-19 casa 
a casa en todos los municipios del país. ✊🇳🇮💉

#nicaraguatriunfa
#todosjuntosvamosadelante https://t.co/b4nnbxcerq
Tweet ID:1458600119843143690
This is not an Extended Tweet

Tweet:undip meluncurkan armada bus anticovid-19 diklaim pertama di indonesia

#bus #covid #19 #undip https://t.co/62n7l8vlbn
Tweet ID:1458600116831412229
This is not an Extended Tweet

Tweet:rt @billpostmus: fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458600109600653313
This is not an Extended Tweet

Tweet:rt @croninmelissa: ⁦from ⁦⁦@authorsguild⁩ bulletin: “the state of the book mid-pandemic”: panel discussion with ⁦@janefriedman⁩. this is ay…
Tweet ID:1458600108048723969
This is not an Extended Tweet

Tweet:rt @billpostmus: fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458600069490520073
This is not an Extended Tweet

Tweet:rt @la_resistensia_: 🟥⚠️esta mascarilla no filtra aerosoles infectivos #covid⚠️🟥
por favor no la use. rechácela. protéjase y proteja a los…
Tweet ID:1458600024548519942
This is not an Extended Tweet

Tweet:#ivermectin is still not proven for #covid and as the ‘evidence’ that it works for covid are scrutinized, more and more flaws are being uncovered like 👇🏽 https://t.co/j8xpvzrhpd       
Tweet ID:1458600023810322437
This is not an Extended Tweet

Tweet:rt @emeimarkus: francesca #donato a #sileri: "si faccia spiegare dai sui colleghi di harvard che cos'è l'immunità da guarigione e quanto du…
Tweet ID:1458599993103769601
This is not an Extended Tweet

Tweet:rt @finanzas_times: #pfizer | #moderna | "todas las vacunas de #arnm contienen óxido de graféno; nanoparticula lípida pegilada".

el "secre…
Tweet ID:1458599907003187202
This is not an Extended Tweet

Tweet:rt @statsjamie: discussing #vaccinepassports in #wales with @iromg 

▪️had 2 vaccines so eligible for pass &amp; just tested +ve for #covid (no…
Tweet ID:1458599896852967427
This is not an Extended Tweet

Tweet:generosity and 21 days of abundance during covid-19 - via @pensignal  https://t.co/1lxhqiyxrw #generosity #abundance #covid-19
Tweet ID:1458599779706015748
This is not an Extended Tweet

Tweet:rt @docbrandenburg: „müssen #jugendliche vor der politik schützen, nicht vor #covid“. korrekt! danke, herr kollege 🙏 👇 https://t.co/b01nit2…
Tweet ID:1458599778279993348
This is not an Extended Tweet

Tweet:rt @retireddent: when are you dumbasses going to learn how to wear your masks properly?
i mean it’s almost been two years!

wear it tightl…
Tweet ID:1458599678061289474
This is not an Extended Tweet

Tweet:what should i do if my company mandates the vax?? what legal standing do i really have and how to i combat this issue properly? lawyers, anyone with knowledge, please let me know. thank 
you!

#law #covid #covid19 #lawyer #mandates #vaccinemandate #vaxxed #vaccinesideeffects
Tweet ID:1458599661003018242
This is not an Extended Tweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458599647144992774
This is not an Extended Tweet

Tweet:rt @johnbasham: report: @pfizer sponsored @nbcnews caught lying about #covid &amp; kids. political commentator @jimmy_dore calls out @drjohntor…
Tweet ID:1458599631340797957
This is not an Extended Tweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458599615347912707
This is not an Extended Tweet

Tweet:rt @billpostmus: fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458599610465800192
This is not an Extended Tweet

Tweet:@andrewjbates46 @markzandi trump gop #covid response and obstruction gave us inflation. #buildbackbetter gives us relief. end #gopinflation pass #bbb
Tweet ID:1458599591549538305
This is an Extended Tweet

Tweet:covid screening questions (white text). available on over 80 products! #stickers #tshirts #pillows #mugs #masks https://t.co/n6iz0yif2k
#covid-19 #giftideas
Tweet ID:1458599519155855362
This is not an Extended Tweet

Tweet:rt @zlj517: to keep the risk of #covid transmission to a minimum, wukesong stadium in #beijing, the venue for olympic ice hockey, even has…
Tweet ID:1458599512126205953
This is not an Extended Tweet

Tweet:rt @banesaddiction: vax passports:
🚫air travel: don't care, i live in the best country
🚫restaurants: good, don't need that seed oil, wheat…
Tweet ID:1458599445608677379
This is not an Extended Tweet

Tweet:rt @mariobeteta: la secretaría de salud informó que este miércoles se registraron 3 mil 556 nuevos casos de #covid-19 y 264 muertes. suman…
Tweet ID:1458599389535027204
This is not an Extended Tweet

Tweet:rt @napoleontemplar: tenés dudas sobre la vacunación pediátrica. en este hilo de @rquiroga777 tenés muchas respuestas
#vacunate #vacunacio…
Tweet ID:1458599382962606094
This is not an Extended Tweet

Tweet:@bowzachary got retweeted by gubernatorial candidate for #ny !
$enzc
#covid #cure #mabs #ai https://t.co/kkmjwuvpvb
Tweet ID:1458599381578526720
This is an Extended Tweet

Tweet:кардиолог шугушев заявил, что covid-19 может привести к значительному изменению давления #covid-19
Tweet ID:1458599112161517572
This is not an Extended Tweet

Tweet:rt @johnbasham: report: 3 more reports of teen deaths after experimental #covid vaccines, as reported injuries from the shot exceed 850,000…
Tweet ID:1458599025415016454
This is not an Extended Tweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458599002476212227
This is not an Extended Tweet

Tweet:rt @billpostmus: fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458599000177889281
This is not an Extended Tweet

Tweet:mortality in unvaccinated children is lower than that of vaccinated adults! #fact #covid
Tweet ID:1458598982612140033
This is not an Extended Tweet

Tweet:#covid treasonous acts🆘👇 https://t.co/dfwwvmkbfw
Tweet ID:1458598968775122947
This is not an Extended Tweet

Tweet:#covid, allarme rosso in #germania: 40mila contagi in 24 ore. e #berlino vieta i locali pubblici ai non vaccinati.
#novax #greenpass #covid19 #vaccinatevi_e_basta https://t.co/nrw5zlafjc
Tweet ID:1458598959270793218
This is not an Extended Tweet

Tweet:how many more people must die because of joe biden? #covid
Tweet ID:1458598914555269120
This is not an Extended Tweet

Tweet:fully vaccinated vikings player hospitalized with #covid -19: coach

https://t.co/b3cvqvogug
Tweet ID:1458598885576699904
This is not an Extended Tweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458598843470155787
This is not an Extended Tweet

Tweet:la comisión europea ha acordado un contrato para comprar hasta 60 millones de dosis de la vacuna #covid-19 desarrollada por #valneva se, lo que ha supuesto un aumento de las acciones de 
la compañía biotecnológica francesa. https://t.co/8ojf9av55n
Tweet ID:1458598818929381380
This is not an Extended Tweet

Tweet:rt @cvmtv: #news: minister of #education, fayval williams, has announced that to date, 99,887 students have gotten at least one dose of the…
Tweet ID:1458598767809208329
This is not an Extended Tweet

Tweet:rt @mojos55: @telegraph
·
patients could sue the #nhs if they catch #covid from unvaccinated staff this winter, a clinical negligence barri…
Tweet ID:1458598765804277761
This is not an Extended Tweet

Tweet:@araujotomas1 @coalitiontexas dr. peter mccullough joins 
@jfradioshow
 to explain the risks associated with the #covid vaccines.

watch the full conversation on #outsidethebeltway here: https://t.co/mew9jbqck9
Tweet ID:1458598735357882370
This is an Extended Tweet

Tweet:rt @shongables: second guessing #covid19 #vaccine for your kid?
look at what's happening in #england.
what happens in england - eventually…
Tweet ID:1458598635143319556
This is not an Extended Tweet

Tweet:scandale en #france  : l’avocat #fabricedivizio pourrait être radié en raison de son opposition au #passsanitaire https://t.co/cnmwcgwvnw via @le courrier du soir #macron20h #covid #coronavirus #didierraoult #covid19 #avocat #radiation #sanction #nonaupassdelahonte
Tweet ID:1458598604705251333
This is not an Extended Tweet

Tweet:rt @val_bernasconi: même si la pandémie semble moins préoccupante, 1 cas de #covid dans une prison pourrait encore avoir des conséquences c…
Tweet ID:1458598587106013189
This is not an Extended Tweet

Tweet:now, however, doctor and esteemed hospital director #lutchmedial is vaccinated and dead

how many #healthcare heroes he managed to lay off before his passing?

in any case, as lutchmedial promised, he--deceased--will not be shedding any tears for those who averted #covid #vaccine
Tweet ID:1458598577790275585
This is not an Extended Tweet

Tweet:we just started and were not stopping! ride the waves with us to the moon or drown not trying. 🤑🤙🏾
also catch us at times square soon!!!
#surfmoon #crpyto #travel #covid #millionaires #pumping #winners #crpytocurrency #bitcoin #bsc #bnb #etherium #gold #timessquare https://t.co/g8ualgyfcc
Tweet ID:1458598572195209224
This is not an Extended Tweet

Tweet:rt @johnbasham: report: @pfizer sponsored @nbcnews caught lying about #covid &amp; kids. political commentator @jimmy_dore calls out @drjohntor…
Tweet ID:1458598558349901827
This is not an Extended Tweet

Tweet:rt @colarchon: @rebekkafaith @112michelle112 @vortmax29 @freethebobnj @paulaco51119295 @jo60087667 @njunited @fcat2222 @tailwags4 @polifact…
Tweet ID:1458598549701251072
This is not an Extended Tweet

Tweets that are Extended: 39
Tweets that are Not Extended: 961
Percentage of Extended Tweets: 27.86%
'''