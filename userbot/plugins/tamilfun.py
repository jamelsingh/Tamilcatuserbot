""" Userbot module for having some fun with people. """
import asyncio
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import catub
from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "tacat"
SURID = bot.uid

plugin_category = "fun"


JOKE_STRINGS = [
   "Which is the only dancing animal? \n Yosinga! \n Theriyalaya? \n AADU..!",
   "500 rupees note la Ghandhi yen sirichitte irukkar ? A: Yenna Alutha nanainjudume !!!",
   "Bus mela nee earinaalum sari, un mela bus earinaalum sari, ticket vaanga poradhu nee dhan!",
   "Tea master evvalavu dhan lighta tea pottalum,adhula irundhu velicham adikkadhu.",
   "Ennadhan naaykku naalu kaal irundhalum, adhala kaal mela kaal pottu ukkara mudiyuma?",
   "Yaanai mela naama ukkandhu pona  Safari. , andha yaanai namma mela ukkandhu 'Oppari'.",
   "Kadal mela kappal pona Jolly, Kappal mela kadal pona Gaali.",
   "Oruthan evalavu dhan gunda irundhalum,avana thuppakki kulla poda mudiyaau.",
   "America naattu janadhipadhiyavae irundhalum, barber'ukku munnadi thala guninjhu dhan ukkaranum.",
   "Kaal evvaluvudhan vegama odunaalum, kaikkudhan prize kadaikkum",
   "Sirpi Kalla Uliyaala Adicha adhu “Kalai” Sirpiya Uliyaala Adicha adhu Kolai",
   "Mandaiya Potta Die \n Mandaila Potta Dye",
   "Bun mela thanni oothina enna aagum? \n Panneer agum!",
   "Sigathai paarthu payapadhada miriguam edhu? \n Innoru Singam!😂",
   "kangal pesinal KADHAL , kanneer pesinal NATPU, panam pesinal SONTHAM , ellarum pesinal ULAGAM , nee mattum pesinal LOOSU. HOW IS IT ????",
   "Bus stop kitta wait panna bus varum,But full stop kitta wait panna full varuma?",
   "oru kakka innoru kakkakita oru ragasiyam sollucham athu enna theriyuma? \n kaa kakka kaa kakka kaa kakka",
   "kasu irunda call taxi, \n kasu illina namma kaal than taxi.",
   "unkku oru maths test, \n aala mara ilai 607, \n arasa mara ilai 807 \n vepa mara ilai 89 kootina enna varum???\n ans: kuppa varum😜.",
   "mottaiku helmet podalam, aanal helmetuku mottai poda mudiyma",
   "Dosai mavula dosai sudalaam chapathi mavula chapathi sudalaam But, kadalai mavula kadalai suda mudiyuma",
   "Muttai(Egg) idatha Paravai(Bird) ethu.?? \n ans : Aan Pravai(Male Bird).",
   "Taj Mahal sollum Message enna? Sethum selavu vaippal kathali!",
   "Pathu roja poova paricha oru mullu kutha dhan seyyum. Adhapola 10 figare'kku route potta, oru seruppadi vaangi than aaganum. Kathal'la idhallem sagajamppa!",
   "Kappal aen aadi aadi pogudhu? Aenna adhu eppoludhum thanniyila irukku.",
   "Paal eppam vetkapadum? Adhoda  aadai ya edutha pinbu.",
   "professor - yenda 20 naala collegukku varala? student- enga appa eppavume solluvar  oru edathukku adikkadi pona mariyathai irukkathu'nu....",
   "Akka friend’a akkaava ninaikkalam, thangachi friend’a thangachiyaa ninaikalam but…. Pondatti frienda pondattiya ninaika mudiyuma?",
   "Bus'sa pinnala thalluna enna aagum? \n A: 'Pin'nnu valanju poiyidum.",
]

@catub.cat_cmd(pattern="joke$", command=("joke", plugin_category))
async def joke(e):
    txt = random.choice(JOKE_STRINGS)
    await edit_or_reply(e, txt)

