import os, time
from time import gmtime, strftime
from selenium import webdriver
from unidecode import unidecode


def get_announce_page(url, pagenumber):

    driver.get(url)

    list = driver.find_elements_by_xpath("//article")

    i = 0
    annonce = ''

    for l in list:

        print i

        try:
            annonce_id = l.get_attribute('data-listing-id')
        except:
            annonce_id = 'NULL'

        try:
            annonce_publication_id = l.get_attribute('data-publication-id')
        except:
            annonce_publication_id = 'NULL'

        try:
            annonce_title = l.find_element_by_xpath('.//h2/a').get_attribute('title')
        except:
            annonce_title = 'NULL'

        try:
            annonce_url = l.find_element_by_xpath('.//h2/a').get_attribute('href')
        except:
            annonce_url = 'NULL'

        try:
            annonce_price = l.find_element_by_xpath(".//*[@class='amount']").text
        except:
            annonce_price = 'NULL'

        try:
            annonce_description = l.find_element_by_xpath(".//*[@class='description']").text
        except:
            annonce_description = 'NULL'
        try:
            annonce_main_charac_1 = l.find_elements_by_xpath(".//*[@class='property_list']/li")[0].text
        except:
            annonce_main_charac_1 = 'NULL'
        try:
            annonce_main_charac_2 = l.find_elements_by_xpath(".//*[@class='property_list']/li")[1].text
        except:
            annonce_main_charac_2 = 'NULL'
        try:
            annonce_main_charac_3 = l.find_elements_by_xpath(".//*[@class='property_list']/li")[2].text
        except:
            annonce_main_charac_3 = 'NULL'
        try:
            annonce_agence_name = l.find_element_by_xpath(".//*[@class='agency_name']").get_attribute("data-tooltip")
        except:
            annonce_agence_name = 'NULL'
        try:
            annonce_agence_url = l.find_element_by_xpath(".//*[contains(@class,'agency_website')]/a").get_attribute(
                "href")
        except:
            annonce_agence_url = 'NULL'

        try:
            annonce_picture_1 = l.find_elements_by_xpath(".//*[@class='slidesjs-control']//img")[0].get_attribute('src')
        except:
            annonce_picture_1 = 'NULL'

        try:
            annonce_picture_2 = l.find_elements_by_xpath(".//*[@class='slidesjs-control']//img")[1].get_attribute('src')
        except:
            annonce_picture_2 = 'NULL'

        try:
            annonce_picture_3 = l.find_elements_by_xpath(".//*[@class='slidesjs-control']//img")[2].get_attribute('src')
        except:
            annonce_picture_3 = 'NULL'

        try:
            annonce_picture_4 = l.find_elements_by_xpath(".//*[@class='slidesjs-control']//img")[3].get_attribute('src')
        except:
            annonce_picture_4 = 'NULL'

        try:
            annonce_picture_5 = l.find_elements_by_xpath(".//*[@class='slidesjs-control']//img")[4].get_attribute('src')
        except:
            annonce_picture_5 = 'NULL'

        if annonce_id is not None :
            annonce_tmp = 'SELOGER' + \
                          '\t' + gmt_tmstp + \
                          '\t' + str(i) + \
                          '\t' + str(pagenumber) + \
                          '\t' + annonce_id + \
                          '\t' + annonce_publication_id + \
                          '\t' + annonce_title + \
                          '\t' + annonce_url + \
                          '\t' + annonce_price + \
                          '\t' + annonce_main_charac_1 + \
                          '\t' + annonce_main_charac_2 + \
                          '\t' + annonce_main_charac_3 + \
                          '\t' + annonce_agence_url + \
                          '\t' + annonce_picture_1 + \
                          '\t' + annonce_picture_2 + \
                          '\t' + annonce_picture_3 + \
                          '\t' + annonce_picture_4 + \
                          '\t' + annonce_picture_5 + '\n'

            try:
               details = get_annonce_details(annonce_url)
            except:
               print 'invalid url'

            print details

            annonce = annonce + annonce_tmp

            print annonce_tmp

        i += 1

    try:
        driver.find_element_by_xpath("//*[@class='pagination_next active']")
        more = 'more'
    except:
        more= 'no more'

    return [annonce, more]

