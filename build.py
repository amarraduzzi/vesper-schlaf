import os
MAIN="https://molitademo1.pages.dev"
B="https://vesper-schlaf.ch"
LANGS=["de","fr","it"]
GO={"de":"Weiter entdecken →","fr":"Aller plus loin →","it":"Vai oltre →"}
MORE={"de":"Mehr zum Thema","fr":"En savoir plus","it":"Approfondisci"}
def L(l,place,label=None,cls="xl"):
    return f'<a class="{cls}" href="{MAIN}/?utm_source=vesper&amp;utm_medium={l}&amp;utm_content={place}" rel="noopener">{label or MORE[l]}</a>'

T={
"de":dict(
 title="Vesper – Schlaf, ruhig erklärt",desc="Schlafrechner, Schlaftyp-Check und klare Fakten rund um Schlaf, Rhythmus und Abendroutine.",
 nav=["Schlafrechner","Schlaftyp","Abendritual","Mythen"],home="Startseite",
 eb="Schlaf, ruhig erklärt",h="Gute Nächte <em>beginnen am Abend</em>",p="Rechner, kleine Tests und klare Fakten rund um Schlaf, Rhythmus und Abendroutine. Ohne Druck, ohne Versprechen.",b1="Schlafrechner öffnen",
 calc=dict(k="Schlafrechner",h="Wann ins Bett, <em>wann aufstehen</em>?",p="Ein Schlafzyklus dauert ungefähr 90 Minuten. Der Rechner zeigt dazu passende Zeiten, plus rund 15 Minuten zum Einschlafen.",t=["Ich muss aufstehen um","Ich gehe ins Bett um"],r=["Ins Bett um","Aufstehen um"],cyc="Zyklen",hr="Std.",note="Richtwerte: Jeder Mensch schläft ein wenig anders."),
 pano="Wenn der Tag leiser wird.",
 ck=dict(k="Dein Schlaftyp",h="Lerche, Taube <em>oder Eule</em>?",p="Drei kurze Fragen, keine Bewertung: ein Überblick über deinen natürlichen Rhythmus.",of="Frage",
  q=[("Wann würdest du an freien Tagen von selbst müde?",["Früh am Abend","Gegen Mitternacht","Spät in der Nacht"]),("Wann bist du am wachsten?",["Am Morgen","Um die Mittagszeit","Am Abend"]),("Wie fühlt sich der Wecker an?",["Kein Problem","Geht so","Eher schwierig"])],
  r={"lark":("Die Lerche","Du bist früh wach und früh müde. Dein Tag funktioniert am besten mit frühen Terminen; abends darfst du früh herunterfahren."),"dove":("Die Taube","Du liegst in der Mitte: Du passt dich gut an frühe wie späte Tage an. Feste Zeiten helfen trotzdem, im Takt zu bleiben."),"owl":("Die Eule","Dein Tag kommt später in Schwung und klingt abends auf. Tageslicht am Morgen kann helfen, den Rhythmus bewusst zu verschieben.")},art="Passend dazu:",again="Nochmal"),
 rt=dict(k="Dein Abendritual",h="Baue dir <em>deinen Abend</em>",p="Tippe auf alles, was du gern vor dem Schlafen tust, und sieh, wie der Mond voller wird.",u="Rituale",
  i=["Bildschirm weglegen","Licht dimmen","Zimmer lüften","Warmen Tee trinken","Ein paar Seiten lesen","Sanft dehnen","Ruhig atmen","Morgen-Liste schreiben"],
  m=["Noch ist es Tag. Tippe auf etwas.","Ein Anfang. Der Abend wird ruhiger.","Schon ein Ritual: so beginnt ein klarer Übergang.","Fast Vollmond. Das ist ein runder Abend.","Voller Mond: dein Abend ist bereit."]),
 my=dict(k="Mythos oder Fakt?",h="Vier Aussagen, <em>kurz geprüft</em>",p="Tippe auf eine Karte und dreh sie um.",v=("Mythos","Fakt"),tap="Umdrehen",c=[
  ("Alle Menschen brauchen genau acht Stunden Schlaf.",0,"Der Bedarf ist individuell. Bei Erwachsenen gelten oft sieben bis neun Stunden als Orientierung, aber nicht für jeden."),
  ("Ein Glas Wein am Abend verbessert den Schlaf.",0,"Alkohol kann das Einschlafen erleichtern, macht den Schlaf aber meist leichter und unruhiger."),
  ("Ein dunkles, eher kühles Zimmer unterstützt den Schlaf.",1,"Dunkelheit und angenehme Kühle gehören zu den am häufigsten genannten Grundlagen guter Schlafbedingungen."),
  ("Feste Schlafenszeiten helfen dem inneren Rhythmus.",1,"Wer meist zu ähnlichen Zeiten schläft und aufsteht, gibt dem Körper einen klaren Takt vor.")]),
 fq=dict(k="Fragen",h="Kurz <em>beantwortet</em>",c=[
  ("Wie viel Schlaf braucht man?","Das ist individuell. Bei Erwachsenen werden oft sieben bis neun Stunden als Orientierung genannt. Entscheidend ist, wie erholt du dich im Alltag fühlst."),
  ("Was ist ein Schlafzyklus?","Eine Nacht besteht aus mehreren Durchgängen von leichtem Schlaf, Tiefschlaf und Traumschlaf. Ein Durchgang dauert ungefähr 90 Minuten, mit Abweichungen von Nacht zu Nacht."),
  ("Ist ein Mittagsschlaf sinnvoll?","Ein kurzes Nickerchen von rund 20 Minuten empfinden viele als erfrischend. Später am Tag kann es das Einschlafen am Abend nach hinten schieben."),
  ("Wann sollte ich ärztlichen Rat suchen?","Wenn du über längere Zeit schlecht schläfst oder tagsüber stark müde bist, sprich mit einer Ärztin oder einem Arzt. Diese Seite gibt allgemeine Informationen und ersetzt keine Beratung.")]),
 tz=dict(k="Zum Weiterlesen",go="Artikel lesen →"),
 foot="Vesper – Schlaf, ruhig erklärt.",dis="Allgemeine Informationen, keine medizinische Beratung.",
 art=dict(slug="abendroutine-einschlafen",title="Die Abendroutine: Wie aus dem Abend eine Nacht wird",lede="Gut schlafen beginnt nicht im Bett, sondern Stunden davor. Ein Überblick über Licht, Rhythmus und kleine Rituale.",
  s=[("Licht ist der Taktgeber","Helles, kühles Licht am Abend sagt dem Körper: noch Tag. Gedimmtes, warmes Licht hilft beim Herunterfahren. Umgekehrt stützt Tageslicht am Morgen den Rhythmus, auch an bewölkten Tagen."),
     ("Rhythmus schlägt Perfektion","Es kommt weniger auf die perfekte Nacht an als auf Regelmäßigkeit. Wer zu ähnlichen Zeiten schlafen geht und aufsteht, gibt dem Körper Orientierung. Am Wochenende hilft es, die Abweichung klein zu halten."),
     ("Kleine Rituale, klarer Übergang","Eine ähnliche Reihenfolge jeden Abend wirkt wie ein Signal: gleich ist Schlafenszeit. Das kann Lesen sein, sanftes Dehnen, ruhiges Atmen oder eine kurze Liste für morgen, damit die Gedanken nicht weiterkreisen.")],
  ch="Dein Abend in fünf Punkten",ci=["Bildschirme eine Weile vor dem Schlafen weglegen","Zimmer abdunkeln und eher kühl halten","Jeden Abend eine ähnliche Reihenfolge","Letzte Mahlzeit nicht zu spät und nicht zu schwer","Morgens Tageslicht tanken"],
  done="Alles abgehakt. Gute Nacht, und mehr dazu hier:",rel="Weiterlesen",fine="Hinweis: Dieser Text gibt allgemeine Informationen und ersetzt keine ärztliche Beratung. Wenn Schlafprobleme länger anhalten, sprich mit einer Ärztin oder einem Arzt.")),
"fr":dict(
 title="Vesper – Le sommeil, expliqué calmement",desc="Calculateur de sommeil, test de profil et repères clairs sur le sommeil, le rythme et la routine du soir.",
 nav=["Calculateur","Profil","Rituel du soir","Mythes"],home="Accueil",
 eb="Le sommeil, expliqué calmement",h="Les bonnes nuits <em>commencent le soir</em>",p="Calculateur, petits tests et repères clairs sur le sommeil, le rythme et la routine du soir. Sans pression, sans promesse.",b1="Ouvrir le calculateur",
 calc=dict(k="Calculateur de sommeil",h="Se coucher quand, <em>se lever quand</em> ?",p="Un cycle de sommeil dure environ 90 minutes. Le calculateur propose des heures adaptées, avec environ 15 minutes pour s’endormir.",t=["Je dois me lever à","Je me couche à"],r=["Se coucher à","Se lever à"],cyc="cycles",hr="h",note="Repères indicatifs : chaque personne dort un peu différemment."),
 pano="Quand le jour se fait plus doux.",
 ck=dict(k="Votre profil de sommeil",h="Alouette, colombe <em>ou chouette</em> ?",p="Trois courtes questions, sans jugement : un aperçu de votre rythme naturel.",of="Question",
  q=[("Quand auriez-vous sommeil de vous-même un jour de repos ?",["Tôt le soir","Vers minuit","Tard dans la nuit"]),("Quand êtes-vous le plus alerte ?",["Le matin","En milieu de journée","Le soir"]),("Comment vivez-vous le réveil ?",["Sans problème","Moyennement","Plutôt difficilement"])],
  r={"lark":("L’alouette","Vous êtes tôt réveillé et tôt fatigué. Votre journée fonctionne mieux avec des rendez-vous matinaux ; le soir, vous pouvez ralentir tôt."),"dove":("La colombe","Vous êtes au milieu : vous vous adaptez bien aux journées tôt comme tard. Des horaires fixes aident quand même à garder le rythme."),"owl":("La chouette","Votre journée démarre plus tard et s’anime le soir. La lumière du jour le matin peut aider à décaler volontairement le rythme.")},art="À lire aussi :",again="Recommencer"),
 rt=dict(k="Votre rituel du soir",h="Composez <em>votre soirée</em>",p="Touchez tout ce que vous aimez faire avant de dormir et regardez la lune se remplir.",u="rituels",
  i=["Poser l’écran","Baisser la lumière","Aérer la chambre","Boire une tisane chaude","Lire quelques pages","S’étirer doucement","Respirer calmement","Écrire la liste de demain"],
  m=["Il fait encore jour. Touchez quelque chose.","Un début. La soirée devient plus calme.","Déjà un rituel : une transition claire s’installe.","Presque pleine lune. Une soirée bien arrondie.","Pleine lune : votre soirée est prête."]),
 my=dict(k="Mythe ou fait ?",h="Quatre affirmations, <em>vite vérifiées</em>",p="Touchez une carte pour la retourner.",v=("Mythe","Fait"),tap="Retourner",c=[
  ("Tout le monde a besoin d’exactement huit heures de sommeil.",0,"Le besoin est individuel. Chez l’adulte, on cite souvent sept à neuf heures comme repère, mais pas pour tout le monde."),
  ("Un verre de vin le soir améliore le sommeil.",0,"L’alcool peut faciliter l’endormissement, mais rend généralement le sommeil plus léger et plus agité."),
  ("Une chambre sombre et plutôt fraîche favorise le sommeil.",1,"L’obscurité et une fraîcheur agréable comptent parmi les bases les plus souvent citées pour bien dormir."),
  ("Des heures de coucher régulières aident le rythme interne.",1,"Dormir et se lever à des heures similaires donne au corps un tempo clair.")]),
 fq=dict(k="Questions",h="Brièvement <em>répondu</em>",c=[
  ("De combien de sommeil a-t-on besoin ?","C’est individuel. Chez l’adulte, on cite souvent sept à neuf heures comme repère. L’essentiel est de savoir comment vous vous sentez reposé au quotidien."),
  ("Qu’est-ce qu’un cycle de sommeil ?","Une nuit se compose de plusieurs passages entre sommeil léger, sommeil profond et sommeil paradoxal. Un passage dure environ 90 minutes, avec des écarts d’une nuit à l’autre."),
  ("La sieste est-elle utile ?","Une courte sieste d’environ 20 minutes est jugée reposante par beaucoup. Plus tard dans la journée, elle peut retarder l’endormissement du soir."),
  ("Quand demander un avis médical ?","Si vous dormez mal pendant longtemps ou êtes très fatigué en journée, parlez-en à un médecin. Ce site donne des informations générales et ne remplace pas un conseil médical.")]),
 tz=dict(k="À lire",go="Lire l’article →"),
 foot="Vesper – Le sommeil, expliqué calmement.",dis="Informations générales, pas de conseil médical.",
 art=dict(slug="routine-du-soir",title="La routine du soir : comment la soirée devient nuit",lede="Bien dormir ne commence pas au lit, mais des heures avant. Un aperçu de la lumière, du rythme et des petits rituels.",
  s=[("La lumière donne le tempo","Une lumière vive et froide le soir dit au corps : il fait encore jour. Une lumière tamisée et chaude aide à ralentir. À l’inverse, la lumière du jour le matin soutient le rythme, même par temps couvert."),
     ("Le rythme avant la perfection","Ce n’est pas la nuit parfaite qui compte, mais la régularité. Se coucher et se lever à des heures similaires donne un repère au corps. Le week-end, mieux vaut garder l’écart réduit."),
     ("Petits rituels, transition claire","Un enchaînement similaire chaque soir agit comme un signal : bientôt l’heure de dormir. Cela peut être lire, s’étirer doucement, respirer calmement ou noter une courte liste pour demain afin que les pensées ne tournent pas en boucle.")],
  ch="Votre soirée en cinq points",ci=["Poser les écrans un moment avant de dormir","Assombrir la chambre et la garder plutôt fraîche","Le même enchaînement chaque soir","Dernier repas ni trop tard ni trop lourd","Prendre la lumière du jour le matin"],
  done="Tout est coché. Bonne nuit, et pour aller plus loin :",rel="À lire aussi",fine="Remarque : ce texte donne des informations générales et ne remplace pas un avis médical. Si des troubles du sommeil durent, parlez-en à un médecin.")),
"it":dict(
 title="Vesper – Il sonno, spiegato con calma",desc="Calcolatore del sonno, test del tipo di sonno e informazioni chiare su sonno, ritmo e routine serale.",
 nav=["Calcolatore","Tipo di sonno","Rituale serale","Miti"],home="Home",
 eb="Il sonno, spiegato con calma",h="Le belle notti <em>iniziano la sera</em>",p="Calcolatore, piccoli test e informazioni chiare su sonno, ritmo e routine serale. Senza pressione, senza promesse.",b1="Apri il calcolatore",
 calc=dict(k="Calcolatore del sonno",h="Quando andare a letto, <em>quando alzarsi</em>?",p="Un ciclo di sonno dura circa 90 minuti. Il calcolatore propone orari adatti, più circa 15 minuti per addormentarsi.",t=["Devo alzarmi alle","Vado a letto alle"],r=["Vai a letto alle","Alzati alle"],cyc="cicli",hr="ore",note="Valori indicativi: ognuno dorme un po’ in modo diverso."),
 pano="Quando il giorno si fa più silenzioso.",
 ck=dict(k="Il tuo tipo di sonno",h="Allodola, colomba <em>o gufo</em>?",p="Tre brevi domande, nessun giudizio: una panoramica del tuo ritmo naturale.",of="Domanda",
  q=[("Quando ti verrebbe sonno da solo nei giorni liberi?",["Presto la sera","Verso mezzanotte","A notte fonda"]),("Quando sei più sveglio?",["Al mattino","A metà giornata","La sera"]),("Come vivi la sveglia?",["Nessun problema","Così così","Piuttosto difficile"])],
  r={"lark":("L’allodola","Ti svegli presto e hai sonno presto. La tua giornata funziona meglio con impegni al mattino; la sera puoi rallentare in anticipo."),"dove":("La colomba","Sei nel mezzo: ti adatti bene sia a giornate presto sia tardi. Orari fissi aiutano comunque a mantenere il ritmo."),"owl":("Il gufo","La tua giornata parte più tardi e si accende la sera. La luce del giorno al mattino può aiutare a spostare il ritmo in modo consapevole.")},art="Da leggere anche:",again="Ricomincia"),
 rt=dict(k="Il tuo rituale serale",h="Costruisci <em>la tua sera</em>",p="Tocca tutto ciò che ti piace fare prima di dormire e guarda la luna riempirsi.",u="rituali",
  i=["Mettere via lo schermo","Abbassare la luce","Arieggiare la stanza","Bere una tisana calda","Leggere qualche pagina","Allungarsi dolcemente","Respirare con calma","Scrivere la lista di domani"],
  m=["È ancora giorno. Tocca qualcosa.","Un inizio. La sera si fa più calma.","Già un rituale: nasce una transizione chiara.","Quasi luna piena. Una sera ben rotonda.","Luna piena: la tua sera è pronta."]),
 my=dict(k="Mito o fatto?",h="Quattro affermazioni, <em>verificate in breve</em>",p="Tocca una carta per girarla.",v=("Mito","Fatto"),tap="Gira",c=[
  ("Tutti hanno bisogno di esattamente otto ore di sonno.",0,"Il bisogno è individuale. Per gli adulti si indicano spesso da sette a nove ore come orientamento, ma non per tutti."),
  ("Un bicchiere di vino la sera migliora il sonno.",0,"L’alcol può facilitare l’addormentamento, ma di solito rende il sonno più leggero e agitato."),
  ("Una stanza buia e piuttosto fresca favorisce il sonno.",1,"Buio e frescura piacevole sono tra le basi più citate per dormire bene."),
  ("Orari fissi per dormire aiutano il ritmo interno.",1,"Dormire e alzarsi più o meno agli stessi orari dà al corpo un tempo chiaro.")]),
 fq=dict(k="Domande",h="Risposte <em>brevi</em>",c=[
  ("Di quanto sonno si ha bisogno?","È individuale. Per gli adulti si indicano spesso da sette a nove ore come orientamento. Conta soprattutto come ti senti riposato nella vita di tutti i giorni."),
  ("Che cos’è un ciclo del sonno?","Una notte è fatta di più passaggi tra sonno leggero, sonno profondo e sonno REM. Un passaggio dura circa 90 minuti, con differenze da una notte all’altra."),
  ("Il sonnellino è utile?","Un breve pisolino di circa 20 minuti è per molti rinfrescante. Più tardi nella giornata può ritardare l’addormentamento serale."),
  ("Quando chiedere un parere medico?","Se dormi male per molto tempo o sei molto stanco di giorno, parlane con un medico. Questo sito offre informazioni generali e non sostituisce una consulenza.")]),
 tz=dict(k="Da leggere",go="Leggi l’articolo →"),
 foot="Vesper – Il sonno, spiegato con calma.",dis="Informazioni generali, non consulenza medica.",
 art=dict(slug="routine-serale",title="La routine serale: come la sera diventa notte",lede="Dormire bene non comincia a letto, ma ore prima. Una panoramica su luce, ritmo e piccoli rituali.",
  s=[("La luce dà il tempo","Una luce intensa e fredda la sera dice al corpo: è ancora giorno. Una luce soffusa e calda aiuta a rallentare. Al contrario, la luce del giorno al mattino sostiene il ritmo, anche con il cielo coperto."),
     ("Il ritmo batte la perfezione","Conta meno la notte perfetta che la regolarità. Andare a dormire e alzarsi a orari simili dà al corpo un punto di riferimento. Nel fine settimana conviene tenere lo scarto contenuto."),
     ("Piccoli rituali, passaggio chiaro","Una sequenza simile ogni sera funziona da segnale: tra poco è ora di dormire. Può essere leggere, allungarsi dolcemente, respirare con calma o scrivere una breve lista per domani, così i pensieri non girano a vuoto.")],
  ch="La tua sera in cinque punti",ci=["Mettere via gli schermi un po’ prima di dormire","Oscurare la stanza e tenerla piuttosto fresca","Ogni sera una sequenza simile","Ultimo pasto non troppo tardi né troppo pesante","Prendere la luce del giorno al mattino"],
  done="Tutto spuntato. Buonanotte, e per approfondire:",rel="Da leggere anche",fine="Nota: questo testo offre informazioni generali e non sostituisce un parere medico. Se i disturbi del sonno durano a lungo, parlane con un medico.")),
}

