import requests
import re
import json
import csv

#url = "lodatlas.lri.fr/lodatlas/rest/search?fields=geo%3Bname%2Ctitle%2Cnotes&isAnd=true";
def get_geourls():
    geo_lista = ['geo','geoda','geoide','geoponia','geonomia','geologia','geogonia','geogenia','geofagia','geodesta','geodesia','geotermal','geotecnia','geoscopia','georgiano','georgiana','geoponico','geoponica','geonomico','geomorfia','geometria','geometral','geomancia','geomancia','geologico','geologica','geologias','geogonico','geogenico','geografic','geografia','geognosta','geognosia','geofisico','geofisica','geodesico','geodesica','geodesias','geoografos','geotermico','geotermica','geotecnico','geotecnica','georgianos','georgianas','geoquimico','geoquimica','geometrico','geometrica','geomantico','geometrias','geologicos','geologicas','geografico','geografica','geografias','geofisicos','geofisicas','geodesicos','geodesicas','geotermicos','geotermicas','geotropismo','geostrofico','geopolitico','geopolitica','geometricos','geometricas','geograficos','geograficas','geognostico','geodinamica','geocentrico','geocentrica','geobotanico','geobotanica'];
    # Lista de urls
    geo_urls = [];
    for palabra in geo_lista:
        url = "http://lodatlas.lri.fr/lodatlas/rest/search?fields=" + palabra + "%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true";
        results = requests.get(url)
        get_info = results.json()
        str_json = json.dumps(get_info)
        urls = re.findall("[\"]htt[p|ps].*?[\"]", str_json)
        for geo_url in urls:
            geo_urls.append(geo_url)
    # Se guarda en un archivo CSV
    archivo = open("LODAtlas_geourls.csv", "w", newline = '')
    guardar = csv.writer(archivo)
    for url in geo_urls:
        guardar.writerow([url])
    # Cantidad de tripletas
    print(len(geo_urls))

get_geourls();