def get_annonce_details(url):
    #chromedriver = "/usr/local/share/chromedriver"
    #os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    try:
        title = driver.find_element_by_xpath(".//*[@class='detail-title']").text
    except:
        title = 'NULL'

    transaction_type = title.split(' ')[0]
    house_type = title.split(' ')[1]
    pieces = title.split(' ')[2]
    superficie = title.split(' ')[4][:-2]
    ville = title.split(' ')[5]

    try:
        price = driver.find_element_by_xpath(".//*[contains(@class,'resume__prix')]").text.replace(' ','')[:-1]
    except:
        price= 'NULL'

    try:
        description = driver.find_element_by_xpath(".//*[@class='description']").text.replace('\t',' ').replace('\n',' ')
    except:
        description = 'NULL'

    try:
        descri_list_web = driver.find_elements_by_xpath(".//*[@class='description-liste']/li")
    except:
        descri_list_web = []

    descri_list=[]

    descri_superficie = ''
    descri_etages = ''
    descri_etages = ''
    descri_pieces= ''
    descri_chambres = ''
    descri_sdbs = ''
    descri_toilette = ''
    descri_ascensseur = ''
    descri_chauffage = ''
    descri_cuisine =''
    descri_construction = ''
    descri_cave = ''
    descri_balcon = ''
    descri_box = ''
    descri_parking = ''
    descri_sejour_superficie = ''
    descri_dpe = ''
    descri_ges = ''



    for i in descri_list_web:

        descri_list.append(unidecode(i.text))

        if 'Surface' in i.text:
            descri_superficie = str([int(s) for s in i.text.split() if s.isdigit()]).replace('[','').replace(']','')
        elif 'Etage' in i.text:
            descri_etage = i.text.replace(' ','').replace('Etage','')
        elif 'Etages' in i.text:
            descri_etages = i.text.replace(' ', '').replace('Etages', '')
        elif 'Piece' in unidecode(i.text):
            descri_pieces = unidecode(i.text).replace(' ', '').replace('Pieces', '').replace('Piece', '')
        elif 'Chambre' in i.text:
            descri_chambres = i.text.replace(' ', '').replace('Chambres', '').replace('Chambre', '')
        elif 'Salle de bains' in i.text:
            descri_sdbs = i.text.replace(' ', '').replace('Salledebains', '')
        elif 'Toilette' in i.text:
            descri_toilette = i.text.replace(' ', '').replace('Toilettes', '').replace('Toilette', '')
        elif 'Ascenseur' in i.text:
            descri_ascensseur = i.text
        elif 'Chauffage' in i.text:
            descri_chauffage = i.text
        elif 'Cuisine' in i.text:
            descri_cuisine = i.text
        elif 'Annee de construction' in unidecode(i.text):
            descri_construction = str([int(s) for s in i.text.split() if s.isdigit()]).replace('[', '').replace(']', '')
        elif 'Cave' in i.text:
            descri_cave = i.text
        elif 'Balcon' in i.text:
            descri_balcon = i.text.replace(' ', '').replace('Balcons', '').replace('Balcon', '')
        elif 'Box' in i.text:
            descri_box = i.text.replace(' ', '').replace('Boxs', '').replace('Box', '')
        elif 'Parking' in i.text:
            descri_parking = i.text.replace(' ', '').replace('Parkings', '').replace('Parking', '')
        elif 'Salle de sejour' in unidecode(i.text):
            descri_sejour_superficie = str([int(s) for s in i.text.split() if s.isdigit()]).replace('[', '').replace(']', '')
        elif 'DPE' in i.text:
            descri_dpe = str([int(s) for s in i.text.split() if s.isdigit()]).replace('[','').replace(']','')
        elif 'GES' in i.text:
            descri_ges = str([int(s) for s in i.text.split() if s.isdigit()]).replace('[', '').replace(']', '')

    descri_elements = [descri_superficie, descri_etages, descri_etages, descri_pieces, descri_chambres, descri_sdbs,
                       descri_toilette, descri_ascensseur, descri_chauffage, descri_cuisine, descri_construction,
                       descri_cave, descri_balcon, descri_box, descri_parking, descri_sejour_superficie, descri_dpe,
                       descri_ges]

    #Images
    #Price Evolution
    #Polygone

    driver.quit()

    return([title, transaction_type, house_type, pieces, superficie, ville, price, description, descri_list, descri_elements])




domain = 'http://www.seloger.com/'
ci = '640122' # Biarritz
idtt = '2' # Ventes Appartement, Maisons
idtypebien='1,2,9'


chromedriver = "/usr/local/share/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


gmt_tmstp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

all_annonces = ''


url_init = domain + '/list.htm?' + 'ci=' + ci + '&idtt=' + idtt + '&idtypebien=' + idtypebien

more = 'more'
pagenumber = 1

while more == 'more' :

    if pagenumber == 1:
        url = url_init
    else:
        url = url_init +  '&LISTING-LISTpg=' + str(pagenumber)

    page = get_announce_page(url, pagenumber)

    all_annonces_tmp = page[0]
    more = page[1]
    print all_annonces_tmp

    all_annonces = all_annonces + all_annonces_tmp

    pagenumber += 1

with open('logs_'+'SELOGER_'+ gmt_tmstp + '.txt','w') as file:
    file.write(all_annonces.encode('utf-8'))

driver.quit()

# url =  'http://www.seloger.com/annonces/achat/appartement/pau-64/101953099.htm'
#
# annonce_details = get_annonce_details(url)
#
# for i in annonce_details:
#     print i