ART2={
"de":dict(slug="schlafzimmer-ruhe",title="Das Schlafzimmer: Ein Ort nur für die Nacht",lede="Dunkelheit, frische Luft, Ruhe: Wie das Zimmer den Schlaf unterstützen kann, ohne teure Anschaffungen.",
 s=[("Dunkelheit zuerst","Schon wenig Licht kann stören: Straßenlaternen, Standby-Lämpchen, ein Handy-Display. Vorhänge oder eine Schlafmaske sind einfache Lösungen. Wer nachts aufsteht, nutzt am besten ein schwaches, warmes Licht."),
    ("Frische Luft, angenehme Kühle","Viele schlafen in einem eher kühlen, gut gelüfteten Zimmer besser. Kurz vor dem Schlafengehen zu lüften ist ein einfacher Anfang. Was angenehm ist, bleibt persönlich."),
    ("Ruhe und ein klarer Zweck","Geräusche lassen sich oft dämpfen, etwa durch geschlossene Türen oder Ohrstöpsel. Hilfreich ist auch, das Bett vor allem zum Schlafen zu nutzen: So verbindet der Kopf das Zimmer mit Ruhe.")],
 ch="Dein Schlafzimmer in fünf Punkten",ci=["Vorhänge oder Maske gegen fremdes Licht","Standby-Lämpchen und Displays abdecken","Vor dem Schlafen kurz lüften","Den Raum eher kühl halten","Das Bett vor allem zum Schlafen nutzen"],
 done="Alles abgehakt. Schlaf gut, und mehr dazu hier:",rel="Weiterlesen",fine="Hinweis: Dieser Text gibt allgemeine Informationen und ersetzt keine ärztliche Beratung. Wenn Schlafprobleme länger anhalten, sprich mit einer Ärztin oder einem Arzt."),
"fr":dict(slug="chambre-sommeil",title="La chambre : un lieu réservé à la nuit",lede="Obscurité, air frais, calme : comment la pièce peut soutenir le sommeil, sans achats coûteux.",
 s=[("L’obscurité d’abord","Même peu de lumière peut gêner : lampadaires, veilles, écran de téléphone. Des rideaux ou un masque sont des solutions simples. Si vous vous levez la nuit, une lumière faible et chaude est préférable."),
    ("Air frais, fraîcheur agréable","Beaucoup dorment mieux dans une pièce plutôt fraîche et bien aérée. Aérer juste avant de se coucher est un bon début. Ce qui est agréable reste personnel."),
    ("Calme et usage clair","Les bruits peuvent souvent être atténués, par exemple avec des portes fermées ou des bouchons d’oreilles. Il aide aussi d’utiliser le lit surtout pour dormir : l’esprit associe alors la pièce au repos.")],
 ch="Votre chambre en cinq points",ci=["Rideaux ou masque contre la lumière extérieure","Couvrir les veilles et les écrans","Aérer brièvement avant de dormir","Garder la pièce plutôt fraîche","Utiliser le lit surtout pour dormir"],
 done="Tout est coché. Bonne nuit, et pour aller plus loin :",rel="À lire aussi",fine="Remarque : ce texte donne des informations générales et ne remplace pas un avis médical. Si des troubles du sommeil durent, parlez-en à un médecin."),
"it":dict(slug="camera-da-letto-sonno",title="La camera da letto: un luogo solo per la notte",lede="Buio, aria fresca, calma: come la stanza può sostenere il sonno, senza acquisti costosi.",
 s=[("Prima di tutto il buio","Anche poca luce può disturbare: lampioni, spie in standby, lo schermo del telefono. Tende o una mascherina sono soluzioni semplici. Se ti alzi di notte, meglio una luce debole e calda."),
    ("Aria fresca, frescura piacevole","Molti dormono meglio in una stanza piuttosto fresca e ben aerata. Arieggiare poco prima di coricarsi è un buon inizio. Ciò che è piacevole resta personale."),
    ("Calma e uno scopo chiaro","I rumori si possono spesso attutire, ad esempio con le porte chiuse o i tappi per le orecchie. Aiuta anche usare il letto soprattutto per dormire: la mente associa così la stanza al riposo.")],
 ch="La tua camera in cinque punti",ci=["Tende o mascherina contro la luce esterna","Coprire le spie in standby e gli schermi","Arieggiare brevemente prima di dormire","Tenere la stanza piuttosto fresca","Usare il letto soprattutto per dormire"],
 done="Tutto spuntato. Buonanotte, e per approfondire:",rel="Da leggere anche",fine="Nota: questo testo offre informazioni generali e non sostituisce un parere medico. Se i disturbi del sonno durano a lungo, parlane con un medico.")}
