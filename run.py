# # run.py

# import asyncio
# import logging

# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message

# from config import TOKEN

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     text = (
#         "Sizga qaysi kasb qiziq, nomini yozing\n\n"
#         "Kasblar nomi:\n\n"
#         "-Dasturchi-\n"
#         "-Shifokor-\n"
#         "-O'qituvchi-\n"
#         "-Muhandis-\n"
#         "-Sotuvchi-\n"
#         "-Jurnalist-\n"
#         "-Haydovchi-\n"
#         "-Oshpaz-\n"
#         "-Advokat-\n"
#         "-San'atkor-\n"
#         "-Buxgalter-\n"
#         "-Elektrik-\n"
#         "-Uchuvchi-\n"
#         "-Ofitsiant-\n"
#         "-Mekanik-\n"
#         "-Hamshira-\n"
#         "-Veterinar-\n"
#         "-Rassom-\n"
#         "-Musiqachi-\n"
#         "-Aktyor-\n"
#         "-Arxeolog-\n"
#         "-Astronom-\n"
#         "-Biolog-\n"
#         "-Geolog-\n"
#         "-Kimyogar-\n"
#         "-Fizik-\n"
#         "-Farmatsevt-\n"
#         "-Arxitektor-\n"
#         "-Toksikolog-\n"
#         "-Antropolog-\n"
#         "-Meteorolog-\n"
#         "-Kriptograf-\n"
#         "-Psixolog-\n"
#         "-Sotsiolog-\n"
#         "-Arxivchi-\n"
#         "-Kutubxonachi-\n"
#         "-Tarjimon-\n"
#         "-Kartograf-\n"
#         "-Botanist-\n"
#         "-Zoolog-\n"
#         "-Arxivolog-\n"
#         "-Paleontolog-\n"
#         "-Fizikoterapevt-\n"
#         "-Genetik-\n"
#         "-Mikrobiolog-\n"
#         "-Akustik-\n"
#         "-Optik-\n"
#         "-Navigatsion-\n"
#         "-Agronom-\n"
#         "-Ekolog-\n"
#         "-Mineralog-\n"
#         "-Vulkanolog-\n"
#         "-Hidrolog-\n"
#         "-Okeanolog-\n"
#         "-Astronavt-\n"
#         "-Kosmolog-\n"
#         "-Operator-\n"
#         "-Veterinar-\n"
#         "-Farmatsevt-\n"
#         "-Akustik muhandis-\n"
#         "-Dron operatori-\n"
#         "-Kiberxavfsizlik mutaxassisi-\n"
#         "-Virtual reallik dizayneri-\n"
#         "-Biotexnolog-\n"
#         "-Kriptovalyuta treyderi-\n"
#         "-Nanotexnolog mutaxassisi-\n"
#         "-Logist-\n"
#         "-Kiberforensika mutaxassisi-\n"
#         "-Podkast prodyuseri-\n"
#         "-Mobil ilova testlovchi-\n"
#         "-Blokcheyn dasturchisi-\n"
#         "-Esport murabbiyi-\n"
#         "-Uy kinoteatri montajchisi-\n"
#         "-UAV texnikasi-\n"
#         "-Astronavt tayyorgarlik instruktori-\n"
#         "-Kiberpsixolog-\n"
#         "-Data-jurnalist-\n"
#         "-Sensor texnolog mutaxassisi-\n"
#         "-Sun’iy intellekt etikasi bo‘yicha ekspert-\n"
#         "-Eko-qurilish muhandisi-\n"
#         "-3D chop etish texnologi-\n"
#         "-Biometrik tizim muhandisi-\n"
#         "-(Big Data) tahlilchisi-\n"
#         "-Kosmik qoldiqlar mutaxassisi-\n"
#         "-Neurointerfeys dizayneri-\n"
#         "-Kiberxavfsizlik auditori-\n"
#         "-Gamifikatsiya mutaxassisi-\n"
#         "-Vertikal qishloq xo‘jaligi mutaxassisi-\n"
#         "-Kosmik turizm gid-\n"
#         "-Energiya samaradorligi bo‘yicha konsultant-\n"
#         "-Avtonom transport muhandisi-\n"
#         "-Kriptograf-\n"
#         "-Aqlli uy tizimlari mutaxassisi-\n"
#         "-Genetik maslahatchi-\n"
#         "-Raqamli marketing analitigi-\n"
#         "-Sun’iy organ ishlab chiqaruvchi muhandis-\n"
#         "-Ovoz effektlari (Foley) mutaxassisi-\n"
#         "-Kiberxavfsizlik bo‘yicha insident javob beruvchi-\n"
#     )
#     await message.answer(text)


# @dp.message(F.text == "Dasturchi")  # /salom
# async def Dasturchi(message: Message):
#     await message.reply("Dasturchi - kompyuter dasturlari va ilovalarini yaratuvchi mutaxassis bo'lib, kod yozish, xatolarni tuzatish va tizimlarni optimallashtirish bilan shug'ullanadi. Tarixan, bu kasb 1940-yillarda kompyuterlar paydo bo'lishi bilan boshlangan, Ada Lovelace birinchi algoritmni yozgan. Ta'lim: kompyuter fanlari bo'yicha bakalavr darajasi, Python, Java kabi tillar o'rganish. Ko'nikmalar: mantiqiy fikrlash, muammo hal qilish, jamoaviy ish. Kundalik vazifalar: dastur loyihalash, test qilish, yangilash. Kasb yo'llari: IT kompaniyalarida, startup'larda yoki frilanser sifatida. O'rtacha maosh: $80,000–$120,000 (mamlakatga qarab). Ish bozori: yuqori talab, AI va mobil ilovalar tufayli o'sish prognoz qilingan. Qiyinchiliklar: tez o'zgaruvchan texnologiyalar, uzoq ish soatlari. Kelajak: AI integratsiyasi bilan yanada muhim bo'ladi.")


# @dp.message(F.text == "Shifokor")
# async def Shifokor(message: Message):
#     await message.reply("Shifokor - inson salomatligini saqlash va davolash bilan shug'ullanuvchi tibbiy mutaxassis. Tarixiy jihatdan, Gippokrat tibbiyot otasi hisoblanadi. Ta'lim: tibbiyot universitetida 6-8 yil o'qish, keyin internatura. Ko'nikmalar: anatomiya bilimi, tashxis qo'yish, etika. Kundalik vazifalar: bemorlarni ko'rikdan o'tkazish, dori yozish, operatsiyalar. Kasb yo'llari: umumiy shifokor, jarroh yoki mutaxassis (kardiolog va h.k.). O'rtacha maosh: $150,000+. Ish bozori: doimiy tanqislik, aholi qarishi tufayli o'sish. Qiyinchiliklar: stress, uzoq navbatchilik, emotsional yuk. Kelajak: telemeditsina va AI yordami bilan rivojlanadi.")


# @dp.message(F.text == "O'qituvchi")
# async def Oqituvchi(message: Message):
#     await message.reply(f"O'qituvchi - bilim berish va tarbiya qilish bilan band bo'lgan pedagog. Tarixan, qadimiy Yunonistonda Sokrat kabi shaxslar bor. Ta'lim: pedagogika bakalavr, litsenziya. Ko'nikmalar: dars rejalashtirish, motivatsiya, psixologiya. Kundalik vazifalar: dars o'tkazish, baholash, ota-onalar bilan muloqot. Kasb yo'llari: maktab o'qituvchisi, universitet lektor. O'rtacha maosh: $40,000–$60,000. Ish bozori: pensiyaga chiqish tufayli o'rinlar ko'p. Qiyinchiliklar: katta sinflar, burn-out. Kelajak: onlayn ta'lim bilan yangi imkoniyatlar")


# @dp.message(F.text  == "Muhandis")
# async def Muhandis(message: Message):
#     await message.reply(f"Muhandis - texnika va qurilish loyihalarini ishlab chiqish bilan shug'ullanadi. Tarixan, Arximed kabi qadimiylar. Ta'lim: muhandislik bakalavr, matematika. Ko'nikmalar: dizayn, tahlil, loyiha boshqaruvi. Kundalik vazifalar: chizmalar yaratish, sinovlar. Kasb yo'llari: fuqaro, mexanika, elektr muhandisi. O'rtacha maosh: $80,000+. Ish bozori: infratuzilma loyihalari tufayli talab yuqori. Qiyinchiliklar: xavfsizlik, ekologiya. Kelajak: yashil texnologiyalar bilan o'sadi.")


# @dp.message(F.text  == "Sotuvchi")
# async def Sotuvchi(message: Message):
#     await message.reply(f"Sotuvchi - tovar va xizmatlarni sotish bilan shug'ullanadi. Tarixan, savdo qadimdan mavjud. Ta'lim: savdo yoki marketing. Ko'nikmalar: muloqot, muzokara. Kundalik vazifalar: mijozlar bilan ish, shartnoma tuzish. Kasb yo'llari: do'kon sotuvchisi, menejer. O'rtacha maosh: $40,000+ komissiya. Ish bozori: elektron savdo bilan o'sish. Qiyinchiliklar: raqobat, rad etilish. Kelajak: onlayn platformalar.")


# @dp.message(F.text  == "Jurnalist")
# async def Jurnalistas(message: Message):
#     await message.reply(f"Jurnalist - yangiliklar to'plash va tarqatish mutaxassisi. Tarixan, 17-asr gazetalari. Ta'lim: jurnalistika bakalavr. Ko'nikmalar: yozish, intervyu. Kundalik vazifalar: tadqiqot, maqola yozish. Kasb yo'llari: reportyor, muharrir. O'rtacha maosh: $50,000+. Ish bozori: digital media bilan o'zgarish. Qiyinchiliklar: fake news, xavf. Kelajak: ijtimoiy tarmoqlar.")


# @dp.message(F.text  == "Haydovchi")
# async def Haydovchi(message: Message):
#     await message.reply(f"Haydovchi - transport vositalarini boshqaruvchi. Tarixan, 19-asr avtomobillari. Ta'lim: haydovchilik guvohnomasi. Ko'nikmalar: xavfsizlik, navigatsiya. Kundalik vazifalar: yo'l qoidalari, yuk tashish. Kasb yo'llari: taksi, yuk haydovchisi. O'rtacha maosh: $40,000+. Ish bozori: logistika o'sishi. Qiyinchiliklar: charchoq, baxtsiz hodisalar. Kelajak: avtonom mashinalar.")


# @dp.message(F.text  == "Oshpaz")
# async def Oshpaz(message: Message):
#     await message.reply(f"Oshpaz - ovqat tayyorlash mutaxassisi. Tarixan, qadimiy oshxonalar. Ta'lim: kulinar maktabi. Ko'nikmalar: retseptlar, gigiena. Kundalik vazifalar: menyular yaratish, pishirish. Kasb yo'llari: restoran oshpazi, shaxsiy. O'rtacha maosh: $40,000+. Ish bozori: turizm bilan o'sish. Qiyinchiliklar: issiq oshxona, vaqt bosimi. Kelajak: vegan tendensiyalari.")


# @dp.message(F.text  == "Advokat")
# async def Advokat(message: Message):
#     await message.reply(f"Advokat - huquqiy himoya qiluvchi. Tarixan, qadimiy Rim. Ta'lim: yuridik fakultet, bar imtihoni. Ko'nikmalar: tahlil, oratorlik. Kundalik vazifalar: sudda himoya, maslahat. Kasb yo'llari: jinoyat, fuqaro advokati. O'rtacha maosh: $100,000+. Ish bozori: barqaror. Qiyinchiliklar: stress, etika. Kelajak: onlayn konsultatsiyalar.")


# @dp.message(F.text  == "San'atkor")
# async def Sanatkor(message: Message):
#     await message.reply(f"San'atkor - ijodiy asarlar yaratuvchi. Tarixan, qadimiy rasmlar. Ta'lim: san'at akademiyasi. Ko'nikmalar: ijodkorlik, texnika. Kundalik vazifalar: rasm chizish, ko'rgazmalar. Kasb yo'llari: rassom, haykaltarosh. O'rtacha maosh: o'zgaruvchan. Ish bozori: galereyalar. Qiyinchiliklar: moliyaviy beqarorlik. Kelajak: digital art.")



# @dp.message(F.text  == "Buxgalter")
# async def Buxgalter(message: Message):
#     await message.reply(f"Buxgalter - moliyaviy hisobotlar yurituvchi. Tarixan, qadimiy hisob kitoblari. Ta'lim: buxgalteriya bakalavr. Ko'nikmalar: matematika, dasturlar. Kundalik vazifalar: hisobotlar, soliqlar. Kasb yo'llari: kompaniya buxgalteri, auditor. O'rtacha maosh: $60,000+. Ish bozori: doimiy talab. Qiyinchiliklar: qonun o'zgarishlari. Kelajak: avtomatizatsiya.")

# @dp.message(F.text  == "Elektrik")
# async def Elektrik(message: Message):
#     await message.reply(f"Elektrchi - elektr tarmoqlarini o'rnatuvchi. Tarixan, Edison zamoni. Ta'lim: texnik kollej. Ko'nikmalar: xavfsizlik, diagrammlar. Kundalik vazifalar: simlar tortish, ta'mirlash. Kasb yo'llari: uy elektrchisi, sanoat. O'rtacha maosh: $50,000+. Ish bozori: qurilish o'sishi. Qiyinchiliklar: xavf, yuqori kuchlanish. Kelajak: yashil energiya.")    


# @dp.message(F.text  == "Uchuvchi")
# async def Uchuvchi(message: Message):
#     await message.reply(f"Uchuvchi - samolyot boshqaruvchi. Tarixan, Wright aka-uka. Ta'lim: aviatsiya akademiyasi. Ko'nikmalar: navigatsiya, qaror qabul. Kundalik vazifalar: parvozlar, nazorat. Kasb yo'llari: tijorat, harbiy uchuvchi. O'rtacha maosh: $100,000+. Ish bozori: aviatsiya rivoji. Qiyinchiliklar: jetlag, mas'uliyat. Kelajak: dronlar.")   


# @dp.message(F.text  == "Ofitsiant")
# async def Ofitsiant(message: Message):
#     await message.reply(f"Ofitsiant - restoranlarda xizmat ko'rsatuvchi. Tarixan, 18-asr kafe'lar. Ta'lim: tajriba. Ko'nikmalar: muloqot, tezlik. Kundalik vazifalar: buyurtmalar olish, ovqat berish. Kasb yo'llari: barista, menejer. O'rtacha maosh: $30,000+ bahshish. Ish bozori: turizm. Qiyinchiliklar: oyoqda ish, mijozlar. Kelajak: robotlar.") 


# @dp.message(F.text  == "Mekanik")
# async def Mekanik(message: Message):
#     await message.reply(f"Mekanik - mashinalarni ta'mirlovchi. Tarixan, sanoat inqilobi. Ta'lim: texnik ta'lim. Ko'nikmalar: diagnostika, asboblar. Kundalik vazifalar: ta'mirlash, sinov. Kasb yo'llari: avto mexanik, sanoat. O'rtacha maosh: $50,000+. Ish bozori: transport o'sishi. Qiyinchiliklar: iflos ish, xavf. Kelajak: elektr mashinalar.") 


# @dp.message(F.text  == "Hamshira")
# async def Hamshira(message: Message):
#     await message.reply(f"Hamshira - bemorlarni parvarish qiluvchi. Tarixan, Florence Nightingale. Ta'lim: tibbiy bakalavr. Ko'nikmalar: rahmdillik, tibbiy ko'nikmalar. Kundalik vazifalar: dori berish, monitoring. Kasb yo'llari: kasalxona hamshirasi, uy. O'rtacha maosh: $70,000+. Ish bozori: salomatlik tanqisligi. Qiyinchiliklar: shift ish, emotsiya. Kelajak: telehealth.") 


# @dp.message(F.text  == "Veterinar")
# async def Veterinar88(message: Message):
#     await message.reply(f"Veterinar - hayvonlarni davolash mutaxassisi. Tarixan, qadimiy fermerlik. Ta'lim: veterinariya doktorligi. Ko'nikmalar: anatomiya, operatsiya. Kundalik vazifalar: ko'rik, emlash. Kasb yo'llari: klinika, zoo. O'rtacha maosh: $90,000+. Ish bozori: uy hayvonlari o'sishi. Qiyinchiliklar: hayvonlar xulqi, evtanaziya. Kelajak: biotexnologiya") 


# @dp.message(F.text  == "Rassom")
# async def Rassom(message: Message):
#     await message.reply(f"Rassom - vizual san'at yaratuvchi. Tarixan, Leonardo da Vinci. Ta'lim: san'at bakalavr. Ko'nikmalar: chizish, ranglar. Kundalik vazifalar: asarlar yaratish, ko'rgazma. Kasb yo'llari: galereya, frilans. O'rtacha maosh: o'zgaruvchan. Ish bozori: NFT bilan o'sish. Qiyinchiliklar: ilhom, sotish. Kelajak: digital tools.") 


# @dp.message(F.text  == "Musiqachi")
# async def Musiqachi(message: Message):
#     await message.reply(f"Musiqachi - musiqa yaratuvchi va ijro etuvchi. Tarixan, Beethoven. Ta'lim: konservatoriya. Ko'nikmalar: asbob chalish, kompozitsiya. Kundalik vazifalar: mashq, konsertlar. Kasb yo'llari: orkestr, solo. O'rtacha maosh: o'zgaruvchan. Ish bozori: streaming. Qiyinchiliklar: raqobat, turne. Kelajak: AI musiqasi.") 


# @dp.message(F.text  == "Aktyor")
# async def Aktyor(message: Message):
#     await message.reply(f"Aktyor - rol o'ynash mutaxassisi. Tarixan, Shakespeare zamoni. Ta'lim: teatr akademiyasi. Ko'nikmalar: emotsiya, memorizatsiya. Kundalik vazifalar: repetitsiya, suratga olish. Kasb yo'llari: film, teatr. O'rtacha maosh: o'zgaruvchan. Ish bozori: Hollywood. Qiyinchiliklar: rad etilish, shuhrat. Kelajak: virtual reality") 


# @dp.message(F.text  == "Arxeolog")
# async def Arxeolog(message: Message):
#     await message.reply(f"Arxeolog – qadimgi madaniyat va sivilizatsiyalarni o‘rganadigan mutaxassis. Tarixan, bu soha XIX asrda tizimli qazish ishlari bilan shakllandi. Ta’lim: arxeologiya yoki tarix bakalavr darajasi. Ko‘nikmalar: qazish texnikasi, tarixiy tahlil, laboratoriya ishlari. Kundalik vazifalar: qazish ishlari olib borish, topilmalarni hujjatlashtirish, tadqiqot maqolalari yozish. Kasb yo‘llari: universitet professori, muzey xodimi, tadqiqotchi. O‘rtacha maosh: $50,000–$80,000. Ish bozori: ilmiy grantlarga bog‘liq. Qiyinchiliklar: uzoq safarlar, ekstremal ob-havo. Kelajak: 3D skanerlash va dron texnologiyalari bilan rivojlanadi.") 


# @dp.message(F.text  == "Astronom")
# async def Astronom(message: Message):
#     await message.reply(f"Astronom – koinot va osmon jismlarini o‘rganadigan olim. Tarixan, qadimgi Bobilda astronomik kuzatuvlar boshlangan. Ta’lim: astronomiya yoki fizika magistr darajasi. Ko‘nikmalar: teleskop ishlatish, hisoblash, ma’lumot tahlili. Kundalik vazifalar: kuzatuvlar, ilmiy tadqiqotlar, maqola yozish. Kasb yo‘llari: universitet olimi, observatoriya xodimi, kosmik agentlik mutaxassisi. O‘rtacha maosh: $80,000+") 


# @dp.message(F.text  == "Biolog")
# async def Biolog(message: Message):
#     await message.reply(f"Biolog – tirik organizmlar tuzilishi va faoliyatini o‘rganuvchi olim. Tarixan, Aristotel biologiya asoschilaridan biri. Ta’lim: biologiya bakalavr yoki magistr. Ko‘nikmalar: laboratoriya ishlari, dala tadqiqotlari, tahlil. Kundalik vazifalar: namunalar yig‘ish, tajribalar, ma’lumot tahlili. Kasb yo‘llari: ekolog, genetik, dengiz biolog. O‘rtacha maosh: $60,000–$90,000. Ish bozori: biotexnologiya va ekologiya sohalarida o‘sish. Qiyinchiliklar: dala sharoitidagi qiyinchiliklar. Kelajak: gen muhandisligi va bioinformatika bilan kengayadi.") 



# @dp.message(F.text  == "Geolog")
# async def Geolog(message: Message):
#     await message.reply(f"Geolog – Yer tuzilishi, tarkibi va jarayonlarini o‘rganuvchi mutaxassis. Tarixan, XIX asrda neft va kon sanoati rivoji bilan muhimlashdi. Ta’lim: geologiya bakalavr. Ko‘nikmalar: dala o‘lchovlari, laboratoriya tahlili, xarita tuzish. Kundalik vazifalar: tog‘ jinslari tahlili, qazilma izlash, yer silkinishi tadqiqoti. Kasb yo‘llari: neft kompaniyasi, ilmiy institut, davlat geologiyasi. O‘rtacha maosh: $70,000+. Ish bozori: tabiiy resurslar tufayli talab yuqori. Qiyinchiliklar: uzoq safarlar, ekstremal sharoit. Kelajak: ekologik monitoring va qidiruv texnologiyalari bilan rivojlanadi.") 


# @dp.message(F.text  == "Kimyogar")
# async def Kimyogar(message: Message):
#     await message.reply(f"Kimyogar – moddalarning tarkibi va xossalarini o‘rganuvchi mutaxassis. Tarixan, kimyo alkimyodan kelib chiqqan. Ta’lim: kimyo bakalavr yoki magistr. Ko‘nikmalar: laboratoriya uskunalari, formulalar, xavfsizlik qoidalari. Kundalik vazifalar: kimyoviy reaksiyalar, tahlillar, yangi modda yaratish. Kasb yo‘llari: farmatsevtika, oziq-ovqat sanoati, ilmiy tadqiqot. O‘rtacha maosh: $60,000–$100,000. Ish bozori: farmatsevtika va ekologiya sohalarida o‘sish. Qiyinchiliklar: xavfli moddalar bilan ishlash. Kelajak: yashil kimyo va nanoteknologiya.") 


# @dp.message(F.text  == "Fizik")
# async def Fizik(message: Message):
#     await message.reply(f"Fizik – moddiy dunyo qonuniyatlarini o‘rganadigan olim. Tarixan, Nyuton va Eynshteyn eng mashhur fiziklar. Ta’lim: fizika bakalavr yoki magistr. Ko‘nikmalar: matematik tahlil, tajriba o‘tkazish, ilmiy metod. Kundalik vazifalar: nazariy modellar yaratish, eksperimentlar o‘tkazish, ma’lumot tahlili. Kasb yo‘llari: ilmiy institut, universitet, sanoat laboratoriyasi. O‘rtacha maosh: $70,000–$120,000. Ish bozori: texnologiya va energetika sohalarida talab mavjud. Qiyinchiliklar: murakkab hisoblar, uzoq tadqiqotlar. Kelajak: kvant texnologiyalari va kosmik izlanishlar.") 


# @dp.message(F.text  == "Farmatsevt")
# async def Farmatsevt(message: Message):
#     await message.reply(f"Farmatsevt – dori vositalarini tayyorlaydigan va sotadigan mutaxassis. Tarixan, qadimgi Misrda dorixonalar bo‘lgan. Ta’lim: farmatsiya bakalavr darajasi. Ko‘nikmalar: farmakologiya, kimyo, mijozlar bilan ishlash. Kundalik vazifalar: dori aralashtirish, retseptlarni bajarish, maslahat berish. Kasb yo‘llari: dorixona, farmatsevtika zavodi, klinika. O‘rtacha maosh: $80,000+. Ish bozori: salomatlik sohasidagi o‘sish bilan kuchli talab. Qiyinchiliklar: aniq dozalarni saqlash mas’uliyati. Kelajak: shaxsiylashtirilgan dorilar ishlab chiqish") 


# @dp.message(F.text  == "Arxitektor")
# async def Arxitektor(message: Message):
#     await message.reply(f"Arxitektor – binolar va inshootlar loyihasini ishlab chiquvchi mutaxassis. Tarixan, Rim va Yunon me’morchiligi asos bo‘ldi. Ta’lim: arxitektura bakalavr yoki magistr. Ko‘nikmalar: dizayn, chizmalar, 3D modellashtirish. Kundalik vazifalar: loyiha yaratish, qurilish jarayonini nazorat qilish. Kasb yo‘llari: shaharsozlik, interyer dizayni, landshaft. O‘rtacha maosh: $70,000+. Ish bozori: qurilish rivojlanishiga bog‘liq. Qiyinchiliklar: buyurtmachining talablariga moslashish. Kelajak: ekologik va “yashil” arxitektura.") 


# @dp.message(F.text  == "Toksikolog")
# async def Toksikolog(message: Message):
#     await message.reply(f"Toksikolog – zaharli moddalar ta’sirini o‘rganuvchi mutaxassis. Tarixan, bu soha qadimiy davrlarda ham mavjud bo‘lgan. Ta’lim: toksikologiya yoki biologiya magistr darajasi. Ko‘nikmalar: laboratoriya ishlari, tahlil, xavfsizlik protokollari. Kundalik vazifalar: namunalar tekshirish, zaharlanish holatlarini aniqlash. Kasb yo‘llari: sud ekspertizasi, farmatsevtika, ekologiya. O‘rtacha maosh: $70,000+. Ish bozori: sanoat xavfsizligi va tibbiyot sohasida talab yuqori. Qiyinchiliklar: xavfli moddalarga duch kelish. Kelajak: biotibbiy tadqiqotlar bilan kengayadi.") 


# @dp.message(F.text  == "Antropolog")
# async def Antropolog(message: Message):
#     await message.reply(f"Antropolog – insoniyatning kelib chiqishi, madaniyati va rivojlanishini o‘rganuvchi olim. Tarixan, XIX asrda fan sifatida shakllangan. Ta’lim: antropologiya bakalavr yoki magistr. Ko‘nikmalar: dala tadqiqotlari, madaniy tahlil, intervyu. Kundalik vazifalar: sayohatlar, ilmiy maqolalar yozish, kuzatish. Kasb yo‘llari: muzeylar, universitetlar, xalqaro tashkilotlar. O‘rtacha maosh: $60,000+. Ish bozori: cheklangan, ammo ilmiy grantlar orqali ishlash mumkin. Qiyinchiliklar: uzoq safarlar, til to‘siqlari. Kelajak: madaniy merosni saqlash texnologiyalari.") 


# @dp.message(F.text  == "Meteorolog")
# async def Meteorolog(message: Message):
#     await message.reply(f"Meteorolog – ob-havo va iqlim o‘zgarishlarini o‘rganuvchi mutaxassis. Tarixan, qadimda osmonga qarab ob-havo bashorat qilinar edi. Ta’lim: meteorologiya yoki geofizika bakalavr. Ko‘nikmalar: ma’lumot tahlili, prognoz yaratish, kompyuter modellari. Kundalik vazifalar: ob-havo xaritalarini tahlil qilish, prognoz e’lon qilish. Kasb yo‘llari: televideniye, ilmiy institut, aviatsiya. O‘rtacha maosh: $60,000+. Ish bozori: tabiiy ofatlar monitoringida talab yuqori. Qiyinchiliklar: noaniqlik, bosim ostida ishlash. Kelajak: sun’iy intellekt yordamida aniqroq prognozlar.") 


# @dp.message(F.text  == "Kriptograf")
# async def Kriptograf(message: Message):
#     await message.reply(f"Kriptograf – ma’lumotlarni shifrlash va xavfsizlik tizimlarini yaratish bo‘yicha mutaxassis. Tarixan, qadim Misr va Rim shifrlash usullari mavjud edi. Ta’lim: kiberxavfsizlik yoki matematika bakalavr. Ko‘nikmalar: algoritmlar, dasturlash, xavfsizlik protokollari. Kundalik vazifalar: shifrlash tizimlarini ishlab chiqish, xavfsizlik tahlili. Kasb yo‘llari: IT kompaniya, hukumat, moliya sektori. O‘rtacha maosh: $90,000+. Ish bozori: internet xavfsizligi tufayli kuchli talab. Qiyinchiliklar: murakkab matematik masalalar. Kelajak: kvant kriptografiya.") 


# @dp.message(F.text  == "Psixolog")
# async def Psixolog(message: Message):
#     await message.reply(f"Psixolog – inson psixologiyasini o‘rganuvchi va maslahat beruvchi mutaxassis. Tarixan, Zigmunt Freyd psixoanaliz asoschisi. Ta’lim: psixologiya bakalavr yoki magistr. Ko‘nikmalar: muloqot, tahlil, empatiya. Kundalik vazifalar: suhbat o‘tkazish, diagnostika, davolash. Kasb yo‘llari: klinik psixolog, ta’lim psixologi, sport psixologi. O‘rtacha maosh: $70,000+. Ish bozori: ruhiy salomatlikka bo‘lgan talab oshmoqda. Qiyinchiliklar: emotsional yuk. Kelajak: onlayn psixologiya xizmatlari.") 


# @dp.message(F.text  == "Sotsiolog")
# async def Sotsiolog(message: Message):
#     await message.reply(f"Sotsiolog – jamiyat, ijtimoiy tizimlar va inson munosabatlarini o‘rganuvchi mutaxassis. Tarixan, Ogyust Kont “sotsiologiya” atamasini kiritgan. Ta’lim: sotsiologiya bakalavr yoki magistr. Ko‘nikmalar: statistik tahlil, so‘rovnomalar, kuzatuv. Kundalik vazifalar: tadqiqotlar, hisobotlar tayyorlash, ilmiy maqolalar yozish. Kasb yo‘llari: ilmiy institut, davlat, NNT. O‘rtacha maosh: $60,000+. Ish bozori: ijtimoiy loyihalarda talab mavjud. Qiyinchiliklar: moliyaviy resurs yetishmasligi. Kelajak: katta ma’lumotlar (big data) tahlili bilan kuchayadi.") 


# @dp.message(F.text  == "Arxivchi")
# async def Arxivchi(message: Message):
#     await message.reply(f"Arxivchi – hujjatlarni saqlash va tizimlashtirish bo‘yicha mutaxassis. Tarixan, bu kasb yozuvlar paydo bo‘lishi bilan yuzaga kelgan. Ta’lim: axborot kutubxonashunosligi yoki tarix bakalavr. Ko‘nikmalar: hujjat tahlili, kataloglash, saqlash texnologiyalari. Kundalik vazifalar: arxiv hujjatlarini tartibga solish, raqamlashtirish. Kasb yo‘llari: davlat arxivi, muzey, kutubxona. O‘rtacha maosh: $50,000+. Ish bozori: tarixiy merosni saqlash sohasida talab mavjud. Qiyinchiliklar: eski materiallar bilan ishlashdagi noziklik. Kelajak: raqamli arxivlar.") 


# @dp.message(F.text  == "Kutubxonachi")
# async def Kutubxonachi(message: Message):
#     await message.reply(f"Kutubxonachi – kitoblar va axborot resurslarini boshqaruvchi mutaxassis. Tarixan, qadimgi Aleksandriya kutubxonasi eng mashhur edi. Ta’lim: kutubxonashunoslik bakalavr. Ko‘nikmalar: kataloglash, foydalanuvchilar bilan ishlash. Kundalik vazifalar: kitoblarni tartibga solish, o‘quvchilarga yordam berish. Kasb yo‘llari: maktab, universitet, davlat kutubxonasi. O‘rtacha maosh: $45,000+. Ish bozori: barqaror, lekin raqamli texnologiyalar ta’sirida. Qiyinchiliklar: texnologik moslashuv. Kelajak: elektron kutubxonalar.") 


# @dp.message(F.text  == "Tarjimon")
# async def Tarjimon(message: Message):
#     await message.reply(f"Tarjimon – matn yoki nutqni bir tildan boshqasiga o‘girish mutaxassisi. Tarixan, tarjimonlar diplomatiyada muhim bo‘lgan. Ta’lim: tilshunoslik bakalavr. Ko‘nikmalar: til bilimi, grammatik to‘g‘rilik, madaniyat tushunchasi. Kundalik vazifalar: matn tarjimasi, sinxron tarjima, subtitrlar tayyorlash. Kasb yo‘llari: xalqaro kompaniya, davlat idorasi, frilanser. O‘rtacha maosh: $50,000+. Ish bozori: xalqaro aloqalar kuchayishi bilan talab oshmoqda. Qiyinchiliklar: murakkab matnlarni tushunish. Kelajak: AI yordamida tezkor tarjimalar.") 


# @dp.message(F.text  == "Jurnalist")
# async def Jurnalistkjhg(message: Message):
#     await message.reply(f"Jurnalist – yangiliklarni to‘plash, tahrirlash va tarqatish bilan shug‘ullanuvchi mutaxassis. Tarixan, birinchi gazeta XVII asrda paydo bo‘lgan. Ta’lim: jurnalistika bakalavr. Ko‘nikmalar: yozish, intervyu olish, tekshirish. Kundalik vazifalar: maqola yozish, intervyu, tadqiqot. Kasb yo‘llari: gazeta, televideniye, onlayn media. O‘rtacha maosh: $50,000+. Ish bozori: raqamli media rivoji bilan o‘zgaruvchan. Qiyinchiliklar: axborot urushi, vaqt bosimi. Kelajak: internet platformalarida ishlash.") 


# @dp.message(F.text  == "Etnograf")
# async def Etnograf(message: Message):
#     await message.reply(f"Etnograf – xalqlar madaniyati va urf-odatlarini o‘rganuvchi mutaxassis. Tarixan, XIX asrda ilmiy yo‘nalish sifatida shakllangan. Ta’lim: etnografiya yoki antropologiya bakalavr. Ko‘nikmalar: dala tadqiqotlari, yozma hisobotlar, madaniy tahlil. Kundalik vazifalar: safar qilish, ma’lumot to‘plash, tadqiqot natijalarini e’lon qilish. Kasb yo‘llari: muzeylar, universitetlar, ilmiy institutlar. O‘rtacha maosh: $55,000+. Ish bozori: ilmiy grantlar orqali. Qiyinchiliklar: uzoq safarlar, til o‘rganish. Kelajak: madaniy merosni raqamlashtirish.") 


# @dp.message(F.text  == "Kartograf")
# async def Kartograf(message: Message):
#     await message.reply(f"Kartograf – xaritalar yaratish va yangilash bilan shug‘ullanuvchi mutaxassis. Tarixan, qadimgi dengizchilar xarita tuzishda ishlatgan. Ta’lim: geoinformatika yoki geografiya bakalavr. Ko‘nikmalar: GIS dasturlari, geodeziya, dizayn. Kundalik vazifalar: joy ma’lumotlarini tahlil qilish, xaritalar chizish. Kasb yo‘llari: davlat geodeziya xizmati, harbiy, turizm kompaniyalari. O‘rtacha maosh: $60,000+. Ish bozori: navigatsiya va logistika sohasida talab mavjud. Qiyinchiliklar: katta hajmdagi ma’lumotlarni qayta ishlash. Kelajak: 3D va interaktiv xaritalar.") 


# @dp.message(F.text  == "Botanist")
# async def Botanist(message: Message):
#     await message.reply(f"Botanist – o‘simliklar hayoti va tuzilishini o‘rganuvchi olim. Tarixan, Karl Linney o‘simliklarni tasniflash tizimini yaratgan. Ta’lim: botanika yoki biologiya bakalavr. Ko‘nikmalar: dala tadqiqotlari, laboratoriya ishlari. Kundalik vazifalar: o‘simlik namunalarini yig‘ish, tahlil qilish, ilmiy maqola yozish. Kasb yo‘llari: qishloq xo‘jaligi, farmatsevtika, ekologiya. O‘rtacha maosh: $55,000+. Ish bozori: biotexnologiya rivoji bilan o‘smoqda. Qiyinchiliklar: dala sharoitida ishlashdagi qiyinchiliklar. Kelajak: genetik o‘simliklar yaratish.") 


# @dp.message(F.text  == "Zoolog")
# async def Zoolog(message: Message):
#     await message.reply(f"Zoolog – hayvonlar biologiyasini o‘rganuvchi mutaxassis. Tarixan, Darvin evolyutsiya nazariyasiga katta hissa qo‘shgan. Ta’lim: zoologiya bakalavr. Ko‘nikmalar: kuzatuv, laboratoriya ishlari, ekologik tahlil. Kundalik vazifalar: hayvonlarni o‘rganish, ma’lumot to‘plash, tahlil. Kasb yo‘llari: milliy bog‘lar, zoologiya institutlari, muzeylar. O‘rtacha maosh: $60,000+. Ish bozori: tabiatni muhofaza qilish sohasida talab yuqori. Qiyinchiliklar: yovvoyi tabiatda ishlashdagi xavflar. Kelajak: dron va sensor texnologiyalari bilan rivojlanadi.") 


# @dp.message(F.text  == "Arxivolog")
# async def Arxivolog(message: Message):
#     await message.reply(f"Arxivolog – qadimiy yozma manbalarni o‘rganadigan mutaxassis. Tarixan, qadimgi qo‘lyozmalarni saqlash va tahlil qilish an’analari mavjud. Ta’lim: tarix yoki filologiya bakalavr. Ko‘nikmalar: paleografiya, tilshunoslik, arxiv ishlari. Kundalik vazifalar: qo‘lyozmalarni o‘qish, tarjima qilish, saqlash. Kasb yo‘llari: muzeylar, universitetlar, ilmiy institutlar. O‘rtacha maosh: $50,000+. Ish bozori: ilmiy grantlarga bog‘liq. Qiyinchiliklar: nozik materiallar bilan ishlash. Kelajak: raqamli saqlash tizimlari.") 


# @dp.message(F.text  == "Paleontolog")
# async def Paleontolog(message: Message):
#     await message.reply(f"Paleontolog – qazilma hayvonlar va o‘simliklarni o‘rganadigan olim. Tarixan, dinozavr suyaklarini topish bilan mashhur bo‘lgan. Ta’lim: paleontologiya yoki geologiya bakalavr. Ko‘nikmalar: qazish, tahlil, rekonstruksiya. Kundalik vazifalar: qazilma qoldiqlarni topish, laboratoriyada tekshirish. Kasb yo‘llari: muzeylar, ilmiy institutlar, universitetlar. O‘rtacha maosh: $60,000+. Ish bozori: cheklangan, ammo ilmiy tadqiqotlar orqali mavjud. Qiyinchiliklar: uzoq safarlar. Kelajak: 3D rekonstruksiya texnologiyalari.") 


# @dp.message(F.text  == "Fizikoterapevt")
# async def Fizikoterapevt(message: Message):
#     await message.reply(f"Fizikoterapevt – bemorlarni jismoniy mashqlar va usullar bilan davolovchi mutaxassis. Tarixan, tibbiy reabilitatsiya XX asrda keng rivojlandi. Ta’lim: fizioterapiya bakalavr. Ko‘nikmalar: anatomiyani bilish, reabilitatsiya metodlari. Kundalik vazifalar: mashqlar belgilash, massaj, fizioterapiya usullarini qo‘llash. Kasb yo‘llari: kasalxona, sport klubi, reabilitatsiya markazi. O‘rtacha maosh: $70,000+. Ish bozori: tibbiyot sohasida yuqori talab. Qiyinchiliklar: bemor bilan doimiy ishlash. Kelajak: robotik reabilitatsiya texnologiyalari.") 


# @dp.message(F.text  == "Genetik")
# async def Genetik(message: Message):
#     await message.reply(f"Genetik – irsiyat va DNK tuzilishini o‘rganadigan olim. Tarixan, Gregor Mendel genetika asoschisi. Ta’lim: genetika yoki biologiya magistr. Ko‘nikmalar: laboratoriya ishlari, genetik tahlil. Kundalik vazifalar: DNK tekshirish, genetik kasalliklarni aniqlash. Kasb yo‘llari: biotexnologiya, tibbiyot, ilmiy institutlar. O‘rtacha maosh: $80,000+. Ish bozori: tibbiy diagnostika va biotexnologiya rivoji bilan kuchli. Qiyinchiliklar: murakkab ilmiy jarayonlar. Kelajak: gen muhandisligi va CRISPR texnologiyasi") 


# @dp.message(F.text  == "Mikrobiolog")
# async def Mikrobiolog(message: Message):
#     await message.reply(f"Mikrobiolog – mikroorganizmlarni o‘rganuvchi mutaxassis. Tarixan, Lui Paster mikrobiologiya asoschilaridan. Ta’lim: mikrobiologiya yoki biologiya bakalavr. Ko‘nikmalar: mikroskop ishlatish, laboratoriya usullari. Kundalik vazifalar: bakteriya, virus va zamburug‘larni tahlil qilish. Kasb yo‘llari: tibbiyot, oziq-ovqat sanoati, ekologiya. O‘rtacha maosh: $65,000+. Ish bozori: tibbiyot va farmatsevtika sohalarida yuqori. Qiyinchiliklar: infektsiya xavfi. Kelajak: vaksina va antibiotik ishlab chiqish.") 


# @dp.message(F.text  == "Akustik")
# async def Akustikt(message: Message):
#     await message.reply(f"Akustik – tovush fizikasi va texnologiyasini o‘rganuvchi mutaxassis. Tarixan, bu soha musiqa va muhandislikda qo‘llanilgan. Ta’lim: akustika yoki fizika bakalavr. Ko‘nikmalar: tovush o‘lchash, signal tahlili. Kundalik vazifalar: akustik tizimlar loyihalash, shovqin izolyatsiyasi. Kasb yo‘llari: studiyalar, qurilish, transport sanoati. O‘rtacha maosh: $70,000+. Ish bozori: ovoz texnologiyalari rivoji bilan o‘smoqda. Qiyinchiliklar: maxsus uskunalar bilan ishlash. Kelajak: 3D audio va virtual haqiqat.") 


# @dp.message(F.text == "Optik")
# async def optik(message: Message):
#     await message.reply(f"Optik – yorug‘lik va optik tizimlarni o‘rganuvchi mutaxassis. Tarixan, Ibn al-Haysam optika ilmida muhim kashfiyotlar qilgan. Ta’lim: optika yoki fizika bakalavr. Ko‘nikmalar: linza dizayni, yorug‘lik tahlili. Kundalik vazifalar: optik asboblar ishlab chiqish, nazorat qilish. Kasb yo‘llari: tibbiyot, astronomiya, texnologiya kompaniyalari. O‘rtacha maosh: $75,000+. Ish bozori: lazer texnologiyasi va tibbiyotda yuqori talab. Qiyinchiliklar: murakkab texnik ishlanmalar. Kelajak: kvant optikasi va AR texnologiyalari.")


# @dp.message(F.text == "Akustik muhandis")
# async def Akustik(message: Message):
#     await message.reply(f"Akustik muhandis — Konsert zallari, kinoteatrlar, yozuv studiyalari va boshqa joylarda tovush sifatini oshirish uchun akustik tizimlarni loyihalash, ovoz tarqalishini hisoblash va optimallashtirish bilan shug‘ullanadi, maxsus dasturlar va fizik qonunlardan foydalanadi, shuningdek, qurilish jarayonida tovush izolyatsiyasini ta’minlashda ishtirok etadi.")


# @dp.message(F.text == "Dron operatori")
# async def operatori(message: Message):
#     await message.reply(f"Dron operatori — Turli sohalarda qo‘llaniladigan dronlarni masofadan boshqaradi, yuqori sifatli foto va video suratga olish, xaritalash, qutqaruv, qishloq xo‘jaligi monitoringi kabi vazifalarni bajaradi, parvoz qoidalariga amal qiladi va maxsus boshqaruv texnologiyalaridan foydalangan holda xavfsiz uchishni ta’minlaydi.")


# @dp.message(F.text == "Kiberxavfsizlik mutaxassisi")
# async def Kiberxavfsizlik(message: Message):
#     await message.reply(f"Kiberxavfsizlik mutaxassisi — Kompaniya yoki tashkilotning kompyuter tizimlarini xakerlik hujumlari, viruslar va ma’lumot o‘g‘irlanishidan himoya qiladi, xavfsizlik protokollarini ishlab chiqadi, tizimlarni muntazam tekshiradi, xavfli kirishlarni aniqlaydi hamda hodisalarga tezkor javob berish uchun maxsus dasturiy vositalardan foydalanadi.")


# @dp.message(F.text == "Virtual reallik dizayneri")
# async def reallik(message: Message):
#     await message.reply(f"Virtual reallik dizayneri — VR texnologiyalari asosida interaktiv o‘yinlar, trening simulyatorlari yoki ta’lim platformalarini yaratadi, foydalanuvchi uchun immersiv tajriba ta’minlaydigan grafik elementlar, sahnalar va muhitlarni ishlab chiqadi, 3D modellashtirish dasturlari va maxsus kodlash vositalaridan foydalanadi.")


# @dp.message(F.text == "Biotexnolog")
# async def Biotexnolog(message: Message):
#     await message.reply(f"Biotexnolog — Biologiya va kimyo bilimlarini qo‘llab, tirik organizmlar asosida dori vositalari, o‘g‘itlar, oziq-ovqat mahsulotlari va ekologik toza texnologiyalar ishlab chiqaradi, genetik modifikatsiya, fermentatsiya va hujayra texnologiyalarini o‘rganadi hamda laboratoriya tajribalarini o‘tkazadi.")


# @dp.message(F.text == "Kriptovalyuta treyderi")
# async def Kriptovalyuta(message: Message):
#     await message.reply(f"Kriptovalyuta treyderi — Bitcoin, Ethereum va boshqa kriptovalyutalar bozorida narxlar o‘zgarishini tahlil qilib, foyda olish maqsadida xarid va sotuv operatsiyalarini amalga oshiradi, texnik va fundamental tahlil usullaridan foydalanadi, risklarni boshqaradi hamda global kripto yangiliklarini kuzatib boradi.")


# @dp.message(F.text == "Kosmetik kimyogar")
# async def Kosmetik(message: Message):
#     await message.reply(f"Kosmetik kimyogar — Krem, shampun, parfyum va boshqa kosmetik mahsulotlar tarkibini ishlab chiqadi, ingredientlarning bir-biriga mosligini tekshiradi, laboratoriya sharoitida formulalar sinovdan o‘tkazadi, xavfsizlik va sifat standartlariga amal qiladi hamda yangi mahsulotlar yaratish jarayonini boshqaradi.")


# @dp.message(F.text == "Nanotexnolog mutaxassisi")
# async def Nanotexnolog(message: Message):
#     await message.reply(f"Nanotexnolog mutaxassisi — Atom va molekula miqyosida yangi materiallar, tibbiyot vositalari yoki elektron qurilmalarni yaratadi, nanostrukturalar ustida ishlaydi, tajriba laboratoriyalarida zamonaviy asbob-uskunalardan foydalanadi va ilmiy izlanishlarni amalga oshiradi, texnologiyani amaliyotga joriy etadi.")


# @dp.message(F.text == "Logist")
# async def Logist(message: Message):
#     await message.reply(f"Logist — Tovarlarni ishlab chiqaruvchidan mijozga yetkazish jarayonini rejalashtiradi, transport, saqlash va taqsimlash tizimlarini optimallashtiradi, xarajatlarni kamaytiradi, yetkazib berish muddatiga rioya qilinishini nazorat qiladi hamda xalqaro savdo va bojxona qoidalarini hisobga oladi.")


# @dp.message(F.text == "Kiberforensika mutaxassisi")
# async def Kiberforensika(message: Message):
#     await message.reply(f"Kiberforensika mutaxassisi — Kompyuter jinoyatlarini tergov qiladi, raqamli dalillarni yig‘adi va tahlil qiladi, sud jarayonlari uchun isbotlar tayyorlaydi, shifrlangan yoki o‘chirilgan ma’lumotlarni tiklaydi, tarmoqlar va qurilmalarda noqonuniy faoliyat izlarini aniqlaydi hamda xavfsizlikni mustahkamlash bo‘yicha tavsiyalar beradi.")


# @dp.message(F.text == "Aeroport xavfsizlik inspektori")
# async def xavfsizlik(message: Message):
#     await message.reply(f"Aeroport xavfsizlik inspektori — Aeroportdagi yo‘lovchilar, yuklar va samolyotlarga xizmat ko‘rsatish jarayonida xavfsizlik qoidalariga rioya qilinishini tekshiradi, metall detektorlar, rentgen apparatlari va boshqa skanerlash uskunalarini boshqaradi, noqonuniy yoki xavfli buyumlarni aniqlash va oldini olish bo‘yicha choralar ko‘radi.")


# @dp.message(F.text == "Ekologik siyosat bo‘yicha maslahatchi")
# async def maslahatchi(message: Message):
#     await message.reply(f"Ekologik siyosat bo‘yicha maslahatchi — Hukumat yoki kompaniyalar uchun atrof-muhitni muhofaza qilish siyosatini ishlab chiqadi, ekologik qonunlarga muvofiqlikni ta’minlaydi, chiqindilarni kamaytirish, energiya samaradorligini oshirish va iqlim o‘zgarishiga moslash bo‘yicha strategiyalarni ishlab chiqishda ishtirok etadi.")


# @dp.message(F.text == "Animatronika muhandisi")
# async def Animatronika(message: Message):
#     await message.reply(f"Animatronika muhandisi — Kino, ko‘ngilochar parklar yoki teatr uchun robot hayvonlar va mexanik figuralarni loyihalash, yig‘ish va boshqarish bo‘yicha ishlaydi, mexanika, elektronika va dasturlash bilimlarini birlashtiradi hamda jonli ko‘rinishli harakatlar yaratadi.")


# @dp.message(F.text == "Kiberpsixolog")
# async def Kiberpsixolog(message: Message):
#     await message.reply(f"Kiberpsixolog — Internet va raqamli texnologiyalarning inson psixologiyasiga ta’sirini o‘rganadi, onlayn xulq-atvor, ijtimoiy tarmoqlardagi odatlar va kibermuloqot jarayonlarini tahlil qiladi, psixologik muammolarni hal qilishda texnologik yondashuvlardan foydalanadi.")


# @dp.message(F.text == "Qayta tiklanuvchi energiya tizimlari muhandisi")
# async def tizimlari(message: Message):
#     await message.reply(f"Qayta tiklanuvchi energiya tizimlari muhandisi — Quyosh panellari, shamol turbinalari va boshqa yashil energiya manbalarini loyihalash, o‘rnatish va texnik xizmat ko‘rsatish bilan shug‘ullanadi, ekologik ta’sirni kamaytirish va energiya samaradorligini oshirish bo‘yicha innovatsion yechimlar ishlab chiqadi.")


# @dp.message(F.text == "Aerojinoyat tergovchisi")
# async def Aerojinoyat(message: Message):
#     await message.reply(f"Aerojinoyat tergovchisi — Samolyotlar va aviatsiya sohasida sodir bo‘lgan jinoyatlarni tekshiradi, samolyot bortidagi voqealarni, qoidabuzarliklarni yoki xavfsizlikka tahdidlarni aniqlash va bartaraf etish bo‘yicha tergov o‘tkazadi, xalqaro aviatsiya qonunlariga amal qiladi.")


# @dp.message(F.text == "Sun’iy organlar dizayneri")
# async def organlar(message: Message):
#     await message.reply(f"Sun’iy organlar dizayneri — Biotexnologiya va muhandislikni birlashtirib, inson tanasi uchun sun’iy yurak, buyrak, protez va boshqa a’zolarni ishlab chiqadi, tibbiyotda foydalanish uchun xavfsiz va mos materiallardan foydalanadi, klinik sinovlarda ishtirok etadi.")


# @dp.message(F.text == "Data etikasi bo‘yicha mutaxassis")
# async def mutaxassis(message: Message):
#     await message.reply(f"Data etikasi bo‘yicha mutaxassis — Ma’lumotlarni yig‘ish, saqlash va qayta ishlashda axloqiy qoidalarga rioya qilinishini ta’minlaydi, shaxsiy ma’lumotlarni himoya qilish, xolis algoritmlar yaratish va sun’iy intellektni adolatli ishlatish bo‘yicha siyosatlar ishlab chiqadi.")


# @dp.message(F.text == "Suv osti dron texnigi")
# async def dron(message: Message):
#     await message.reply(f"Suv osti dron texnigi — Dengiz va ko‘llarni o‘rganish, suv ostidagi infratuzilmani tekshirish yoki qutqaruv ishlarida foydalaniladigan masofadan boshqariladigan dronlarni sozlash, boshqarish va ta’mirlash bilan shug‘ullanadi, maxsus kamera va sensorlardan foydalanadi.")


# @dp.message(F.text == "Geoinformatsion tizim (GIS) analitigi")
# async def GIS(message: Message):
#     await message.reply(f"Geoinformatsion tizim (GIS) analitigi — Yer yuzasiga oid ma’lumotlarni yig‘ish, xaritalash va tahlil qilishda maxsus dasturlar (ArcGIS, QGIS) bilan ishlaydi, shahar rejalashtirish, ekologiya, transport va favqulodda vaziyatlar boshqaruvida foydalaniladigan geografik ma’lumotlar bazalarini yaratadi.")


# @dp.message(F.text == "Kosmik qutqaruvchi")
# async def Kosmik(message: Message):
#     await message.reply(f"Kosmik qutqaruvchi — Orbitada yoki kosmik stansiyalarda yuz bergan favqulodda vaziyatlarda yordam berish uchun tayyorlangan mutaxassis bo‘lib, astronavtlarni evakuatsiya qilish, texnik nosozliklarni bartaraf etish va hayotiy tizimlarni tiklash bo‘yicha maxsus kosmik texnologiyalar va mashg‘ulotlardan foydalanadi.")


# @dp.message(F.text == "Neyrointerfeys muhandisi")
# async def Neyrointerfeys(message: Message):
#     await message.reply(f"Neyrointerfeys muhandisi — Inson miyasi bilan kompyuter yoki robot qurilmalari o‘rtasida aloqa o‘rnatadigan tizimlarni ishlab chiqadi, neyrosignallarni o‘qish va boshqarish texnologiyalarini yaratadi, tibbiyot va reabilitatsiyada qo‘llaniladigan innovatsion interfeyslarni loyihalaydi.")



# @dp.message(F.text == "Suv osti arxeologi")
# async def soz83(message: Message):
#     await message.reply(f"Suv osti arxeologi — Dengiz, ko‘l va daryo tubidagi qadimiy kemalar, shaharlar va artefaktlarni izlab topadi, ularni ilmiy jihatdan o‘rganadi, maxsus sho‘ng‘ish uskunalari va suv osti xaritalash texnologiyalaridan foydalanadi, topilmalarni saqlash va restavratsiya qilish ishlarini olib boradi")


# @dp.message(F.text == "Elektromobil texnigi")
# async def soz84(message: Message):
#     await message.reply(f"Elektromobil texnigi — Elektr transport vositalarini ta’mirlash, batareyalarini diagnostika qilish va yangilash bilan shug‘ullanadi, energiya samaradorligini oshirish bo‘yicha ishlaydi, zamonaviy elektrotexnika vositalaridan foydalanib, ekologik toza transport infratuzilmasini qo‘llab-quvvatlaydi.")


# @dp.message(F.text == "Oziq-ovqat dizayneri")
# async def soz85(message: Message):
#     await message.reply(f"Oziq-ovqat dizayneri — Restoran, oziq-ovqat brendlari yoki media uchun taomlarning ko‘rinishini jozibador qilish, rang, shakl va taqdimot usullarini yaratish bilan shug‘ullanadi, badiiy va gastronomik mahoratni uyg‘unlashtiradi, reklama va fotosuratlarda ishlatiladigan taomlarni tayyorlaydi.")


# @dp.message(F.text == "Iqlim modellovchi")
# async def soz86(message: Message):
#     await message.reply(f"Iqlim modellovchi — Atmosfera, okean va yer tizimlarining o‘zaro ta’sirini matematik modellar yordamida o‘rganadi, kelajakdagi iqlim o‘zgarishlarini bashorat qiladi, hukumat va tadqiqot markazlariga ekologik strategiyalar ishlab chiqishda yordam beradi.")


# @dp.message(F.text == "Xalqaro protokol bo‘yicha mutaxassis")
# async def soz87(message: Message):
#     await message.reply(f"Xalqaro protokol bo‘yicha mutaxassis — Diplomatik uchrashuvlar, konferensiyalar va rasmiy marosimlarni tashkil qiladi, xalqaro odob-axloq qoidalariga amal qilinishini ta’minlaydi, davlat vakillari va mehmonlar uchun barcha tashkiliy detallarni puxta rejalashtiradi.")


# @dp.message(F.text == "Biometrik tizimlar muhandisi")
# async def soz88(message: Message):
#     await message.reply(f"Biometrik tizimlar muhandisi — Barmoq izi, yuz tanish, ovoz identifikatsiyasi kabi texnologiyalarni ishlab chiqadi, xavfsizlik tizimlariga joriy etadi, biometrik ma’lumotlarni saqlash va ishlov berishda yuqori darajada maxfiylikni ta’minlaydi.")


# @dp.message(F.text == "Golografik kontent yaratuvchisi")
# async def soz89(message: Message):
#     await message.reply(f"Golografik kontent yaratuvchisi — 3D gologramma texnologiyalari yordamida ko‘rgazma, reklama yoki ta’lim uchun vizual materiallar tayyorlaydi, maxsus dasturiy ta’minot va lazer texnologiyalaridan foydalanadi, foydalanuvchi uchun realistik uch o‘lchamli tajriba yaratadi.")


# @dp.message(F.text == "Kosmik qishloq xo‘jaligi mutaxassisi")
# async def soz90(message: Message):
#     await message.reply(f"Kosmik qishloq xo‘jaligi mutaxassisi — Kosmosda yoki boshqa sayyoralarda oziq-ovqat yetishtirish texnologiyalarini ishlab chiqadi, yopiq ekotizimlar, gidroponika va sun’iy yorug‘lik tizimlarini qo‘llaydi, astronavtlar uchun barqaror oziq-ovqat ta’minotini ta’minlaydi.")


# @dp.message(F.text == "Genetik maslahatchi")
# async def soz91(message: Message):
#     await message.reply(f"Genetik maslahatchi — Inson genetik ma’lumotlarini tahlil qiladi, irsiy kasalliklar xavfi haqida tavsiyalar beradi, oilaviy rejalashtirish va tibbiy qarorlar qabul qilishda yordam beradi, DNK diagnostikasi va molekulyar biologiya usullaridan foydalanadi.")


# @dp.message(F.text == "Sun’iy intellekt etikasi bo‘yicha ekspert")
# async def soz92(message: Message):
#     await message.reply(f"Sun’iy intellekt etikasi bo‘yicha ekspert — AI tizimlarining adolatli, xolis va xavfsiz ishlashini ta’minlash bo‘yicha siyosatlar ishlab chiqadi, diskriminatsiya va noto‘g‘ri qarorlar xavfini kamaytiradi, algoritmik shaffoflik ustida ishlaydi.")


# @dp.message(F.text == "Vulkanolog")
# async def soz93(message: Message):
#     await message.reply(f"Vulkanolog — Vulkan faoliyatini o‘rganadi, otilish xavfini baholaydi, seysmik va geotermal ma’lumotlarni tahlil qiladi, aholini ogohlantirish tizimlarini ishlab chiqadi va favqulodda vaziyatlarda xavfsizlik choralarini belgilaydi.")


# @dp.message(F.text == "Bioinformatik")
# async def soz94(message: Message):
#     await message.reply(f"Bioinformatik — Genom ma’lumotlari va biologik tizimlarni kompyuter orqali tahlil qiladi, katta hajmdagi biologik ma’lumotlarni qayta ishlash, yangi dorilar yaratish va kasalliklarni aniqlashda algoritmlar ishlab chiqadi.")                      



# @dp.message(F.text == "Astronomik ma’lumotlar analitigi")
# async def soz95(message: Message):
#     await message.reply(f"Astronomik ma’lumotlar analitigi — Teleskop va sun’iy yo‘ldoshlar orqali olingan kosmik ma’lumotlarni tahlil qiladi, yangi sayyoralar, yulduz tizimlari yoki galaktikalarni aniqlash uchun ilmiy modellarni qo‘llaydi.")



# @dp.message(F.text == "Robot psixologi ")
# async def soz96(message: Message):
#     await message.reply(f"Robot psixologi — Inson va robot o‘rtasidagi muloqot jarayonini o‘rganadi, foydalanuvchi tajribasini yaxshilash uchun robotlarning xatti-harakat algoritmlarini optimallashtiradi, ijtimoiy robotlar uchun moslashuvchan kommunikatsiya usullarini ishlab chiqadi.")



# @dp.message(F.text == "Chuqur suv muhandisi ")
# async def soz97(message: Message):
#     await message.reply(f"Chuqur suv muhandisi — Okean tubida infratuzilmalarni qurish, quvur liniyalari va energetika tizimlarini o‘rnatish bilan shug‘ullanadi, ekstremal suv bosimi va past harorat sharoitida ishlash texnologiyalarini ishlab chiqadi.")



# @dp.message(F.text == "Metaverse arxitektori")
# async def soz98(message: Message):
#     await message.reply(f"Metaverse arxitektori — Virtual dunyolarni loyihalash, foydalanuvchilar uchun interaktiv makonlar yaratish, iqtisodiy tizimlar va virtual mulk tuzilmalarini ishlab chiqish bilan shug‘ullanadi, 3D dizayn va dasturlashni uyg‘unlashtiradi.")



# @dp.message(F.text == "Quyosh nuri muhandisi")
# async def soz99(message: Message):
#     await message.reply(f"Quyosh nuri muhandisi — Quyosh energiyasini maksimal samarada yig‘ish va taqsimlash tizimlarini ishlab chiqadi, innovatsion panellar va energiya saqlash usullarini yaratadi, ekologik toza energiya manbalarini kengaytiradi.")
 



# @dp.message(F.text == "Atmosfera kimyogari ")
# async def atmosfera100(message: Message):
#     await message.reply("Atmosfera kimyogari — Havodagi gazlar, aerozollar va boshqa moddalarni o‘rganadi, iqlim o‘zgarishi, ifloslanish va ekologik xavf omillarini tahlil qiladi, atmosfera sifatini yaxshilash uchun ilmiy tavsiyalar ishlab chiqadi.")


# @dp.message(F.text == "Raqamli marketing analitigi")
# async def hechnima(message: Message):
#     await message.reply("bu onlayn marketing faoliyati natijalarini ma’lumotlar asosida tahlil qilish va optimallashtirish jarayoni. U veb-sayt trafigi, mijozlar harakati, konversiya darajalari, ROI va boshqa ko‘rsatkichlarni kuzatish orqali marketing strategiyasini samaraliroq qilishga yordam beradi. Asosiy vositalar: Google Analytics, CRM tizimlar, A/B testlar va SEO monitoring. Maqsad – xarajatlarni kamaytirib, sotuvlarni oshirish.")


# @dp.message(F.text == "Kiberxavfsizlik bo‘yicha insident javob beruvchi")
# async def hshshhsh(message: Message):
#     await message.reply("Kiberxavfsizlik insidentiga javob beruvchi – bu tarmoq hujumlari, maʼlumotlar buzilishi yoki boshqa xavfli hodisalar sodir boʻlganda ularni tez aniqlash, zararni kamaytirish va tizimni tiklash uchun javob choralarini koʻradigan mutaxassis.")


# @dp.message(F.text == "Sun’iy organ ishlab chiqaruvchi muhandis")
# async def asdfghjkl(message: Message):
#     await message.reply("Sun'iy organlar ishlab chiqaruvchi muhandis – bu tibbiyot va texnologiyani birlashtirib, amputatsiya qilingan yoki nogironlikka ega bo'lgan odamlar uchun funksional protezlar va implantlar yaratuvchi mutaxassis. Ular biomexanika, materialshunoslik va elektronika sohalaridagi bilimlaridan foydalanadi.")



# @dp.message(F.text == "Ekolog")
# async def sxdfcgvhbjn(message: Message):
#     await message.reply("Ekolog – tabiatni muhofaza qilish, atrof-muhitni o‘rganish va ekologik muammolarni hal etish bilan shug‘ullanuvchi mutaxassis. U havo, suv, tuproq holatini kuzatadi, ifloslanishni kamaytirish choralarini ishlab chiqadi va inson faoliyatining tabiatga ta’sirini baholaydi.")


# @dp.message(F.text == "Navigatsion")
# async def fghuklcjcxk(message: Message):
#     await message.reply("Navigatsion – kema, samolyot yoki boshqa transport vositalarining to‘g‘ri yo‘nalishda harakatlanishini ta’minlovchi soha. Bu kasb egalari xarita, kompas, GPS va boshqa navigatsiya uskunalaridan foydalanib, xavfsiz va aniq manzilga yetib borishni tashkil qiladi.")  



# @dp.message()
# async def hechnarsa(message: Message):
#     await message.reply("ro'yxatdagi kasb nomini kiriting")


    
# async def main():
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("\nGoodbye")


# run.py

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        "Sizga qaysi kasb qiziq, nomini yozing\n\n"
        "Kasblar nomi:\n\n"
        "- Dasturchi\n"
        "- Shifokor\n"
        "- O'qituvchi\n"
        "- Muhandis\n"
        "- Sotuvchi\n"
        "- Jurnalist\n"
        "- Haydovchi\n"
        "- Oshpaz\n"
        "- Advokat\n"
        "- San'atkor\n"
        "- Buxgalter\n"
        "- Elektrik\n"
        "- Uchuvchi\n"
        "- Ofitsiant\n"
        "- Mekanik\n"
        "- Hamshira\n"
        "- Veterinar\n"
        "- Rassom\n"
        "- Musiqachi\n"
        "- Aktyor\n"
        "- Arxeolog\n"
        "- Astronom\n"
        "- Biolog\n"
        "- Geolog\n"
        "- Kimyogar\n"
        "- Fizik\n"
        "- Farmatsevt\n"
        "- Arxitektor\n"
        "- Toksikolog\n"
        "- Antropolog\n"
        "- Meteorolog\n"
        "- Kriptograf\n"
        "- Psixolog\n"
        "- Sotsiolog\n"
        "- Arxivchi\n"
        "- Kutubxonachi\n"
        "- Tarjimon\n"
        "- Kartograf\n"
        "- Botanist\n"
        "- Zoolog\n"
        "- Arxivolog\n"
        "- Paleontolog\n"
        "- Fizikoterapevt\n"
        "- Genetik\n"
        "- Mikrobiolog\n"
        "- Akustik\n"
        "- Optik\n"
        "- Navigatsion\n"
        "- Agronom\n"
        "- Ekolog\n"
        "- Mineralog\n"
        "- Vulkanolog\n"
        "- Hidrolog\n"
        "- Okeanolog\n"
        "- Astronavt\n"
        "- Kosmolog\n"
        "- Operator\n"
        "- Akustik muhandis\n"
        "- Dron operatori\n"
        "- Kiberxavfsizlik mutaxassisi\n"
        "- Virtual reallik dizayneri\n"
        "- Biotexnolog\n"
        "- Kriptovalyuta treyderi\n"
        "- Nanotexnolog mutaxassisi\n"
        "- Logist\n"
        "- Kiberforensika mutaxassisi\n"
        "- Podkast prodyuseri\n"
        "- Mobil ilova testlovchi\n"
        "- Blokcheyn dasturchisi\n"
        "- Esport murabbiyi\n"
        "- Uy kinoteatri montajchisi\n"
        "- UAV texnikasi\n"
        "- Astronavt tayyorgarlik instruktori\n"
        "- Kiberpsixolog\n"
        "- Data-jurnalist\n"
        "- Sensor texnolog mutaxassisi\n"
        "- Sun'iy intellekt etikasi bo'yicha ekspert\n"
        "- Eko-qurilish muhandisi\n"
        "- 3D chop etish texnologi\n"
        "- Biometrik tizim muhandisi\n"
        "- Big Data tahlilchisi\n"
        "- Kosmik qoldiqlar mutaxassisi\n"
        "- Neurointerfeys dizayneri\n"
        "- Kiberxavfsizlik auditori\n"
        "- Gamifikatsiya mutaxassisi\n"
        "- Vertikal qishloq xo'jaligi mutaxassisi\n"
        "- Kosmik turizm gid\n"
        "- Energiya samaradorligi bo'yicha konsultant\n"
        "- Avtonom transport muhandisi\n"
        "- Aqlli uy tizimlari mutaxassisi\n"
        "- Genetik maslahatchi\n"
        "- Raqamli marketing analitigi\n"
        "- Sun'iy organ ishlab chiqaruvchi muhandis\n"
        "- Ovoz effektlari (Foley) mutaxassisi\n"
        "- Kiberxavfsizlik bo'yicha insident javob beruvchi\n"
    )
    await message.answer(text)

