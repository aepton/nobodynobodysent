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
    for i in obj['features']:
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
    #cook_comms = 'cook_county_comm_10.geojson'
    #cook_comm_property = 'District_N'
    #cook_subcircuits = 'cook_subcircuits.geojson'
    #cook_subcircuit_property = 'DISTRICT'
    counties = 'counties_09.geojson'
    counties_property = 'NAME'
    load_and_split('%s%s' % (DATA_PATH_PREFIX, counties), 'counties', counties_property)