BR={
"de":dict(k="Atemübung",h="Vier ein, <em>sechs aus</em>",p="Folge dem Kreis: Er wächst beim Einatmen und schrumpft beim Ausatmen. Eine ruhige Übung für zwischendurch, kein Heilmittel.",go="Starten",st="Stoppen",i="Einatmen",o="Ausatmen",rd="Bereit",u="Runden",nav="Atmen"),
"fr":dict(k="Exercice de respiration",h="Quatre pour inspirer, <em>six pour expirer</em>",p="Suivez le cercle : il grandit à l’inspiration et rétrécit à l’expiration. Un exercice calme, pour une pause, pas un remède.",go="Démarrer",st="Arrêter",i="Inspirez",o="Expirez",rd="Prêt",u="tours",nav="Respirer"),
"it":dict(k="Esercizio di respirazione",h="Quattro per inspirare, <em>sei per espirare</em>",p="Segui il cerchio: cresce quando inspiri e si restringe quando espiri. Un esercizio calmo per una pausa, non un rimedio.",go="Avvia",st="Ferma",i="Inspira",o="Espira",rd="Pronto",u="giri",nav="Respiro")}
for _l in T:
    T[_l]["arts"]=[T[_l]["art"],ART2[_l]];T[_l]["br"]=BR[_l]
