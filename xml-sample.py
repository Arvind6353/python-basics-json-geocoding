import xml.etree.ElementTree as ET 

data = ''' 
<person>
    <name> Arvind </name>
    <age type='int'>2</age>
    <address> sjs jwjs sjwjs </address>
</person>
'''

parsedData = ET.fromstring(data)

# getting data from xml element
print(parsedData.find('name').text)

#getting attributes of xml element
print(parsedData.find('age').get('type'))