# Profession handlers (100 unique professions)
@dp.message(F.text == "Dasturchi")
async def Dasturchi(message: Message):
    await message.reply("Dasturchi - kompyuter dasturlari va ilovalarini yaratuvchi mutaxassis bo'lib, kod yozish, xatolarni tuzatish va tizimlarni optimallashtirish bilan shug'ullanadi. Tarixan, bu kasb 1940-yillarda kompyuterlar paydo bo'lishi bilan boshlangan, Ada Lovelace birinchi algoritmni yozgan. Ta'lim: kompyuter fanlari bo'yicha bakalavr darajasi, Python, Java kabi tillar o'rganish. Ko'nikmalar: mantiqiy fikrlash, muammo hal qilish, jamoaviy ish. Kundalik vazifalar: dastur loyihalash, test qilish, yangilash. Kasb yo'llari: IT kompaniyalarida, startup'larda yoki frilanser sifatida. O'rtacha maosh: $80,000–$120,000 (mamlakatga qarab). Ish bozori: yuqori talab, AI va mobil ilovalar tufayli o'sish prognoz qilingan. Qiyinchiliklar: tez o'zgaruvchan texnologiyalar, uzoq ish soatlari. Kelajak: AI integratsiyasi bilan yanada muhim bo'ladi.")

