'''
Jesus Macias

This program looks at 10000 tweets to count and display number of tweets
in each language.
'''
import tweepy
import keys
from collections import Counter

# accessing the twitter account
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# initializing api
api = tweepy.API(auth, wait_on_rate_limit=True)

# search term and date
search_words = "#covid"
date_since = "2021-11-1"

# collect tweets
tweets = tweepy.Cursor(api.search, q=search_words, since=date_since).items(1000)
language = []
for tweet in tweets:
    print(tweet.text)
    print("Language of the Status:", tweet.lang,"\n")
    language.append(tweet.lang)
print("Languages of Tweets:", language)
set = set(language)
numLanguages = len(set)
print("Number of Different Languages:", numLanguages)

print("\nDifferent Languages of Tweets and thie Occurance:")
print(Counter(language).keys())
print(Counter(language).values())

'''
Sample Output:
RT @MelissaLMRogers: People and government powers are out there celebrating high vaccination rates KNOWING the only reason the numbers are…
Language of the Status: en

5 millones de muertos oficiales por #COVID en el mundo
Muertos por Covid-19 en el mundo llegan a cinco millones y… https://t.co/cOlmp0sRHL       
Language of the Status: es

#DePaís | Rocío Karina llevo este día a su hija a recibir la primera dosis contra la #COVID, aseguró que es algo ne… https://t.co/dxGcumsuVt
Language of the Status: es

UNC and Duke offer hope for a universal coronavirus antibody therapy
#covid #immunotherapy
https://t.co/FJimnfigA3
Language of the Status: en

RT @BNFC_13: En temps de guerre, Blanquer ministre des armées rendrait certainement à l'État une partie du budget de la Défense.
#Covid #ec…
Language of the Status: fr

RT @ndtv: #LeftRightCentre | "These pills are given in the first five days (of infection) 
so that people don't see the descent (into critic…
Language of the Status: en

RT @douchink: @RougeOfficiel 💉#Covid  Une journaliste argentine :
"Je ne vais pas vous mentir même si c'est mon dernier jour sur cette cha…
Language of the Status: fr

RT @jamesvgingerich: It's a real #Covid mask.  Over-engineered egghead, or really cool you have to have one?  Your thoughts?  (GiGadgets) #…
Language of the Status: en 

RT @MWielichowska: Kolejne bardzo niepokojące wieści z ministerstwa liczenia i statystyk: 
ostatniej doby potwierdzono 18 550 przypadków wyk…
Language of the Status: pl

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/kH2Mxg778u
Language of the Status: de

RT @ajplus: U.S. consumer prices surged by 6.2% in the last year — a record increase since 1990.

Food banks are struggling to meet demands…
Language of the Status: en

RT @elchamocandanga: Buen día Venezuela
Aquí regresando por estos lares
Sobreviviendo al #covid solo aquí solo aquí en casa
Y lo venci 👊👏👏…
Language of the Status: es

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr 

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr

La jugada globalista consiste en crear emergencias para eliminar el sistema democrático capitalista en favor del co… https://t.co/D9Ed0W7sTE
Language of the Status: es

RT @MelissaLMRogers: Just a reminder that 0.06% of Covid deaths in Canada were among those aged 19 and under

#Canada #Ontario #Quebec #Co…
Language of the Status: en

RT @Adnkronos: #Covid, dalla senatrice Granato tesi no vax in Aula: "Governo ci ha venduti a multinazionali". E i #vaccini, dice, valgono "…
Language of the Status: it

RT @Margotte57000: Écoutez bien!Mme @MLP_officiel aurait autorisé les médecins "ayant un traitement #covid" à nous prendre comme cobayes en…
Language of the Status: fr

RT @Si_or_just_Si: @DrJudyAMikovits #Truth wins #COVID #COVID19 https://t.co/5rMFvyAWpp   
Language of the Status: en

RT @DavidKoubbi: Pourquoi le #President a t’il changé de voix ? Est-ce un sosie ? Est-il enrhumé ? A t’il le #covid ? Est-ce la 5G ? Nous a…
Language of the Status: fr

RT @France24_fr: 🇫🇷 Retour sur les principales annonces d'Emmanuel #Macron lors de son a  
llocution, mardi soir ⤵️

#Covid #Macron20h https:/…
Language of the Status: fr

RT @clayandbuck: “When you're talking to your pediatrician about #ChildVaccines, ask them, what's the incidence of myocarditis after the se…
Language of the Status: en

RT @Sonic_urticant: 🔥📣[BOUM !]

En pre-print depuis près d'un an

la plus grande META-ANALYSE sur l'#Hydroxychloroquine contre #Covid:

tod…
Language of the Status: fr

RT @ColArchon: #Newjersey #BOE Meeting
#Covid #Vaccine Buses Are Coming To Our Schools People
STAY ALERT 📢
Tell Your Kids to Pay Attention…
Language of the Status: en

RT @MuslimDiasporas: French health authority advises against #Moderna #COVID vaccine for under 30s because of increased risks of Myocarditi…
Language of the Status: en

RT @PublicHealthAZ: New ⁦@PublicHealthAZ⁩ Data Brief:

Arizona is the ONLY State in the U.S. where #COVID Has Been the Leading Cause of De…      
Language of the Status: en

RT @MuslimDiasporas: “Germany’s vaccine advisory board on Wednesday recommended against using #Moderna ‘s Covid-19 shot in people under 30”…
Language of the Status: en 

#Covid #Covid19 #CovidVax #VaxMandate #StoptheInsanity https://t.co/B3W7mNPILk
Language of the Status: und

RT @DavidKoubbi: Pourquoi le #President a t’il changé de voix ? Est-ce un sosie ? Est-il enrhumé ? A t’il le #covid ? Est-ce la 5G ? Nous a…
Language of the Status: fr

@Bueronymus @Die_Gruenen Ich hatte von Anfang an geringe Erwartungen - und es scheint die 
werden noch unterboten.… https://t.co/nnFXu8BO00
Language of the Status: de

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/CJlue0Q7u9
Language of the Status: de

Magnífica viñeta de @ferranmartin vía https://t.co/OQFAKHM0wq
, Ayuso y el desmadre de la Comunidad de Madrid, lueg… https://t.co/IVkcWRFH6a
Language of the Status: es

RT @jeperego: Per l'ondata di nuovi contagi #covid che ha portato le terapie intensive ad 
avere ancora solo il 10% di posti liberi, il gove…
Language of the Status: it

RT @SuselyMorfaG: Inicia hoy III proceso de rendición de cuenta de los delegados a sus electores. El cual tendrá lugar en el ámbito de la c…
Language of the Status: es

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr 

@DrEricDing Stay safe folks &amp; earn up to $100/help make a difference by sharing your experience in online surveys.… https://t.co/cJdqmK7bO0
Language of the Status: en

RT @SandhyaRamanat1: @NicoleDwyerNZ @MoonbaseOtago @farmgeek @SiouxsieW For advice and my 
demo on how to use #pulseoximeters, as well as #b…
Language of the Status: en

RT @myrtamerlino: "Le forme legittime di dissenso non possono mai sopraffare il dovere civico di proteggere i più deboli: dobbiamo sconfigg…
Language of the Status: it 

RT @Humans_of_STL: “I was a 1st-year fellow when Ebola hit. 2 years later, I was pregnant 
when along came Zika. Then in my 2nd pregnancy, #…
Language of the Status: en

RT @FNInfermieri: 🗞 Secondo i dati #FNOPI ripresi da @Adnkronos e @fattoquotidiano sono c 
irca 3.800 gli #infermieri sospesi (pari allo 0,8%…
Language of the Status: it

Join me on 'Montana Right Now' on @ABCFOXMT and @KULR for my uninterrupted conversation with @GovGianforte. From… https://t.co/JMMJ1tfTRN
Language of the Status: en

RT @cityofwinnipeg: As of this Friday, we will support #COVID vaccination screening at all 11 City-operated arenas during peak hours, from…
Language of the Status: en

bdoceanne(@bdoceanne) on TikTok: #covid19 #covid #vaccin #pourtoi https://t.co/Vq7sserrpQ 
Language of the Status: ht

#Covid #JoesJab #myocarditis #CovidCult https://t.co/HwJ1rH1jXz
Language of the Status: und

@LCI Vague bien lointaine encore hier... Parano manipulateur Macron irresponsable agent inquiétudes. Incitations, v… https://t.co/gTYCGbVk2Q
Language of the Status: fr

RT @JeroenSmeets76: Het is zover. Alle bijeenkomsten voor huisartsen fysiek geannuleerd. Bijna 15% vd huisartsen covid pos. Zorg continuïte…
Language of the Status: nl

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/CJlue0Q7u9
Language of the Status: de

RT @jamesvgingerich: It's a real #Covid mask.  Over-engineered egghead, or really cool you have to have one?  Your thoughts?  (GiGadgets) #…
Language of the Status: en

RT @tempoweb: L'allarme di Galli a #StaseraItalia: "Rischiano di morire bambini e adolescenti" (VIDEO) #covid #vaccino #iltempoquotidiano…
Language of the Status: it

RT @Adnkronos: #Covid oggi Austria, l'offerta del bordello di Vienna per incentivare i #vaccini.
https://t.co/bCngRFeIrl
Language of the Status: it

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr

RT @Adnkronos: #Covid, dalla senatrice Granato tesi no vax in Aula: "Governo ci ha venduti a multinazionali". E i #vaccini, dice, valgono "…
Language of the Status: it

bdoceanne(@bdoceanne) on TikTok: #covid19 #covid #vaccin https://t.co/43tJ3gkXuh
Language of the Status: ht 

📢 Believe it or not, while the world faced COVID -19, an acute respiratory syndrome, 192 
million people used cannab… https://t.co/ZFDAA6or8M
Language of the Status: en

RT @JuanSaaa: ALSO PART OF THE PANEL is Javier Quiroz Castro, who is a #DACA recipient working in the frontlines of Texas' #COVID 19 recove…
Language of the Status: en

RT @SandhyaRamanat1: @NicoleDwyerNZ @MoonbaseOtago @farmgeek @SiouxsieW For advice and my 
demo on how to use #pulseoximeters, as well as #b…
Language of the Status: en

RT @ConflitsFrance: 🇫🇷 FLASH | Selon une étude, les #étudiants sont plus concernés par d  
es troubles anxieux et #dépressifs que le reste de…
Language of the Status: fr

#Covid deaths in #Oklahoma https://t.co/8E0EA1SfAt
Language of the Status: en

Che tristezza. Le cose non migliorano. Leggo solo di sto #covid #novax #NoGreenPass Un po’ di speranza voglio nutrirmi stasera. Help me
Language of the Status: it

Cases of #scurvy on the rise in kids in the #UK .

Here's some more information on the symptom.

#COVID19… https://t.co/P4DaZVZw6G
Language of the Status: en

RT @douchink: @EldoRhaan @yvesbourdillon @towersight @fquedeville 💉#Covid Un journaliste 
allemand :
« L’une des grandes nouvelles en proven…
Language of the Status: fr

RT @jeperego: Per l'ondata di nuovi contagi #covid che ha portato le terapie intensive ad 
avere ancora solo il 10% di posti liberi, il gove…
Language of the Status: it

RT @TgLa7: #Covid: #Baviera decreta stato emergenza https://t.co/PrBeAxU6Bp
Language of the Status: it

Data on severe #COVID show higher risk of adverse #cardiac event post recovery. Focus likely on hospitalized patien… https://t.co/IYaYf1TkQO
Language of the Status: en

RT @MediasetTgcom24: Berlino vieterà ingresso a ristoranti, cinema e mostre ai non vaccinati  #covid https://t.co/I1P79Dwoqi https://t.co/h…
Language of the Status: it

Hampton Roads' average #COVID-19 percent positivity rate exceeds statewide average https://t.co/YlNhOm8aKZ https://t.co/xaxymTQO9j
Language of the Status: en

RT @matigrje: #COVID #FJB #LetsGoBrandon #JoeBiden #Democrats #OSHA #CDC #WakeUpAmerica #Vaccine #mandate #WalkOut https://t.co/DiphluP9un
Language of the Status: und

RT @matigrje: #COVID #FJB #LetsGoBrandon #JoeBiden #Democrats #OSHA #CDC #WakeUpAmerica #Vaccine #mandate #WalkOut https://t.co/DiphluP9un
Language of the Status: und 

💥 La vacuna de la #Covid-19 sembla que s’ha generalitzat entre la població; però no podem baixar la guàrdia perquè… https://t.co/n0lCfHlcZh
Language of the Status: ca

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/CJlue0Q7u9
Language of the Status: de

RT @ferranmartin: Esta noche ha venido a divertirse con nosotrooooos…
Vía https://t.co/q1ffsuatT4
#ayuso #vacunas #covid #viñetas https://t…
Language of the Status: es

RT @LiuBaoBei1: I've lived in #China, I'm familiar with social credit systems and tyrannical control

Oh, you crossed the road without a gr…
Language of the Status: en

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de

RT @peterlepoutre: @FranckenTheo Die zwarte dag was het eerste #overlegcomité rond #covid, toen het land op slot ging door #vivaldiplus. To…
Language of the Status: nl

Check out the @GovCanHealth’s interactive data visualizations of COVID-19 cases, tests, and other criteria over tim… https://t.co/4jbIRvUUrx
Language of the Status: en

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

I dati sul #Covid oggi in Italia. https://t.co/dGO2mUgtIe
Language of the Status: it

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de

RT @dirflash: Last 24-hour #COVID-19 data from #Colorado:
2,505 new cases
1,501 hospitalizations
22 deaths
775,587 total cases
8,713 total…
Language of the Status: en

RT @Hofix53: Chronik mit Bild . . . . 
#corona #covid #bild https://t.co/nYJvfDDPyh
Language of the Status: de

RT @USRepMikeDoyle: By year's end @HouseDemocrats will have:
✅Passed the #AmericanRescuePlan - historic #COVID relief
✅Passed an unpreceden…
Language of the Status: en

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr 

#ElPaso health care providers seen a rise in anxiety, depression and suicidality stemming 
from social isolation, di… https://t.co/RWmd2mhoFW
Language of the Status: en

RT @tvlofficiel: #Covid-19 : Port du #masque obligatoire dans les files d'attente des remontées mécaniques
https://t.co/Mryba2eoGX
Language of the Status: fr

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de

RT @GiovaQuez: A Berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. I tamponi non saranno più sufficienti #Covid
Language of the Status: it 

RT @dirflash: Last 24-hour #COVID-19 data from #Colorado:
2,505 new cases
1,501 hospitalizations
22 deaths
775,587 total cases
8,713 total…
Language of the Status: en

@FranckenTheo Die zwarte dag was het eerste #overlegcomité rond #covid, toen het land op slot ging door… https://t.co/ExubGhlqCu
Language of the Status: nl

@fehi60 @drkaanyl @kaan_levin #COVID19 is an animal virus (mix of bat, bird, pig #coronavirus ). It does not act li… https://t.co/wK4SldrPyy
Language of the Status: en

@KCPublicHealth reports 24 new COVID deaths and 316 new cases on Wednesday. #COVID #KernCounty
A CLOSER LOOK AT THE… https://t.co/Ei5agZpBWO
Language of the Status: en

How to Renegotiate Your Commercial Rent After the Pandemic #CRE #COVID-19 #NewNormal #Negotiation #Rent
https://t.co/WOwFrVa0Kq
Language of the Status: en

In #Missouri, determining whether service providers are #vaccinated against #Covid is not 
easy due to privacy rules… https://t.co/2NqAstECsl
Language of the Status: en

Last 24-hour #COVID-19 data from #Colorado:
2,505 new cases
1,501 hospitalizations
22 deaths
775,587 total cases
8,… https://t.co/gJ7qiKEIHG
Language of the Status: en

V současné době je v nemocnicích 3,295 hospitalizovaných lidí s nemocí COVID-19. Celkem bylo kvůli covidu poprvé ho… https://t.co/FFZhj3VSDf
Language of the Status: cs

BIONTECH VE #PFIZER AŞISI 5-11 YAŞ ARASI ÇOCUKLARDA YÜZDE 90.7 ETKİLİ

ABD merkezli Massachusetts Tıp Derneği taraf… https://t.co/lrLKsUm0R7
Language of the Status: tr

#After | #Climate | #China | #Covid | #Who | #Rittenhouse | #Crisis | #Cop | #Man | #Vacci via https://t.co/wooaMBbZWW
Language of the Status: en

El titular de la @SRE_mx @m_ebrard anunció que la próxima semana se realizará la Novena Cumbre de Líderes del Norte… https://t.co/v7XdF6FpXb
Language of the Status: es 

As vaccination rates rise in many parts of the world and even countries that previously had strict #COVID-containme… https://t.co/BYFaTWsmdw
Language of the Status: en

🇩🇪💉⚕️

Germany bans unvaccinated people from hospitality and leisure venues https://t.co/QxSKREih1f via  @BBCNews h… https://t.co/amMjXNm3AF
Language of the Status: en

Are we really approaching the end of Covid? Some brands are banking on it.
Travel stocks rally, stay-at-home compan… https://t.co/cIwZUNxUSg
Language of the Status: en

¡Ojo! El secretario de Salud de Puebla, informó que la #vacuna para prevenir la influenza 
y la vacuna contra el… https://t.co/auOwdsIU2y
Language of the Status: es

RT @FrancisLalanne4: .Petit message les amis ! On ne lâche rien ! #Pfizergate #covid #vaccination #Lalanne https://t.co/wqRoMwXl6Q
Language of the Status: fr

RT @sputnikvaccine: One of Sputnik V key creators Alexander #Gintsburg turns 70🎂

Dr Gintsburg &amp; his Gamaleya Center team created safe &amp; ef…
Language of the Status: en

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de 

RT @Unomattina: Le principali notizie del giorno @CBrachino, giornalista politico del @ilgiornale e di @Italpress. Partiamo dal #covid, ier…
Language of the Status: it

RT @OsmiCovidBot: #COVID Update 904:
• Tests: 409241 (+1455)
• Cases: 60475 (+512)
• Active: 6036 (+278)
• Deaths: 1806 (+12)
• Recover…
Language of the Status: en

RT @EClinicalMed: A new clinical trial analysed effectiveness of #Lopinavir/#ritonavir (LPV/r) as post-exposure prophylaxis for #COVID-19.…
Language of the Status: en

RT @GiovaQuez: A Berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. I tamponi non saranno più sufficienti #Covid
Language of the Status: it

RT @JeroenSmeets76: Het is zover. Alle bijeenkomsten voor huisartsen fysiek geannuleerd. Bijna 15% vd huisartsen covid pos. Zorg continuïte…
Language of the Status: nl

Attention #parents #teachers #schools #education.
#Maskup for school. #delta #covid
Kids size Premium #KN95 Respir… https://t.co/DX35uF9igY
Language of the Status: en

RT @TrishaJamesMBA: 🆓#COVID-19 and outcomes in patients with inflammatory bowel disease: 
Systematic review and meta-analysis

🔶Tripathi K B…
Language of the Status: en

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr 

@SenBooker Imagine if a superpower blocked 🇺🇸 economic, financial, &amp; commercial tran  
sactions; intensified that in p… https://t.co/oQcTr8d188
Language of the Status: en

RT @DavidHarrisAJC: When I wonder how long we’ll be in #COVID lockdown, I think of my:    

-Wife, then 16, hiding for weeks in Libya in 1967,…
Language of the Status: en

RT @ConflitsFrance: 🇫🇷 FLASH | Selon une étude, les #étudiants sont plus concernés par d  
es troubles anxieux et #dépressifs que le reste de…
Language of the Status: fr

RT @NDCS_UK: Big thanks to Nick Brown MP and @TulipSiddiq for raising #deaf children’s mental wellbeing and the impact of #Covid and #facem…
Language of the Status: en

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr

RT @IdeaGov: Hey Parents! #covid requires masks for schools.
#Maskup for school. #delta
Kids size Premium #KN95 Respirator Mask  - 50 piec…
Language of the Status: en

RT @MediasetTgcom24: Speranza: "Dal primo dicembre terza dose a 40-60enni"  #covid https://t.co/I1P79Dwoqi https://t.co/dZl8CVh63g
Language of the Status: it

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

RT @berettasudaca: Donde está el #seremi @SaludSsrv qué onda? Esta sin mascarilla y escupiendo ASCO #Covid @SeremiSalud_IX  @CarabValparaiso
Language of the Status: es

RT @QualityCare_TX: Fall season = flu season 🤧
Getting the flu shot is the best way to prevent you from becoming sick with the flu or to 
l…
Language of the Status: en

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/kH2Mxg778u
Language of the Status: de

RT @EvelyneNahellec: #hdpros2 @CNEWS @PascalPraud
Vous dites qu'en Allemagne il n'y a jamais eu autant de cas de #Covid !  Vous oubliez ju… 
Language of the Status: fr

RT @GiovaQuez: A Berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. I tamponi non saranno più sufficienti #Covid
Language of the Status: it

RT @LawTechHum: 🆕article: @anitalavorgna @PamelaUgwudike @lescarr @Yadira_Sz @GopalaSRekha Resistance to #COVID contact tracing apps in the…
Language of the Status: en 

RT @ElInformadorVE: ##10Nov Coalición sindical del magisterio larense denunció  brote de #covid-19  y solicita emplazar a las autoridades e…
Language of the Status: es

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

RT @clayandbuck: “When you're talking to your pediatrician about #ChildVaccines, ask them, what's the incidence of myocarditis after the se…
Language of the Status: en

RT @ErinSandersNP: 19/ Of watching people unwilling to do something mildly uncomfortable to protect others

Of watching whole countries ref…
Language of the Status: en

“Germany’s vaccine advisory board on Wednesday recommended against using #Moderna ‘s Covid-19 shot in people under… https://t.co/yLHZLEOjZD
Language of the Status: en

Compartimos actualización de #Situación #ElSalvador por el #COVID-19, hasta las 2:00 pm de este 10 de noviembre de… https://t.co/pk7ntSteXj
Language of the Status: es

Great work by @EmergencyDocs to clear up #COVID #misinformation leading to #vaccinehesitancy. Bad information is on… https://t.co/L2ipKBIHv7
Language of the Status: en

I despise #COVID19 minimizers. They are killers.

At this point, it's Depraved Indifference Homicide by all the con… https://t.co/UqJ0yvk6tkLanguage of the Status: en

RT @Takeactioncan: Lest we forget, some tried to warn the world and the evil CCP prevented it.

https://t.co/S8AmtoLy9o

#CCP #CCPChina #co…
Language of the Status: en

RT @PublicHealthAZ: New ⁦@PublicHealthAZ⁩ Data Brief:

Arizona is the ONLY State in the U.S. where #COVID Has Been the Leading Cause of De…      
Language of the Status: en

RT @flamecapitain: #Macron20h #Pfizergate #billgates #Moderna #COVID19 #COVID

Ca commence a faire mal....💥💥
Language of the Status: fr 

RT @radiobakker: Gisteren was ook bij #Op1 te zien de groep met vaccinatie + zelf opgebouwde weerstand tegen #COVID
Dat was de groep waar…
Language of the Status: nl

RT @ConflitsFrance: 🇫🇷 FLASH | Selon une étude, les #étudiants sont plus concernés par d  
es troubles anxieux et #dépressifs que le reste de…
Language of the Status: fr

RT @jeha2019: Tägl. gibt es neue Erkenntnisse zur #Covid-#Impfung; nicht selten sind es negative.
Für unter 30jährige gibt es nunmehr nur n…
Language of the Status: de

RT @BMSG: A big thank you to reporters @newsterrier @radiobilingue @n_llopez for speaking 
to #TogetherTowardHealth grantees, local health d…
Language of the Status: en 

RT @malvernhillshr: Good evening #MalvernHillsHour how are we all this week? We know that 
several of our lovely followers have not been wel…
Language of the Status: en

RT @DieSlodo: Wer #LockdownJetzt fordert, nachdem der "kurze Wellenbrecherlockdown" von 6 
Monaten Länge letztes Jahr so extrem gut funktion…
Language of the Status: de

RT @NEbigdatahub: We're hiring a Program Manager for the @CIC_COVID! Apply today to join our fantastic team!

Learn more: https://t.co/Gobx…
Language of the Status: en

RT @SuselyMorfaG: Inicia hoy III proceso de rendición de cuenta de los delegados a sus electores. El cual tendrá lugar en el ámbito de la c…
Language of the Status: es

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr

RT @ajplus: U.S. consumer prices surged by 6.2% in the last year — a record increase since 1990.

Food banks are struggling to meet demands…
Language of the Status: en

We're hiring a Program Manager for the @CIC_COVID! Apply today to join our fantastic team!
Learn more:… https://t.co/qAZu4J6n0I
Language of the Status: en

RT @Geopolitics_Emp: "#Israel will hold a national exercise to prepare for the next #COVID19 outbreak. The "#OmegaExercise" will be held in…
Language of the Status: en

RT @roslemusmartin: En tan solo unos días ya hay más de 1 millón de niños  vacunados contra #COVID: !Los niños ponen el ejemplo a los adult…
Language of the Status: es

Io non ho mai negato l'esistenza del #Covid, dico solo che non è così mortale come ci dicono. Non è che sono tutti… https://t.co/KjKLyiLvs8
Language of the Status: it

RT @PraharajArun: Thanks to Korean Ambasador H.E. Chung Hae Kwan @korembbah for invitation to #Korean DASRUM music concert in honor of 45 y…
Language of the Status: en

RT @Cs_CLM: 🚨La subida de la cuota a los #Autónomos en un momento de inflación y con la factura de la luz por las nubes es condenarles.

‼️…
Language of the Status: es

Incentive to get kids 5 to 11 vaccinated #Covid
-$50 gift card for kids after the first &amp; second shot
-50 scholarsh… https://t.co/Dmcq6tjCaI
Language of the Status: en

RT @MediasetTgcom24: Berlino vieterà ingresso a ristoranti, cinema e mostre ai non vaccinati  #covid https://t.co/I1P79Dwoqi https://t.co/h…
Language of the Status: it

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de

RT @ConflitsFrance: 🇫🇷 FLASH | Selon une étude, les #étudiants sont plus concernés par d  
es troubles anxieux et #dépressifs que le reste de…
Language of the Status: fr

RT @DavidKoubbi: Pourquoi le #President a t’il changé de voix ? Est-ce un sosie ? Est-il enrhumé ? A t’il le #covid ? Est-ce la 5G ? Nous a…
Language of the Status: fr

RT @clayandbuck: Covid Data: California Vs. Florida
"#Florida has the lowest rate of #covid infection -- this is per capita, per hundred th…  
Language of the Status: en

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/CJlue0Q7u9
Language of the Status: de

@harry59degroot #covid-19 jabs do not qualify as vaccination. It’s gene therapy. And experimental at that.
Language of the Status: en

RT @SandhyaRamanat1: @NicoleDwyerNZ @MoonbaseOtago @farmgeek @SiouxsieW For advice and my 
demo on how to use #pulseoximeters, as well as #b…
Language of the Status: en

RT @LongbeachUSD: The @LBHealthDept has started administering the #COVID vaccine to children ages 5 to 11. Read more and view the November…
Language of the Status: en

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/FIrgdYHfSA
Language of the Status: de

RT @jeha2019: Tägl. gibt es neue Erkenntnisse zur #Covid-#Impfung; nicht selten sind es negative.
Für unter 30jährige gibt es nunmehr nur n…
Language of the Status: de

⭕️Balance de #Trazabilidad por contacto de contagio #COVID-19 entregado por el @ministeriosalud para la semana del… https://t.co/jpvjpFmb3P
Language of the Status: es

RT @WolfieLoneSome: This Tory Government are totally talking the p'ss out of us, what can 
be done about it one wonders!!!
#NationInWaiting…
Language of the Status: en

French health authority advises against #Moderna #COVID vaccine for under 30s because of increased risks of Myocard… https://t.co/g1Dg4vca20
Language of the Status: en

RT @MWLOrg_en: The World Science Day for Peace and Development was established to highlight the role scientists play in making our societie…
Language of the Status: en

Fema is in this hospital and probably not jabbed themselves as tyrannical mandates are being made on the regular st… https://t.co/MJFpzSFWOw
Language of the Status: en

RT @CoryPippinTV: Breakthrough #COVID cases increased in #Alabama as #vaccinated residents account for 1 in 5 people in the hospital battli…
Language of the Status: en 

Sign ups for this class have been extended to Sunday November 14th at 11:59 pm ET, so be sure to sign up and join u… https://t.co/JIHCvP0vCu
Language of the Status: en

RT @ConflitsFrance: 🇫🇷 FLASH | Selon une étude, les #étudiants sont plus concernés par d  
es troubles anxieux et #dépressifs que le reste de…
Language of the Status: fr

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

No hay información oficial sobre presuntos menores fallecidos por COVID-19: Educación y Cultura
#Camargo #vacuna… https://t.co/BSiuQg3bG3
Language of the Status: es

RT @M49liberorso: 30 persone in pellegrinaggio a #Medjugorje positive al #Covid https://t.co/wLSffpeZky
Language of the Status: it

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/CJlue0Q7u9
Language of the Status: de

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

RT @GaucheMafia: 🇫🇷@ZemmourEric: « Il y a une volonté du Président de la République de r  
éimposer le thème du #Covid, pour chasser tactiquem…
Language of the Status: fr

RT @artemi_ecrit: Für alle, die glauben, sie könnten den Anschnallgurt im Auto mit der #Covid-#Impfung vergleichen. Als Schutz eben. Da ist…
Language of the Status: de

RT @aloa5: #COVID in Deutschland, #Endgame #Tag1

Es wird ganz, ganz böse. Nicht vielleicht, sondern sicher.  Nicht sicher bin ich, wie ich…Language of the Status: de

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

'As we all adjust to a world changed forever by #Covid, this book provides a blueprint for how we might build back… https://t.co/lDuGcc657J
Language of the Status: en

RT @GaucheMafia: 🇫🇷@ZemmourEric: « Il y a une volonté du Président de la République de r  
éimposer le thème du #Covid, pour chasser tactiquem…
Language of the Status: fr

RT @la_resistensia_: 🟥⚠️ESTA MASCARILLA NO FILTRA AEROSOLES INFECTIVOS #COVID⚠️🟥
Por favor no la use. Rechácela. Protéjase y proteja a los…
Language of the Status: es

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr 

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

RT @DieSlodo: Wer #LockdownJetzt fordert, nachdem der "kurze Wellenbrecherlockdown" von 6 
Monaten Länge letztes Jahr so extrem gut funktion…
Language of the Status: de

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr

RT @jesusortegam: La gestión del gobierno mexicano para la crisis de salud por #Covid es desastrosa. https://t.co/TC8EFOsjfP
Language of the Status: es

I've lived in #China, I'm familiar with social credit systems and tyrannical control      

Oh, you crossed the road with… https://t.co/HH7SninbgT
Language of the Status: en

RT @Verhaeghe: C'est moi ou, vous aussi, vous avez eu l'impression que #Macron20h était l'oeuvre d'un homme qui ne serait pas candidat en a…
Language of the Status: fr

RT @HelenBranswell: We are all sick and tired of #Covid, but pretending it is over does not make it so. As you contemplate the risks you ar…
Language of the Status: en

RT @Adnkronos: #Covid, dalla senatrice Granato tesi no vax in Aula: "Governo ci ha venduti a multinazionali". E i #vaccini, dice, valgono "…
Language of the Status: it

RT @GiovaQuez: A Berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. I tamponi non saranno più sufficienti #Covid
Language of the Status: it

RT @GaucheMafia: 🇫🇷@ZemmourEric: « Il y a une volonté du Président de la République de r  
éimposer le thème du #Covid, pour chasser tactiquem…
Language of the Status: fr

RT @GaucheMafia: 🇫🇷@ZemmourEric: « Il y a une volonté du Président de la République de r  
éimposer le thème du #Covid, pour chasser tactiquem…
Language of the Status: fr

RT @intuslegens: Da più di un mese si susseguono manifestazioni con migliaia di persone in tutta Italia, non vaccinati, senza mascherine né…
Language of the Status: it

@BradleyWhitford Doesn't he want to run for @texasgov ?

#antivaxx fits the political strategy.

#Covid #vaccine #vaccination
Language of the Status: en

PREVENTING COVID
Even in high risk situations, this ancient herb helps protect you from #COVID:… https://t.co/hisbCWxV8e
Language of the Status: en

RT @peaksurfer: If we are unable to cope with minor #Covid restrictions, how then shall we emotionally handle much more serious changes — l…
Language of the Status: en 

RT @Adnkronos: #Covid, dalla senatrice Granato tesi no vax in Aula: "Governo ci ha venduti a multinazionali". E i #vaccini, dice, valgono "…
Language of the Status: it

#COVID La ocupación de pacientes en las #UCI de #CastillayLeón se reduce casi medio punto 
en las últimas 24 horas y… https://t.co/biqyxqCbnh
Language of the Status: es

De quels médicaments contre le #covid parle Emmanuel Macron pour la fin d'année ? https://t.co/smZHlHQgsZ https://t.co/G5rMPtW6AW
Language of the Status: fr

RT @WhistleblowerHB: #Whistleblower News:

#Arkansas Man Charged in $100M #COVID #HealthCare Fraud

Man Sentenced to Prison After Pleading…
Language of the Status: en

RT @M_T_Franz: Ich werd jetzt grantig mit dieser völlig falschen #Covid Politik!! https://t.co/FIrgdYHfSA
Language of the Status: de

#Covid deja mas muerte en la región #Delicias 2, #Camargo 1 y #Saucillo 1 https://t.co/dAPN6ZH8Xx https://t.co/f9AMTY8QiU
Language of the Status: es

RT @Adnkronos: #Covid, dalla senatrice Granato tesi no vax in Aula: "Governo ci ha venduti a multinazionali". E i #vaccini, dice, valgono "…
Language of the Status: it

RT @LCP: "Le fait que la #Covid cible plus les gens ayant des comorbidités, veut dire que 
quand il y aura une immunité suffisante dans la p…
Language of the Status: fr

RT @MelissaLMRogers: People and government powers are out there celebrating high vaccination rates KNOWING the only reason the numbers are…
Language of the Status: en

RT @DieSlodo: Wer #LockdownJetzt fordert, nachdem der "kurze Wellenbrecherlockdown" von 6 
Monaten Länge letztes Jahr so extrem gut funktion…
Language of the Status: de

RT @GiovaQuez: A Berlino potranno accedere nei ristoranti solo i vaccinati ed i guariti. I tamponi non saranno più sufficienti #Covid
Language of the Status: it

Languages of Tweets: ['pt', 'it', 'en', 'it', 'it', 'it', 'en', 'it', 'fr', 'es', 'it', 'en', 'de', 'en', 'en', 'en', 'fr', 'en', 'fr', 'en', 'it', 'fr', 'en', 'nl', 'pt', 'en', 'fr', 'fr', 'en', 'nl', 'nl', 'en', 'it', 'en', 'en', 'nl', 'en', 'en', 'fr', 'fr', 'en', 'en', 'es', 'en', 'en', 'es', 'en', 'en', 'it', 'ca', 'es', 'fr', 'es', 'fr', 'de', 'it', 'nl', 'ca', 'en', 'fr', 'fr', 'en', 'en', 'en', 'en', 'it', 'da', 'en', 'en', 'en', 'en', 'en', 'en', 'es', 'en', 'fr', 'de', 'en', 'en', 'es', 'fr', 'en', 'es', 'en', 'en', 'fr', 'fr', 'fr', 'fr', 'en', 'es', 'nl', 'fr', 'de', 'en', 'it', 'fr', 'es', 'en', 'it', 'en', 'ru', 'en', 'es', 'fr', 'fr', 'en', 'fr', 'de', 'fr', 'es', 'en', 'es', 'fr', 'en', 'de', 'und', 'it', 'en', 'en', 'en', 'en', 'en', 'en', 'el', 'nl', 'es', 'es', 'de', 'fr', 'fr', 'en', 'de', 'de', 'es', 'de', 'en', 'es', 'en', 'en', 'en', 'en', 'el', 'en', 'nl', 'en', 'en', 'en', 'fr', 'en', 'es', 'en', 'en', 'en', 'en', 'en', 'tr', 'it', 'it', 'es', 'de', 'es', 'de', 'en', 'und', 'en', 'pt', 'de', 'fr', 'de', 'it', 'fr', 'en', 'es', 'en', 'de', 
'it', 'en', 'de', 'en', 'en', 'de', 'de', 'fr', 'en', 'de', 'fr', 'it', 'fr', 'en', 'en', 
'en', 'en', 'it', 'en', 'en', 'fr', 'en', 'en', 'it', 'it', 'de', 'es', 'en', 'fr', 'en', 
'en', 'fr', 'fr', 'fr', 'es', 'fr', 'it', 'es', 'es', 'en', 'de', 'fr', 'fr', 'en', 'en', 
'ru', 'und', 'und', 'fr', 'fr', 'de', 'de', 'de', 'en', 'es', 'und', 'es', 'fr', 'de', 'es', 'it', 'en', 'de', 'en', 'en', 'en', 'en', 'en', 'fr', 'en', 'en', 'it', 'en', 'fr', 'en', 'nl', 'en', 'pt', 'es', 'en', 'und', 'en', 'es', 'fr', 'de', 'it', 'fr', 'en', 'en', 'es', 'fr', 'it', 'en', 'fr', 'es', 'en', 'en', 'en', 'es', 'fr', 'es', 'it', 'de', 'en', 'en', 'da', 'in', 'und', 'en', 'fr', 'de', 'en', 'en', 'en', 'fr', 'it', 'en', 'en', 'en', 'fr', 'en', 'en', 'de', 'de', 'en', 'fr', 'it', 'nl', 'en', 'en', 'es', 'fr', 'en', 'en', 'en', 'en', 'fr', 'en', 'pt', 'en', 'fr', 'en', 'de', 'en', 'en', 'en', 'en', 'en', 'fr', 'de', 'fr', 'es', 'en', 'fr', 'nl', 'en', 'en', 'en', 'es', 'fr', 'en', 'fr', 'und', 'fr', 
'fr', 'en', 'es', 'es', 'en', 'en', 'fr', 'it', 'fr', 'en', 'it', 'de', 'en', 'en', 'de', 
'de', 'de', 'en', 'en', 'de', 'en', 'en', 'de', 'de', 'en', 'es', 'en', 'es', 'en', 'en', 
'pt', 'en', 'es', 'fr', 'en', 'en', 'en', 'en', 'en', 'en', 'en', 'de', 'de', 'it', 'es', 
'sv', 'fr', 'nl', 'fr', 'nl', 'de', 'es', 'it', 'fr', 'en', 'en', 'en', 'de', 'und', 'en', 'nl', 'fr', 'de', 'en', 'en', 'es', 'it', 'de', 'en', 'es', 'en', 'nl', 'de', 'nl', 'fr', 'fr', 'en', 'de', 'de', 'fr', 'it', 'en', 'nl', 'es', 'fr', 'en', 'en', 'de', 'fr', 'de', 'ar', 'de', 'it', 'pt', 'en', 'pl', 'it', 'en', 'de', 'en', 'fr', 'en', 'da', 'es', 'de', 'fr', 'it', 'en', 'fr', 'en', 'es', 'en', 'it', 'fr', 'en', 'fr', 'de', 'de', 'fr', 'fr', 'de', 'es', 'fr', 'en', 'en', 'it', 'en', 'en', 'de', 'de', 'en', 'fr', 'fr', 'es', 'de', 'es', 'en', 'en', 'de', 'nl', 'fr', 'it', 'de', 'en', 'es', 'es', 'fr', 'en', 'de', 'it', 'en', 'en', 'en', 'de', 'fr', 'en', 'en', 'es', 'es', 'de', 'en', 'en', 'es', 'es', 'fr', 'en', 'und', 'en', 'it', 'und', 'fr', 'de', 'en', 'und', 'en', 'en', 'fr', 'en', 'es', 'de', 'en', 'en', 'en', 'en', 'de', 'fr', 'es', 'fr', 'es', 'fr', 'en', 'en', 'de', 'en', 'de', 'en', 'es', 'de', 'en', 'fr', 'es', 'de', 'it', 'en', 'en', 'en', 'de', 'fr', 'en', 'es', 'en', 'en', 'en', 'fr', 'de', 'en', 'en', 'en', 'en', 'en', 'en', 'fr', 'und', 'it', 'de', 'en', 'fr', 'und', 'en', 'es', 'fr', 'es', 'en', 'en', 'en', 'de', 'de', 'en', 'en', 
'fr', 'en', 'nl', 'es', 'it', 'fr', 'it', 'en', 'en', 'en', 'es', 'en', 'en', 'it', 'en', 
'fr', 'it', 'und', 'en', 'de', 'fr', 'fr', 'it', 'it', 'nl', 'en', 'it', 'nl', 'en', 'de', 'en', 'it', 'en', 'it', 'pl', 'fr', 'en', 'pt', 'es', 'fr', 'it', 'en', 'es', 'en', 'de', 'de', 'fr', 'en', 'it', 'fr', 'en', 'es', 'de', 'it', 'en', 'en', 'en', 'it', 'en', 'en', 'it', 'und', 'fr', 'fr', 'de', 'de', 'en', 'de', 'fr', 'de', 'fr', 'fr', 'es', 'en', 'de', 'und', 'fr', 'nl', 'it', 'it', 'en', 'en', 'tr', 'fr', 'fr', 'fr', 'fr', 'en', 'fr', 'fr', 'es', 'fr', 'es', 'nl', 'fr', 'in', 'de', 'fr', 'fr', 'de', 'en', 'en', 'und', 'en', 'de', 'nl', 'fr', 'nl', 'en', 'fr', 'de', 'fr', 'fr', 'en', 'es', 'en', 'en', 'en', 'fr', 'und', 'it', 'fr', 'en', 'pt', 'en', 'und', 'fr', 'fr', 'en', 'es', 'en', 'it', 'en', 'pt', 
'en', 'en', 'de', 'de', 'en', 'es', 'es', 'es', 'it', 'de', 'pt', 'it', 'es', 'en', 'en', 
'de', 'en', 'de', 'fr', 'pt', 'en', 'nl', 'it', 'es', 'it', 'fr', 'de', 'it', 'fr', 'en', 
'fr', 'en', 'fr', 'fr', 'en', 'en', 'de', 'fr', 'es', 'fr', 'en', 'es', 'fr', 'it', 'en', 
'en', 'de', 'tl', 'en', 'fr', 'en', 'ru', 'es', 'es', 'und', 'it', 'es', 'es', 'en', 'es', 'en', 'en', 'el', 'fr', 'en', 'it', 'en', 'en', 'es', 'fr', 'pl', 'fr', 'de', 'en', 'es', 'es', 'en', 'fr', 'en', 'fr', 'en', 'pl', 'de', 'en', 'es', 'fr', 'fr', 'es', 'en', 'it', 'fr', 'en', 'fr', 'fr', 'en', 'fr', 'en', 'en', 'en', 'en', 'und', 'fr', 'de', 'de', 'es', 'it', 'es', 'fr', 'en', 'en', 'it', 'en', 'it', 'en', 'en', 'ht', 'und', 'fr', 'nl', 'de', 'en', 'it', 'it', 'fr', 'it', 'ht', 'en', 'en', 'en', 'fr', 'en', 'it', 'en', 'fr', 'it', 'it', 'en', 'it', 'en', 'und', 'und', 'ca', 'fr', 'de', 'es', 'en', 'de', 'nl', 'en', 'fr', 'it', 'de', 'en', 'de', 'en', 'fr', 'en', 'fr', 'de', 'it', 'en', 'nl', 'en', 'en', 'en', 'en', 'en', 'cs', 'tr', 'en', 'es', 'en', 'en', 'en', 'es', 'fr', 'en', 'de', 'it', 'en', 'en', 'it', 'nl', 'en', 'en', 'fr', 'en', 'en', 'fr', 'en', 'fr', 'en', 'it', 'fr', 'es', 'en', 'fr', 'de', 'fr', 'it', 'en', 'es', 'fr', 'en', 'en', 'en', 'es', 'en', 'en', 'en', 'en', 'fr', 'nl', 'fr', 'de', 'en', 'en', 'de', 'en', 'es', 'fr', 'en', 'en', 'en', 'es', 'it', 'en', 'es', 'en', 'it', 'de', 'fr', 'fr', 'en', 'de', 'en', 'en', 'en', 'de', 'de', 'es', 'en', 'en', 'en', 'en', 'en', 'en', 'fr', 'fr', 'es', 'it', 'de', 'fr', 'fr', 'de', 'de', 'fr', 'en', 'fr', 'es', 'fr', 'fr', 'de', 'fr', 'es', 'en', 'fr', 'en', 'it', 'it', 'fr', 'fr', 'it', 'en', 'en', 'en', 'it', 'es', 'fr', 'en', 'de', 'es', 'it', 'fr', 'en', 'de', 'it']
Number of Different Languages: 20

Different Languages of Tweets and thie Occurance:
dict_keys(['pt', 'it', 'en', 'fr', 'es', 'de', 'nl', 'ca', 'da', 'ru', 'und', 'el', 'tr', 'in', 'sv', 'ar', 'pl', 'tl', 'ht', 'cs'])
dict_values([12, 98, 381, 193, 110, 123, 31, 3, 3, 3, 25, 3, 3, 2, 1, 1, 4, 1, 2, 1])

'''

