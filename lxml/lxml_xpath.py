from lxml import html, etree
import requests

page_html = requests.get("http://localhost:8080/planets.html").text

tree = html.fromstring(page_html)

#Buscando elementos
#print([tr for tr in tree.xpath("/html/body/div/table/tr")])

#Buscando e decodificando elementos com etree
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr")])

#Buscando e filtrando com atributo [@class]
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr[@class='planet']")])

#Buscando e filtrando com atributo [@class], nesse caso buscando os diferentes
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[@id='planets']/table/tr[@id!='planetHeader']")])

#Buscando e filtrando por índice de vetor <div>, em XPath o primeiro índice é 1
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[1]/table/tr")])

#Buscando e filtrando com base em posição, por exemplo em caso de não haver atributo
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[@id='planets']/table/tr[position() > 4]")])

#Buscando e filtrando usando parent::*
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/parent::table")])

#Buscando e filtrando usando ..
#print([etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/..")])

#Buscando a massa de um planeta
#print(tree.xpath("/html/body/div[1]/table/tr[@name='Earth']/td[3]/text()[1]")[0].strip())
      