@dp.message(F.text == "Shifokor")
async def Shifokor(message: Message):
    await message.reply("Shifokor - inson salomatligini saqlash va davolash bilan shug'ullanuvchi tibbiy mutaxassis. Tarixiy jihatdan, Gippokrat tibbiyot otasi hisoblanadi. Ta'lim: tibbiyot universitetida 6-8 yil o'qish, keyin internatura. Ko'nikmalar: anatomiya bilimi, tashxis qo'yish, etika. Kundalik vazifalar: bemorlarni ko'rikdan o'tkazish, dori yozish, operatsiyalar. Kasb yo'llari: umumiy shifokor, jarroh yoki mutaxassis (kardiolog va h.k.). O'rtacha maosh: $150,000+. Ish bozori: doimiy tanqislik, aholi qarishi tufayli o'sish. Qiyinchiliklar: stress, uzoq navbatchilik, emotsional yuk. Kelajak: telemeditsina va AI yordami bilan rivojlanadi.")

@dp.message(F.text == "O'qituvchi")
async def Oqituvchi(message: Message):
    await message.reply("O'qituvchi - bilim berish va tarbiya qilish bilan band bo'lgan pedagog. Tarixan, qadimiy Yunonistonda Sokrat kabi shaxslar bor. Ta'lim: pedagogika bakalavr, litsenziya. Ko'nikmalar: dars rejalashtirish, motivatsiya, psixologiya. Kundalik vazifalar: dars o'tkazish, baholash, ota-onalar bilan muloqot. Kasb yo'llari: maktab o'qituvchisi, universitet lektor. O'rtacha maosh: $40,000–$60,000. Ish bozori: pensiyaga chiqish tufayli o'rinlar ko'p. Qiyinchiliklar: katta sinflar, burn-out. Kelajak: onlayn ta'lim bilan yangi imkoniyatlar")