ABUSE_STRINGS = [
   "Idhula enna perumai🤨",
   "Neennga nallavara kettavara?🤐",
   "Nee enna avlo periya Appatukera ah 😌?",
   "Nee Poi Love Sonna Paravala. Neeye Vedikathan Paarka Pora.🤣",
   "Sing in the rain .. I'm shoinng in the rain🤩..",
   "You mean wasteland 🙃...",
   "Manda bathiram.🤯..",
   "Sandai na satta kilya dhan seiyum.Sandaila kiliyatha satta enga iruku...😞",
   "Adhu eppdi da enna pathu andha kelvi kekalam?",
   "Policekar policekar enaku onnum theriyadhu policekar...😶",
   "Petromax light-ey thaan venuma?☺",
   "Ithu ulaga maga nadipuda saami..",
   "Ammu kutty, chella kutty, jaangri, boondhi, …",
   "Why blood same blood?😟",
   "Peasama poriya ila vaaikula kathiya vitu aatava?",
   "Valela poganda iyokiya rascals!🤕",
   "Vita kirukan aaikurvanga pola😬",
   "Sir ! Athu oru panaada kudatha idea Sir😳",
   "Yeanda eruma saaniya moonjila appinaa maadiriye thiriyura😛?",
   "Dei, Carpet mandaya🤠",
   "Dei tiffin box thalaya👻",
   "Dei sunnambu thalayaa💀",
   "Sathya Sodana😒",
   "Oh, Pichakaaranuku Security, Pichakaaraneeey",
   "nee vaangura indha paththu anju pichaiku, idhu thevathaanaa?",
   "Naalu Perukku Nallathunnaa  Ethuvume Thappilla",
    "Vera Vela Iruntha Paaruya",
    "Avar Enna Echakalai Egambaramnnu Ninaichiya",
    "Padikkaadha Muttalnnuthana Padichi Padichi Sonnen",
    "Ennaivida Adhigama Sambadhikkara Thimira",
    "Ni eallam rattam kakki tanda cava😡",
    "Mandaiya Udaichiruven Poya",
    "Pesurathai Paatha Ore Dialouge Ah Than Oorukkulla Sollikittu Thiriyira Polirukku",
    "Athukku Peru Than Dubakoor",
    "Intha Patha Vaangittu Oodi Poyidu",
    "Kevalam Oru Pichaikkaariyai Kooda Vittu Vaikkalaiya da",
    "Adapaavi Un Mogaraiyai Muzhusa Kooda Paakkalaiye Da",
    "Nee Varama Irukurathu Than Enakku Safety",
    "Unakallam coronavala than da savu 😂",
    "Ennada Arivu Ketta Thanama Pesikitu Irukka😶",
]

@catub.cat_cmd(pattern="tabuse$", command=("tabuse", plugin_category))
async def tabuse(e):
    txt = random.choice(ABUSE_STRINGS)
    await edit_or_reply(e, txt)
        
