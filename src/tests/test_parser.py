"""
Test parser
"""
from techiaith.tts.testun.normaliser import parse_text

tests = [
    [
        "Dyma'r tywydd presennol gan OpenWeatherMap ar gyfer Bangor. "
        + "Mae hi'n gymylog ac mae'r tymheredd yn 16 gradd Celsius. "
        + "Am 9 o'r gloch yn y bore, bydd hi'n bwrw glaw gyda'r tymheredd yn 16 gradd Celsius.",
        "Dyma'r tywydd presennol gan Open Weather Map ar gyfer Bangor. "
        + "Mae hi'n gymylog ac mae'r tymheredd yn un deg chwech gradd Celsius. "
        + "Am naw o'r gloch yn y bore, bydd hi'n bwrw glaw gyda'r tymheredd yn un deg chwech gradd Celsius.",
    ],
    [
        """mae gen i 12 y cant o'r arian sef, £20""",
        """mae gen i ddeuddeg y cant o'r arian sef, ugain punt""",
    ],
    ["""Boneddigion a boneddigesau""", """Boneddigion a boneddigesau"""],
    ["""Annwyl Syr / Madam""", """Annwyl Syr / Madam"""],
    ["""Yr eiddoch yn gywir""", """Yr eiddoch yn gywir"""],
    ["""Oddi wrth""", """Oddi wrth"""],
    ["""Hafan""", """Hafan"""],
    ["""Amdanom ni""", """Amdanom ni"""],
    ["""Cysylltu â ni""", """Cysylltu â ni"""],
    ["""Cysylltwch â ni ar Twitter @S4C""", """Cysylltwch â ni ar Twitter at Es Pedwar Ec"""],
    ["""#yrawrgymraeg""", """hash nod yrawrgymraeg"""],
    ["""😉""", """😉"""],
    [
        """Anfonwch e-bost at: techiaith@bangor.ac.uk""",
        """Anfonwch e-bost at: techiaith at bangor.ac.uk""",
    ],
    ["""Grêt, mi drïai hynny felly.""", """Grêt, mi drïai hynny felly."""],
    ["""Cymraeg / Welsh""", """Cymraeg / Welsh"""],
    ["""Hwre!""", """Hwre!"""],
    ["""Haha!""", """Haha!"""],
    ["""Da!""", """Da!"""],
    ["""Helo! Ti'n oce?""", """Helo! Ti'n oce?"""],
    ["""Iawn?""", """Iawn?"""],
    ["""Shwmae?""", """Shwmae?"""],
    ["""Sae moen e bennu nawr""", """Sae moen e bennu nawr"""],
    [
        """'Sdim ots pa bwysau y'f fi, ma'r struggle dal 'na.""",
        """'Sdim ots pa bwysau y'f fi, ma'r struggle dal 'na.""",
    ],
    ["""Paid""", """Paid"""],
    ["""Ar agor""", """Ar agor"""],
    ["""Safle ar gau""", """Safle ar gau"""],
    ["""Ffonia 999""", """Ffonia naw naw naw"""],
    ["""Wyt ti’n gwachad o?""", """Wyt ti’n gwachad o?"""],
    ["""Ti'n oce?""", """Ti'n oce?"""],
    [
        """Mae'r llawr gwaelod (ground floor) wedi'i labelu'n Lefel 0.""",
        """Mae'r llawr gwaelod (ground floor) wedi'i labelu'n Lefel dim.""",
    ],
    [
        """Mae bin olwynion du newydd yn costio £25.""",
        """Mae bin olwynion du newydd yn costio ddau ddeg pump punt.""",
    ],
    [
        """Treth Trafodiadau Tir: Dim treth ar brynu cartrefi am lai na £225,000.""",
        """Treth Trafodiadau Tir: Dim treth ar brynu cartrefi am lai na dau gant dau ddeg pum mil punt.""",
    ],
    ["""Y dyddiad yw'r 1af o Fawrth.""", """Y dyddiad yw'r cyntaf o Fawrth."""],
    [
        """Bydd Cymru’n herio Bosnia-Herzegovina yn Stadiwm Dinas Caerdydd ddydd Iau (Hydref 6) – gyda’r gic \
gyntaf am 7:15yb.""",
        """Bydd Cymru’n herio Bosnia-Herzegovina yn Stadiwm Dinas Caerdydd ddydd Iau (Hydref chwech) – gyda’r \
gic gyntaf am chwarter awr wedi saith y bore.""",
    ],
    [
        """“A fedrwn ni fod yn fwy gobeithiol na Saunders Lewis yn 1962? Yn sicr ni allwn fforddio anobeithio,” \
medd Dafydd Morgan Lewis, y golygydd.""",
        """“A fedrwn ni fod yn fwy gobeithiol na Saunders Lewis yn fil naw chwech dau? Yn sicr ni allwn fforddio \
anobeithio,” medd Dafydd Morgan Lewis, y golygydd.""",
    ],
    [
        """Neithiwr, roedd y tymheredd yn 20.5 gradd selsiws yn Aberporth yng Ngheredigion, gan dorri’r record \
flaenorol o 18.9 gradd selsiws yn y Rhyl yn 1949.""",
        """Neithiwr, roedd y tymheredd yn ugain pwynt pump gradd selsiws yn Aberporth yng Ngheredigion, gan \
dorri’r record flaenorol o un deg wyth pwynt naw gradd selsiws yn y Rhyl yn fil naw pedwar naw.""",
    ],
    [
        """Bydd y trên nesaf sy'n cyrraedd platfform 2 yn gadael am Sanclêr am 4:35yp.""",
        """Bydd y trên nesaf sy'n cyrraedd platfform dau yn gadael am Sanclêr am pump munud ar hugain i bump \
        y bore.""",
    ],
    [
        """Sefyllfa'r GIG 'ar ei waethaf' ers 25 mlynedd.""",
        """Sefyllfa'r GIG 'ar ei waethaf' ers dau ddeg pump mlynedd.""",
    ],
    [
        """Daw rhybudd undeb BMA Cymru wedi i weithiwr gwyno am brinder staff a \
morâl isel mewn un bwrdd iechyd.""",
        """Daw rhybudd undeb BMA Cymru wedi i weithiwr gwyno am brinder staff a \
morâl isel mewn un bwrdd iechyd.""",
    ],
    [
        """Gwynedd i ymgynghori ar dreth 300% ar ail gartrefi.""",
        """Gwynedd i ymgynghori ar dreth tri chant y cant ar ail gartrefi.""",
    ],
    [
        """'Sa ti 'di deutha fi pan o'n i'n wyth mlwydd oed fyswn i yn y Pafiliwn, yn 34, yn gwisgo ffrog a \
sodla' o flaen cynulleidfa o 2,000 bobl, fyswn i ddim 'di dy goelio di.""",
        """'Sa ti 'di deutha fi pan o'n i'n wyth mlwydd oed fyswn i yn y Pafiliwn, yn dri deg pedwar, yn gwisgo \
ffrog a sodla' o flaen cynulleidfa o ddwy fil bobl, fyswn i ddim 'di dy goelio di.""",
    ],
    [
        """Dywedodd Rebecca Evans, y Gweinidog Cyllid a Llywodraeth Leol: "Mae hwn yn newid sydd wedi ei deilwra \
i anghenion unigryw'r farchnad dai yng Nghymru ac mae'n cyfrannu at ein gweledigaeth ehangach o greu \
system drethi decach. "Ni fydd 61% o brynwyr tai yn gorfod talu treth. Bydd y newidiadau hyn yn rhoi \
cymorth i'r bobl sydd ei angen, ac yn helpu ag effaith y cynnydd mewn cyfraddau llog.""",
        """Dywedodd Rebecca Evans, y Gweinidog Cyllid a Llywodraeth Leol: "Mae hwn yn newid sydd wedi ei deilwra \
i anghenion unigryw'r farchnad dai yng Nghymru ac mae'n cyfrannu at ein gweledigaeth ehangach o greu \
system drethi decach. "Ni fydd chwe deg un y cant o brynwyr tai yn gorfod talu treth. Bydd y newidiadau \
hyn yn rhoi cymorth i'r bobl sydd ei angen, ac yn helpu ag effaith y cynnydd mewn cyfraddau llog.""",
    ],
    [
        """Yn ogystal, nid ydym yn argymell cymariaethau rhwng yr amcangyfrifon cysgu allan o'r casgliad misol \
hwn a'r cyfrif blynyddol o gysgu allan (hyd at fis Tachwedd 2019). Yn y casgliad misol hwn, gofynnir i \
awdurdodau lleol seilio eu hamcangyfrifon ar ddeallusrwydd lleol. Mae gan y cyfrif blynyddol o gysgu \
allan fethodoleg wahanol: ymarfer casglu gwybodaeth dwy wythnos, ac yna cyfrif ciplun un noson.""",
        """Yn ogystal, nid ydym yn argymell cymariaethau rhwng yr amcangyfrifon cysgu allan o'r casgliad misol \
hwn a'r cyfrif blynyddol o gysgu allan (hyd at fis Tachwedd dwy fil un deg naw). Yn y casgliad misol \
hwn, gofynnir i awdurdodau lleol seilio eu hamcangyfrifon ar ddeallusrwydd lleol. Mae gan y cyfrif \
blynyddol o gysgu allan fethodoleg wahanol: ymarfer casglu gwybodaeth dwy wythnos, ac yna cyfrif \
ciplun un noson.""",
    ],
    [
        """Nid i ni, O Arglwydd, nid i ni, Ond i’th enw dy hun, rho ogoniant, Er mwyn dy gariad a’th ffyddlondeb.\
Pam y mae’r cenhedloedd yn dweud, “Ble mae eu Duw?” Y mae ein Duw ni yn y nefoedd; Fe wna beth bynnag a\
ddymuna.""",
        """Nid i ni, O Arglwydd, nid i ni, Ond i’th enw dy hun, rho ogoniant, Er mwyn dy gariad a’th ffyddlondeb.\
Pam y mae’r cenhedloedd yn dweud, “Ble mae eu Duw?” Y mae ein Duw ni yn y nefoedd; Fe wna beth bynnag a\
ddymuna.""",
    ],
    [
        """Mae'r Mesur hwn, a basiwyd gan Gynulliad Cenedlaethol Cymru ar 7 Rhagfyr 2010 ac a gymeradwywyd gan Ei\
 Mawrhydi yn Ei Chyngor ar 9 Chwefror 2011, yn deddfu'r darpariaethau a ganlyn:""",
        """Mae'r Mesur hwn, a basiwyd gan Gynulliad Cenedlaethol Cymru ar seithfed Rhagfyr dwy fil a deg ac a\
 gymeradwywyd gan Ei Mawrhydi yn Ei Chyngor ar nawfed Chwefror dwy fil un deg un, yn deddfu'r\
 darpariaethau a ganlyn:""",
    ],
    ["""Helo a chroeso i'r podlediad Am Blant.""", """Helo a chroeso i'r podlediad Am Blant."""],
    ["""Oce, pnawn da pawb.""", """Oce, pnawn da pawb."""],
    [
        """So ma'r concept 'ma o lunia' a rhannu llunia' a bo’ 'na lun yn gallu mynd yn fyd-eang mewn eiliada' \
o'i dynnu de a bod ch'mod ffôns 'fo ansawdd da a ballu mae o, mae o'n frawychus mewn ffor'.""",
        """So ma'r concept 'ma o lunia' a rhannu llunia' a bo’ 'na lun yn gallu mynd yn fyd-eang mewn eiliada' \
o'i dynnu de a bod ch'mod ffôns 'fo ansawdd da a ballu mae o, mae o'n frawychus mewn ffor'.""",
    ],
    [
        """A dwi'n meddwl hefyd fel rhieni bo' gyno ni rei arferion ansaff bob mis Medi ma' pawb efo ma' 'na \
lot does ar hyd y cyfrynga’ cymdeithasol llunia' a'r Facebook o blentyn yn mynd i'r ysgol yn ei wisg \
ysgol, mae'r bathodyn ysgol yna.""",
        """A dwi'n meddwl hefyd fel rhieni bo' gyno ni rei arferion ansaff bob mis Medi ma' pawb efo ma' 'na \
lot does ar hyd y cyfrynga’ cymdeithasol llunia' a'r Facebook o blentyn yn mynd i'r ysgol yn ei wisg \
ysgol, mae'r bathodyn ysgol yna.""",
    ],
    [
        """Wel un o'r petha' efo ecsbloetiaeth un o'r prif nodweddion ecsbloetiaeth ydi bo' bobol ddim yn \
dalld bo' n'w'n ca'l i ecsbloetio a ddim yn 'im yn gw'bod bo' 'na rywun yn cymud mantais ohonyn n'w \
ac yn dadla' bron iawn i'r gwrthwyneb ma'i cariad a parch a ballu sy'n mynd ymlaen mewn ffor'.""",
        """Wel un o'r petha' efo ecsbloetiaeth un o'r prif nodweddion ecsbloetiaeth ydi bo' bobol ddim yn \
dalld bo' n'w'n ca'l i ecsbloetio a ddim yn 'im yn gw'bod bo' 'na rywun yn cymud mantais ohonyn n'w \
ac yn dadla' bron iawn i'r gwrthwyneb ma'i cariad a parch a ballu sy'n mynd ymlaen mewn ffor'.""",
    ],
    [
        """Be o'dd dy ymateb di i'r ffaith bod angen 'falla' i ni ail ystyried hawlia' plant yng ngoleuni'r \
COVID un deg naw?""",
        """Be o'dd dy ymateb di i'r ffaith bod angen 'falla' i ni ail ystyried hawlia' plant yng ngoleuni'r \
COVID un deg naw?""",
    ],
    [
        """Boneddigion a Boneddigesau, Bechgyn a Genethod, dowch yn llu! Mae atyniad newydd wedi cyrraedd \
Pen Y Pier... Y Syrcas! Ond nid syrcas arferol mo hon, o na!""",
        """Boneddigion a Boneddigesau, Bechgyn a Genethod, dowch yn llu! Mae atyniad newydd wedi cyrraedd \
Pen Y Pier... Y Syrcas! Ond nid syrcas arferol mo hon, o na!""",
    ],
    [
        """1: 1 tbsp Olew olewydd oil
        2: 1 Winwnsyn mawr, heb groen ac wedi ei dorri yn ddeisiauiced
        3: 2 Moronen, heb groen ac wedi eu torri yn ddeisiauunks
        4: 2 Brigyn o seleri, heb y diweddion ac wedi eu torri yn ddeisiauiced
        5: 2 Clof garlleg, heb groen ac wedi eu torri’n fânpped
        6: 200 kg Cnau castan (defnyddiwch y rhai mewn paced os ydy’n haws), wedi eu hanerughly
        7: 275 g (Hanner jar) o domatos heulsych, gyda’r olew wedi eu draenio ac wedi eu torritorn
        8: 2 Afal, wedi eu creiddio a’u torru yn ddeisiauunks""",
        """un: un tbsp Olew olewydd oil
        dau: un Winwnsyn mawr, heb groen ac wedi ei dorri yn ddeisiauiced
        tri: dau Moronen, heb groen ac wedi eu torri yn ddeisiauunks
        pedwar: dau Brigyn o seleri, heb y diweddion ac wedi eu torri yn ddeisiauiced
        pump: dau Clof garlleg, heb groen ac wedi eu torri’n fânpped
        chwech: dau gant kg Cnau castan (defnyddiwch y rhai mewn paced os ydy’n haws), wedi eu hanerughly
        saith: dau gant saith deg pump g (Hanner jar) o domatos heulsych, gyda’r olew wedi eu \
draenio ac wedi eu torritorn
        wyth: dau Afal, wedi eu creiddio a’u torru yn ddeisiauunks""",
    ],
    [
        """1af: 1 tbsp Olew olewydd oil
        2ail: 1 Winwnsyn mawr, heb groen ac wedi ei dorri yn ddeisiauiced
        3ydd: 2 Moronen, heb groen ac wedi eu torri yn ddeisiauunks
        4ydd: 2 Brigyn o seleri, heb y diweddion ac wedi eu torri yn ddeisiauiced
        5ed: 2 Clof garlleg, heb groen ac wedi eu torri’n fânpped
        6ed: 200 kg Cnau castan (defnyddiwch y rhai mewn paced os ydy’n haws), wedi eu hanerughly
        7fed: 275 g (Hanner jar) o domatos heulsych, gyda’r olew wedi eu draenio ac wedi eu torritorn
        8fed: 2 Afal, wedi eu creiddio a’u torru yn ddeisiauunks""",
        """cyntaf: un tbsp Olew olewydd oil
        ail: un Winwnsyn mawr, heb groen ac wedi ei dorri yn ddeisiauiced
        trydydd: dau Moronen, heb groen ac wedi eu torri yn ddeisiauunks
        pedwerydd: dau Brigyn o seleri, heb y diweddion ac wedi eu torri yn ddeisiauiced
        pumed: dau Clof garlleg, heb groen ac wedi eu torri’n fânpped
        chweched: dau gant kg Cnau castan (defnyddiwch y rhai mewn paced os ydy’n haws), wedi eu hanerughly
        seithfed: dau gant saith deg pump g (Hanner jar) o domatos heulsych, gyda’r olew wedi eu \
draenio ac wedi eu torritorn
        wythfed: dau Afal, wedi eu creiddio a’u torru yn ddeisiauunks""",
    ],
    ["mae gen i £200", "mae gen i ddau gan punt"],
    ["9/11/2024", "nawfed o Dachwedd dwy fil dau ddeg pedwar"],
    ["Dwi am fynd adref cyn 12", "Dwi am fynd adref cyn deuddeg"],
]

