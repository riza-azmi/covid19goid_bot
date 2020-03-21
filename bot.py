#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# Author: Riza Azmi (Puslitbang SDP3I, Kemkominfo)

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
        "Halo! Selamat datang di *Pusat Informasi Covid-19 powered by Kemkominfo RI*. "
        "Semoga kamu sehat-sehat selalu. ",
        reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)

    update.message.reply_text(
        "Apa saja sih yang ingin kamu ketahui mengenai Covid-19?\n"
        "A. Kabar Covid-19 terkini di Indonesia\n"
        "B. Sebenarnya apa sih Covid-19 itu?\n"
        "C. Apa saja gejala Covid-19?\n"
        "D. Bagaimana cara melindungi diri?\n"
        "E. Bagaimana cara melindungi orang lain?\n"
        "F. Masker perlu gak sih?\n"
        "G. Rumah Sakit Rujukan Covid-19.\n\n"
        "Ketik A, B, C, D, E, F, atau G, lalu kirim ke kami. Maka, kami akan menjawab pertanyaan kamu.\n\n"
        "Bagikan info akurat tentang COVID-19 ke teman dan keluargamu 🙏\n\n\n"
        "www.covid19.go.id\n"
        "0811 333 99 000\n"
        "Hotline 119 ext 9 untuk mendapatkan bantuan apabila ada gejala\n"
        "Semoga kamu sehat-sehat selalu. ",
        reply_markup=markup)
        
    return CHOOSING