SINGING_STRINGS = [
   "🎙Unna nenachu nenachu urugi poenen mezhuga nenja odhachu odhachu parandhu ponaa azhagaa🎶",
   "🎙Life is very short nanba Always be happy Palavidha problems will come and go Konjam chill pannu maappi🎶 ",
   "🎙Varayo Varayo Kadhal Kolla Poovodu Pesadha Katru Illa Ean Indha Kadhalum Netru Illa Neeye Sol Maname🎶",
   "🎙Urugudhe Marugudhe Ore Parvaiyale Uzhagame Suzhaludhe Unnai Parthathale Thangam Urugutha Angam Karaiyutha Vetkam Udaiyutha Mutham Thodarutha 🎶",
   "🎙Ennakku Breakup, Adhula En Thappu, Edhuvum Illainaley, Enna Villanaley, Enakku Shock Adichu,Adhula Heart Veduchu, Karugi Poiruchu, Poda Goyaley,🎶",
   "🎙Venmathi Venmathiye Nillu, Nee Vanukka Maegathukka Sollu, Vanamtham Unnudaiya Ishtam Enral, Megathukillai Oru Nashtam,🎶",
   "🎙Yengayo Vikkudhu, Yennamo Sikkudhu Kitt Nee Vandhuta Yedhedho Kolaru, Status Single-u Ready To Mingle-u  Love-u Nu Vandhuta Full Time Nee Paru.🎶",
   "🎙Thodu vaanam thodugindra neram Tholaivinil pogum Ada tholainthume pogum Thodu vaanamaai pakkam aagiraai Thodum podhile thoalivaagiraai🎶",
   "🎙Anal Mele Pani Thuli Alaipaayum Oru Kili Maram Thedum Mazhai Thuli Ivaithaane Ival Ini Imai Irandum Thani Thani Urakkangal Urai Pani Etharkaaga Thadai Ini..🎶",
   "🎙Chittu Kuruvi Ondru Snega Paarvai Kondu Vatta Paaraiyin Mel Ennai Vaa Vaa Endrathu Keechu Keech Endrathu Kitta Vaa Endrathu Pechu Yethumindri Piriyama Endrathu🎶",
   "🎙Naan Un Azhaginile Deivam Unarugiren Unthan Aruginile Ennai Unarugiren Ennil inaiya Unnai Adaiya Enna Thavangal Seitheno Nenjam Irandum Korthu Nadanthu Konjum Ulagai Kaanbom Kadhal Oliyil Kaala Veliyil Kaalgal Pathiththu Povom🎶 ",
   "🎙Vennilave Vennilavey Vinnai Thaandi Varuvaaya Vilaiyaada Jodi Thevai Intha Bhoologaththil Yarum Paarkkum Munne Unnai Athikaalai Anuppi Vaippom🎶 ",
   "🎙 Ennai Pirinthaai Uyire Uyire Kanneeril Urainthaai Kanave.. Iravum En Pagalum Un Vizhiyin Oram Pookindrathey Uthirum En Uyirum Un Oru Sol Thedi Alaigindrathey Ennaanatho En Kaadhale Man Thaagam Theerum Mazhaiyile..🎶 ",
   "🎙 Idhayam Ketkum Kaadhalukku Ver Edhaiyum Kettida Theriyathu Anbai Ketkum Kadhalukku Sandhegam Thaangida Mudiyathu Medum Pallam illamal Oru Paadhai Ingu Kidaiyathu🎶 ",
   " 🎶Nilavidam Vaadagai Vaangi Vizhi Veettinil Kudi Vaikkalaama Naam Vaazhum Veetukul Veraarum Vanthaale Thaguma🎙 ",
   "🎙Adi Karuppu Nerathazhagi Udhattu SivappazhagiSillaraya Sedharittendi Un Sirippil Sillaraya Sedharitten Di🎶 ",
   "🎙Thoovaanam Thoova Thoova Mazhaithuligalil Unnaikanden En Meley Eeramaaga Uyir Karaivadhai Naaney Kanden Kadavul Varangal Tharum Pala Kadhai Ketten Avarey Varamaai Varuvadhai Ingu Paarthen Veru Enna Vendum Vaazhvil🎶 ",
   "🎙Enakku Ippo Kalyaana Vayasu Thaan Vanthuruchu Di Date Pannavaa illa Chat Pannavaa Unkuda Senthu Vaazha Aasaithaan Vanthuduchchu di Meet Pannavaa illa Wait Pannavaa🎶 ",
   "🎙Ada Kadhal Enbathu Maayavalai Sikkaamal Ponavan Yaarumillai Sidhaiyaamal Vaazhum Vaazhkaiye Thevai illai Thevai Illai🎶 ",
   "🎙Verethuvum Thevai illai Nee Mattum Podhum Kannil Vaithu Kaathiruppen Ennavanaalum Un Ethiril Naan Irukkum Ovvoru Naalum Uchchi Mudhal Paadham Varai Veesuthu Vaasam🎶 ",
]

