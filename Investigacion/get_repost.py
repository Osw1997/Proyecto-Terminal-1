import requests
import re
import json
import csv
import time
#url = "lodatlas.lri.fr/lodatlas/rest/search?fields=geo%3Bname%2Ctitle%2Cnotes&isAnd=true";
def get_geourls():
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
    print(len(geo_lista))
    geo_lista = list(set(geo_lista))
    print(len(geo_lista))

    # Lista de urls
    geo_urls = [];
    total = 0
    for palabra in geo_lista:
        #url = "http://lodatlas.lri.fr/lodatlas/rest/search?fields=" + palabra + \
        #      "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true";
        url = "http://lodatlas.lri.fr/lodatlas/rest/search?format=RDF&format=RDF-XML&format=SPARQL&" \
              "fields=" + palabra + "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%" \
              "2Cresources.usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true&show=format"
        results = requests.get(url)
        get_info = results.json()
        str_json = json.dumps(get_info)
        urls = re.findall("[\"]htt[p|ps].*?[\"]", str_json)
        for geo_url in urls:
            geo_urls.append(geo_url)
        total += len(urls)
    # Se guarda en un archivo CSV
    archivo = open("LODAtlas_geourls_formato.csv", "w", newline = '')
    guardar = csv.writer(archivo)
    for url in geo_urls:
        guardar.writerow([url])
    # Cantidad de tripletas
    print(len(geo_urls))
    print(total)

get_geourls();
