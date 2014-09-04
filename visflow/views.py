from django.shortcuts import render
from django.contrib import messages
import csv

def visflowmap(request):
    cnty = []#{'lat': 30.7438773366999, 'lng': -87.7211256969, 'FIPS': 1001}
    
    csvfile = 'C:/_DATA/migration_census_2000/cnty/latlng.csv'
    f = open(csvfile)
    ra = csv.DictReader(f, dialect="excel")
    for record in ra:
        temp = {}
        temp['lng'] = float(record['lng'])
        temp['lat'] = float(record['lat'])
        temp['FIPS'] = record['FIPS']
        cnty.append(temp)
    flowtable = []
    return render(request, 'visflow/flowmap.html', {'cnty': cnty, 'flowtable': flowtable,
                                                    'messages': messages.get_messages(request)})
    
    
def visflowmaptest(request):
    return render(request, 'visflow/flowmap_test.html', {
                                                    'messages': messages.get_messages(request)})
    
def visflowmapwithoptions(request):
    ageoptions = [{'value':'allage', 'display': 'all age groups - Census2000'}, 
                                {'value':'above65', 'display': 'age above 65 - Census2000'},
                                {'value':'allage_1m_acs2006_2010', 'display': 'all age groups - ACS2006-2010'}, 
                                {'value':'above65_1m_acs2006_2010', 'display': 'age above 65 - ACS2006-2010'}]
    if request.POST:
        mapdataoption = request.POST['mapdataoption']
    else:
        mapdataoption = 'above65'
    return render(request, 'visflow/flowmap_options.html', {'mapdataoption': mapdataoption, 'ageoptions': ageoptions,
                                                    'messages': messages.get_messages(request)})