@catub.cat_cmd(pattern="tsing$", command=("tsing", plugin_category))
async def tsing(e):
    txt = random.choice(SINGING_STRINGS)
    await edit_or_reply(e, txt)

TAMQUOTES_STRINGS = [
  "நிம்மதியாக இருக்கும் வயதில் மனைவியைத் தேடுவதும், மனைவி வந்தப்பின் நிம்மதியைத் தேடுவதுமே..  ஆண்களின் வாழ்க்கை தேடல்..",
  "அழகை பற்றிக் கவிதை எழுத சொன்னார்கள்! நான் உன்னை பற்றி எழுதினேன்!.. அடி பின்னிடாங்க!!!",
  "ஆண்பாலாக பிறந்ததற்கு பதில் ஆவின் பாலாக பிறந்திருந்தால் மனைவிக்கு முன் தைரியமாக பொங்கியிருக்கலாம்!",
  "உன்னை யாரும் காதலிக்கவில்லை  என்று கவலைப்பட வேண்டாம்.. அது உன் வருங்கால மனைவியின் வேண்டுதலாகக் கூட இருக்கலாம்..",
  "வீட்ல ஃப்ரிட்ஜ் வாங்கின பிறகு, தினமும் நான்கு வகையான சட்னி கிடைக்குது..  காலைல வச்சது, நேற்று வச்சது, முந்தாநாள் வச்சது...!",
  "யோசிச்சுப்பாத்தா, இந்த யோசிக்கிற பழக்கம்தான் எல்லா பிரச்சனைக்கும் காரணம்னு தோணுது...",
  "அதிகாலையில் கஷ்டப்பட்டு எந்திரிச்சு கூவுறது சேவல். பேரு வாங்குறது கோழி.. \n கோழி கூவுது !! \n ஆண் பாவம்",
  "இந்தியாவின் அனைத்து நதிகளுக்கும் பெண்கள் பெயரை வைத்துவிட்டு இணை என்றால், நதிகள் எப்படி இணையும்..!!",
  "இதுவும் கடந்து போகும்னு எனக்கு தெரியும்.. ஆனா இது ஏன் இவ்வளவு மெதுவா நடந்து போகுதுங்கிறது தான் பிரச்சனையே..!!",
  "மனநிறைவு என்பது இயற்கையாகவே நம்மிடம் உள்ள செல்வம்.ஆடம்பரம் என்பது நாமே தேடிக்கொள்ளும் வறுமை.",
  "இசையை ரசிக்கத் தெரிந்தவர்கள் வாழ்க்கையையும் ரசிக்கத் தெரிந்தவர்களாகவே இருப்பார்கள்.",
  "உங்கள் மனம் அழகானதாக இருந்தால் நீங்கள் காணும் காட்சிகளும் அழகாகவே இருக்கும்.",
  "எதையும் மன்னிக்கும் ஒரே நீதிமன்றம் தாயின் இதயம் மட்டுமே.",
  "சித்தாந்தம் தோற்றுப்போன இடத்தில் வேதாந்தம் தானே கை கொடுக்கிறது?",
  "ஊரிலே சாக்கடை என்பது மோசமான பகுதி தான், ஆனால் அப்படியொன்று இல்லாவிட்டால் ஊரே சாக்கடையாகி விடாதா?",
  "அறிவாளிகளுக்கு அறிவு அதிகம், முட்டாள்களுக்கு அனுபவம் அதிகம்.",
  "நீயாகவே முடிவு செய். நீயாகவே செயல் படு.முடிந்தால் நன்மை செய்.",
  "கேட்கும் போது சிரிப்பு வரவேண்டும். சிந்தித்து பார்த்தால் அழுகை வரவேண்டும் அதுதான் நல்ல நகைச்சுவை.",
  "நல்லதே நினை, நல்லதே பேசு, நல்லதே கேள், நல்லதே நடக்கும்.",
  "இருப்பது ஒரு பிடி அன்னமானாலும் தனக்கென இல்லது பிள்ளைக்கு ஊட்டி மகிழ்பவளே தாய்",
  "யாருக்காகவும் உன்னை மாற்றி கொள்ளாதே, ஒரு வேளை மாற நினைத்தால் , ஒவ்வொரு மனிதர்களுக்காகவும் நீ மாற வேண்டி இருக்கும்.",
  "அளவுக்கு மிஞ்சிய சாமர்த்தியம் முட்டாள் தனத்தில்தான் முடியும்.",
  "நீ உன் சிறகை விரிக்கும் வரை நீ எட்டும் உயரம் யாரறிவார்?",
  "உங்கள் குறைகளை நீங்களே அடையாளம் கண்டுகொள்வதுதான் வளர்ச்சியின் அடையாளம்.",
  "எதிரியை வெல்வதைவிட அவனைபுரிந்துகொள்வதே மேல்.",
  "அளவிள்ளாத வேதனைகளை தாங்கிக்கொண்டு சாதனை படைக்கிறவன்தான் மேதை.",
  "மனைவி இறந்தற்காக கணவன் கட்டிய வெள்ளை புடவை தாஜ்மகால்",
]