item_counting_phrases = [
    # MASC
    ["1 crys", "un crys"],
    ["2 grys", "dau grys"],
    ["3 chrys", "tri chrys"],
    ["4 crys", "pedwar crys"],
    # FEM
    ["1 glustog", "un glustog"],
    ["2 glustog", "dwy glustog"],
    ["2 gwmwl", "dau gwmwl"],
    ["2 gadair", "dwy gadair"],
    ["3 chwmwl", "tri chwmwl"],
    ["3 clustog", "tair clustog"],
    ["3 cadair", "tair cadair"],
    # ["4 chwmwl", "pedair chwmwl"],
    ["4 clustog", "pedair clustog"],
    ["4 cadair", "pedair cadair"],
    # NOUNS
    # ["5 ci", "pum ci"],
    # ["6 chi", "chwe chi"],
    # ["5 cath", "pum cath"],
    # ["6 chath", "chwe chath"],
    # ["100 cath", "can cath"]
]

lexically_mutated_numbers = [
    # SOFT
    ["dyma 2 gath", "dyma ddwy gath"],
    ["dyna 2 gath", "dyna ddwy gath"],
    ["wele 2 gath", "wele ddwy gath"],
    ["y 2 gath", "y ddwy gath"],
    ["neu 2 gath", "neu ddwy gath"],
    ["dy 2 gath", "dy ddwy gath"],
    ["ei 2 gath", "ei ddwy gath"],
    ["a'i 2 gath", "a'i ddwy gath"],
    ["i'w 2 gath", "i'w ddwy gath"],
    ["pa 2 gath?", "pa ddwy gath?"],
    ["sut 2 gath?", "sut ddwy gath?"],
    ["yn 2 gath", "yn ddwy gath"],  # PREDICATE ONLY - NOT AFTER PREPOSITION
    ["'n 2 gath", "'n ddwy gath"],  # PREDICATE ONLY - NOT AFTER PREPOSITION
    ["am 2 gath", "am ddwy gath"],
    ["ar 2 gath", "ar ddwy gath"],
    ["at 2 gath", "at ddwy gath"],
    ["dan 2 gath", "dan ddwy gath"],
    ["dros 2 gath", "dros ddwy gath"],
    ["drwy 2 gath", "drwy ddwy gath"],
    ["gan 2 gath", "gan ddwy gath"],
    ["heb 2 gath", "heb ddwy gath"],
    ["hyd 2 gath", "hyd ddwy gath"],
    ["o 2 gath", "o ddwy gath"],
    ["tros 2 gath", "tros ddwy gath"],
    ["trwy 2 gath", "trwy ddwy gath"],
    ["wrth 2 gath", "wrth ddwy gath"],
    # NASAL
    ["fy 2 gath", "fy nwy gath"],
    ["'y 2 gath", "'y nwy gath"],
    # ["yn 2 gath", "'yn nwy gath"],  # PREPOSITION ONLY - NOT AFTER PREDICATE
    # ASPIRATE
    ["gyda 3 cath", "gyda thair cath"],
    ["tua 3 cath", "tua thair cath"],
    # ["ei 3 cath", "ei thair cath"],
    # ["'i 3 cath", "'i thair cath"],
    # ["a 3 cath", "a thair cath"]
]

grammatically_mutated_numbers = [
    ["mae yna 2 gath", "mae yna ddwy gath"],
    [
        "cafodd 2 gath",
        "cafodd ddwy gath",
    ],  # etc. VERB + NUM = NUM MUTATES (SOFT) # not always necessary
]

tests = tests + item_counting_phrases + lexically_mutated_numbers + grammatically_mutated_numbers


def test_parser():
    for text in tests:
        result = parse_text(text[0])
        assert result == text[1]