def regular_choice(update, context):
    x = update.message.text.upper()
    context.user_data['choice'] = x
    if x == 'A':
        from urllib.request import urlopen
        html = urlopen("https://www.covid19.go.id/").read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        mes = ""
        for s in soup.find('div', class_='fusion-layout-column fusion_builder_column fusion_builder_column_1_3 fusion-builder-column-7 fusion-one-third fusion-column-first 1_3').find_all('span'):
            mes += s.text + '\n'
        mes += "Untuk info peta sebaran COVID-19 bisa klik link berikut: https://www.covid19.go.id/situasi-virus-corona/ \n\n" + "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini. "
        update.message.reply_text(mes,reply_markup=markup2)
    elif x == 'B':
        update.message.reply_text(
            "Coronavirus itu merupakan keluarga besar virus yang dapat menyerang manusia dan hewan. Nah, pada manusia, biasanya menyebabkan penyakit infeksi saluran pernafasan, mulai dari flu biasa hingga penyakit serius, seperti MERS dan SARS. \n\n" 
            "Covid-19 sendiri merupakan coronavirus jenis baru yang ditemukan pada manusia di daerah Wuhan, Provinsi Hubei, China pada tahun 2019. \n\n"
            "Maka dari itu, Coronavirus jenis baru ini diberi nama Coronavirus Disease-2019 yang disingkat menjadi Covid-19. \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini..",reply_markup=markup2)
    elif x == 'C':
        update.message.reply_text(
            "Gejala Covid-19 ini pada umumnya berupa:  \n"
            " - Demam 38°C  \n"
            " - Batuk kering  \n"
            " - Sesak nafas  \n\n"
            "Nah, kalau kamu habis berpergian dan 14 hari kemudian mengalami gejala ini, segera ke Rumah Sakit rujukan untuk memeriksakan diri kamu lebih menyeluruh. Oh ya, saat ke Rumah Sakit, jangan menggunakan transportasi umum ya.  \n\n"
            "Kenapa? Untuk mencegah penyebaran Covid-19 lebih luas.    \n\n"
            "Bisa hubungi 119 ext 9 untuk mendapatkan bantuan lebih lanjut.  \n\n"
            "Kamu mau tahu Rumah Sakit mana saja yang menjadi rujukan? Ketik G, atau ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2)
    elif x == 'D':
        update.message.reply_text(
            "Yang dapat kamu lakukan dalam melindungi diri sendiri adalah dengan cara:   \n\n"
            "- Rajin-rajin cuci tangan dengan sabun! Jangan lupa! Sebelum makan, setelah dari toilet, setelah memegang binatang, atau setelah berpergian.  \n"
            "- Ketika batuk atau bersin jangan lupa untuk menutup mulut dan hidung kamu, ya. Pakai tissue, saputangan, atau lipatan siku.  \n"
            "- Hindari kontak dekat dengan orang yang menunjukkan gejala Covid-19  \n"
            "- Hindari kerumunan  \n"
            "- Jangan lupa untuk jaga jarak lebih dari 1 meter  antar kamu dan orang-orang di sekitarmu (social distancing)  \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2)
    elif x == 'E':
        update.message.reply_text(
            "Yang bisa kamu lakukan untuk melindungi orang-orang terdekatmu dari Covid-19, yaitu:  \n\n"
            "- Saat kamu batuk atau bersin, jangan lupa untuk menjauh dan menutup mulut serta  hidung kamu dengan tissue, saputangan, atau lipatan siku.  \n"
            "- Segera membuang tisu atau masker yang telah kamu gunakan ke tempat sampah.   \n"
            "- Jangan lupa untuk merobek masker yang telah digunakan ya, untuk mencegah penggunaan ulang masker.   \n"
            "- Jangan lupa untuk mencuci tanganmu dengan sabun setelah batuk atau bersin.   \n"
            "- Jangan meludah disembarang tempat  \n"
            "- Segera menghubungi Rumah Sakit rujukan bila orang terdekatmu mengalami gejala Covid-19 dengan menghubungi 119 ext 9  \n\n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2)
    elif x == 'F':
        update.message.reply_text(
            "Pemakaian masker sebenarnya hanya untuk mereka yang sedang batuk-batuk atau bersin. Penggunaan masker juga dikhususkan bagi petugas yang merawat Covid-19 ataupun orang-orang terdekat yang merawat orang bergejala Covid-19   \n\n"
            "Bagi kamu yang masih merasa khawatir dan tidak memiliki masker, alternatif yang dapat kamu lakukan adalah dengan menggunakan kain. Jangan lupa untuk selalu mencuci kain yang dijadikan masker.  \n\n"
            "Ada lagi yang ingin kamu tanyakan? Kalau ada, ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini.",reply_markup=markup2)
    elif x == 'G':
        update.message.reply_text(
            "Kementerian Kesehatan sudah menentukan 132 Rumah Sakit rujukan untuk menangani kasus Covid-19.  \n\n"
            "Untuk meminimalisir membludaknya isi chat kamu, saya perlu tahu kamu berada di Provinsi mana. Jawab saja kamu berada di Provinsi mana, contohnya Jawa Barat.   \n\n"
            "Atau kamu bisa ketik MENU untuk kembali ke menu utama, atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini.")
        return TYPING_REPLY
    elif x == 'SELESAI':
        update.message.reply_text(
            "Terima kasih sudah mampir ke pusat informasi Covid-19. Jaga kesehatan selalu. Jangan lupa rajin cuci tangan dengan sabun, makan-makanan yang sehat dan teratur,  serta menggunakan masker bila kamu sedang merasa tidak enak badan.   \n\n"
            "Jangan lupa juga untuk jaga jarak aman lebih dari 1 meter. Ayo kita cegah penyebaran Covid-19 lebih luas.   \n\n"
            "Untuk informasi lebih lanjut dapat kunjungi www.covid19.go.id. \n\nKetik MENU jika ingin mengulangi perbincangan kembali.")
    else:
        update.message.reply_text(
            "Jika ada  yang ingin kamu tanyakan ketik MENU atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini. ",reply_markup=markup2)
    return CHOOSING


def received_information(update, context):
    x = update.message.text.upper()
    context.user_data['rumkit'] = x
    if x == 'ACEH':
        update.message.reply_text(
            "ACEH\n\n"
            "1. RSUD Dr Zainoel Abidin, Banda Aceh.\n"
            "   Telepon: (0651 -34562)\n"
            "2. RSUD Cut Meutia, Lhokseumawe, Kabupaten Aceh Utara.\n"
            "   Telepon: (0645) 46334\n\n"
            "Pemerintah Daerah Provinsi Aceh Darussalam membuka sambungan telepon untuk penanganan wabah corona pada nomor 081370113666")
    elif x == 'SUMATERA UTARA':
        update.message.reply_text(
            "SUMATERA UTARA\n\n"
            "1. RSUP H Adam Malik, Medan.\n"
            "   Telepon: (061) 8360051\n"
            "2. RSUD Kota Padang Sidempuan.\n"
            "   Telepon: (0634) 21780\n"
            "3. RSUD Kabanjahe\n"
            "   Telepon: (0628) 20012\n"
            "4. RSUD Tarutung, Tapanuli Utara.\n"
            "   Telepon: (0633) 21303, 20450\n"
            "5. RSUD Dr Djasamen Saragih, Pematang Siantar.\n"
            "   Telepon: (0622) 22959\n"
            "\n"
            "Dinas Kesehatan Sumatera Utara membuka juga layanan untuk informasi wabah corona melalui nomor 082164902482.")
    elif x == 'SUMATERA BARAT':
        update.message.reply_text(
            "SUMATERA BARAT\n\n"
            "1. RSUP dr M Djamil, Padang.\n"
            "   Telepon: (0751) 32371\n"
            "2. RSUD Dr Achmad Mochtar, Bukittinggi.\n"
            "   Telepon: (0752) 2172\n"
            "3. Provinsi Sumatera Barat membuka posko suspect wabah virus Corona untuk pengawasan terhadap orang-orang yang diduga terjangkit. Posko ini berlokasi di lantai 1 Kantor Dinas Kesehatan Sumbar, Jalan Perintis Kemerdekaan No 65 A, Padang.")
    elif x == 'RIAU':
        update.message.reply_text(
            "RIAU\n\n"
            "1. RSUD Arifin Achmad, Pekanbaru.\n"
            "   Telepon: (0761) 23418, 21618, 21657\n"
            "2. RSUD Puri Husada, Tembilahan.\n"
            "   Telepon: (0768) 24563\n"
            "3. RSUD Kota Dumai\n"
            "   Telepon: (0765) 440992\n"
            "4. Sambungan telepon layanan terkait wabah virus Corona bagi warga Provinsi Riau melalui nomor (0761) 23810.")
    elif x == 'KEPULAUAN RIAU':
        update.message.reply_text(
            "RIAU\n\n"
            "1. RSUD Embung Fatimah, Batu Aji, Kota Batam.\n"
            "   Telepon: (0778) 364446\n"
            "2. RSBP Batam, Sekupang, Batam.\n"
            "   Telepon: (0778) 322046, 322121\n"
            "4. RSUD Provinsi Kepulauan Riau, Tanjungpinang.\n"
            "   Telepon: (0771) 7335203\n"
            "5. RSUD Muhammad Sani, Tanjung Balai Karimun, Kabupatan Karimun.\n"
            "   Telepon: (0777) 327808")
    elif x == 'BANGKA BELITUNG':
        update.message.reply_text(
            "BANGKA BELITUNG\n\n"
            "1. RSUD Dr H Marsidi Judono, Tanjungpandang, Kabupaten Belitung.\n"
            "   Telepon: (0719) 22190\n"
            "2. RSUD Depati Hamzah, Pangkal Pinang.\n"
            "   Telepon: (0717) 438660\n"
            "3. Bandara Depati Amir Pangkal Pinang terkoneksi ke RSUD Depati Hamzah, sementara Bandara HS Hanandjoeddin Belitung terhubung ke RSUD H Marsidi Judono, untuk pelayanan kesehatan apabila diperlukan.")
    elif x == 'SUMATERA SELATAN':
        update.message.reply_text(
            "SUMATERA SELATAN\n\n"
            "1. RSUP Dr Mohammad Hoesin, Palembang.\n"
            "   Telepon: (0711) 354088, IGD: (0711) 315444\n"
            "2. RS Dr Rivai Abdullah, Kabupaten Banyuasin.\n"
            "   Telepon: (0711) 7537201\n"
            "3. RSUD Kayuagung, Ogan Komering Ilir.\n"
            "   Telepon: (0712) 323889\n"
            "4. RSUD Lahat.\n"
            "   Telepon: (0731) 323080\n"
            "5. RSUD Siti Fatimah, Palembang.\n"
            "   Telepon: (0711) 5178883, 5718889")
    elif x == 'BENGKULU':
        update.message.reply_text(
            "BENGKULU\n\n"
            "1. RSUD Dr M Yunus, Bengkulu.\n"
            "   Telepon: (0736) 52004, (0736) 5111\n"
            "2. RSUD Hasanuddin Damrah Manna, Kabupaten Bengkulu Selatan.\n"
            "   Telepon: 085381637684\n"
            "3. RSUD Arga Makmur, Kabupaten Bengkulu Utara.\n"
            "   Telepon: (0737) 521118")
    elif x == 'JAMBI':
        update.message.reply_text(
            "JAMBI\n\n"
            "1. RSUD Raden Mattaher, Kota Jambi.\n"
            "   Telepon: (0741) 61692")
    elif x == 'LAMPUNG':
        update.message.reply_text(
            "LAMPUNG\n\n"
            "1. RSUD Dr H Abdul Moeloek, Bandar Lampung.\n"
            "   Telepon: (0721) 703312\n"
            "2. RSUD Dr H Bob Bazar SKM, Kabupaten Lampung Selatan.\n"
            "   Telepon: (0727) 322159\n"
            "3. RSD May Jend HM Ryacudu, Kotabumi\n"
            "   Telepon: (0724) 22095\n"
            "4. RSUD Jend Ahmad Yani, Kota Metro.\n"
            "   Telepon: (0725) 41820")
    elif x == 'BANTEN':
        update.message.reply_text(
            "BANTEN\n\n"
            "1. RSU Kabupaten Tangerang, Kota Tangerang.\n"
            "   Telepon: (021) 5523507\n"
            "2. RSUD Dr Drajat Prawiranegara, Kota Serang.")
    elif x == 'JAWA BARAT':
        update.message.reply_text(
            "JAWA BARAT\n\n"
            "1. RSUP Dr Hasan Sadikin, Kota Bandung.\n"
            "   Telepon: (022) 203495355, (022) 2551111, (022) 2034954\n"
            "2. RS Paru Dr H A Rotinsulu, Kota Bandung.\n"
            "   Telepon: (022) 3034446\n"
            "3. RS Paru Dr M Goenawan Partowidigdo, Cisarua, Bogor.\n"
            "   Telepon: (0251) 8253630\n"
            "4. RSUD R Syamsudin SH, Kota Sukabumi\n"
            "   Telepon: (0266) 225180, 225181\n"
            "5. RSUD Kabupaten Indramayu\n"
            "   Telepon: (0234) 272655\n"
            "6. RSUD Dr Slamet Garut\n"
            "   Telepon: (0262) 232720, (0262) 237791\n"
            "7. RSD Gunung Jati Kota Cirebon\n"
            "   Telepon: (0231) 206330, (0231)202441\n"
            "8. RS TK II 03.05.01 Dustira, Kota Cimahi.\n"
            "   Telepon: (022) 6652207, (022) 2034446\n"
            "9. RSUD Subang\n"
            "   Telepon: (0260) 417442, (0260) 411421\n"
            "\n"
            "Dinas Kesehatan Jawa Barat membuka sambungan telepon di nomor 08112093306 bagi masyarakat yang membutuhkan informasi mengenai virus Corona.")
    elif x == 'JAKARTA':
        update.message.reply_text(
            "JAKARTA\n\n"
            "1. RSPI Sulianti Saroso, Sunter, Jakarta Utara.\n"
            "   Telepon: (021) 6506559\n"
            "2. RSPAD Gatot Soebroto, Jakarta Pusat.\n"
            "   Telepon: (021) 3440693\n"
            "3. RSUD Cengkareng, Cengkareng, Jakarta Barat.\n"
            "   Telepon: (021) 54372874\n"
            "4. RS Umum Bhayangkara Tk 1 R Said Sukanto (RS Polri), Jakarta Timur.\n"
            "   Telepon: (021) 8093288\n"
            "5. RSUP Persahabatan, Jakarta Timur.\n"
            "   Telepon: (021) 4891708\n"
            "6. RSAL Mintoharjo, Jakarta Pusat.\n"
            "   Telepon: (021) 5703081\n"
            "7. RSUD Pasar Minggu, Jakarta Selatan.\n"
            "   Telepon: (021) 29059999\n"
            "8. RSUP Fatmawati, Jakarta Selatan.\n"
            "   Telepon: (021) 7501524\n"
            "\n"
            "Nomor darurat #JakartaTanggapCorona Dinas Kesehatan Provinsi DKI Jakarta di 112 atau Posko Dinas Kesehatan di nomor WA 0813-8837-6955.⁣")
    elif x == 'JAWA TENGAH':
        update.message.reply_text(
            "1. RSUP dr Kariadi, Semarang.\n"
            "   Telepon: (024) 8413476\n"
            "2. RSUD KRMT Wongsonegoro, Kota Semarang.\n"
            "   Telepon: (024) 6711500\n"
            "3. RSU Columbia Asia, Semarang.\n"
            "   Telepon: (024) 7629999\n"
            "4. RSU Sultan Agung, Semarang.\n"
            "   Telepon: (024) 6580019\n"
            "5. RSU St Elizabeth, Semarang.\n"
            "   Telepon: (024) 8310035\n"
            "6. RSU Telogorejo, Semarang.\n"
            "   Telepon: (024) 86466000\n"
            "7. RSU Tk III Bhakti Wira Tamtama, Kota Semarang.\n"
            "   Telepon: (024) 3555944\n"
            "8. RSUD Tugurejo, Semarang.\n"
            "   Telepon: (024) 7605297\n"
            "9. RSUP dr Soeradji Tirtonegoro, Klaten.\n"
            "   Telepon: (0272) 321041\n"
            "10.RSUD Kraton Kabupaten, Pekalongan.\n"
            "   Telepon: (0285) 421621\n"
            "11.RSUD Dr H RM Soeselo, Slawi, Kabupaten Tegal.\n"
            "   Telepon: (0283) 491016\n"
            "12.RSUD Dr H Soewondo, Kendal.\n"
            "   Telepon: (0294) 381433\n"
            "13.RSUD Prof Dr Margono, Banyumas.\n"
            "   Telepon: (0281) 632708\n"
            "14.RSUD Tidar Kota, Magelang.\n"
            "   Telepon: (0293) 362260\n"
            "15.RSUD Dr Moewardi, Solo.\n"
            "   Telepon: (0271) 634634\n"
            "16.RS Paru Dr Ario Wirawan, Salatiga.\n"
            "   Telepon: (0298) 326130\n"
            "17.RSUD Banyumas.\n"
            "   Telepon: (0281) 796182\n"
            "18.RSUD Dr Loekmonohadi, Kudus.\n"
            "   Telepon: (0291) 431831\n"
            "19.RSUD Kardinah, Tegal.\n"
            "   Telepon: (0283) 350377\n"
            "20.RSUD Salatiga.\n"
            "   Telepon: (0298) 324074\n"
            "21.RSU Tk IV 04.07.03 dr Asmir, Salatiga\n"
            "   Telepon: (0298) 326045\n"
            "22.RSUD Ambarawa\n"
            "   Telepon: (0298) 591020\n"
            "23.RSUD Sunan Kalijaga, Demak.\n"
            "   Telepon: (0291) 685018\n"
            "24.RSUD dr R Soedjati, Grobogan.\n"
            "   Telepon: (0292) 421004\n"
            "25.RSU Bhayangkara, Semarang.\n"
            "   Telepon: (024) 6720675\n"
            "26.RSU Tk II dr Seodjono, Magelang.\n"
            "   Telepon: (0293) 363061\n"
            "27.RSUD RAA Soewondo, Pati.\n"
            "   Telepon: (0295) 381102\n"
            "28.RSUD RA Kartini, Jepara.\n"
            "   Telepon: (0291) 591175\n"
            "29.RSUD dr R Soetrasno, Rembang.\n"
            "   Telepon: (0295) 691444\n"
            "30.RSUD dr R Soetijono, Blora.\n"
            "   Telepon: (0296) 531118\n"
            "31.RSU Mardi Rahayu, Kudus.\n"
            "   Telepon: (0291) 438234\n"
            "32.RSUD Bendan, Kota Pekalongan.\n"
            "   Telepon: (0285) 437222\n"
            "33.RSUD Kajen, Kabupaten Pekalongan.\n"
            "   Telepon: (0285) 385231\n"
            "34.RSUD Batang.\n"
            "   Telepon: (0285) 4493034\n"
            "35.RSUD Dr M Ashari, Pemalang.\n"
            "   Telepon: (0284) 321614\n"
            "36.RSUD Brebes.\n"
            "   Telepon: (0283) 671431\n"
            "37.RSU Islam Harapan Anda, Kota Tegal.\n"
            "   Telepon: (0283) 358244\n"
            "38.RSUD Cilacap\n"
            "   Telepon: (0282) 533010\n"
            "39.RSUD Hj Anna Lasmanah, Banjarnegara.\n"
            "   Telepon: (0286) 591464\n"
            "40.RSUD dr R Goeteng Taroenadibrata, Purbalingga.\n"
            "   Telepon: (0281) 891016\n"
            "41.RSUD Setjonegoro, Wonosobo.\n"
            "   Telepon: (0286) 321091\n"
            "42.RSUD dr Soedirman, Kabupaten Kebumen.\n"
            "   Telepon: (0287) 381101\n"
            "43.RSU Tk III Wijayakusuma, Purwokerto.\n"
            "   Telepon: (0281) 633062\n"
            "44.RSUD Kota Surakarta.\n"
            "   Telepon: (0271) 715300\n"
            "45.RSUD Ir Soekarno, Sukoharjo.\n"
            "   Telepon: (0271) 593118\n"
            "46.RSUD Pandan Arang, Boyolali.\n"
            "   Telepon: (0276) 321065\n"
            "47.RSUD Bagas Waras, Klaten.\n"
            "   Telepon: (0272) 3359666\n"
            "48.RSUD Soehadi Prijonegoro, Sragen.\n"
            "   Telepon: (0271) 891068\n"
            "49.RSUD Karanganyar.\n"
            "   Telepon: (0271) 495673\n"
            "50.RSUD Dr Soediran MS, Wonogiri.\n"
            "   Telepon: (0273) 321008\n"
            "51.RSU PKU Muhammadiyah, Surakarta.\n"
            "   Telepon: (0271) 714578\n"
            "52.RSU Islam, Klaten.\n"
            "   Telepon: (0272) 322252\n"
            "53.RS Kasih Ibu, Surakarta.\n"
            "   Telepon: (0271) 714422\n"
            "54.RS dr Oen, Surakarta.\n"
            "   Telepon: (0271) 643139\n"
            "55.RSU Tk IV Slamet Riyadi, Surakarta.\n"
            "   Telepon: (0271) 714656\n"
            "56.RSUD Djojonegoro, Temanggung.\n"
            "   Telepon: (0293) 491119\n"
            "57.RSUD Dr Tjitrowardojo, Purworejo.\n"
            "   Telepon: (0275) 321118\n"
            "58.RSUD Muntilan, Kabupaten Magelang.\n"
            "   Telepon: (0293) 587004\n"
            "\n"
            "Hotline Dinas Kesehatan Jawa Tengah : 024-3580713 dan 082313600560")
    elif x == 'DAERAH ISTIMEWA YOGYAKARTA':
        update.message.reply_text(
            "1. RSUD Kota Yogyakarta.\n"
            "   Telepon: (0274) 371195, 386691\n"
            "2. RSUP dr Sardjito, Sleman.\n"
            "   Telepon: (0274) 631190, 587333\n"
            "3. RSUD Panembahan Senopati, Bantul.\n"
            "   Telepon: (0274) 367381, 367386\n"
            "4. RSUD Wates\n"
            "   Telepon: (0274) 773169\n\n"
            "Tersedia juga layanan kontak darurat di nomor 08112764800 untuk warga DI Yogyakarta yang membutuhkan informasi terkait wabah virus Corona.")
    elif x == 'JAWA TIMUR':
        update.message.reply_text(
            "1. RSUD Dr Soebandi, Kabupaten Jember.\n"
            "   Telepon: (0331) 487441\n"
            "2. RSUD Kabupaten Kediri\n"
            "   Telepon: (0354) 391718\n"
            "3. RSUD Dr Soetomo, Surabaya.\n"
            "   Telepon: (031) 5501001, IGD: (031) 5501239\n"
            "4. RSUD Dr Soedono, Madiun.\n"
            "   Telepon: (0351) 464325, 464326, 454567\n"
            "5. RSUD Dr Saiful Anwar, Malang.\n"
            "   Telepon: (0341) 362101\n"
            "6. RSUD dr R Koesma, Kabupaten Tuban.\n"
            "   Telepon: (0356) 321010, 325696, 323266\n"
            "7. RSUD Blambangan, Banyuwangi.\n"
            "   Telepon: (0333) 421118, 421071\n"
            "8. RSUD Dr R Sosodoro Djatikoesoemo, Bojonegoro.\n"
            "   Telepon: (0353) 3412133\n"
            "9. RSUD Dr Iskak, Kabupaten Tulungagung\n"
            "   Telepon: (0355) 322609\n"
            "10.RSUD Sidoarjo\n"
            "   Telepon: (031) 8961649\n"
            "11.RS Universitas Airlangga Kampus C Universitas Airlangga, Mulyorejo, Surabaya.\n"
            "   Telepon: (031) 5916290, 5916287, 58208280\n"
            "\n"
            "Pemprov Jatim melalui Dinkes Jatim membuat layanan Call Center Cangkrukan Kesehatan (Cacak Jatim) untuk layanan kesehatan termasuk untuk konsultasi terkait Corona Virus Disease (COVID-19).\n"
            "\n"
            "Layanan call center dibuka di dua saluran yaitu di nomor 031-8430313 untuk layanan di hari aktif dan jam kerja, dan di nomor 081334367800 untuk di luar jam kerja yang juga aktif di hari libur.")
    elif x == 'KALIMANTAN UTARA':
        update.message.reply_text(
            "1. RSUD Tanjung Selor, Kabupaten Bulungan.\n"
            "   Telepon: (0552) 21118\n"
            "2. RSUD Tarakan, Tarakan Tengah, Kota Tarakan.\n"
            "   Telepon: (0551) 21166")
    elif x == 'KALIMANTAN TENGAH':
        update.message.reply_text(
            "1. RSUD Dr Doris Sylvanus, Palangkaraya.\n"
            "   Telepon: (0536) 3224695, 3224695\n"
            "2. RSUD Dr Murjani, Sampit.\n"
            "   Telepon: (0531) 21010\n"
            "3. RSUD Sultan Imanuddin, Pangkalan Bun.\n"
            "   Telepon: (0532) 21404")
    elif x == 'KALIMANTAN SELATAN':
        update.message.reply_text(
            "1. RSUD Ulin Banjarmasin.\n"
            "   Telepon: (0511) 3252180\n"
            "2. RSUD H Boejasin Pelaihari, Angsau, Kabupaten Tanah Laut.\n"
            "   Telepon: (0512) 21083, IGD (0512) 22009")
    elif x == 'KALIMANTAN TIMUR':
        update.message.reply_text(
            "1. RSUD Abdul Wahab Sjahranie, Samarinda.\n"
            "   Telepon: (0541) 738118\n"
            "2. RSUD Dr Kanujoso Djatiwibowo, Balikpapan.\n"
            "   Telepon: (0542) 873901, (0542) 887955, (0542) 887966\n"
            "3. RSUD Panglima Sebaya, Kabupaten Paser.\n"
            "   Telepon: (0543) 24563\n"
            "4. RSU Taman Husada, Bontang.\n"
            "   Telepon: (0548) 22111, IGD (0548) 23000\n"
            "5. RSUD Aji Muhammad Parikesit, Tenggarong, Seberang Kutai Kertanegara.\n"
            "   Telepon: (0541) 661015")
    elif x == 'KALIMANTAN BARAT':
        update.message.reply_text(
            "1. RSUD Dr Soedarso, Pontianak.\n"
            "   Telepon: (0561) 737701\n"
            "2. RSUD Dr Abdul Azis, Singkawang.\n"
            "   Telepon: (0562) 631798\n"
            "3. RSUD Ade Mohammad Djoen, Sintang.\n"
            "   Telepon: (0565) 21002, 081345435555\n"
            "4. RSUD Dr Agoesdjam, Ketapang.\n"
            "   Telepon: (0534) 3037239\n\n"
            "Kontak darurat terkait wabah virus Corona untuk Kalimantan Barat adalah 021-5210411. Sementara nomor 081212123119 untuk masyarakat yang membutuhkan informasi mengenai virus Corona.")
    elif x == 'GORONTALO':
        update.message.reply_text(
            "1. RSUD Prof Dr H Aloei Saboe\n"
            "   Telepon: 08124315555, IGD: 085298208997")
    elif x == 'SULAWESI TENGAH':
        update.message.reply_text(
            "1. RSUD Undata Palu.\n"
            "   Telepon: (0451) 4908020\n"
            "2. RSUD Kabupaten Banggai Luwuk, Luwuk.\n"
            "   Telepon: (0461) 21820\n"
            "3. RSU Mokopido Toli-Toli, Kabupaten Toli-Toli.\n"
            "   Telepon: (0453) 21301\n"
            "4. RSUD Kolonedale, Kolonedale.\n"
            "   Telepon: (0465) 21010\n"
            "5. RSU Anutapura Palu\n"
            "   Telepon: (0451) 460570")
    elif x == 'SULAWESI UTARA':
        update.message.reply_text(
            "1. RSUP Prof Dr R D Kandou, Manado.\n"
            "   Telepon: (0431) 8383058\n"
            "2. RSUD Kota Kotamobagu\n"
            "   Telepon: (0434) 822816\n"
            "3. RSU Ratatotok, Buyat.\n"
            "   Telepon: (0431) 3177610\n"
            "4. RSUD Dr Sam Ratulangi, Luaan, Tondano Timur.\n"
            "   Telepon: (0431) 321171\n\n"
            "Layanan khusus informasi terkait COVID-19 untuk masyarakat Sulawesi Utara dapat melalui nomor 085341223577.")
    elif x == 'SULAWESI BARAT':
        update.message.reply_text(
            "1. RSUD Provinsi Sulawesi Barat, Mamuju.\n"
            "   Telepon: (0426) 2703260, 2703204\n\n"
            "Selain itu, Dinas Kesehatan Sulawesi Barat juga membuka pusat informasi dan call center yang bisa dihubungi untuk menanyakan soal virus corona ini, yaitu di nomor:\n"
            "081247758484\n"
            "08114608210\n"
            "085242908201\n"
            "085241255494\n"
            "085390206504")
    elif x == 'SULAWESI SELATAN':
        update.message.reply_text(
            "1. RSUP dr Wahidin Sudirohusodo, Makassar.\n"
            "   Telepon: (0411) 584677\n"
            "2. RS Dr Tadjuddin Chalid, MPH, Makassar\n"
            "   Telepon: (0411) 512902\n"
            "3. RSUD Labuang Baji, Makassar.\n"
            "   Telepon: (0411) 872120\n"
            "4. RS Tk II Pelamonia, Makassar.\n"
            "   Telepon: (0411) 7402332\n"
            "5. RSU Lakipadada Toraja, Tana Toraja.\n"
            "   Telepon: (0423) 22264\n"
            "6. RSU Andi Makkasau Parepare, Parepare.\n"
            "   Telepon: (0421) 21823\n\n"
            "Khusus Parepare, tersedia juga layanan kontak khusus (hotline) melalui telepon dan pesan layanan pendek (SMS) ke nomor: 081356240321, 082393232905.\n"
            "7. RSUD Kabupaten Sinjai\n"
            "   Telepon: (0482) 21132\n"
            "\n"
            "Untuk informasi seputar COVID-19 dapat menghubungi Dinas Kesehatan Sulsel:\n"
            "085299354451, 081244244473, 085242088868")
    elif x == 'SULAWESI TENGGARA':
        update.message.reply_text(
            "1. RS Bahtera Mas Provinsi Sulawesi Tenggara, atau RS Kendari.\n"
            "   Telepon: (0401-3195611)\n\n"
            "Ikatan Dokter Indonesia (IDI) Sulawesi Tenggara membuka hotline untuk wabah virus corona di nomor 082187433107.")
    elif x == 'BALI':
        update.message.reply_text(
            "1. RSUP Sanglah, Denpasar.\n"
            "   Telepon: (0361) 227911-15\n"
            "2. RSUD Sanjiwani, Gianyar.\n"
            "   Telepon: (0361) 943049\n"
            "3. RSU Tabanan\n"
            "   Telepon: (0361) 811027, 819810, 811202\n"
            "4. RSUD Kabupaten Buleleng, Singaraja.\n"
            "   Telepon: (0362) 22046, 3307744")
    elif x == 'NUSA TENGGARA BARAT':
        update.message.reply_text(
            "1. RSUD Provinsi NTB, Bima.\n"
            "   Telepon: (0370) 7502424, IGD (0370) 7504288\n"
            "2. RSU Bima\n"
            "   Telepon: (0374) 43142\n"
            "3. RS H L Manambai Abdulkadir, Sumbawa Besar.\n"
            "   Telepon: (0371) 2628078\n"
            "4. RSUD Dr R Soedjono, Selong.\n"
            "   Telepon IGD: 01-123 2234567")
    elif x == 'NUSA TENGGARA TIMUR':
        update.message.reply_text(
            "1. RSU Prof Dr WZ Johanes, Kupang.\n"
            "   Telepon: (0380) 833614\n"
            "2. RSUD Dr Tc Hillers Jl Wairklau, Maumere, Kabupaten Sikka.\n"
            "   Telepon: 081261153944\n"
            "3. RSUD Komodo Labuan Bajo, Kabupaten Manggarai Barat.\n"
            "   Telepon: 081337055250")
    elif x == 'MALUKU':
        update.message.reply_text(
            "1. RSU Dr M. Haulussy, Ambon.\n"
            "   Telepon: (0911) 344871\n"
            "2. RSUP dr J Leimena, Ambon.\n"
            "3. RSUD Dr P P Magretti, Saumlaki, Tanimbar Selatan.\n"
            "   Telepon: (0918) 21113")
    elif x == 'MALUKU UTARA':
        update.message.reply_text(
            "1. RSUD Dr H Chasan Boesoirie, Ternate.\n"
            "   Telepon: (0921) 3121281")
    elif x == 'PAPUA':
        update.message.reply_text(
            "1. RSU Jayapura\n"
            "   Telepon: (0967) 533616\n"
            "2. RSU Merauke\n"
            "   Telepon: (0971) 32112\n"
            "3. RSU Nabire\n"
            "   Telepon: (0984) 21845")
    elif x == 'PAPUA BARAT':
        update.message.reply_text(
            "1. RSUD Manokwari\n"
            "   Telepon: (0986) 211440\n"
            "2. RSUD Kabupaten Sorong\n"
            "   Telepon: (0951) 321850.")
    else:
        update.message.reply_text('Daerah tidak ditemukan. Silakan mengakses covid19.go.id untuk melihat daftar Rumah Sakit rujukan.')
        
    update.message.reply_text(
            "Jika ada  yang ingin kamu tanyakan ketik MENU atau ketik SELESAI bila mau mengakhiri perbincangan kita hari ini. ",reply_markup=markup2)

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
    updater = Updater("MASUKKAN:TOKENDISINI", use_context=True)

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
