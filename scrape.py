#!/bin/bash
#declare -a arr=("scholar" "yahoo" "duckduckgo" "google" "bing")
#-o- OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
#The name of the output file. If the file ending is
#"json", write a json file, if the ending is "csv",
#write a csv file.
#--shell               Fire up a shell with a loaded sqlalchemy session.
#-n NUM_RESULTS_PER_PAGE, --num-results-per-page NUM_RESULTS_PER_PAGE
#The number of results per page. Must be smaller than
#100, by default 50 for raw mode and 10 for selenium
#mode. Some search engines ignore this setting.
#-p NUM_PAGES_FOR_KEYWORD, --num-pages-for-keyword NUM_PAGES_FOR_KEYWORD
#The number of pages to request for each keyword. Each
#page is requested by a unique connection and if
#                        possible by a unique IP (at least in "http" mode).
## now loop through the above array
#declare -a arr=("google" "yandex" "bing" "yahoo" "baidu" "duckduckgo" "ask")
#declare -a arr2=("GMO" "Vaccine" "Play+Dough" "Genetically+Modified+Organism" "Livestrong" "Neutron" "Neuromorphic hardware")
#python run.py --keyword "Vaccine" --search-engines="$i"
#python run.py --keyword "Play Dough" --search-engines="$i"
#python run.py --keyword "Genetically_Modified" --search-engines="$i"
#python run.py --keyword "Genetically_Modified" --search-engines="$i"
#python run.py --keyword "Livestrong" --search-engines="$i" -o

from utils import search_params
SEARCHLIST, WEB, LINKSTOGET = search_params()

import utils
from numpy import random
flat_iter = [ (b,category) for category in SEARCHLIST for b in range(0,3) ]
random.shuffle(flat_iter)
import time
random.shuffle(flat_iter)
random.shuffle(flat_iter)
import utils
import os
se = {0:"google",1:"yahoo",2:"duckduckgo",3:"ask"}

def scraplandtext(fi):
    #se, _ = utils.engine_dict_list()

    b,category = fi
    print(b,category)
    os.system('python run.py --keyword '+'"'+str(category)+'"'+' --search-engines='+str(se[b])+' -p=10 --output-filename '+'"'+str(category)+str(se[b])+'.csv+'+'"')
    if b ==2 :
       time.sleep(random.uniform(10.0,20.0))
    return 0
_= list(map(scraplandtext,flat_iter))