@dp.message(F.text == "Muhandis")
async def Muhandis(message: Message):
    await message.reply("Muhandis - texnika va qurilish loyihalarini ishlab chiqish bilan shug'ullanadi. Tarixan, Arximed kabi qadimiylar. Ta'lim: muhandislik bakalavr, matematika. Ko'nikmalar: dizayn, tahlil, loyiha boshqaruvi. Kundalik vazifalar: chizmalar yaratish, sinovlar. Kasb yo'llari: fuqaro, mexanika, elektr muhandisi. O'rtacha maosh: $80,000+. Ish bozori: infratuzilma loyihalari tufayli talab yuqori. Qiyinchiliklar: xavfsizlik, ekologiya. Kelajak: yashil texnologiyalar bilan o'sadi.")

@dp.message(F.text == "Sotuvchi")
async def Sotuvchi(message: Message):
    await message.reply("Sotuvchi - tovar va xizmatlarni sotish bilan shug'ullanadi. Tarixan, savdo qadimdan mavjud. Ta'lim: savdo yoki marketing. Ko'nikmalar: muloqot, muzokara. Kundalik vazifalar: mijozlar bilan ish, shartnoma tuzish. Kasb yo'llari: do'kon sotuvchisi, menejer. O'rtacha maosh: $40,000+ komissiya. Ish bozori: elektron savdo bilan o'sish. Qiyinchiliklar: raqobat, rad etilish. Kelajak: onlayn platformalar.")

