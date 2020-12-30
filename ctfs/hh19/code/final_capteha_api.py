#!/usr/bin/env python3
# Fridosleigh.com CAPTEHA API - Made by Krampus Hollyfeld
import requests
import json
import sys
import base64
import os
import shutil
import glob

def main():
    yourREALemailAddress = "YourRealEmail@SomeRealEmailDomain.RealTLD"

    # Creating a session to handle cookies
    s = requests.Session()
    url = "https://fridosleigh.com/"

    json_resp = json.loads(s.get("{}api/capteha/request".format(url)).text)
    b64_images = json_resp['images']                    # A list of dictionaries eaching containing the keys 'base64' and 'uuid'
    challenge_image_type = json_resp['select_type'].split(',')     # The Image types the CAPTEHA Challenge is looking for.
    challenge_image_types = [challenge_image_type[0].strip(), challenge_image_type[1].strip(), challenge_image_type[2].replace(' and ','').strip()] # cleaning and formatting

	# begin custom...err junk code;
    hhimgs = ([img['base64'] for img in b64_images])
    hhuuids = ([img['uuid'] for img in b64_images])
    for index, (item1, item2) in enumerate(zip(hhimgs, hhuuids)):
        filename = '{}.txt'.format(item2)
        with open(filename, 'w') as f_out:
            f_out.write('{}\n'.format(item1))

    for index, (item1, item2) in enumerate(zip(hhimgs, hhuuids)):
        filename = '{}.txt'.format(item2)
        filename2 = '{}.png'.format(item2)
        with open(filename, 'rb') as fr_out:
            with open(filename2, 'wb') as fw_out:
                fw_out.write(base64.b64decode(fr_out.read()))

    source = '/home/bz/'
    dest = '/home/bz/unknown_images'

    files = glob.iglob(os.path.join(source, "*.png"))
    txtfiles = glob.iglob(os.path.join(source, "*.txt"))

    for file in files:
        shutil.move(file, dest)

    os.system('/home/bz/predict_images_using_trained_model.py')
    var = []
    for i in challenge_image_types:
        if i == "Stockings":
            j = os.listdir(i)
            x1 = ','.join([x.split('.')[0] for x in j])
            var.append(x1)
        elif i == "Presents":
            k = os.listdir(i)
            x2 = ','.join([x.split('.')[0] for x in k])
            var.append(x2)
        elif i == "Ornaments":
            l = os.listdir(i)
            x3 = ','.join([x.split('.')[0] for x in l])
            var.append(x3)
        elif i == "Christmas Trees":
            m = os.listdir(i)
            x4 = ','.join([x.split('.')[0] for x in m])
            var.append(x4)
        elif i == "Candy Canes":
            n = os.listdir(i)
            x5 = ','.join([x.split('.')[0] for x in n])
            var.append(x5)
        elif i == "Santa Hats":
            o = os.listdir(i)
            x6 = ','.join([x.split('.')[0] for x in o])
            var.append(x6)
        else:
            break

    for file in txtfiles:
        os.remove(file)

    final_answer = ','.join(var)
	
	# end the horrible code already;
	
    # This should be JUST a csv list image uuids ML predicted to match the challenge_image_type .
    # final_answer = ','.join( [ img['uuid'] for img in b64_images ] )
    json_resp = json.loads(s.post("{}api/capteha/submit".format(url), data={'answer':final_answer}).text)
    if not json_resp['request']:
        # If it fails just run again. ML might get one wrong occasionally
        print('FAILED MACHINE LEARNING GUESS')
        print('--------------------\nOur ML Guess:\n--------------------\n{}'.format(final_answer))
        print('--------------------\nServer Response:\n--------------------\n{}'.format(json_resp['data']))
        sys.exit(1)

    print('CAPTEHA Solved!')
    # If we get to here, we are successful and can submit a bunch of entries till we win
    userinfo = {
        'name':'Krampus Hollyfeld',
		# replace this with real email
        'email':'real.email.here',
        'age':180,
        'about':"Cause they're so flippin yummy!",
        'favorites':'thickmints'
    }
    # If we win the once-per minute drawing, it will tell us we were emailed.
    # Should be no more than 200 times before we win. If more, somethings wrong.
    entry_response = ''
    entry_count = 1
    while yourREALemailAddress not in entry_response and entry_count < 200:
        print('Submitting lots of entries until we win the contest! Entry #{}'.format(entry_count))
        entry_response = s.post("{}api/entry".format(url), data=userinfo).text
        entry_count += 1
    print(entry_response)


if __name__ == "__main__":
    main()