@catub.cat_cmd(pattern="tquotes$", command=("tquotes", plugin_category))
async def tquotes(e):
    txt = random.choice(TAMQUOTES_STRINGS)
    await edit_or_reply(e, txt)

POEM_STRINGS = [
  "யார்சூட மலர்ந்திருக்கின்றன விண்வெளித் தோட்டத்தில் நட்சத்திரப் பூக்கள்...!",
  "விட்டு விட்டு தான் நினைக்கிறேன்...\n விட்டு விட தான் நினைக்கிறேன்... \n ஆனாலும் என் விரல் பிடித்தே வருகிறது...\n உன் அழகான நினைவுகள்...",
  "இதழ் என்னும் மலர் கொண்டு கடிதங்கள் வரைந்தாய்.பதில் நானும் தரும் முன்பே.கனவாகி கலைந்தாய்...!",
  "நீ நடந்த பாதைகளில் நானும் நடக்கிறேன். நம் காதல் தான் ஒன்று சேரவில்லை.நம் கால் தடங்களாவது ஒன்று சேரட்டும்...!",
  "உன் முந்தானையில் ஒரு முகக்கவசம் கொடு. ஆயுள் முழுவதும்  வாழ்கிறேன் ஆக்ஸிஜன் இன்றி..",
  "அழகிய பொம்மை என நினைத்து கண் சிமிட்டாமல் பார்த்து கொண்டிருந்தேன். நீ கண் சிமிட்டிய நொடியில் கண் சிமிட்டா பொம்மையானேன் நான்...!",
  "உனக்கான இதயம் உன்னை ஒருபோதும் மறக்காது அப்படி மறந்தால் அது உனக்கான இதயமாக இருக்காது...!",
  "நினைவுகள் பல சுமக்கும் இதயம்.கனவுகள் பல காணும் மனது..நீங்காமல் அலை மோதும் நினைவு...உயிர் பிரிந்தாலும் பிரியாது உன் நினைவு",
  "ஒரு பூவாக நீ மலர்கிறாய்...ஒரு வண்டு போல் நான் நுழைகின்றேன். தேன் தேடும் வண்டுகள் போல் நான் இல்லை...நீ சம்மதம் சொல்லும் வரை...",
  "நீ நிலவும் இல்லை நட்சத்திரமும் இல்லை.இவைகளை எல்லாம் அள்ளி சூடிக்கொள்ளும் வானம் நீ...!!",
  "உன்னை உண்மையாக நேசித்த இதயத்தை விட்டு பிரிந்து விடாதே. எத்தனை இதயங்கள் உன்னை நேசித்தாலும்.அந்த ஒரு இதயம் போல் ஆகாது...",
  "உன்னை சிறைபிடிக்க நினைத்து நான் கைதி ஆனேன் உன்னிடம்.",
  "உன் கரம் பிடித்து, என் கனவுகளை நிஜமாக்கி, வாழ்ந்து மடிவதற்கு, போதாதடி இந்த ஒர் ஜென்மம். மீண்டும் ஜனனம் இருந்தால்! நீயே வேண்டும். என் உயிராக..!",
  "பக்கத்தில் நீயும் இல்லை பாவிமனம் ஏங்குதடி. வானத்தில் நீயும் நின்றால் பார்க்க விழி உயருதடி. உச்சத்தில் நீயும் வந்தாய் எந்தன் உள்ளம் ரசிக்குதடி. வெக்கத்தில் நீயும் சென்றாய் என் சின்ன இதயம் தவிக்குதடி",
  "அழகியே என் இதயத்தின் அரசியே! நீ ஆணையிட்டால் போதும், வாழ்நாள் முழுவதும் நான் உன் அடிமை என்று எழுதி தருகிறேன்.",
  "ஒரு நிமிடம் கண்களை மூடு. ஏன்? மூட சொல்கிறாய்? மூடு சொல்கிறேன். சரி மூடியாச்சு. இப்போ ஏதாவது தெரிகிறதா? இல்லை. நீ இல்லாமல் என் வாழ்வும் அப்படித்தான்",
  "அடி என்னவளே! ஏழு ஜென்மம் வாழும் ஆசையெல்லாம் இல்லையடி எனக்கு. ஓர் ஜென்மம் வாழ்ந்தாலும் அது உன்னுடன் வாழவேண்டும். அவ்வளவு தான்",
  "நீ என்னை கண்டதும் முகத்தை இருக்கமாக வைத்திருந்தாலும், என் உளவாளியான உன் கண்கள் உன் காதலை என்னிடம் சொல்லி விடுகிறது என் இனியவளே👁️👁️!",
  "புவி அசைவில் கூட தடுமாறாத நான் உன் விழி அசைவில் தடுமாறி இடம்மாறி மொத்தமாய் சாய்ந்தேனடி.",
  "என்னை பிடிக்கவில்லை என்றே சொல்லி இருக்கலாம் நீ. பிடித்திருக்கிறது என்று சொல்லி பார்க்கவும் முடியாமல் பேசவும் முடியாமல் பித்துபிடிக்க வைத்து விட்டாயடி.",
  "நீ மட்டும் போதும் என முடிவு செய்து விட்டேனடி. இனி எதை இழந்தாலும் உன்னை இழப்பதாய் இல்லை.",
  "உன்னை நினைத்து நான் எழுதும் கவிதைகள் எல்லாம் வெறும் கவிதைகள் அல்ல. நாம் காதல் கொண்டு, ஊடலும், கூடலும் இல்லாமல் பிறந்த குழந்தைகள், என் கவிதைகள்",
  "நினைவுகள் சுகமானது என்பது அனைவருக்கும் தெரியும். ஆனால்! அது கனமான ரணமானது என்பது சுமப்பவர்க்கு மட்டுமே தெரியும்.",
  "கை அளவு இதயம் தான். அதில் கடல் அளவு உன் நினைவுகள்...சுமையாக அல்ல... சுகமாக.",
  "அன்பு என்பது ஆகாயம் போன்றது! அதன் உச்சத்தை ஆரவாரமின்றி தொட்டவர் அம்மா  உழைப்பு என்பது கடல் போன்றது! அதன் ஆழத்தை அச்சமின்றி தொட்டவர் அப்பா! ",
  "இந்த உலகத்தில் கலப்படம் இல்லாதது எதுவென்றால்! அது தாய்ப்பாலும், தாய் பாசமும் மட்டும் தான்.!",
  "தாயைப் போல் ஒரு உறவினை தரணி எங்கும் தேடினும் கிடைத்திடுமோ! இவள் தேவதையின் மறுவடிவமன்றோ",
  "கடல் அலைக்கு எல்லை உண்டு. தாய் அன்புக்கு எல்லை உண்டோ! தாய் மடி தந்த சுகம் வேறொரு மடி தருமோ!",
  "தன்னலம் விரும்பி வாழும் உலகில், என் நலம் விரும்பி வாழும் ஓர் உயிர் 'அம்மா'.",
  "அருகில் இருக்கும் போதே அள்ளிக்கொள். தொலைந்து போன பின் தேடாதே. அது மீண்டும் கிடைக்காத பொக்கிஷம்.அன்னையின் அன்பு...!",
  "துயரம் என்பது உன்னை சிதைக்க வருவதல்ல! உன்னை சுற்றி உள்ள போலி முகங்களின் முகத்திரையை கிழிக்க வருவது! ",
  "எதிரியை காலம் கடந்தால் கூட மன்னித்து விடு. ஆனால் துரோகியை காலம் கடத்தாமல் துண்டித்து விடு. ",
]