@dp.message(F.text == "Jurnalist")
async def Jurnalist(message: Message):
    await message.reply("Jurnalist - yangiliklar to'plash va tarqatish mutaxassisi. Tarixan, 17-asr gazetalari. Ta'lim: jurnalistika bakalavr. Ko'nikmalar: yozish, intervyu. Kundalik vazifalar: tadqiqot, maqola yozish. Kasb yo'llari: reportyor, muharrir. O'rtacha maosh: $50,000+. Ish bozori: digital media bilan o'zgarish. Qiyinchiliklar: fake news, xavf. Kelajak: ijtimoiy tarmoqlar.")

@dp.message(F.text == "Haydovchi")
async def Haydovchi(message: Message):
    await message.reply("Haydovchi - transport vositalarini boshqaruvchi. Tarixan, 19-asr avtomobillari. Ta'lim: haydovchilik guvohnomasi. Ko'nikmalar: xavfsizlik, navigatsiya. Kundalik vazifalar: yo'l qoidalari, yuk tashish. Kasb yo'llari: taksi, yuk haydovchisi. O'rtacha maosh: $40,000+. Ish bozori: logistika o'sishi. Qiyinchiliklar: charchoq, baxtsiz hodisalar. Kelajak: avtonom mashinalar.")

@dp.message(F.text == "Oshpaz")
async def Oshpaz(message: Message):
    await message.reply("Oshpaz - ovqat tayyorlash mutaxassisi. Tarixan, qadimiy oshxonalar. Ta'lim: kulinar maktabi. Ko'nikmalar: retseptlar, gigiena. Kundalik vazifalar: menyular yaratish, pishirish. Kasb yo'llari: restoran oshpazi, shaxsiy. O'rtacha maosh: $40,000+. Ish bozori: turizm bilan o'sish. Qiyinchiliklar: issiq oshxona, vaqt bosimi. Kelajak: vegan tendensiyalari.")

@dp.message(F.text == "Advokat")
async def Advokat(message: Message):
    await message.reply("Advokat - huquqiy himoya qiluvchi. Tarixan, qadimiy Rim. Ta'lim: yuridik fakultet, bar imtihoni. Ko'nikmalar: tahlil, oratorlik. Kundalik vazifalar: sudda himoya, maslahat. Kasb yo'llari: jinoyat, fuqaro advokati. O'rtacha maosh: $100,000+. Ish bozori: barqaror. Qiyinchiliklar: stress, etika. Kelajak: onlayn konsultatsiyalar.")

@dp.message(F.text == "San'atkor")
async def Sanatkor(message: Message):
    await message.reply("San'atkor - ijodiy asarlar yaratuvchi. Tarixan, qadimiy rasmlar. Ta'lim: san'at akademiyasi. Ko'nikmalar: ijodkorlik, texnika. Kundalik vazifalar: rasm chizish, ko'rgazmalar. Kasb yo'llari: rassom, haykaltarosh. O'rtacha maosh: o'zgaruvchan. Ish bozori: galereyalar. Qiyinchiliklar: moliyaviy beqarorlik. Kelajak: digital art.")

@dp.message(F.text == "Buxgalter")
async def Buxgalter(message: Message):
    await message.reply("Buxgalter - moliyaviy hisobotlar yurituvchi. Tarixan, qadimiy hisob kitoblari. Ta'lim: buxgalteriya bakalavr. Ko'nikmalar: matematika, dasturlar. Kundalik vazifalar: hisobotlar, soliqlar. Kasb yo'llari: kompaniya buxgalteri, auditor. O'rtacha maosh: $60,000+. Ish bozori: doimiy talab. Qiyinchiliklar: qonun o'zgarishlari. Kelajak: avtomatizatsiya.")

@dp.message(F.text == "Elektrik")
async def Elektrik(message: Message):
    await message.reply("Elektrchi - elektr tarmoqlarini o'rnatuvchi. Tarixan, Edison zamoni. Ta'lim: texnik kollej. Ko'nikmalar: xavfsizlik, diagrammlar. Kundalik vazifalar: simlar tortish, ta'mirlash. Kasb yo'llari: uy elektrchisi, sanoat. O'rtacha maosh: $50,000+. Ish bozori: qurilish o'sishi. Qiyinchiliklar: xavf, yuqori kuchlanish. Kelajak: yashil energiya.")

@dp.message(F.text == "Uchuvchi")
async def Uchuvchi(message: Message):
    await message.reply("Uchuvchi - samolyot boshqaruvchi. Tarixan, Wright aka-uka. Ta'lim: aviatsiya akademiyasi. Ko'nikmalar: navigatsiya, qaror qabul. Kundalik vazifalar: parvozlar, nazorat. Kasb yo'llari: tijorat, harbiy uchuvchi. O'rtacha maosh: $100,000+. Ish bozori: aviatsiya rivoji. Qiyinchiliklar: jetlag, mas'uliyat. Kelajak: dronlar.")

@dp.message(F.text == "Ofitsiant")
async def Ofitsiant(message: Message):
    await message.reply("Ofitsiant - restoranlarda xizmat ko'rsatuvchi. Tarixan, 18-asr kafe'lar. Ta'lim: tajriba. Ko'nikmalar: muloqot, tezlik. Kundalik vazifalar: buyurtmalar olish, ovqat berish. Kasb yo'llari: barista, menejer. O'rtacha maosh: $30,000+ bahshish. Ish bozori: turizm. Qiyinchiliklar: oyoqda ish, mijozlar. Kelajak: robotlar.")

@dp.message(F.text == "Mekanik")
async def Mekanik(message: Message):
    await message.reply("Mekanik - mashinalarni ta'mirlovchi. Tarixan, sanoat inqilobi. Ta'lim: texnik ta'lim. Ko'nikmalar: diagnostika, asboblar. Kundalik vazifalar: ta'mirlash, sinov. Kasb yo'llari: avto mexanik, sanoat. O'rtacha maosh: $50,000+. Ish bozori: transport o'sishi. Qiyinchiliklar: iflos ish, xavf. Kelajak: elektr mashinalar.")

@dp.message(F.text == "Hamshira")
async def Hamshira(message: Message):
    await message.reply("Hamshira - bemorlarni parvarish qiluvchi. Tarixan, Florence Nightingale. Ta'lim: tibbiy bakalavr. Ko'nikmalar: rahmdillik, tibbiy ko'nikmalar. Kundalik vazifalar: dori berish, monitoring. Kasb yo'llari: kasalxona hamshirasi, uy. O'rtacha maosh: $70,000+. Ish bozori: salomatlik tanqisligi. Qiyinchiliklar: shift ish, emotsiya. Kelajak: telehealth.")

@dp.message(F.text == "Veterinar")
async def Veterinar(message: Message):
    await message.reply("Veterinar - hayvonlarni davolash mutaxassisi. Tarixan, qadimiy fermerlik. Ta'lim: veterinariya doktorligi. Ko'nikmalar: anatomiya, operatsiya. Kundalik vazifalar: ko'rik, emlash. Kasb yo'llari: klinika, zoo. O'rtacha maosh: $90,000+. Ish bozori: uy hayvonlari o'sishi. Qiyinchiliklar: hayvonlar xulqi, evtanaziya. Kelajak: biotexnologiya")

@dp.message(F.text == "Rassom")
async def Rassom(message: Message):
    await message.reply("Rassom - vizual san'at yaratuvchi. Tarixan, Leonardo da Vinci. Ta'lim: san'at bakalavr. Ko'nikmalar: chizish, ranglar. Kundalik vazifalar: asarlar yaratish, ko'rgazma. Kasb yo'llari: galereya, frilans. O'rtacha maosh: o'zgaruvchan. Ish bozori: NFT bilan o'sish. Qiyinchiliklar: ilhom, sotish. Kelajak: digital tools.")

@dp.message(F.text == "Musiqachi")
async def Musiqachi(message: Message):
    await message.reply("Musiqachi - musiqa yaratuvchi va ijro etuvchi. Tarixan, Beethoven. Ta'lim: konservatoriya. Ko'nikmalar: asbob chalish, kompozitsiya. Kundalik vazifalar: mashq, konsertlar. Kasb yo'llari: orkestr, solo. O'rtacha maosh: o'zgaruvchan. Ish bozori: streaming. Qiyinchiliklar: raqobat, turne. Kelajak: AI musiqasi.")