AK=["abend","schlafzimmer"]
def img(n): return os.path.exists(f"assets/img/{n}.jpg")
def bg(n): return f' style="background-image:linear-gradient(180deg,rgba(7,10,26,.55),rgba(7,10,26,.9)),url(/assets/img/{n}.jpg);background-size:cover;background-position:center"' if img(n) else ""

def url(l,sub=""): return f"/{l}/{sub}"
def head(l,title,desc,path_by_lang,self_path):
    alts="".join(f'<link rel="alternate" hreflang="{x}" href="{B}{p}">' for x,p in path_by_lang.items())+f'<link rel="alternate" hreflang="x-default" href="{B}{path_by_lang["de"]}">'
    return f'<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{B}{self_path}">{alts}<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta name="theme-color" content="#070a1a"><link rel="icon" href="/assets/vesper.svg"><link rel="stylesheet" href="/assets/style.css"></head><body>'
def header(l,paths,home=True):
    t=T[l]
    if home:
        links="".join(f'<a href="#{a}">{n}</a>' for a,n in zip(["rechner","check","abend","atem","mythen"],t["nav"][:3]+[t["br"]["nav"],t["nav"][3]]))+L(l,"nav","Molita ↗")
        nvl=f'<nav class="nvl">{links}</nav>'
    else:
        nvl=f'<nav class="nvl"><a href="/{l}/">← {t["home"]}</a>{L(l,"nav","Molita ↗")}</nav>'
    lg="".join(f'<a href="{paths[x]}"{" class=on" if x==l else ""} hreflang="{x}">{x.upper()}</a>' for x in LANGS)
    return f'<header class="nv"><div class="nvi"><a class="logo" href="/{l}/"><i></i>Vesper</a>{nvl}<div class="lg">{lg}</div></div></header>'
