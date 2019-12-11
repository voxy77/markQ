global doc
import post_xml
import json, xmltodict
from files import files_to_send, parse_files, get, error_log


class HAL_file:
    def __init__(self, num):
        print(num)


# gets the list of all files in the working directory to send into HAL
list_to_send = files_to_send()
# print(list_to_send)

# iterates through each file in turn and calls the 'parse' function, setting the global 'doc' variable
# which gives a JSON representation of the file we send into HAL, and then send each file to be uploaded
for num in list_to_send:
    doc = parse_files(num)
    f = HAL_file(num)
    post_xml.main(num)
    compare_data = (get('https://firstqtooltest.s3.eu-west-2.amazonaws.com/' + num).text)
    r_f = (get('https://firstqtooltest.s3.eu-west-2.amazonaws.com/file2.xml').url)
    # assert the content of the local file that was sent, and the file from the end-point
    assert json.dumps(doc) == json.dumps(xmltodict.parse(compare_data)), error_log(num, r_f)
    # print (json.dumps(doc))
    # print (json.dumps(xmltodict.parse(compare_data)))