@dp.message(F.text == "Aktyor")
async def Aktyor(message: Message):
    await message.reply("Aktyor - rol o'ynash mutaxassisi. Tarixan, Shakespeare zamoni. Ta'lim: teatr akademiyasi. Ko'nikmalar: emotsiya, memorizatsiya. Kundalik vazifalar: repetitsiya, suratga olish. Kasb yo'llari: film, teatr. O'rtacha maosh: o'zgaruvchan. Ish bozori: Hollywood. Qiyinchiliklar: rad etilish, shuhrat. Kelajak: virtual reality")

@dp.message(F.text == "Arxeolog")
async def Arxeolog(message: Message):
    await message.reply("Arxeolog – qadimgi madaniyat va sivilizatsiyalarni o'rganadigan mutaxassis. Tarixan, bu soha XIX asrda tizimli qazish ishlari bilan shakllandi. Ta'lim: arxeologiya yoki tarix bakalavr darajasi. Ko'nikmalar: qazish texnikasi, tarixiy tahlil, laboratoriya ishlari. Kundalik vazifalar: qazish ishlari olib borish, topilmalarni hujjatlashtirish, tadqiqot maqolalari yozish. Kasb yo'llari: universitet professori, muzey xodimi, tadqiqotchi. O'rtacha maosh: $50,000–$80,000. Ish bozori: ilmiy grantlarga bog'liq. Qiyinchiliklar: uzoq safarlar, ekstremal ob-havo. Kelajak: 3D skanerlash va dron texnologiyalari bilan rivojlanadi.")

@dp.message(F.text == "Astronom")
async def Astronom(message: Message):
    await message.reply("Astronom – koinot va osmon jismlarini o'rganadigan olim. Tarixan, qadimgi Bobilda astronomik kuzatuvlar boshlangan. Ta'lim: astronomiya yoki fizika magistr darajasi. Ko'nikmalar: teleskop ishlatish, hisoblash, ma'lumot tahlili. Kundalik vazifalar: kuzatuvlar, ilmiy tadqiqotlar, maqola yozish. Kasb yo'llari: universitet olimi, observatoriya xodimi, kosmik agentlik mutaxassisi. O'rtacha maosh: $80,000+")

@dp.message(F.text == "Biolog")
async def Biolog(message: Message):
    await message.reply("Biolog – tirik organizmlar tuzilishi va faoliyatini o'rganuvchi olim. Tarixan, Aristotel biologiya asoschilaridan biri. Ta'lim: biologiya bakalavr yoki magistr. Ko'nikmalar: laboratoriya ishlari, dala tadqiqotlari, tahlil. Kundalik vazifalar: namunalar yig'ish, tajribalar, ma'lumot tahlili. Kasb yo'llari: ekolog, genetik, dengiz biolog. O'rtacha maosh: $60,000–$90,000. Ish bozori: biotexnologiya va ekologiya sohalarida o'sish. Qiyinchiliklar: dala sharoitidagi qiyinchiliklar. Kelajak: gen muhandisligi va bioinformatika bilan kengayadi.")

@dp.message(F.text == "Geolog")
async def Geolog(message: Message):
    await message.reply("Geolog – Yer tuzilishi, tarkibi va jarayonlarini o'rganuvchi mutaxassis. Tarixan, XIX asrda neft va kon sanoati rivoji bilan muhimlashdi. Ta'lim: geologiya bakalavr. Ko'nikmalar: dala o'lchovlari, laboratoriya tahlili, xarita tuzish. Kundalik vazifalar: tog' jinslari tahlili, qazilma izlash, yer silkinishi tadqiqoti. Kasb yo'llari: neft kompaniyasi, ilmiy institut, davlat geologiyasi. O'rtacha maosh: $70,000+. Ish bozori: tabiiy resurslar tufayli talab yuqori. Qiyinchiliklar: uzoq safarlar, ekstremal sharoit. Kelajak: ekologik monitoring va qidiruv texnologiyalari bilan rivojlanadi.")

@dp.message(F.text == "Kimyogar")
async def Kimyogar(message: Message):
    await message.reply("Kimyogar – moddalarning tarkibi va xossalarini o'rganuvchi mutaxassis. Tarixan, kimyo alkimyodan kelib chiqqan. Ta'lim: kimyo bakalavr yoki magistr. Ko'nikmalar: laboratoriya uskunalari, formulalar, xavfsizlik qoidalari. Kundalik vazifalar: kimyoviy reaksiyalar, tahlillar, yangi modda yaratish. Kasb yo'llari: farmatsevtika, oziq-ovqat sanoati, ilmiy tadqiqot. O'rtacha maosh: $60,000–$100,000. Ish bozori: farmatsevtika va ekologiya sohalarida o'sish. Qiyinchiliklar: xavfli moddalar bilan ishlash. Kelajak: yashil kimyo va nanoteknologiya.")

@dp.message(F.text == "Fizik")
async def Fizik(message: Message):
    await message.reply("Fizik – moddiy dunyo qonuniyatlarini o'rganadigan olim. Tarixan, Nyuton va Eynshteyn eng mashhur fiziklar. Ta'lim: fizika bakalavr yoki magistr. Ko'nikmalar: matematik tahlil, tajriba o'tkazish, ilmiy metod. Kundalik vazifalar: nazariy modellar yaratish, eksperimentlar o'tkazish, ma'lumot tahlili. Kasb yo'llari: ilmiy institut, universitet, sanoat laboratoriyasi. O'rtacha maosh: $70,000–$120,000. Ish bozori: texnologiya va energetika sohalarida talab mavjud. Qiyinchiliklar: murakkab hisoblar, uzoq tadqiqotlar. Kelajak: kvant texnologiyalari va kosmik izlanishlar.")

@dp.message(F.text == "Farmatsevt")
async def Farmatsevt(message: Message):
    await message.reply("Farmatsevt – dori vositalarini tayyorlaydigan va sotadigan mutaxassis. Tarixan, qadimgi Misrda dorixonalar bo'lgan. Ta'lim: farmatsiya bakalavr darajasi. Ko'nikmalar: farmakologiya, kimyo, mijozlar bilan ishlash. Kundalik vazifalar: dori aralashtirish, retseptlarni bajarish, maslahat berish. Kasb yo'llari: dorixona, farmatsevtika zavodi, klinika. O'rtacha maosh: $80,000+. Ish bozori: salomatlik sohasidagi o'sish bilan kuchli talab. Qiyinchiliklar: aniq dozalarni saqlash mas'uliyati. Kelajak: shaxsiylashtirilgan dorilar ishlab chiqish")

@dp.message(F.text == "Arxitektor")
async def Arxitektor(message: Message):
    await message.reply("Arxitektor – binolar va inshootlar loyihasini ishlab chiquvchi mutaxassis. Tarixan, Rim va Yunon me'morchiligi asos bo'ldi. Ta'lim: arxitektura bakalavr yoki magistr. Ko'nikmalar: dizayn, chizmalar, 3D modellashtirish. Kundalik vazifalar: loyiha yaratish, qurilish jarayonini nazorat qilish. Kasb yo'llari: shaharsozlik, interyer dizayni, landshaft. O'rtacha maosh: $70,000+. Ish bozori: qurilish rivojlanishiga bog'liq. Qiyinchiliklar: buyurtmachining talablariga moslashish. Kelajak: ekologik va 'yashil' arxitektura.")

@dp.message(F.text == "Toksikolog")
async def Toksikolog(message: Message):
    await message.reply("Toksikolog – zaharli moddalar ta'sirini o'rganuvchi mutaxassis. Tarixan, bu soha qadimiy davrlarda ham mavjud bo'lgan. Ta'lim: toksikologiya yoki biologiya magistr darajasi. Ko'nikmalar: laboratoriya ishlari, tahlil, xavfsizlik protokollari. Kundalik vazifalar: namunalar tekshirish, zaharlanish holatlarini aniqlash. Kasb yo'llari: sud ekspertizasi, farmatsevtika, ekologiya. O'rtacha maosh: $70,000+. Ish bozori: sanoat xavfsizligi va tibbiyot sohasida talab yuqori. Qiyinchiliklar: xavfli moddalarga duch kelish. Kelajak: biotibbiy tadqiqotlar bilan kengayadi.")

@dp.message(F.text == "Antropolog")
async def Antropolog(message: Message):
    await message.reply("Antropolog – insoniyatning kelib chiqishi, madaniyati va rivojlanishini o'rganuvchi olim. Tarixan, XIX asrda fan sifatida shakllangan. Ta'lim: antropologiya bakalavr yoki magistr. Ko'nikmalar: dala tadqiqotlari, madaniy tahlil, intervyu. Kundalik vazifalar: sayohatlar, ilmiy maqolalar yozish, kuzatish. Kasb yo'llari: muzeylar, universitetlar, xalqaro tashkilotlar. O'rtacha maosh: $60,000+. Ish bozori: cheklangan, ammo ilmiy grantlar orqali ishlash mumkin. Qiyinchiliklar: uzoq safarlar, til to'siqlari. Kelajak: madaniy merosni saqlash texnologiyalari.")

@dp.message(F.text == "Meteorolog")
async def Meteorolog(message: Message):
    await message.reply("Meteorolog – ob-havo va iqlim o'zgarishlarini o'rganuvchi mutaxassis. Tarixan, qadimda osmonga qarab ob-havo bashorat qilinar edi. Ta'lim: meteorologiya yoki geofizika bakalavr. Ko'nikmalar: ma'lumot tahlili, prognoz yaratish, kompyuter modellari. Kundalik vazifalar: ob-havo xaritalarini tahlil qilish, prognoz e'lon qilish. Kasb yo'llari: televideniye, ilmiy institut, aviatsiya. O'rtacha maosh: $60,000+. Ish bozori: tabiiy ofatlar monitoringida talab yuqori. Qiyinchiliklar: noaniqlik, bosim ostida ishlash. Kelajak: sun'iy intellekt yordamida aniqroq prognozlar.")

@dp.message(F.text == "Kriptograf")
async def Kriptograf(message: Message):
    await message.reply("Kriptograf – ma'lumotlarni shifrlash va xavfsizlik tizimlarini yaratish bo'yicha mutaxassis. Tarixan, qadim Misr va Rim shifrlash usullari mavjud edi. Ta'lim: kiberxavfsizlik yoki matematika bakalavr. Ko'nikmalar: algoritmlar, dasturlash, xavfsizlik protokollari. Kundalik vazifalar: shifrlash tizimlarini ishlab chiqish, xavfsizlik tahlili. Kasb yo'llari: IT kompaniya, hukumat, moliya sektori. O'rtacha maosh: $90,000+. Ish bozori: internet xavfsizligi tufayli kuchli talab. Qiyinchiliklar: murakkab matematik masalalar. Kelajak: kvant kriptografiya.")

@dp.message(F.text == "Psixolog")
async def Psixolog(message: Message):
    await message.reply("Psixolog – inson psixologiyasini o'rganuvchi va maslahat beruvchi mutaxassis. Tarixan, Zigmunt Freyd psixoanaliz asoschisi. Ta'lim: psixologiya bakalavr yoki magistr. Ko'nikmalar: muloqot, tahlil, empatiya. Kundalik vazifalar: suhbat o'tkazish, diagnostika, davolash. Kasb yo'llari: klinik psixolog, ta'lim psixologi, sport psixologi. O'rtacha maosh: $70,000+. Ish bozori: ruhiy salomatlikka bo'lgan talab oshmoqda. Qiyinchiliklar: emotsional yuk. Kelajak: onlayn psixologiya xizmatlari.")

@dp.message(F.text == "Sotsiolog")
async def Sotsiolog(message: Message):
    await message.reply("Sotsiolog – jamiyat, ijtimoiy tizimlar va inson munosabatlarini o'rganuvchi mutaxassis. Tarixan, Ogyust Kont 'sotsiologiya' atamasini kiritgan. Ta'lim: sotsiologiya bakalavr yoki magistr. Ko'nikmalar: statistik tahlil, so'rovnomalar, kuzatuv. Kundalik vazifalar: tadqiqotlar, hisobotlar tayyorlash, ilmiy maqolalar yozish. Kasb yo'llari: ilmiy institut, davlat, NNT. O'rtacha maosh: $60,000+. Ish bozori: ijtimoiy loyihalarda talab mavjud. Qiyinchiliklar: moliyaviy resurs yetishmasligi. Kelajak: katta ma'lumotlar (big data) tahlili bilan kuchayadi.")

@dp.message(F.text == "Arxivchi")
async def Arxivchi(message: Message):
    await message.reply("Arxivchi – hujjatlarni saqlash va tizimlashtirish bo'yicha mutaxassis. Tarixan, bu kasb yozuvlar paydo bo'lishi bilan yuzaga kelgan. Ta'lim: axborot kutubxonashunosligi yoki tarix bakalavr. Ko'nikmalar: hujjat tahlili, kataloglash, saqlash texnologiyalari. Kundalik vazifalar: arxiv hujjatlarini tartibga solish, raqamlashtirish. Kasb yo'llari: davlat arxivi, muzey, kutubxona. O'rtacha maosh: $50,000+. Ish bozori: tarixiy merosni saqlash sohasida talab mavjud. Qiyinchiliklar: eski materiallar bilan ishlashdagi noziklik. Kelajak: raqamli arxivlar.")

@dp.message(F.text == "Kutubxonachi")
async def Kutubxonachi(message: Message):
    await message.reply("Kutubxonachi – kitoblar va axborot resurslarini boshqaruvchi mutaxassis. Tarixan, qadimgi Aleksandriya kutubxonasi eng mashhur edi. Ta'lim: kutubxonashunoslik bakalavr. Ko'nikmalar: kataloglash, foydalanuvchilar bilan ishlash. Kundalik vazifalar: kitoblarni tartibga solish, o'quvchilarga yordam berish. Kasb yo'llari: maktab, universitet, davlat kutubxonasi. O'rtacha maosh: $45,000+. Ish bozori: barqaror, lekin raqamli texnologiyalar ta'sirida. Qiyinchiliklar: texnologik moslashuv. Kelajak: elektron kutubxonalar.")

@dp.message(F.text == "Tarjimon")
async def Tarjimon(message: Message):
    await message.reply("Tarjimon – matn yoki nutqni bir tildan boshqasiga o'girish mutaxassisi. Tarixan, tarjimonlar diplomatiyada muhim bo'lgan. Ta'lim: tilshunoslik bakalavr. Ko'nikmalar: til bilimi, grammatik to'g'rilik, madaniyat tushunchasi. Kundalik vazifalar: matn tarjimasi, sinxron tarjima, subtitrlar tayyorlash. Kasb yo'llari: xalqaro kompaniya, davlat idorasi, frilanser. O'rtacha maosh: $50,000+. Ish bozori: xalqaro aloqalar kuchayishi bilan talab oshmoqda. Qiyinchiliklar: murakkab matnlarni tushunish. Kelajak: AI yordamida tezkor tarjimalar.")

@dp.message(F.text == "Kartograf")
async def Kartograf(message: Message):
    await message.reply("Kartograf – xaritalar yaratish va yangilash bilan shug'ullanuvchi mutaxassis. Tarixan, qadimgi dengizchilar xarita tuzishda ishlatgan. Ta'lim: geoinformatika yoki geografiya bakalavr. Ko'nikmalar: GIS dasturlari, geodeziya, dizayn. Kundalik vazifalar: joy ma'lumotlarini tahlil qilish, xaritalar chizish. Kasb yo'llari: davlat geodeziya xizmati, harbiy, turizm kompaniyalari. O'rtacha maosh: $60,000+. Ish bozori: navigatsiya va logistika sohasida talab mavjud. Qiyinchiliklar: katta hajmdagi ma'lumotlarni qayta ishlash. Kelajak: 3D va interaktiv xaritalar.")

