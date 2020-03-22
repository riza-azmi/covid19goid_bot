#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# Riza Azmi (Puslitbang SDP3I)

import logging
import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['A', 'B', 'C'],
                  ['D', 'E', 'F'],
                  ['G']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [['MENU'],['SELESAI']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    update.message.reply_text(
        "Halo! Selamat datang di *Bot Informasi Covid-19*. "
        "Semoga kamu sehat-sehat selalu. ",
        reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)

    update.message.reply_text(
        "Apa saja sih yang ingin kamu ketahui mengenai Covid-19?\n"
        "*A*. Kabar Covid-19 terkini di Indonesia\n"
        "*B*. Sebenarnya apa sih Covid-19 itu?\n"
        "*C*. Apa saja gejala Covid-19?\n"
        "*D*. Bagaimana cara melindungi diri?\n"
        "*E*. Bagaimana cara melindungi orang lain?\n"
        "*F*. Masker perlu gak sih?\n"
        "*G*. Rumah Sakit Rujukan Covid-19.\n\n"
        "Ketik A, B, C, D, E, F, atau G, lalu kirim ke kami. Maka, kami akan menjawab pertanyaan kamu.\n\n"
        "Bagikan info akurat tentang COVID-19 ke teman dan keluargamu 🙏\n\n\n"
        "www.covid19.go.id\n"
        "0811 333 99 000\n"
        "Hotline 119 ext 9 untuk mendapatkan bantuan apabila ada gejala\n"
        "Semoga kamu sehat-sehat selalu. ",
        reply_markup=markup,parse_mode=telegram.ParseMode.MARKDOWN)
        
    return CHOOSING


def regular_choice(update, context):
    x = update.message.text.upper()
    context.user_data['choice'] = x
    if x == 'A':
        try:
            from urllib.request import urlopen
            html = urlopen("https://www.covid19.go.id/").read()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            mes = ""
            for s in soup.find('div', class_='fusion-layout-column fusion_builder_column fusion_builder_column_1_3 fusion-builder-column-7 fusion-one-third fusion-column-first 1_3').find_all('span'):
                mes += s.text + '\n'
            mes += "Untuk info peta sebaran COVID-19 bisa klik link berikut: https://www.covid19.go.id/situasi-virus-corona/ \n\n" + "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini. "
            update.message.reply_text(mes,reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Untuk info peta sebaran COVID-19 bisa klik link berikut: https://www.covid19.go.id/situasi-virus-corona/ \n\n" + "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini. " 
                "",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'B':
        update.message.reply_text(
            "Coronavirus itu merupakan keluarga besar virus yang dapat menyerang manusia dan hewan. Nah, pada manusia, biasanya menyebabkan penyakit infeksi saluran pernafasan, mulai dari flu biasa hingga penyakit serius, seperti MERS dan SARS. \n\n" 
            "Covid-19 sendiri merupakan coronavirus jenis baru yang ditemukan pada manusia di daerah Wuhan, Provinsi Hubei, China pada tahun 2019. \n\n"
            "Maka dari itu, Coronavirus jenis baru ini diberi nama Coronavirus Disease-2019 yang disingkat menjadi Covid-19. \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini..",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'C':
        update.message.reply_text(
            "Gejala Covid-19 ini pada umumnya berupa:  \n"
            " *- Demam 38°C*  \n"
            " *- Batuk kering*  \n"
            " *- Sesak nafas*  \n\n"
            "Nah, kalau kamu habis berpergian dan 14 hari kemudian mengalami gejala ini, segera ke Rumah Sakit rujukan untuk memeriksakan diri kamu lebih menyeluruh. *Oh ya, saat ke Rumah Sakit, jangan menggunakan transportasi umum ya*.  \n\n"
            "Kenapa? Untuk mencegah penyebaran Covid-19 lebih luas.    \n\n"
            "Bisa hubungi *119 ext 9* untuk mendapatkan bantuan lebih lanjut.  \n\n"
            "Kamu mau tahu Rumah Sakit mana saja yang menjadi rujukan? Ketik *G*, atau ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'D':
        update.message.reply_text(
            "Yang dapat kamu lakukan dalam *melindungi diri sendiri* adalah dengan cara:   \n\n"
            "- Rajin-rajin cuci tangan dengan sabun! Jangan lupa! Sebelum makan, setelah dari toilet, setelah memegang binatang, atau setelah berpergian.  \n"
            "- Ketika batuk atau bersin jangan lupa untuk menutup mulut dan hidung kamu, ya. Pakai tissue, saputangan, atau lipatan siku.  \n"
            "- Hindari kontak dekat dengan orang yang menunjukkan gejala Covid-19  \n"
            "- Hindari kerumunan  \n"
            "- Jangan lupa untuk jaga jarak lebih dari 1 meter  antar kamu dan orang-orang di sekitarmu (social distancing)  \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'E':
        update.message.reply_text(
            "Yang bisa kamu lakukan untuk *melindungi orang-orang terdekatmu* dari Covid-19, yaitu:  \n\n"
            "- Saat kamu batuk atau bersin, jangan lupa untuk menjauh dan menutup mulut serta  hidung kamu dengan tissue, saputangan, atau lipatan siku.  \n"
            "- Segera membuang tisu atau masker yang telah kamu gunakan ke tempat sampah.   \n"
            "- Jangan lupa untuk merobek masker yang telah digunakan ya, untuk mencegah penggunaan ulang masker.   \n"
            "- Jangan lupa untuk mencuci tanganmu dengan sabun setelah batuk atau bersin.   \n"
            "- Jangan meludah disembarang tempat  \n"
            "- Segera menghubungi Rumah Sakit rujukan bila orang terdekatmu mengalami gejala Covid-19 dengan menghubungi 119 ext 9  \n\n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'F':
        update.message.reply_text(
            "Pemakaian masker sebenarnya *hanya* untuk mereka yang sedang batuk-batuk atau bersin. Penggunaan masker juga *dikhususkan bagi petugas* yang merawat Covid-19 ataupun *orang-orang terdekat* yang merawat orang bergejala Covid-19   \n\n"
            "Bagi kamu yang masih merasa khawatir dan tidak memiliki masker, *alternatif* yang dapat kamu lakukan adalah dengan *menggunakan kain*. Jangan lupa untuk *selalu mencuci kain yang dijadikan masker*.  \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'G':
        update.message.reply_text(
            "Kementerian Kesehatan sudah menentukan *132 Rumah Sakit* rujukan untuk menangani kasus Covid-19.  \n\n"
            "Untuk meminimalisir membludaknya isi chat kamu, saya perlu tahu kamu berada di Provinsi mana. Jawab saja kamu berada di Provinsi mana, contohnya *Jawa Barat*.   \n\n"
            "Atau kamu bisa ketik *MENU* (/start) untuk kembali ke menu utama, atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini.",parse_mode=telegram.ParseMode.MARKDOWN)
        return TYPING_REPLY
    elif x == 'SELESAI':
        update.message.reply_text(
            "Terima kasih sudah mampir ke pusat informasi Covid-19. Jaga kesehatan selalu. Jangan lupa rajin cuci tangan dengan sabun, makan-makanan yang sehat dan teratur,  serta menggunakan masker bila kamu sedang merasa tidak enak badan.   \n\n"
            "Jangan lupa juga untuk jaga jarak aman lebih dari 1 meter. Ayo kita cegah penyebaran Covid-19 lebih luas.   \n\n"
            "Untuk informasi lebih lanjut dapat kunjungi www.covid19.go.id. \n\nketik *MENU* (/start) jika ingin mengulangi perbincangan kembali.",parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
            "Jika ada  yang ingin kamu tanyakan ketik *MENU* (/start) atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini. ",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING


def received_information(update, context):
    x = update.message.text.upper()
    context.user_data['rumkit'] = x
    if x == 'ACEH':
        update.message.reply_text(
            "*ACEH*\n\n"
            "1. RSUD Dr Zainoel Abidin, Banda Aceh. Telepon: (0651 -34562)\n"
            "2. RSUD Cut Meutia, Lhokseumawe, Kabupaten Aceh Utara. Telepon: (0645) 46334\n\n"
            "Pemerintah Daerah Provinsi Aceh Darussalam membuka sambungan telepon untuk penanganan wabah corona pada nomor 081370113666",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SUMATERA UTARA':
        update.message.reply_text(
            "*SUMATERA UTARA*\n\n"
            "1. RSUP H Adam Malik, Medan. Telepon: (061) 8360051\n"
            "2. RSUD Kota Padang Sidempuan. Telepon: (0634) 21780\n"
            "3. RSUD Kabanjahe Telepon: (0628) 20012\n"
            "4. RSUD Tarutung, Tapanuli Utara. Telepon: (0633) 21303, 20450\n"
            "5. RSUD Dr Djasamen Saragih, Pematang Siantar. Telepon: (0622) 22959\n"
            "\n"
            "Dinas Kesehatan Sumatera Utara membuka juga layanan untuk informasi wabah corona melalui nomor 082164902482.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SUMATERA BARAT':
        update.message.reply_text(
            "*SUMATERA BARAT*\n\n"
            "1. RSUP dr M Djamil, Padang. Telepon: (0751) 32371\n"
            "2. RSUD Dr Achmad Mochtar, Bukittinggi. Telepon: (0752) 2172\n\n"
            "Provinsi Sumatera Barat membuka posko suspect wabah virus Corona untuk pengawasan terhadap orang-orang yang diduga terjangkit. Posko ini berlokasi *di lantai 1 Kantor Dinas Kesehatan Sumbar, Jalan Perintis Kemerdekaan No 65 A, Padang*.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'RIAU':
        update.message.reply_text(
            "*RIAU*\n\n"
            "1. RSU Arifin Achmad, Pekanbaru. Telepon: (0761) 23418, 21618, 21657\n"
            "2. RSU Kab. Karimun, Tg. Balai Karimun\n"
            "3. RSU Tanjung Pinang, Tanjung Pinang. Telepon: (0771) 21163\n"
            "4. RSU Puri Husada, Tembilahan. Telepon: (0768) 24563\n"
            "5. RSU Kota Dumai Telepon: (0765) 440992\n\n"
            "Sambungan telepon layanan terkait wabah virus Corona bagi warga Provinsi Riau melalui nomor (0761) 23810.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KEPULAUAN RIAU':
        update.message.reply_text(
            "*KEPULAUAN RIAU*\n\n"
            "1. RS Otorita Batam, Sekupang\n",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'BANGKA BELITUNG':
        update.message.reply_text(
            "*BANGKA BELITUNG*\n\n"
            "1. RSUD Dr H Marsidi Judono, Tanjungpandang, Kabupaten Belitung. Telepon: (0719) 22190\n"
            "2. RSUD Depati Hamzah, Pangkal Pinang. Telepon: (0717) 438660\n\n"
            "Bandara Depati Amir Pangkal Pinang terkoneksi ke RSUD Depati Hamzah, sementara Bandara HS Hanandjoeddin Belitung terhubung ke RSUD H Marsidi Judono, untuk pelayanan kesehatan apabila diperlukan.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SUMATERA SELATAN':
        update.message.reply_text(
            "*SUMATERA SELATAN*\n\n"
            "1. RSUP Dr Mohammad Hoesin, Palembang. Telepon: (0711) 354088, IGD: (0711) 315444\n"
            "2. RSUD Kayuagung, Ogan Komering Ilir. Telepon: (0712) 323889\n"
            "3. RSUD Lahat. Telepon: (0731) 323080\n"
            "4. RSU Lubuk Linggau. Telepon: (0733) 321013",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'BENGKULU':
        update.message.reply_text(
            "*BENGKULU*\n\n"
            "1. RSUD Dr M Yunus, Bengkulu. Telepon: (0736) 52004, (0736) 5111\n"
            "2. RSUD Hasanuddin Damrah Manna, Kabupaten Bengkulu Selatan. Telepon: 085381637684\n"
            "3. RSUD Arga Makmur, Kabupaten Bengkulu Utara. Telepon: (0737) 521118",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'JAMBI':
        update.message.reply_text(
            "*JAMBI*\n\n"
            "1. RSUD Raden Mattaher, Kota Jambi. Telepon: (0741) 61692",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'LAMPUNG':
        update.message.reply_text(
            "*LAMPUNG*\n\n"
            "1. RSUD Dr H Abdul Moeloek, Bandar Lampung. Telepon: (0721) 703312\n"
            "2. RSU Kalianda, Kabupaten Lampung Selatan. Telepon: (0727) 322160\n"
            "3. RSD May Jend HM Ryacudu, Kotabumi Telepon: (0724) 22095\n"
            "4. RSUD Jend Ahmad Yani, Kota Metro. Telepon: (0725) 41820",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'BANTEN':
        update.message.reply_text(
            "*BANTEN*\n\n"
            "1. RSU Kabupaten Tangerang, Kota Tangerang. Telepon: (021) 5523507\n"
            "2. RSUD Dr Drajat Prawiranegara, Kota Serang.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'JAWA BARAT':
        update.message.reply_text(
            "*JAWA BARAT*\n\n"
            "1. RSUP Dr Hasan Sadikin, Kota Bandung. Telepon: (022) 203495355, (022) 2551111, (022) 2034954\n"
            "2. RS Paru Dr H A Rotinsulu, Kota Bandung. Telepon: (022) 3034446\n"
            "3. RSUD R Syamsudin SH, Kota Sukabumi Telepon: (0266) 225180, 225181\n"
            "4. RSUD Kabupaten Indramayu Telepon: (0234) 272655\n"
            "5. RSUD Dr Slamet Garut Telepon: (0262) 232720, (0262) 237791\n"
            "6. RSD Gunung Jati Kota Cirebon Telepon: (0231) 206330, (0231)202441\n"
            "7. RSUD Subang Telepon: (0260) 417442, (0260) 411421\n"
            "\n"
            "Dinas Kesehatan Jawa Barat membuka sambungan telepon di nomor 08112093306 bagi masyarakat yang membutuhkan informasi mengenai virus Corona.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'JAKARTA':
        update.message.reply_text(
            "*JAKARTA*\n\n"
            "1. RSPI Sulianti Saroso, Sunter, Jakarta Utara. Telepon: (021) 6506559\n"
            "2. RSPAD Gatot Soebroto, Jakarta Pusat. Telepon: (021) 3440693\n"
            "3. RSUP Persahabatan, Jakarta Timur. Telepon: (021) 4891708\n"
            "\n"
            "Nomor darurat #JakartaTanggapCorona Dinas Kesehatan Provinsi DKI Jakarta di 112 atau *Posko Dinas Kesehatan di nomor WA* https://wa.me/6281388376955.⁣",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'JAWA TENGAH':
        update.message.reply_text(
            "*JAWA TENGAH*\n\n"
            "1. RSUP dr Kariadi, Semarang. Telepon: (024) 8413476\n"
            "2. RSUP dr Soeradji Tirtonegoro, Klaten. Telepon: (0272) 321041\n"
            "3. RSUD Dr H RM Soeselo, Slawi, Kabupaten Tegal. Telepon: (0283) 491016\n"
            "4. RSUD Dr H Soewondo, Kendal. Telepon: (0294) 381433\n"
            "5. RSUD Prof Dr Margono, Banyumas. Telepon: (0281) 632708\n"
            "6. RSUD Tidar Kota, Magelang. Telepon: (0293) 362260\n"
            "7. RSUD Dr Moewardi, Solo. Telepon: (0271) 634634\n"
            "8. RSUD Banyumas. Telepon: (0281) 796182\n"
            "9. RSUD Dr Loekmonohadi, Kudus. Telepon: (0291) 431831\n"
            "10. RSUD Bendan, Kota Pekalongan. Telepon: (0285) 437222\n"
            "\n"
            "Hotline *Dinas Kesehatan Jawa Tengah* : 024-3580713 dan 082313600560",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'YOGYAKARTA':
        update.message.reply_text(
            "*YOGYAKARTA*\n\n"
            "1. RSUP dr Sardjito, Sleman. Telepon: (0274) 631190, 587333\n"
            "2. RSUD Panembahan Senopati, Bantul. Telepon: (0274) 367381, 367386\n"
            "Tersedia juga *layanan kontak darurat di nomor 08112764800 untuk warga DI Yogyakarta* yang membutuhkan informasi terkait wabah virus Corona.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'JAWA TIMUR':
        update.message.reply_text(
            "*JAWA TIMUR*\n\n"
            "1. RSUD Dr Soebandi, Kabupaten Jember. Telepon: (0331) 487441\n"
            "2. RSUD Kabupaten Kediri Telepon: (0354) 391718\n"
            "3. RSUD Dr Soetomo, Surabaya. Telepon: (031) 5501001, IGD: (031) 5501239\n"
            "4. RSUD Dr Soedono, Madiun. Telepon: (0351) 464325, 464326, 454567\n"
            "5. RSUD Dr Saiful Anwar, Malang. Telepon: (0341) 362101\n"
            "6. RSUD dr R Koesma, Kabupaten Tuban. Telepon: (0356) 321010, 325696, 323266\n"
            "7. RSUD Blambangan, Banyuwangi. Telepon: (0333) 421118, 421071\n"
            "8. RSUD Dr R Sosodoro Djatikoesoemo, Bojonegoro. Telepon: (0353) 3412133\n\n"
            "Pemprov Jatim melalui Dinkes Jatim membuat layanan *Call Center Cangkrukan Kesehatan (Cacak Jatim)* untuk layanan kesehatan termasuk untuk konsultasi terkait Corona Virus Disease (COVID-19).\n"
            "\n"
            "*Layanan call center dibuka di dua saluran* yaitu di nomor 031-8430313 untuk layanan di hari aktif dan jam kerja, dan di nomor 081334367800 untuk di luar jam kerja yang juga aktif di hari libur.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KALIMANTAN UTARA':
        update.message.reply_text(
            "*KALIMANTAN UTARA*\n\n"
            "1. RSUD Tanjung Selor, Kabupaten Bulungan. Telepon: (0552) 21118\n"
            "2. RSUD Tarakan, Tarakan Tengah, Kota Tarakan. Telepon: (0551) 21166",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KALIMANTAN TENGAH':
        update.message.reply_text(
            "*KALIMANTAN TENGAH*\n\n"
            "1. RSUD Dr Doris Sylvanus, Palangkaraya. Telepon: (0536) 3224695, 3224695\n"
            "2. RSUD Dr Murjani, Sampit. Telepon: (0531) 21010\n",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KALIMANTAN SELATAN':
        update.message.reply_text(
            "1. RSUD Ulin Banjarmasin. Telepon: (0511) 3252180\n"
            "2. RSUD H Boejasin Pelaihari, Angsau, Kabupaten Tanah Laut. Telepon: (0512) 21083, IGD (0512) 22009\n\n"
            "Dinkes Kalsel: 08217718672 & 082157718673\n"
            "BPBD Kalsel: 1500-474\nBanjarmasin: 08118835566\nBanjar: 08126112119\nKota Baru: 082256000065 & 082256000099\nTapin:0811519772\nTanah Laut: 082252224118, 08115184, 081348379787\nTanah Bumbu: 081349680690 & 081382411780\nHST: 082159004569\nBalangan: 081250005119\nHSU: 0813 4938 0885\nHSS: 0811514686\nTabalong:08125005372",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KALIMANTAN TIMUR':
        update.message.reply_text(
            "*KALIMANTAN TIMUR*\n\n"
            "1. RSUD Abdul Wahab Sjahranie, Samarinda. Telepon: (0541) 738118\n"
            "2. RSUD Dr Kanujoso Djatiwibowo, Balikpapan. Telepon: (0542) 873901, (0542) 887955, (0542) 887966\n"
            "3. RSUD Panglima Sebaya, Kabupaten Paser. Telepon: (0543) 24563\n"
            "4. RSU Taman Husada, Bontang. Telepon: (0548) 22111, IGD (0548) 23000\n"
            "5. RSUD Aji Muhammad Parikesit, Tenggarong, Seberang Kutai Kertanegara. Telepon: (0541) 661015",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'KALIMANTAN BARAT':
        update.message.reply_text(
            "*KALIMANTAN BARAT*\n\n"
            "1. RSUD Dr Soedarso, Pontianak. Telepon: (0561) 737701\n"
            "2. RSUD Dr Abdul Azis, Singkawang. Telepon: (0562) 631798\n"
            "3. RSUD Ade Mohammad Djoen, Sintang. Telepon: (0565) 21002, 081345435555\n\n"
            "Kontak darurat terkait wabah virus Corona untuk Kalimantan Barat adalah 021-5210411. Sementara nomor 081212123119 untuk masyarakat yang membutuhkan informasi mengenai virus Corona.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'GORONTALO':
        update.message.reply_text(
            "*GORONTALO*\n\n"
            "1. RSUD Prof Dr H Aloei Saboe Telepon: 08124315555, IGD: 085298208997",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SULAWESI TENGAH':
        update.message.reply_text(
            "*SULAWESI TENGAH*\n\n"
            "1. RSUD Undata Palu. Telepon: (0451) 4908020\n"
            "2. RSUD Kabupaten Banggai Luwuk, Luwuk. Telepon: (0461) 21820\n"
            "3. RSU Mokopido Toli-Toli, Kabupaten Toli-Toli. Telepon: (0453) 21301\n"
            "4. RSUD Kolonedale, Kolonedale. Telepon: (0465) 21010\n"
            "5. RSU Anutapura Palu Telepon: (0451) 460570",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SULAWESI UTARA':
        update.message.reply_text(
            "*SULAWESI UTARA*\n\n"
            "1. RSUP Prof Dr R D Kandou, Manado. Telepon: (0431) 8383058\n"
            "2. RSUD Kota Kotamobagu Telepon: (0434) 822816\n"
            "3. RSU Ratatotok, Buyat. Telepon: (0431) 3177610\n"
            "4. RSUD Dr Sam Ratulangi, Luaan, Tondano Timur. Telepon: (0431) 321171\n\n"
            "Layanan khusus informasi terkait COVID-19 untuk masyarakat Sulawesi Utara dapat melalui nomor 085341223577.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SULAWESI BARAT':
        update.message.reply_text(
            "*SULAWESI BARAT*\n\n"
            "1. RSUD Provinsi Sulawesi Barat, Mamuju. Telepon: (0426) 2703260, 2703204\n\n"
            "Selain itu, Dinas Kesehatan Sulawesi Barat juga membuka pusat informasi dan call center yang bisa dihubungi untuk menanyakan soal virus corona ini, yaitu di nomor:\n"
            "081247758484\n"
            "08114608210\n"
            "085242908201\n"
            "085241255494\n"
            "085390206504",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SULAWESI SELATAN':
        update.message.reply_text(
            "*SULAWESI SELATAN*\n\n"
            "1. RSUP dr Wahidin Sudirohusodo, Makassar. Telepon: (0411) 584677\n"
            "2. RS Dr Tadjuddin Chalid, MPH, Makassar Telepon: (0411) 512902\n"
            "3. RSUD Labuang Baji, Makassar. Telepon: (0411) 872120\n"
            "4. RS Tk II Pelamonia, Makassar. Telepon: (0411) 7402332\n"
            "5. RSU Lakipadada Toraja, Tana Toraja. Telepon: (0423) 22264\n"
            "6. RSU Andi Makkasau Parepare, Parepare. Telepon: (0421) 21823\n\n"
            "Khusus Parepare, tersedia juga layanan kontak khusus (hotline) melalui telepon dan pesan layanan pendek (SMS) ke nomor: 081356240321, 082393232905.\n"
            "7. RSUD Kabupaten Sinjai Telepon: (0482) 21132\n"
            "\n"
            "Untuk informasi seputar COVID-19 dapat menghubungi Dinas Kesehatan Sulsel:\n"
            "085299354451, 081244244473, 085242088868",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SULAWESI TENGGARA':
        update.message.reply_text(
            "*SULAWESI TENGGARA*\n\n"
            "1. RS Bahtera Mas Provinsi Sulawesi Tenggara, atau RS Kendari. Telepon: (0401-3195611)\n\n"
            "Ikatan Dokter Indonesia (IDI) Sulawesi Tenggara membuka hotline untuk wabah virus corona di nomor 082187433107.",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'BALI':
        update.message.reply_text(
            "*SULAWESI BALI*\n\n"
            "1. RSUP Sanglah, Denpasar. Telepon: (0361) 227911-15\n"
            "2. RSUD Sanjiwani, Gianyar. Telepon: (0361) 943049\n"
            "3. RSU Tabanan Telepon: (0361) 811027, 819810, 811202\n",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'NUSA TENGGARA BARAT':
        update.message.reply_text(
            "*NUSA TENGGARA BARAT*\n\n"
            "1. RSUD Provinsi NTB, Bima. Telepon: (0370) 7502424, IGD (0370) 7504288\n"
            "2. RSU Bima Telepon: (0374) 43142\n"
            "3. RS H L Manambai Abdulkadir, Sumbawa Besar. Telepon: (0371) 2628078\n"
            "4. RSUD Dr R Soedjono, Selong. Telepon IGD: 01-123 2234567",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'NUSA TENGGARA TIMUR':
        update.message.reply_text(
            "*NUSA TENGGARA TIMUR*\n\n"
            "1. RSU Prof Dr WZ Johanes, Kupang. Telepon: (0380) 833614\n"
            "2. RSUD Dr Tc Hillers Jl Wairklau, Maumere, Kabupaten Sikka. Telepon: 081261153944\n",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'MALUKU':
        update.message.reply_text(
            "*MALUKU*\n\n"
            "1. RSU Dr M. Haulussy, Ambon. Telepon: (0911) 344871\n"
            "2. RSUP dr J Leimena, Ambon.\n"
            "3. RSUD Dr P P Magretti, Saumlaki, Tanimbar Selatan. Telepon: (0918) 21113",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'MALUKU UTARA':
        update.message.reply_text(
            "*MALUKU UTARA*\n\n"
            "1. RSUD Dr H Chasan Boesoirie, Ternate. Telepon: (0921) 3121281",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'PAPUA':
        update.message.reply_text(
            "*PAPUA*\n\n"
            "1. RSU Jayapura Telepon: (0967) 533616\n"
            "2. RSU Merauke Telepon: (0971) 32112\n"
            "3. RSU Nabire Telepon: (0984) 21845",parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'PAPUA BARAT':
        update.message.reply_text(
            "*PAPUA BARAT*\n\n"
            "1. RSUD Manokwari Telepon: (0986) 211440\n"
            "2. RSUD Kabupaten Sorong Telepon: (0951) 321850.",parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text('Silakan mengakses http://komin.fo/RSRujukanCOVID19 untuk melihat daftar Rumah Sakit rujukan COVID-19.')
        
    update.message.reply_text(
            "Jika ada  yang ingin kamu tanyakan ketik *MENU* (/start) atau ketik *SELESAI* bila mau mengakhiri perbincangan kita hari ini. ",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

    return CHOOSING

def done(update, context):
    update.message.reply_text("Terimakasih!")
    user_data.clear()
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1012224527:AAEzqU9wOBC66cZYLR05Gy8IIp-3-xnE1YI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
    #Filters.regex('^Something else...$')
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(A|B|C|D|E|F|G|SELESAI)$'),
                                      regular_choice),
                       MessageHandler(Filters.text,
                                      start)
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.text,
                                           regular_choice)
                            ],

            TYPING_REPLY: [MessageHandler(Filters.text,
                                          received_information),
                           ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )
    
    dp.add_handler(conv_handler)
    
    # log all errors
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
