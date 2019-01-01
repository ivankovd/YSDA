import numpy as np
import requests
# from bs4 import BeautifulSoup

PAGES_IN_QUEUE = set()
START_PAGE = "/wiki/Sherutni_patrin"
_WIKI_PAGE_DEPTHS = {}


def bfs(start_page):
    queue_pages = [(start_page, 0)]
    while len(queue_pages) > 0:
        if len(queue_pages) == 1:
            print(1)
        # print("len stack {}".format(len(queue_pages)))
        # print(queue_pages)
        page, depth = queue_pages.pop(0)
        page = make_page_for_request(page)
        html_page = get_html_code(page)
        links_depth_for_queue = get_all_links_and_titles(html_page, depth)
        queue_pages.extend(links_depth_for_queue)
        # print(_WIKI_PAGE_DEPTHS)


def get_all_links_and_titles(html_code_page, depth):
    soup = BeautifulSoup(html_code_page, "lxml")
    raw_title = soup.findAll('a', attrs={"dir": "ltr"})[0].text
    title = get_title(raw_title)
    if title not in _WIKI_PAGE_DEPTHS:
        _WIKI_PAGE_DEPTHS[title] = depth

    elif _WIKI_PAGE_DEPTHS[title] > depth:
        _WIKI_PAGE_DEPTHS[title] = depth

    a_titles = soup.findAll("a")
    links = []
    for a_title in a_titles:
        attrs = a_title.__dict__["attrs"]
        if "class" not in attrs and "href" in attrs:
            if is_need_href(attrs["href"]):
                links.append(attrs["href"])

    links = np.unique(links)
    PAGES_IN_QUEUE.update(links)
    links_depth_for_queue = [(l, depth + 1) for l in links]
    return links_depth_for_queue


def get_html_code(page):
    return requests.get(page).text


def get_title(raw_title):
    return raw_title.split("title=")[-1].split("&")[0]


def make_page_for_request(page):
    if page.startswith("/wiki/"):
        return "https://rmy.wikipedia.org" + page
    # print("page dont stat with /wiki, {}".format(page))
    return page


def is_need_href(href):
    if href.startswith("/wiki/") and len(href.split("/")) == 3 and \
            href not in PAGES_IN_QUEUE and len(href.split(":")) == 1:
        return True
    return False


# bfs(START_PAGE)
# WIKI_PAGE_DEPTHS = _WIKI_PAGE_DEPTHS
# print(WIKI_PAGE_DEPTHS)