@dp.message(F.text == "Botanist")
async def Botanist(message: Message):
    await message.reply("Botanist – o'simliklar hayoti va tuzilishini o'rganuvchi olim. Tarixan, Karl Linney o'simliklarni tasniflash tizimini yaratgan. Ta'lim: botanika yoki biologiya bakalavr. Ko'nikmalar: dala tadqiqotlari, laboratoriya ishlari. Kundalik vazifalar: o'simlik namunalarini yig'ish, tahlil qilish, ilmiy maqola yozish. Kasb yo'llari: qishloq xo'jaligi, farmatsevtika, ekologiya. O'rtacha maosh: $55,000+. Ish bozori: biotexnologiya rivoji bilan o'smoqda. Qiyinchiliklar: dala sharoitida ishlashdagi qiyinchiliklar. Kelajak: genetik o'simliklar yaratish.")

@dp.message(F.text == "Zoolog")
async def Zoolog(message: Message):
    await message.reply("Zoolog – hayvonlar biologiyasini o'rganuvchi mutaxassis. Tarixan, Darvin evolyutsiya nazariyasiga katta hissa qo'shgan. Ta'lim: zoologiya bakalavr. Ko'nikmalar: kuzatuv, laboratoriya ishlari, ekologik tahlil. Kundalik vazifalar: hayvonlarni o'rganish, ma'lumot to'plash, tahlil. Kasb yo'llari: milliy bog'lar, zoologiya institutlari, muzeylar. O'rtacha maosh: $60,000+. Ish bozori: tabiatni muhofaza qilish sohasida talab yuqori. Qiyinchiliklar: yovvoyi tabiatda ishlashdagi xavflar. Kelajak: dron va sensor texnologiyalari bilan rivojlanadi.")

@dp.message(F.text == "Arxivolog")
async def Arxivolog(message: Message):
    await message.reply("Arxivolog – qadimiy yozma manbalarni o'rganadigan mutaxassis. Tarixan, qadimgi qo'lyozmalarni saqlash va tahlil qilish an'analari mavjud. Ta'lim: tarix yoki filologiya bakalavr. Ko'nikmalar: paleografiya, tilshunoslik, arxiv ishlari. Kundalik vazifalar: qo'lyozmalarni o'qish, tarjima qilish, saqlash. Kasb yo'llari: muzeylar, universitetlar, ilmiy institutlar. O'rtacha maosh: $50,000+. Ish bozori: ilmiy grantlarga bog'liq. Qiyinchiliklar: nozik materiallar bilan ishlash. Kelajak: raqamli saqlash tizimlari.")

@dp.message(F.text == "Paleontolog")
async def Paleontolog(message: Message):
    await message.reply("Paleontolog – qazilma hayvonlar va o'simliklarni o'rganadigan olim. Tarixan, dinozavr suyaklarini topish bilan mashhur bo'lgan. Ta'lim: paleontologiya yoki geologiya bakalavr. Ko'nikmalar: qazish, tahlil, rekonstruksiya. Kundalik vazifalar: qazilma qoldiqlarni topish, laboratoriyada tekshirish. Kasb yo'llari: muzeylar, ilmiy institutlar, universitetlar. O'rtacha maosh: $60,000+. Ish bozori: cheklangan, ammo ilmiy tadqiqotlar orqali mavjud. Qiyinchiliklar: uzoq safarlar. Kelajak: 3D rekonstruksiya texnologiyalari.")

@dp.message(F.text == "Fizikoterapevt")
async def Fizikoterapevt(message: Message):
    await message.reply("Fizikoterapevt – bemorlarni jismoniy mashqlar va usullar bilan davolovchi mutaxassis. Tarixan, tibbiy reabilitatsiya XX asrda keng rivojlandi. Ta'lim: fizioterapiya bakalavr. Ko'nikmalar: anatomiyani bilish, reabilitatsiya metodlari. Kundalik vazifalar: mashqlar belgilash, massaj, fizioterapiya usullarini qo'llash. Kasb yo'llari: kasalxona, sport klubi, reabilitatsiya markazi. O'rtacha maosh: $70,000+. Ish bozori: tibbiyot sohasida yuqori talab. Qiyinchiliklar: bemor bilan doimiy ishlash. Kelajak: robotik reabilitatsiya texnologiyalari.")

@dp.message(F.text == "Genetik")
async def Genetik(message: Message):
    await message.reply("Genetik – irsiyat va DNK tuzilishini o'rganadigan olim. Tarixan, Gregor Mendel genetika asoschisi. Ta'lim: genetika yoki biologiya magistr. Ko'nikmalar: laboratoriya ishlari, genetik tahlil. Kundalik vazifalar: DNK tekshirish, genetik kasalliklarni aniqlash. Kasb yo'llari: biotexnologiya, tibbiyot, ilmiy institutlar. O'rtacha maosh: $80,000+. Ish bozori: tibbiy diagnostika va biotexnologiya rivoji bilan kuchli. Qiyinchiliklar: murakkab ilmiy jarayonlar. Kelajak: gen muhandisligi va CRISPR texnologiyasi")

@dp.message(F.text == "Mikrobiolog")
async def Mikrobiolog(message: Message):
    await message.reply("Mikrobiolog – mikroorganizmlarni o'rganuvchi mutaxassis. Tarixan, Lui Paster mikrobiologiya asoschilaridan. Ta'lim: mikrobiologiya yoki biologiya bakalavr. Ko'nikmalar: mikroskop ishlatish, laboratoriya usullari. Kundalik vazifalar: bakteriya, virus va zamburug'larni tahlil qilish. Kasb yo'llari: tibbiyot, oziq-ovqat sanoati, ekologiya. O'rtacha maosh: $65,000+. Ish bozori: tibbiyot va farmatsevtika sohalarida yuqori. Qiyinchiliklar: infektsiya xavfi. Kelajak: vaksina va antibiotik ishlab chiqish.")

@dp.message(F.text == "Akustik")
async def Akustik(message: Message):
    await message.reply("Akustik – tovush fizikasi va texnologiyasini o'rganuvchi mutaxassis. Tarixan, bu soha musiqa va muhandislikda qo'llanilgan. Ta'lim: akustika yoki fizika bakalavr. Ko'nikmalar: tovush o'lchash, signal tahlili. Kundalik vazifalar: akustik tizimlar loyihalash, shovqin izolyatsiyasi. Kasb yo'llari: studiyalar, qurilish, transport sanoati. O'rtacha maosh: $70,000+. Ish bozori: ovoz texnologiyalari rivoji bilan o'smoqda. Qiyinchiliklar: maxsus uskunalar bilan ishlash. Kelajak: 3D audio va virtual haqiqat.")

@dp.message(F.text == "Optik")
async def Optik(message: Message):
    await message.reply("Optik – yorug'lik va optik tizimlarni o'rganuvchi mutaxassis. Tarixan, Ibn al-Haysam optika ilmida muhim kashfiyotlar qilgan. Ta'lim: optika yoki fizika bakalavr. Ko'nikmalar: linza dizayni, yorug'lik tahlili. Kundalik vazifalar: optik asboblar ishlab chiqish, nazorat qilish. Kasb yo'llari: tibbiyot, astronomiya, texnologiya kompaniyalari. O'rtacha maosh: $75,000+. Ish bozori: lazer texnologiyasi va tibbiyotda yuqori talab. Qiyinchiliklar: murakkab texnik ishlanmalar. Kelajak: kvant optikasi va AR texnologiyalari.")

@dp.message(F.text == "Navigatsion")
async def Navigatsion(message: Message):
    await message.reply("Navigatsion – kema, samolyot yoki boshqa transport vositalarining to'g'ri yo'nalishda harakatlanishini ta'minlovchi soha. Bu kasb egalari xarita, kompas, GPS va boshqa navigatsiya uskunalaridan foydalanib, xavfsiz va aniq manzilga yetib borishni tashkil qiladi.")

@dp.message(F.text == "Agronom")
async def Agronom(message: Message):
    await message.reply("Agronom – qishloq xo'jaligi ekinlarini yetishtirish va unumdorligini oshirish bo'yicha mutaxassis. Tarixan, qadimgi Misr va Mesopotamiya yer islohotlari bilan boshlangan. Ta'lim: agronomiya bakalavr. Ko'nikmalar: tuproqshunoslik, ekinlarni parvarish qilish. Kundalik vazifalar: dalalarni tekshirish, hosildorlikni baholash. Kasb yo'llari: fermer xo'jaliklari, ilmiy institutlar. O'rtacha maosh: $50,000+. Ish bozori: oziq-ovqat ishlab chiqarish talabi ortishi. Qiyinchiliklar: ob-havo sharoiti. Kelajak: aniq qishloq xo'jaligi texnologiyalari.")

@dp.message(F.text == "Ekolog")
async def Ekolog(message: Message):
    await message.reply("Ekolog – tabiatni muhofaza qilish, atrof-muhitni o'rganish va ekologik muammolarni hal etish bilan shug'ullanuvchi mutaxassis. U havo, suv, tuproq holatini kuzatadi, ifloslanishni kamaytirish choralarini ishlab chiqadi va inson faoliyatining tabiatga ta'sirini baholaydi.")

@dp.message(F.text == "Mineralog")
async def Mineralog(message: Message):
    await message.reply("Mineralog – minerallarning fizik va kimyoviy xususiyatlarini o'rganuvchi mutaxassis. Tarixan, qadimgi konchilik bilan bog'liq. Ta'lim: geologiya yoki kimyo bakalavr. Ko'nikmalar: kristallografiya, spektral tahlil. Kundalik vazifalar: mineral namunalarini tahlil qilish. Kasb yo'llari: kon kompaniyalari, muzeylar. O'rtacha maosh: $60,000+. Ish bozori: qazilma boyliklarni qidirishda talab. Qiyinchiliklar: dala sharoitida ishlash. Kelajak: yangi materiallar kashfiyoti.")

@dp.message(F.text == "Vulkanolog")
async def Vulkanolog(message: Message):
    await message.reply("Vulkanolog – vulkan faoliyatini o'rganadi, otilish xavfini baholaydi, seysmik va geotermal ma'lumotlarni tahlil qiladi, aholini ogohlantirish tizimlarini ishlab chiqadi va favqulodda vaziyatlarda xavfsizlik choralarini belgilaydi.")

@dp.message(F.text == "Hidrolog")
async def Hidrolog(message: Message):
    await message.reply("Hidrolog – suv resurslari va ularning aylanishini o'rganuvchi mutaxassis. Tarixan, qadimgi irrigatsiya tizimlari bilan bog'liq. Ta'lim: gidrologiya yoki geografiya bakalavr. Ko'nikmalar: suv sathini o'lchash, model qurish. Kundalik vazifalar: daryo va ko'llarni kuzatish. Kasb yo'llari: ekologiya xizmati, suv xo'jaligi. O'rtacha maosh: $65,000+. Ish bozori: suv tanqisligi muammolari tufayli talab. Qiyinchiliklar: ekstremal sharoitlar. Kelajak: iqlim o'zgarishi monitoringi.")

@dp.message(F.text == "Okeanolog")
async def Okeanolog(message: Message):
    await message.reply("Okeanolog – okeanlar va dengizlarni o'rganuvchi mutaxassis. Tarixan, qadimgi dengizchilik bilan boshlangan. Ta'lim: okeanologiya bakalavr. Ko'nikmalar: gidroakustika, suv osti tadqiqotlari. Kundalik vazifalar: okean parametrlarini o'lchash. Kasb yo'llari: ilmiy institutlar, ekologik tashkilotlar. O'rtacha maosh: $70,000+. Ish bozori: okean resurslarini o'rganish talabi. Qiyinchiliklar: uzoq ekspeditsiyalar. Kelajak: chuqur suv tadqiqotlari.")

@dp.message(F.text == "Astronavt")
async def Astronavt(message: Message):
    await message.reply("Astronavt – kosmosga parvoz qiluvchi mutaxassis. Tarixan, 1961-yilda Yuriy Gagarin birinchi bo'ldi. Ta'lim: muhandislik yoki fanlar bakalavri, kosmonavtlar maktabi. Ko'nikmalar: vaznsizlikka moslashish, texnik bilimlar. Kundalik vazifalar: kosmik kemani boshqarish, tajribalar o'tkazish. Kasb yo'llari: kosmik agentliklar. O'rtacha maosh: $100,000+. Ish bozori: cheklangan, ammo kosmik turizm rivoji bilan. Qiyinchiliklar: ekstremal sharoitlar. Kelajak: Marsga parvozlar.")

@dp.message(F.text == "Kosmolog")
async def Kosmolog(message: Message):
    await message.reply("Kosmolog – koinotning kelib chiqishi va evolyutsiyasini o'rganuvchi olim. Tarixan, qadimgi astronomiyadan boshlangan. Ta'lim: astronomiya yoki fizika magistr. Ko'nikmalar: matematik modellashtirish, nazariy fizika. Kundalik vazifalar: koinot tuzilishi haqida tadqiqotlar. Kasb yo'llari: universitetlar, ilmiy markazlar. O'rtacha maosh: $80,000+. Ish bozori: fundamental tadqiqotlar uchun grantlar. Qiyinchiliklar: murakkab nazariyalar. Kelajak: qorong'u materiya va energiya tadqiqoti.")

@dp.message(F.text == "Operator")
async def Operator(message: Message):
    await message.reply("Operator – turli texnik qurilmalarni boshqaruvchi mutaxassis. Tarixan, sanoat inqilobi bilan rivojlangan. Ta'lim: texnik ta'lim. Ko'nikmalar: qurilmalarni sozlash, texnik xizmat. Kundalik vazifalar: ishlab chiqarish jarayonini nazorat qilish. Kasb yo'llari: fabrikalar, ishlab chiqarish korxonalari. O'rtacha maosh: $45,000+. Ish bozori: avtomatlashtirish tufayli o'zgaruvchan. Qiyinchiliklar: monoton ish. Kelajak: robotlashtirilgan tizimlar.")

@dp.message(F.text == "Akustik muhandis")
async def Akustik_muhandis(message: Message):
    await message.reply("Akustik muhandis — Konsert zallari, kinoteatrlar, yozuv studiyalari va boshqa joylarda tovush sifatini oshirish uchun akustik tizimlarni loyihalash, ovoz tarqalishini hisoblash va optimallashtirish bilan shug'ullanadi, maxsus dasturlar va fizik qonunlardan foydalanadi, shuningdek, qurilish jarayonida tovush izolyatsiyasini ta'minlashda ishtirok etadi.")

@dp.message(F.text == "Dron operatori")
async def Dron_operatori(message: Message):
    await message.reply("Dron operatori — Turli sohalarda qo'llaniladigan dronlarni masofadan boshqaradi, yuqori sifatli foto va video suratga olish, xaritalash, qutqaruv, qishloq xo'jaligi monitoringi kabi vazifalarni bajaradi, parvoz qoidalariga amal qiladi va maxsus boshqaruv texnologiyalaridan foydalanadi.")

@dp.message(F.text == "Kiberxavfsizlik mutaxassisi")
async def Kiberxavfsizlik_mutaxassisi(message: Message):
    await message.reply("Kiberxavfsizlik mutaxassisi — Kompaniya yoki tashkilotning kompyuter tizimlarini xakerlik hujumlari, viruslar va ma'lumot o'g'irlanishidan himoya qiladi, xavfsizlik protokollarini ishlab chiqadi, tizimlarni muntazam tekshiradi, xavfli kirishlarni aniqlaydi hamda hodisalarga tezkor javob berish uchun maxsus dasturiy vositalardan foydalanadi.")

@dp.message(F.text == "Virtual reallik dizayneri")
async def Virtual_reallik_dizayneri(message: Message):
    await message.reply("Virtual reallik dizayneri — VR texnologiyalari asosida interaktiv o'yinlar, trening simulyatorlari yoki ta'lim platformalarini yaratadi, foydalanuvchi uchun immersiv tajriba ta'minlaydigan grafik elementlar, sahnalar va muhitlarni ishlab chiqadi, 3D modellashtirish dasturlari va maxsus kodlash vositalaridan foydalanadi.")

@dp.message(F.text == "Biotexnolog")
async def Biotexnolog(message: Message):
    await message.reply("Biotexnolog — Biologiya va kimyo bilimlarini qo'llab, tirik organizmlar asosida dori vositalari, o'g'itlar, oziq-ovqat mahsulotlari va ekologik toza texnologiyalar ishlab chiqaradi, genetik modifikatsiya, fermentatsiya va hujayra texnologiyalarini o'rganadi hamda laboratoriya tajribalarini o'tkazadi.")

