import json
from copy import deepcopy

DATA_PATH_PREFIX = 'data/'

def load_and_split(path, name_prefix, name_property):
    """
    Extract all feature objects from a geojson object at path.
    """
    fh = open(path)
    obj = json.loads(fh.read())
    fh.close()
    print 'About to operate on %d features' % len(obj['features'])
    print 'Figure out how to: spit out color-coded map for certain set of features'
    print 'Like: auto-generate county-by-county color-coded map for gov'
    print 'Or: precinct-level color-coded map for state rep races'
    for i in obj['features']:
        #print i['properties']
        #break
        name = '%s_%s.geojson' % (name_prefix, i['properties'][name_property].replace(' ', '_'))
        print 'Starting %s' % name
        newobj = deepcopy(obj)
        newobj['features'] = [deepcopy(i)]
        fh = open('%s%s' % (DATA_PATH_PREFIX, name), 'w')
        fh.write(json.dumps(newobj))
        fh.close()

if __name__ == '__main__':
    #state_reps = 'state_reps_09.geojson'
    #state_rep_property = 'SLDLST'
    #state_sens = 'state_sens_09.geojson'
    #state_sen_property = 'SLDUST'
    #cook_comms = 'cook_county_comm_10.geojson'
    #cook_comm_property = 'District_N'
    #cook_subcircuits = 'cook_subcircuits.geojson'
    #cook_subcircuit_property = 'DISTRICT'
    #counties = 'counties_09.geojson'
    #counties_property = 'NAME'
    #cong = 'pa_97-14_cong.geojson'
    #cong_property = 'District_N'
    #wards = 'wards_12.geojson'
    #wards_property = 'District_N'
    precincts = 'precincts.geojson'
    precinct_property = 'WARD_PRECI'
    load_and_split('%s%s' % (DATA_PATH_PREFIX, precincts), 'precincts/precinct', precinct_property)
