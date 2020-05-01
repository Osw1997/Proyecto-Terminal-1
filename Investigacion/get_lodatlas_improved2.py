import requests
import time

geo_lista = ['geo','geoda','geoide','geoponia','geonomia','geologia','geogonia','geogenia','geofagia','geodesta',
                 'geodesia','geotermal','geotecnia','geoscopia','georgiano','georgiana','geoponico','geoponica',
                 'geonomico','geomorfia','geometria','geometral','geomancia','geomancia','geologico','geologica',
                 'geologias','geogonico','geogenico','geografic','geografia','geognosta','geognosia','geofisico',
                 'geofisica','geodesico','geodesica','geodesias','geoografos','geotermico','geotermica','geotecnico',
                 'geotecnica','georgianos','georgianas','geoquimico','geoquimica','geometrico','geometrica',
                 'geomantico','geometrias','geologicos','geologicas','geografico','geografica','geografias',
                 'geofisicos','geofisicas','geodesicos','geodesicas','geotermicos','geotermicas','geotropismo',
                 'geostrofico','geopolitico','geopolitica','geometricos','geometricas','geograficos','geograficas',
                 'geognostico','geodinamica','geocentrico','geocentrica','geobotanico','geobotanica',
                'geo', 'geode', 'geoid', 'geoponia', 'geonomia', 'geologia', 'geogonia', 'geogenia', 'geophagy', 'geodesta',
                'geodesy', 'geothermal', 'geotechnics', 'geoscopy', 'georgian', 'georgian', 'geoponic', 'geoponica',
                'geonomic', 'geomorphy', 'geometry', 'geometral', 'geomancy', 'geomancy', 'geological', 'geological',
                'geologies', 'geogonic', 'geogenic', 'geografic', 'geography', 'geognosta', 'geognosia', 'geophysical',
                'geophysics', 'geodesic', 'geodesic', 'geodesies', 'geographers', 'geothermal', 'geothermal', 'geotechnical',
                'geotechnical', 'Georgian', 'Georgian', 'geochemical', 'geochemical', 'geometric', 'geometric',
                'geomantico', 'geometrias', 'geologicos', 'geologicas', 'geografico', 'geografica', 'geografias',
                'geophysics', 'geophysics', 'geodesics', 'geodesics', 'geothermal', 'geothermal', 'geotropism',
                'geostrophic', 'geopolitical', 'geopolitical', 'geometric', 'geometric', 'geographical', 'geographical',
                'geognostic', 'geodynamic', 'geocentric', 'geocentric', 'geobotanic', 'geobotanic',
                'geoespacial', 'geospatial', 'geodato', 'geodata']
geo_lista = list(set(geo_lista))
print('Palabras distintas: ' + str(len(geo_lista)))

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
  'Content-Type': 'application/json; charset=utf-8',
  'Referer': 'http://lodatlas.lri.fr/',
  'Accept-Language': 'es-US,es;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6'
}


headers_se = {
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
  'Content-Type': 'application/json; charset=utf-8',
  'Referer': 'http://lodatlas.lri.fr/',
  'Accept-Language': 'es-US,es;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6'
}


archivo = open("LODAtlas_geourls_wSparqlEndpoint.csv", "w", newline='\n')
archivo.write('Palabra@Nombre repositorio@Nombre dataset@Titulo@Triple count@Conteo outgoing links@Conteo incoming link\n')


total = 0
for palabra in geo_lista:
    # url = "http://lodatlas.lri.fr/lodatlas/rest/search?format=RDF&format=RDF-XML&format=SPARQL&fields=" + palabra + \
    #       "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties" \
    #       "%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true&show=format "

    url = "http://lodatlas.lri.fr/lodatlas/rest/search?format=SPARQL&format=api%2Fsparql&format=SPARQL%20web%20form" \
          "&fields=" + palabra + "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources" \
          ".usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true&show=format "


    # url = "http://lodatlas.lri.fr/lodatlas/rest/search?format=RDF&format=RDF-XML&format=SPARQL&fields=" + palabra + \
    #       "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties" \
    #       "%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true&show=format"
    # resp = requests.get(url, headers=headers, data=payload).json()

    print('---> Palabra: ' + palabra)
    # Se extrae la información
    resp = requests.get(url, headers=headers, data=payload).json()
    print('#Listas: ' + str(len(resp['hitList']['hits'])))
    # Si lo devuelto no tiene información, se le dará 5 oportunidades para devolver info.
    chances = 5
    while len(resp['hitList']['hits']) <= 0 and chances > 0:
        resp = requests.get(url, headers=headers, data=payload).json()
        chances -= 1
        time.sleep(0.5)

    # Una vez devuelta la información y no agotadas las oportunidades, se guarda
    if len(resp['hitList']['hits']):
        total += len(resp['hitList']['hits'])
        for list in resp['hitList']['hits']:
            # Se extrae la URI del SPARQL endpoint
            try:
                url_SE = 'http://lodatlas.lri.fr/lodatlas/rest/repos/datahub/datasets/' + list['name']
                request_SE = requests.get(url_SE, headers=headers_se, data=payload).json()
                print('Response: ')
                print(request_SE)
                # time.sleep(10)

            except Exception as e:
                print('Error SPARQL endpoint')
                print(e)
            try:
                # 'Palabra,Nombre repositorio,Nombre dataset,titulo,triple count,Conteo outgoing links,Conteo incoming link\n'
                archivo.write(palabra + '@' + list['rN'] + '@' + list['name'] + '@' + list['title'] + '@' +
                              str(list['tc']) + '@' + str(list['olC']) + '@' + str(list['ilC']) + '\n')
            except Exception as e:
                print('Error escritura')
                print(list)
                print(e)

print('Total registros: ' + str(total))
archivo.close()