def footer(l):
    t=T[l];a=t["art"]
    return f'<footer><div class="wrap fi"><div>{t["foot"]}</div><div><a href="/{l}/">{t["home"]}</a>{"".join(f'<a href="/{l}/{x["slug"]}/">{x["title"].split(":")[0]}</a>' for x in t["arts"])}{L(l,"footer")}</div><div class="dis">{t["dis"]}</div></div></footer><script src="/assets/app.js" defer></script></body></html>'
def paths_home(): return {x:f"/{x}/" for x in LANGS}
def paths_art(i=0): return {x:f'/{x}/{T[x]["arts"][i]["slug"]}/' for x in LANGS}

def home(l):
    t=T[l];c=t["calc"];k=t["ck"];r=t["rt"];m=t["my"];f=t["fq"];a=t["art"]
    o=head(l,t["title"],t["desc"],paths_home(),f"/{l}/")+header(l,paths_home())
    o+=f'<section class="hero"><canvas id="stars"></canvas><div class="hm"><div class="moon cr"></div></div><div class="wrap"><span class="eyebrow">{t["eb"]}</span><h1>{t["h"]}</h1><p>{t["p"]}</p><div class="btns"><a class="btn g" href="#rechner">{t["b1"]}</a>{L(l,"hero",GO[l],"btn o")}</div></div></section>'
    o+=f'<section id="rechner" class="calc"><div class="wrap"><span class="eyebrow">{c["k"]}</span><h2>{c["h"]}</h2><p class="sub">{c["p"]}</p><div class="card rv" id="calc" data-l1="{c["r"][0]}" data-l2="{c["r"][1]}" data-cyc="{c["cyc"]}" data-hr="{c["hr"]}"><div class="tabs" role="tablist"><button role="tab" aria-selected="true">{c["t"][0]}</button><button role="tab" aria-selected="false">{c["t"][1]}</button></div><label class="tin"><input type="time" value="07:00" aria-label="{c["t"][0]}"></label><div class="cres"></div><p class="note">{c["note"]} {L(l,"rechner")}</p></div></div></section>'
    o+=f'<section class="pano"{bg("pano")}><p>{t["pano"]}</p>{L(l,"pano",GO[l])}</section>'
    qs="".join(f'<div class="cq"{"" if i==0 else " hidden"}><small>{k["of"]} {i+1} / 3</small><b>{q}</b><div class="co">'+"".join(f'<button type="button" data-v="{v}">{x}</button>' for v,x in enumerate(os_))+'</div></div>' for i,(q,os_) in enumerate(k["q"]))
    res="".join(f'<div class="cr" data-k="{kk}" hidden><span class="eyebrow">{k["k"]}</span><h3>{ti}</h3><p>{d}</p></div>' for kk,(ti,d) in k["r"].items())
    aurl=f'/{l}/{a["slug"]}/'
    o+=f'<section id="check" class="ck"><div class="wrap"><span class="eyebrow">{k["k"]}</span><h2>{k["h"]}</h2><p class="sub">{k["p"]}</p><div class="card ckb rv"><div class="cdots"><i></i><i></i><i></i></div>{qs}{res}<div class="cf2" hidden><span class="cs">{k["art"]}</span><a class="cl" href="{aurl}">{a["title"]}</a>{L(l,"check",GO[l],"cta2")}<button type="button" class="cagain">{k["again"]}</button></div></div></div></section>'
    tiles="".join(f'<button type="button" class="tile" aria-pressed="false">{x}</button>' for x in r["i"])
    o+=f'<section id="abend" class="rt"><div class="wrap"><span class="eyebrow">{r["k"]}</span><h2>{r["h"]}</h2><p class="sub">{r["p"]}</p><div class="grid"><div class="moon rv"><i class="sh"></i></div><div class="rv"><div class="tiles">{tiles}</div><p class="rmsg" data-m="{"|".join(r["m"])}">{r["m"][0]}</p><span class="rcount" data-u="{r["u"]}">0 / {len(r["i"])} {r["u"]}</span> {L(l,"ritual")}</div></div></div></section>'
    cards="".join(f'<button class="mc rv" aria-pressed="false"><span class="mi"><span class="mf"><small>{i+1} / {len(m["c"])}</small><b>{q}</b><em>{m["tap"]} ↻</em></span><span class="mb"><small class="v{v}">{m["v"][v]}</small><p>{e}</p></span></span></button>' for i,(q,v,e) in enumerate(m["c"]))
    o+=f'<section id="mythen" class="my"><div class="wrap"><span class="eyebrow">{m["k"]}</span><h2>{m["h"]}</h2><p class="sub">{m["p"]}</p><div class="myths">{cards}</div><p class="mlink">{L(l,"myth")}</p></div></section>'
    b=t["br"]
    o+=f'<section id="atem" class="br"><div class="wrap"><span class="eyebrow">{b["k"]}</span><h2>{b["h"]}</h2><p class="sub">{b["p"]}</p><div class="brw rv" data-i="{b["i"]}" data-o="{b["o"]}" data-go="{b["go"]}" data-st="{b["st"]}" data-u="{b["u"]}"><div class="brc"><span>{b["rd"]}</span></div><div class="brs">0 {b["u"]}</div><button type="button" class="btn g brb">{b["go"]}</button></div></div></section>'
    fq="".join(f'<details class="rv"><summary>{q}</summary><p>{x}</p></details>' for q,x in f["c"])
    o+=f'<section id="faq"><div class="wrap two"><div><span class="eyebrow">{t["tz"]["k"]}</span>{"".join(f'<a class="art rv" href="/{l}/{x["slug"]}/" style="margin-top:14px"><div class="moon cr"></div><h3>{x["title"]}</h3><p>{x["lede"]}</p><span class="go">{t["tz"]["go"]}</span></a>' for x in t["arts"])}</div><div><span class="eyebrow">{f["k"]}</span><h2>{f["h"]}</h2>{fq}<p class="mlink">{L(l,"faq")}</p></div></div></section>'
    return o+footer(l)

