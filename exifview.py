#! /usr/bin/env python3

from exif import Image
import sys

with open(sys.argv[1], 'rb') as image_file:
    my_image = Image(image_file)
    if my_image.has_exif:
        print(my_image['software'])
        # print(my_image['exif_version'])
        print("lens: {}".format(my_image['lens_specification']))
        print("focal length: {} - 35mm equiv: {}".format(my_image['focal_length'], my_image['focal_length_in_35mm_film']))
        print("exposure: {}, f/stop: {}".format(my_image['exposure_time'], my_image['f_number']))
        # print(my_image['make'], " - ", my_image['maker_note'])
        # print("GPS: {} lat, {} long".format(my_image['gps_latitude_ref'], my_image['gps_longitude_ref']))
        print("X resolution: {}, Y resolution: {}".format(my_image['x_resolution'], my_image['y_resolution']))

        for i in my_image:
            print(i)
