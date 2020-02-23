import requests

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
                'geognostic', 'geodynamic', 'geocentric', 'geocentric', 'geobotanic', 'geobotanic']
geo_lista = list(set(geo_lista))

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'Cache-Control': 'max-age=0'
}

archivo = open("LODAtlas_geourls_.csv", "w", newline = '')
archivo.write('Palabra,Category,url_name,count,selected\n')

for palabra in geo_lista:
    url = "http://lodatlas.lri.fr/lodatlas/rest/search?format=RDF&format=RDF-XML&format=SPARQL&fields=" + palabra + \
          "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties" \
          "%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true&show=format"
    resp = requests.get(url, headers=headers, data=payload).json()
    # print(resp['facetList']['groups'])
    for category in resp['facetList']['groups']:
        if category['category'] in ['vocabs', 'props', 'classes']:
            try:
                print(category['category'])
                for list in category['list']:
                    print(list)
                    archivo.write(palabra + ',' + str(category['category']) + ',' + str(list['name']) + ',' +
                                  str(list['count']) + ',' + str(list['selected']) + '\n')
            except Exception as e:
                print(e)
archivo.close()
