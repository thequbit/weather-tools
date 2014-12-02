import datetime
import urllib
import time

def leading_zeros(number):

    text_number = ''
    for i in range(0,5-len(str(number))):
        text_number += '0'
    text_number = text_number + str(number)
    return text_number

def download_map(url, output_file_name):

    print '[{0}] Downloading {1} ...'.format(datetime.datetime.now(), output_file_name)

    urllib.urlretrieve(url, filename=output_file_name)

    print '[{0}] Done.'.format(datetime.datetime.now())

def run(url):

    try:
        file_number = 0
        while(1):

            output_file_name = 'map-{0}.png'.format(leading_zeros(file_number))
            download_map(url, output_file_name)

            time.sleep(60*5) # 5 mins

            file_number += 1

    except:
        pass

if __name__ == '__main__':

    print "[{0}] Starting ...".format(datetime.datetime.now())

    url = "http://forecast.weather.gov/wwamap/png/US.png"

    run(url)