@catub.cat_cmd(pattern="tpoem$", command=("tpoem", plugin_category))
async def tporm(e):
    txt = random.choice(TAMQUOTES_STRINGS)
    await edit_or_reply(e, txt)

SLAP_TEMPLATES = [
    "[{user1}](tg://user?id={SURID}) kalaaitathil {victim}  vanthi, peathi yai vanthulathu 🤮💩😪🤣 .",
    "[{user1}](tg://user?id={SURID}) kalaaithathal {victim} kanathil palar eana arainthullar🤢🤮 .",
    "️[{user1}](tg://user?id={SURID}) aluke pona thakkali ,muttaiyai kondu {victim} thalaiyel earinthaar 🤭😜.",
    "[{user1}](tg://user?id={SURID}) ️kaallai vari vetu {victim} keelai vilunthu, meesaiyel man otechi 🤓☹️",
    "️[{user1}](tg://user?id={SURID}) in girl friend  ammi kall aal {victim} in thalaiyai pilanthar 😱😱🤭 .",
    "[{user1}](tg://user?id={SURID}) {victim} ai kupetu kenathil thalli potar 🤗🤗😝 .",
    "️[{user1}](tg://user?id={SURID}) kakathai kupettu {victim} thalaiyil ka ga poka vaithar 😝🤣 .",
    "[{user1}](tg://user?id={SURID}) {victim} disturb pannathala mungilayai mithithar 😂😜 .",
    "[{user1}](tg://user?id={SURID}) {victim} Vidamal adithyhil {victim} nak-out aanar 🤭😜.",
    "️[{user1}](tg://user?id={SURID}) நாயை விட்டு {victim} கன்னத்தை கடிக்க வைத்தார்🤭🤣.",
    "[{user1}](tg://user?id={SURID}) சானியை  {victim} முகத்தில் அடித்தார்🤣🤣😛.",
    "️[{user1}](tg://user?id={SURID}) adithathil moolai kulambi poi {victim} mentel aanar 😂😂😛.",
    "[{user1}](tg://user?id={SURID}) {victim} kannai noondi valiyai eaduthar 😳🤭😜",
    "[{user1}](tg://user?id={SURID}) ஐ பார்த்து {victim} பயந்து ஓடி போய்ட்டார்🤭🤭😜",
]

@catub.cat_cmd(
    pattern="tslap(?:\s|$)([\s\S]*)",
    command=("tslap", plugin_category),
    info={
        "header": "To slap a person with random objects !!",
        "usage": "{tr}slap reply/username>",
    },
)
async def who(event):
    "To slap a person with random objects !!"
    replied_user = await get_user(event)
    if replied_user is None:
        return
    caption = await slap(replied_user, event)
    try:
        await edit_or_reply(event, caption)
    except BaseException:
        await edit_or_reply(
            event, "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None
    return replied_user


async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)

    caption = temp.format(user1=DEFAULTUSER, victim=slapped, SURID=SURID)

    return caption


