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
```sh
# Normal usage for potentially unsafe XML files:
pip install defusedxml
./xml2json.py sample_input.xml > sample_output.json

# Without defusedxml
./xml2json.py --unsafe sample_input.xml > sample_output.json

# Also supports reading from stdin:
./xml2json.py < sample_input.xml > sample_output.json
```

# Conversion logic
Each element gets converted into an object of the form: `{ tagName : {@text: optional, @children: optional, ...attributes} }`
## Input
```xml
<rootelem foo="bar">
  some text
  <child1>
    <child2 attr1="baz" attr2="foo"/>
    <child2 attr2="baz" attr3="foo"/>
  </child1>
</rootelem>
```
## Output
```json
{
  "rootelem": {
    "foo": "bar",
    "@text": "some text",
    "@children": [
      {
        "child1": {
          "@children": [
            {
              "child2": {
                "attr1": "baz",
                "attr2": "foo"
              }
            },
            {
              "child2": {
                "attr2": "baz",
                "attr3": "foo"
              }
            }
          ]
        }
      }
    ]
  }
}
```