@dp.message(F.text == "Kriptovalyuta treyderi")
async def Kriptovalyuta_treyderi(message: Message):
    await message.reply("Kriptovalyuta treyderi — Bitcoin, Ethereum va boshqa kriptovalyutalar bozorida narxlar o'zgarishini tahlil qilib, foyda olish maqsadida xarid va sotuv operatsiyalarini amalga oshiradi, texnik va fundamental tahlil usullaridan foydalanadi, risklarni boshqaradi hamda global kripto yangiliklarini kuzatib boradi.")

@dp.message(F.text == "Nanotexnolog mutaxassisi")
async def Nanotexnolog_mutaxassisi(message: Message):
    await message.reply("Nanotexnolog mutaxassisi — Atom va molekula miqyosida yangi materiallar, tibbiyot vositalari yoki elektron qurilmalarni yaratadi, nanostrukturalar ustida ishlaydi, tajriba laboratoriyalarida zamonaviy asbob-uskunalardan foydalanadi va ilmiy izlanishlarni amalga oshiradi, texnologiyani amaliyotga joriy etadi.")

@dp.message(F.text == "Logist")
async def Logist(message: Message):
    await message.reply("Logist — Tovarlarni ishlab chiqaruvchidan mijozga yetkazish jarayonini rejalashtiradi, transport, saqlash va taqsimlash tizimlarini optimallashtiradi, xarajatlarni kamaytiradi, yetkazib berish muddatiga rioya qilinishini nazorat qiladi hamda xalqaro savdo va bojxona qoidalarini hisobga oladi.")

@dp.message(F.text == "Kiberforensika mutaxassisi")
async def Kiberforensika_mutaxassisi(message: Message):
    await message.reply("Kiberforensika mutaxassisi — Kompyuter jinoyatlarini tergov qiladi, raqamli dalillarni yig'adi va tahlil qiladi, sud jarayonlari uchun isbotlar tayyorlaydi, shifrlangan yoki o'chirilgan ma'lumotlarni tiklaydi, tarmoqlar va qurilmalarda noqonuniy faoliyat izlarini aniqlaydi hamda xavfsizlikni mustahkamlash bo'yicha tavsiyalar beradi.")

@dp.message(F.text == "Podkast prodyuseri")
async def Podkast_prodyuseri(message: Message):
    await message.reply("Podkast prodyuseri — Audio kontent yaratish va tarqatish jarayonini boshqaradi, mavzularni ishlab chiqadi, mehmonlarni taklif qiladi, texnik jihatdan yozib olish va montaj qilishni amalga oshiradi, auditoriyani oshirish uchun marketing strategiyalarini ishlab chiqadi.")

@dp.message(F.text == "Mobil ilova testlovchi")
async def Mobil_ilova_testlovchi(message: Message):
    await message.reply("Mobil ilova testlovchi — Yangi mobil dasturlarning ishlashini tekshiradi, xatolarni aniqlaydi va hisobot qiladi, turli qurilmalar va operatsion tizimlarda ilovalarning muvofiqligini baholaydi, test rejalarini ishlab chiqadi va sifat nazoratini amalga oshiradi.")

@dp.message(F.text == "Blokcheyn dasturchisi")
async def Blokcheyn_dasturchisi(message: Message):
    await message.reply("Blokcheyn dasturchisi — Blockchain texnologiyasiga asoslangan ilovalar va aqlli shartnomalar yaratadi, kriptografik algoritmlardan foydalanadi, tarqatilgan registr tizimlarini ishlab chiqadi hamda moliya, sog'liqni saqlash yoki ta'minot zanjiri kabi sohalarda xavfsiz yechimlarni taklif qiladi.")

@dp.message(F.text == "Esport murabbiyi")
async def Esport_murabbiyi(message: Message):
    await message.reply("Esport murabbiyi — Professional kompyuter o'yinchi jamoalarini tayyorlaydi, o'yin strategiyalarini ishlab chiqadi, raqiblarni tahlil qiladi, o'yinchilarning shaxsiy ko'nikmalarini oshirishga yordam beradi va musobaqalarga psixologik tayyorgarlik ko'radi.")

@dp.message(F.text == "Uy kinoteatri montajchisi")
async def Uy_kinoteatri_montajchisi(message: Message):
    await message.reply("Uy kinoteatri montajchisi — Uy sharoitida professional kinoteatr tizimlarini o'rnatadi, audio-video uskunalarni sozlaydi, proyektor va ovoz tizimlarini optimal joylashtiradi, mijozlarga texnik yordam ko'rsatadi va tizimlarni yangilab boradi.")

@dp.message(F.text == "UAV texnikasi")
async def UAV_texnikasi(message: Message):
    await message.reply("UAV texnikasi — Pilotli uchuvchi apparatlarni (dronlar) texnik xizmat ko'rsatadi, ta'mirlaydi va sozlaydi, parvozdan oldin texnik holatini tekshiradi, yangi UAV modellarini o'rganadi va ularni ishlatish bo'yicha texnik ko'rsatmalar tayyorlaydi.")

@dp.message(F.text == "Astronavt tayyorgarlik instruktori")
async def Astronavt_tayyorgarlik_instruktori(message: Message):
    await message.reply("Astronavt tayyorgarlik instruktori — Astronavtlarni kosmik parvozlarga tayyorlaydi, vaznsizlik sharoitida ishlash ko'nikmalarini o'rgatadi, favqulodda vaziyatlarda qanday harakat qilishni tushuntiradi, simulyatorlarda mashg'ulotlar o'tkazadi va kosmik kemalarning tizimlari haqida bilim beradi.")

@dp.message(F.text == "Kiberpsixolog")
async def Kiberpsixolog(message: Message):
    await message.reply("Kiberpsixolog — Internet va raqamli texnologiyalarning inson psixologiyasiga ta'sirini o'rganadi, onlayn xulq-atvor, ijtimoiy tarmoqlardagi odatlar va kibermuloqot jarayonlarini tahlil qiladi, psixologik muammolarni hal qilishda texnologik yondashuvlardan foydalanadi.")

@dp.message(F.text == "Data-jurnalist")
async def Data_jurnalist(message: Message):
    await message.reply("Data-jurnalist — Katta hajmdagi ma'lumotlarni tahlil qilib, ular asosida jurnalistik materiallar yaratadi, vizuallashtirish vositalaridan foydalanadi, murakkab ijtimoiy yoki iqtisodiy tendentsiyalarni oddiy tushunarli shaklda bayon etadi va ochiq ma'lumotlar bazalaridan foydalanadi.")

@dp.message(F.text == "Sensor texnolog mutaxassisi")
async def Sensor_texnolog_mutaxassisi(message: Message):
    await message.reply("Sensor texnolog mutaxassisi — Turli sohalar uchun sensorlar va sezgir qurilmalar ishlab chiqadi, ularning ishlashini optimallashtiradi, ma'lumotlarni qayta ishlash algoritmlarini yaratadi va sensor tarmoqlarini boshqarish tizimlarini loyihalaydi.")

@dp.message(F.text == "Sun'iy intellekt etikasi bo'yicha ekspert")
async def Suniy_intellekt_etikasi(message: Message):
    await message.reply("Sun'iy intellekt etikasi bo'yicha ekspert — AI tizimlarining adolatli, xolis va xavfsiz ishlashini ta'minlash bo'yicha siyosatlar ishlab chiqadi, diskriminatsiya va noto'g'ri qarorlar xavfini kamaytiradi, algoritmik shaffoflik ustida ishlaydi.")

@dp.message(F.text == "Eko-qurilish muhandisi")
async def Eko_qurilish_muhandisi(message: Message):
    await message.reply("Eko-qurilish muhandisi — Atrof-muhitga zararsiz qurilish materiallari va texnologiyalarini qo'llaydi, energiya samaradorligini oshirish, chiqindilarni kamaytirish va tabiiy resurslarni tejashga qaratilgan loyihalarni ishlab chiqadi va amalga oshiradi.")

@dp.message(F.text == "3D chop etish texnologi")
async def _3D_chop_etish_texnologi(message: Message):
    await message.reply("3D chop etish texnologi — 3D printerlar yordamida turli modellarni yaratadi, materiallarni tanlaydi, chop etish jarayonini boshqaradi, qurilmalarni sozlaydi va texnik xizmat ko'rsatadi, shuningdek, yangi ishlab chiqarish usullarini ishlab chiqadi.")

@dp.message(F.text == "Biometrik tizim muhandisi")
async def Biometrik_tizim_muhandisi(message: Message):
    await message.reply("Biometrik tizim muhandisi — Barmoq izi, yuz tanish, ovoz identifikatsiyasi kabi texnologiyalarni ishlab chiqadi, xavfsizlik tizimlariga joriy etadi, biometrik ma'lumotlarni saqlash va ishlov berishda yuqori darajada maxfiylikni ta'minlaydi.")

@dp.message(F.text == "Big Data tahlilchisi")
async def Big_Data_tahlilchisi(message: Message):
    await message.reply("Big Data tahlilchisi — Katta hajmdagi tuzilmagan ma'lumotlarni qayta ishlaydi, tahlil qiladi va foydali natijalarni ajratib oladi, statistika va mashinali o'rganish usullaridan foydalanadi, korxonalarga strategik qarorlar qabul qilishda yordam beradi.")

@dp.message(F.text == "Kosmik qoldiqlar mutaxassisi")
async def Kosmik_qoldiqlar_mutaxassisi(message: Message):
    await message.reply("Kosmik qoldiqlar mutaxassisi — Orbitadagi chiqindi va eski sun'iy yo'ldoshlarni kuzatadi, ularning harakatini bashorat qiladi, kosmik kemalar uchun xavfni baholaydi va kosmosni tozalash bo'yicha texnologiyalarni ishlab chiqishda ishtirok etadi.")

@dp.message(F.text == "Neurointerfeys dizayneri")
async def Neurointerfeys_dizayneri(message: Message):
    await message.reply("Neurointerfeys dizayneri — Inson miyasi bilan kompyuter yoki robot qurilmalari o'rtasida aloqa o'rnatadigan tizimlarni ishlab chiqadi, neyrosignallarni o'qish va boshqarish texnologiyalarini yaratadi, tibbiyot va reabilitatsiyada qo'llaniladigan innovatsion interfeyslarni loyihalaydi.")

@dp.message(F.text == "Kiberxavfsizlik auditori")
async def Kiberxavfsizlik_auditori(message: Message):
    await message.reply("Kiberxavfsizlik auditori — Tashkilotlarning axborot xavfsizligi tizimlarini tekshiradi, zaif tomonlarni aniqlaydi, himoya choralarini baholaydi va xavfsizlik standartlariga muvofiqligini tekshiradi, shuningdek, xavfsizlikni oshirish bo'yicha tavsiyalar beradi.")

@dp.message(F.text == "Gamifikatsiya mutaxassisi")
async def Gamifikatsiya_mutaxassisi(message: Message):
    await message.reply("Gamifikatsiya mutaxassisi — O'yin elementlari va printsipilarini o'yin bo'lmagan sohalarga (ta'lim, marketing, biznes) qo'llaydi, foydalanuvchilarni jalb qilish va motivatsiyani oshirish uchun interaktiv tizimlarni ishlab chiqadi, o'yinlashtirish strategiyalarini yaratadi.")

@dp.message(F.text == "Vertikal qishloq xo'jaligi mutaxassisi")
async def Vertikal_qishloq_xojaligi_mutaxassisi(message: Message):
    await message.reply("Vertikal qishloq xo'jaligi mutaxassisi — Shaharlarda ko'p qavatli binolarda o'simliklar yetishtirish tizimlarini loyihalaydi va boshqaradi, gidroponika, aeroponika va LED yoritish texnologiyalaridan foydalanadi, resurslarni tejash va mahsuldorlikni oshirish uchun innovatsion usullarni qo'llaydi.")

@dp.message(F.text == "Kosmik turizm gid")
async def Kosmik_turizm_gid(message: Message):
    await message.reply("Kosmik turizm gid — Kosmik sayohatchilarga kosmos haqida ma'lumot beradi, parvoz paytidagi xavfsizlik qoidalarini tushuntiradi, kosmik stansiyalarda orientirlashda yordam beradi va kosmik tajribani qiziqarli qilish uchun maxsus dasturlar tayyorlaydi.")

@dp.message(F.text == "Energiya samaradorligi bo'yicha konsultant")
async def Energiya_samaradorligi_konsultant(message: Message):
    await message.reply("Energiya samaradorligi bo'yicha konsultant — Korxonalar va uy xo'jaliklarida energiya sarfini kamaytirish bo'yicha tavsiyalar beradi, energiya auditi o'tkazadi, qayta tiklanadigan energiya manbalaridan foydalanishni targ'ib qiladi va energiya tejash texnologiyalarini joriy etishda yordam beradi.")

@dp.message(F.text == "Avtonom transport muhandisi")
async def Avtonom_transport_muhandisi(message: Message):
    await message.reply("Avtonom transport muhandisi — O'zi boshqariladigan avtomobillar, dronlar yoki boshqa transport vositalarini ishlab chiqadi, ularning sensor tizimlari va boshqaruv algoritmlarini takomillashtiradi, xavfsizlik va samaradorlikni oshirish uchun sinovlar o'tkazadi.")

@dp.message(F.text == "Aqlli uy tizimlari mutaxassisi")
async def Aqlli_uy_tizimlari_mutaxassisi(message: Message):
    await message.reply("Aqlli uy tizimlari mutaxassisi — Uy va ofislarda avtomatlashtirilgan boshqaruv tizimlarini o'rnatadi va sozlaydi, yoritish, isitish, xavfsizlik va boshqa tizimlarni birlashtiradi, foydalanuvchilarga qulaylik va energiya tejashni ta'minlaydi.")

@dp.message(F.text == "Genetik maslahatchi")
async def Genetik_maslahatchi(message: Message):
    await message.reply("Genetik maslahatchi — Inson genetik ma'lumotlarini tahlil qiladi, irsiy kasalliklar xavfi haqida tavsiyalar beradi, oilaviy rejalashtirish va tibbiy qarorlar qabul qilishda yordam beradi, DNK diagnostikasi va molekulyar biologiya usullaridan foydalanadi.")

@dp.message(F.text == "Raqamli marketing analitigi")
async def Raqamli_marketing_analitigi(message: Message):
    await message.reply("Raqamli marketing analitigi — Onlayn marketing faoliyati natijalarini ma'lumotlar asosida tahlil qilish va optimallashtirish jarayoni. U veb-sayt trafigi, mijozlar harakati, konversiya darajalari, ROI va boshqa ko'rsatkichlarni kuzatish orqali marketing strategiyasini samaraliroq qilishga yordam beradi. Asosiy vositalar: Google Analytics, CRM tizimlar, A/B testlar va SEO monitoring. Maqsad – xarajatlarni kamaytirib, sotuvlarni oshirish.")

@dp.message(F.text == "Sun'iy organ ishlab chiqaruvchi muhandis")
async def Suniy_organ_ishlab_chiqaruvchi_muhandis(message: Message):
    await message.reply("Sun'iy organ ishlab chiqaruvchi muhandis — Biotexnologiya va muhandislikni birlashtirib, inson tanasi uchun sun'iy yurak, buyrak, protez va boshqa a'zolarni yaratuvchi mutaxassis. Ular biomexanika, materialshunoslik va elektronika sohalaridagi bilimlaridan foydalanadi, tibbiyotda foydalanish uchun xavfsiz va mos materiallardan foydalanadi, klinik sinovlarda ishtirok etadi.")

@dp.message(F.text == "Ovoz effektlari (Foley) mutaxassisi")
async def Ovoz_effektlari_mutaxassisi(message: Message):
    await message.reply("Ovoz effektlari (Foley) mutaxassisi — Filmlar, videoo'yinlar va boshqa media mahsulotlar uchun tabiiy ovoz effektlarini yaratadi, maxsus studiyada turli buyumlar yordamida kerakli tovushlarni ishlab chiqaradi, ovozlarni yozib oladi va ularni video bilan sinxronlashtiradi.")

@dp.message(F.text == "Kiberxavfsizlik bo'yicha insident javob beruvchi")
async def Kiberxavfsizlik_insident_javob_beruvchi(message: Message):
    await message.reply("Kiberxavfsizlik insidentiga javob beruvchi – bu tarmoq hujumlari, ma'lumotlar buzilishi yoki boshqa xavfli hodisalar sodir bo'lganda ularni tez aniqlash, zararni kamaytirish va tizimni tiklash uchun javob choralarini ko'radigan mutaxassis.")

@dp.message()
async def hechnarsa(message: Message):
    await message.reply("Ro'yxatdagi kasb nomini kiriting")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye")