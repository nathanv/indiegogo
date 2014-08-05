import scraperwiki
import lxml.html
from threading import Thread
url = ['http://www.indiegogo.com/projects?filter_category=Art&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Comic&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Dance&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Design&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Fashion&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Film&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Gaming&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Music&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Photography&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Theatre&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Transmedia&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Video+%2F+Web&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Writing&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Animals&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Community&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Education&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Environment&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Health&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Politics&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Religion&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_nonprofit=nonprofit&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Food&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Small+Business&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Sports&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=','http://www.indiegogo.com/projects?filter_category=Technology&filter_country=CTRY_FR&filter_quick=popular_all&pg_num=']
for x in url:
    def indiegogo():
        for i in range(1,73):
            try:
                url = x+str(i)
                root = scraperwiki.scrape(url)
                content = lxml.html.etree.HTML(root)
                categorie = content.xpath('//div[contains(@class,"project-category")]')
                nom = content.xpath('//div[contains(@class,"project-details")]/a')
                #porteur_projet = content.xpath('//p[contains(@class,"creator")]/a')
                porteur_projet = content.xpath('//p[contains(@class,"creator")]/span/a')
                details = content.xpath('//p[contains(@class,"description")]')
                stats = content.xpath('//span[contains(@id,"project-stats-funding-pct")]')
                montant = content.xpath('//span[contains(@class,"currency currency-medium")]/span')
                lien = content.xpath('//div[contains(@class,"project-details")]/a[@href]')
                for karazana,projet,olona,deta,marika,vola,rohy in zip(categorie,nom,porteur_projet,details,stats,montant,lien):
            #print olona.text,asa.text,deta.text,marika.text,vola.text
                    data = {
                                'Categorie': karazana.text,
                                'Projet' : projet.text,
                                'Nom du porteur': olona.text,
                                'details': deta.text,
                                'statistique': marika.text,
                                'montant obtenu': vola.text,
                                'lien':  "http://www.indiegogo.com"+rohy.attrib.get('href')
                            }
                    scraperwiki.sqlite.save(unique_keys=['Projet'], data=data)
            except:
                print "None"
    t = Thread(target=indiegogo)
    t.start()