WIKI_PAGE_DEPTHS = {
    'Sherutni_patrin': 0, 'Banjara': 1, 'Chexanipen': 1,
    'Chiba_le_romenge': 1, 'Desi': 1, 'Devnagrī': 1, 'Kale': 1,
    'Lekh': 1, 'Pativ': 1, 'Patrinipen_le_bare_Romengo': 1,
    'Phuvipen': 1, 'Poraimos': 1, 'Romani_chib': 1,
    'Romano_lekhipen': 1, 'Romano_siklyaripen': 1,
    'Sikavdimos': 1, 'Sinti': 1,
    'Standardizuimi_Romani_chib': 1, 'Vikipidiya': 1,
    'Foro': 2, 'Gav': 2, 'Seloro': 2, 'Shelbersh': 2,
    'Sudutni_Asiya': 2, 'Chexay': 2, 'Jegeya': 2, 'Phuv': 2,
    'Samodor': 2, 'Shiyaron': 2, 'ABCD': 2,
    'Bari_Britaniya': 2, 'Nordutni_Amerika': 2, 'Them': 2,
    'Andalusiya': 2, 'Franchiya': 2,
    'Indo-Europikane_chhiba': 2, 'Kalo': 2,
    'Mashkarutne_Indo-Ariyane_chhiba': 2, 'Portugaliya': 2,
    'Romane_manusha': 2, 'Spaniya': 2, 'Adriyan_Minune': 2,
    'Azis': 2, 'Cedomir_Yovanovic': 2, 'Deliya_Grigore': 2,
    'Django_Reinhardt': 2, 'Esma_Rejepova': 2, 'Fazliya': 2,
    'Grigorash_Diniku': 2, 'Haso_Menovin_Frohlish': 2,
    'Johann_Trollmann': 2, 'Katarina_Taikon': 2,
    'Liviya_Yaroka': 2, 'Nicolaye_Gyorge': 2, 'Raiko_Juric': 2,
    'Reyhan': 2, 'Romika_Puchanu': 2, 'Ronald_Lee': 2,
    'Rosa_Taikon': 2, 'Sandro': 2, 'Selahetin_Kruezi': 2,
    'Shaban_Bayramovic': 2, 'Shtefan_Bǎnikǎ': 2,
    'Shtefan_Răzvan': 2, 'Sofi_Marinova': 2,
    'Valery_Novoselsky': 2, 'Vali_Vizheliye': 2,
    'Vasile_Yonesko': 2, 'Viktoriya_Mohaci': 2,
    'Xoakin_Kortes': 2, 'Yanosh_Bogdan': 2, 'Yon_Voiku': 2,
    'Zhean_Konstantin': 2, 'Zvonko_Demirovic': 2,
    'Phuvipnaske_patrinimata': 2, 'Europa': 2, 'Bharat': 2,
    'Budeshti': 2, 'Chave': 2, 'Chhib': 2, 'Jermaniya': 2,
    'Norvejiya': 2, 'Pakistan': 2, 'Rekshan': 2,
    'Republika_Makedoniya': 2, 'Shuto_Orizari': 2,
    'Valshenengi_Romani_chhib': 2, 'Bulgariya': 2,
    'Chexiya': 2, 'Rumuniya': 2, 'Rusiya': 2, 'Ungariya': 2,
    'Romano_siklyaripen_la_Rumuniyatar': 2,
    'Romano_siklyaripen_la_Ungariyatar': 2,
    'Romano_siklyaripen_le_Slovaikostar': 2,
    'Sikingro%27Kher': 2, 'Italiya': 2, 'Manush': 2,
    'Nasho': 2, 'Transilvaniya': 2,
    'Standardizuyimi_Romani_qhib_(Selahetin_Kruezi)': 2,
    'Mesto_software': 2, 'Thanipen': 3, 'Bersh': 3,
    'Afrika': 3, 'Britanikane_dvipa': 3, 'Eurasiya': 3,
    'Khetanipen_la_Sudutne_Asiyako_vash_o_Perutno_Somkerdipen': 3,
    'Sahel': 3, 'Sudutni_Amerika': 3, 'Kham': 3, 'Zaro': 3,
    'Kham-Sestemi': 3, 'Pharnovon': 3, 'Budor': 3, 'Ketor': 3,
    'Kuror': 3, 'Manjor': 3, 'Rahor': 3, 'Shani': 3,
    'Shukor': 3, 'Dvip': 3,
    'Phandlo_Thagaripen_la_Bare_Britaniyako_thai_le_Nordutne_Irlandesko': 3,
    'Patrinipen_le_themengo': 3, 'Sel': 3, 'Shagede': 3,
    'Stato': 3, 'Córdoba,_Spaniya': 3, 'Sherutno_foro': 3,
    'Andorra': 3, 'Austriya': 3, 'Beljiya': 3,
    'Buxlyarimos_le_Europikane_Ekipnasko': 3, 'Danemarka': 3,
    'Dvipa_Faroe': 3, 'Elveciya': 3, 'Estoniya': 3,
    'Europikano_Ekipen': 3, 'Finland': 3, 'Latviya': 3,
    'Lituaniya': 3, 'Luksemburgo': 3, 'Malta': 3, 'Moldova': 3,
    'Olanda': 3, 'Paris': 3,
    'Patrinipen_le_themengo_palal_o_butvaripen_le_manushengo': 3,
    'Patrinipen_le_themengo_palal_o_gin_le_manushengo': 3,
    'Patrinipen_le_themengo_palal_o_indekso_le_manushutne_baryaripnasko': 3,
    'Patrinipen_le_themengo_thai_le_durutne_umalengo_palal_lengo_baripen': 3,
    'Polska': 3, 'Republika_Irland': 3, 'Shkiperiya': 3,
    'Slovaiko': 3, 'Turkiya': 3, 'Ukraina': 3, 'Vatican': 3,
    'Jermanikani_chib': 3, 'Rumunikano_lekhipen': 3,
    'Euroroma': 3, '1971': 3, 'Menix': 3, 'London': 3,
    'Bukureshti': 3, 'Berlin': 3, 'Kanada': 3, 'Arxentina': 3,
    'Otomano_Thagaripen': 3, 'Chalga': 3, 'Israel': 3,
    'Roma_Virtual_Network': 3, 'Aven_Amentza': 3,
    'Flamenko': 3, 'Madrid': 3,
    'Gandhi_(mashkarutni_shkola_ando_Pech)': 3, 'Pech': 3,
    'Patrinipen_le_dvipengo_palal_o_baripen': 3,
    'Staturya_thai_teritorurya_la_Indiyake': 3,
    'Patrinipen_le_thanimatengo_la_Rumuniyake_kai_beshen_but_roma': 3,
    'Zhudetso': 3, 'Derya': 3, 'Ketnepen': 3, 'Paxro': 3,
    'Skopiye': 3, 'Sofiya': 3, 'Praga': 3, 'Rusikani_chhib': 3,
    'Peshta': 3, 'Ungarikani_chib': 3,
    'Gandhiskri_shkola_(Zvolenostar)': 3, 'Romanipen': 3,
    'Kher': 3, 'Dimashko': 3, 'Shero': 3, 'Vasho': 3,
    'Irland_(dvip)': 4, 'Nordutno_Irland': 4, 'Boliviya': 4,
    'Brazil': 4, 'Chile': 4, 'Ekuador': 4, 'Kuba': 4,
    'Mêsire': 4, 'Nordutni_Koreya': 4, 'Paraguay': 4,
    'Peru': 4, 'Sudutni_Koreya': 4, 'Uruguay': 4,
    'Venezuela': 4, 'Yelenistan': 4, 'New_York_City': 4,
    'Phandle_Staturya_la_Amerikiyake': 4,
    'Patrinipen_le_sherutne_forurengo': 4,
    'Patrinipen_le_themengo_kai_o_sherutno_foro_nai_o_bareder_foro': 4,
    'Patrinipen_le_themengo_le_buteder_sherutne_forurenca': 4,
    'Brusel': 4, 'Tallinn': 4, 'Butvaripen_le_manushengo': 4,
    'Kolombiya': 4, 'Palestina': 4,
    'Indekso_le_manushutne_baryaripnasko': 4,
    'Washington,_D.C.': 4, 'Nad_Tatrou_sa_blýska': 4,
    'Kiev': 4, 'Daki_chib': 4, 'Latinikano_lekhipen': 4,
    'Rumunikani_chhib': 4, 'Gelem,_Gelem': 4,
    'Mashkarthemutno_Romano_Kongreso': 4,
    'Styago_le_romengo': 4, 'Buenos_Aires': 4, 'Kontinento': 4,
    'Mahatma_Gandhi': 4, 'Ekhipnasko_Teritoryo': 4,
    'Diskriminaciya': 4, 'Okeyanu': 4, 'Krimeya': 4,
    'Slavikane_chhiba': 4, 'Uralikane_chhiba': 4, 'Zvolen': 4,
    'Indo-Aryano': 4, 'Baro_Belfast': 5, 'Belfast': 5,
    'Santiago,_Chile': 5, 'Lima': 5, 'Thagaripen_Inka': 5,
    'Lisbon': 5, 'Brasília': 5, 'Ho_Chi_Minh_City': 5,
    'Mumbai': 5, 'China': 5, 'Valparaíso': 5, 'Bogotá': 5,
    'Romanikane_chhiba': 5, 'Kali_Deryav': 5,
    'Patrinipen_le_internetoske_umalurengo_(TLD)': 5,
    'Prinjardi_chhib': 5, 'Chhibavipnaski_familiya': 5,
    'Distrikturya_la_Indiyake': 6,
    'Patrinipen_le_distrikturengo_la_Indiyake': 6, 'Asia': 6,
    'Angluni_chhib': 6, 'Chhibavipnasko_azbalipen': 6,
    'Korkori_chhib': 6,
    'Patrinipen_le_chhibavipnaske_familiyengo': 6, 'Tehsil': 7
}