def article(l,i0=0):
    t=T[l];a=t["arts"][i0];ps=paths_art(i0);oth=t["arts"][1-i0]
    o=head(l,a["title"]+" – Vesper",a["lede"],ps,ps[l])+header(l,ps,False)
    o+=f'<div class="ah"{bg(AK[i0])}><div class="moon cr"></div><div class="wrap"><span class="eyebrow">Vesper</span><h1>{a["title"]}</h1><p>{a["lede"]}</p></div></div><article class="body">'
    for i,(h,p) in enumerate(a["s"]):
        o+=f'<h2>{h}</h2><p>{p}</p>'
        if i==0: o+=f'<div class="cb"><p>{MORE[l]}:</p>{L(l,"art-mid",GO[l])}</div>'
        if i<2: o+='<div class="sep">· · ·</div>'
    o+=f'<h2>{a["ch"]}</h2><div class="chk">'+"".join(f'<label><input type="checkbox"><span>{x}</span></label>' for x in a["ci"])+f'</div><p class="done" hidden>{a["done"]} {L(l,"art-end",GO[l])}</p>'
    o+=f'<p class="fine">{a["fine"]}</p><div class="rel"><span class="eyebrow">{a["rel"]}</span><p><a class="xl" href="/{l}/#check">{t["ck"]["k"]} →</a> &nbsp; <a class="xl" href="/{l}/#rechner">{t["calc"]["k"]} →</a> &nbsp; <a class="xl" href="/{l}/{oth["slug"]}/">{oth["title"]} →</a></p></div></article>'
    return o+footer(l)

