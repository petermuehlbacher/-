api_key   = "[your key goes here]"
levels    = "1,2,3,4,5,6,7,8,9,10,11"
threshold = 5

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

response = urlopen("https://www.wanikani.com/api/user/"+api_key+"/vocabulary/"+levels)
data = json.loads(str(response.read()))

filtered_data = []

for item in data['requested_information']:
    if item['user_specific']['reading_incorrect'] + item['user_specific']['meaning_incorrect'] > threshold:
        u = item['user_specific']
        filtered_data.append([item['character'],item['kana'],item['meaning'],
                             int(u['reading_incorrect']),int(u['reading_correct']),
                             int(u['meaning_incorrect']),int(u['meaning_correct']),
                             int(u['reading_incorrect']+u['meaning_incorrect'])])
sorted_data = sorted(filtered_data, key=lambda k: k[7], reverse=True)

for item in sorted_data:
    char, kana, meaning, ir, cr, im, cm, errors = item

    print("errors: "+str(errors)+", reading: "+str(cr)+"/"+str(cr+ir)+", meaning:"+str(cm)+"/"+str(cm+im)+", "+char+u'\uFF08'+kana+u'\uFF09' + " "+meaning)
