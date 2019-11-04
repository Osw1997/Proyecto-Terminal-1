import requests

#url = "lodatlas.lri.fr/lodatlas/rest/search?fields=geo%3Bname%2Ctitle%2Cnotes&isAnd=true";
url = "http://lodatlas.lri.fr/lodatlas/rest/search?fields=geo%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies&isAnd=true";

#url = "lodatlas.lri.fr/lodatlas/rest/search?fields=";
#fields = "geo%3Bname%2Ctitle%2Cnotes%2Cresources.usedClasses%2Cresources.classLabels%2Cresources.usedProperties%2Cresources.propertyLabels%2Cresources.vocabularies";

results = requests.get(url);
get_info = results.json();
print(get_info['facetList']);
