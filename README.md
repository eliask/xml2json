# xml2json
Convert XML to JSON with Python 3 and defusedxml or plain ElementTree

# Usage
```
$ ./xml2json.py -h
usage: xml2json.py [-h] [--unsafe] [infile]

Convert an XML file to JSON.

positional arguments:
  infile

optional arguments:
  -h, --help  show this help message and exit
  --unsafe    do not use defusedxml: only for known-safe XML!
```

# Examples
```
# Normal usage for potentially unsafe XML files:
pip install defusedxml
./xml2json.py sample_input.xml > sample_output.json

# Without defusedxml
./xml2json.py --unsafe sample_input.xml > sample_output.json

# Also supports reading from stdin:
./xml2json.py < sample_input.xml > sample_output.json
```