for l in LANGS:
    open(f"{l}/index.html","w",encoding="utf-8").write(home(l)) if os.path.isdir(l) else (os.makedirs(l),open(f"{l}/index.html","w",encoding="utf-8").write(home(l)))
    for i0,ar in enumerate(T[l]["arts"]):
        os.makedirs(f"{l}/{ar['slug']}",exist_ok=True)
        open(f"{l}/{ar['slug']}/index.html","w",encoding="utf-8").write(article(l,i0))
open("index.html","w").write('<!doctype html><meta charset="utf-8"><title>Vesper</title><meta name="viewport" content="width=device-width,initial-scale=1"><script>var n=(navigator.language||"de").slice(0,2);location.replace("/"+(n=="fr"||n=="it"?n:"de")+"/")</script><noscript><a href="/de/">Vesper</a></noscript>')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {B}/sitemap.xml\n")
u=[f"/{l}/" for l in LANGS]+[f'/{l}/{ar["slug"]}/' for l in LANGS for ar in T[l]["arts"]]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{B}{x}</loc></url>\n" for x in u)+"</urlset>\n")
open("assets/vesper.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#070a1a"/><circle cx="32" cy="32" r="16" fill="#f3ead7"/><circle cx="40" cy="27" r="14" fill="#070a1a"/></svg>')
print("built",len(u),"pages")
