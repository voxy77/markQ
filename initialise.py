global doc
import post_xml
import json, xmltodict, requests
from files import files_to_send, error_log

# setup a class that can be used to create individual file objects. ---Is this the best way? Is it needed???---
class HAL_file():
    def __init__(self):
        pass

    def parse_files(self, insert_file):  # this function will return the file in dict format that can be asserted.

        # parse a copy of the file that we sent to the endpoint
        with open(insert_file) as fd:
            doc = xmltodict.parse(fd.read())
            return doc

    def get(self, fn):  # the function to retrieve the contents of the file from an end-point
        to_compare = requests.get(fn)
        return to_compare


# call the files_to_send fucntion in order to get the list of all files in the working directory
list_to_send = files_to_send()

# iterates through each file in turn and calls the 'parse' function, setting the global 'doc' variable
# which gives a JSON representation of the file we send into HAL, and then send each file to be uploaded
for num in list_to_send:
    current_file = HAL_file()  # set current file as object of class 'HAL_file'
    doc = current_file.parse_files(num)  # sets the doc variable to contain the parsed file content from the
    # pre-uploaded file using the class parse_file method

    post_xml.main(num)  # calls the function to post the file to the endpoint

    compare_data = (current_file.get('https://firstqtooltest.s3.eu-west-2.amazonaws.com/' + num).text) # sets the
    # content of the uploaded file
    uploaded_file_url = (current_file.get('https://firstqtooltest.s3.eu-west-2.amazonaws.com/file2.xml').url) # sets
    # the url of the uploaded file

    # assert the content of the local file that was sent, and the file from the end-point
    assert json.dumps(doc) == json.dumps(xmltodict.parse(compare_data)), error_log(num, uploaded_file_url)

