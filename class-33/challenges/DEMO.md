# Ops Challenge - Signature-based Malware Detection Part 3 of 3

## Resources

- [Video - Python: VirusTotal Lookup Script](Python: Virus Total Lookup Script)
- [Virustotal Search GitHub Repo](https://github.com/eduardxyz/virustotal-search)

## Staging

- Copy and paste the demo script below into a new Python file on your system.
- Download [virustotal-search.py](https://github.com/eduardxyz/virustotal-search) and place it in the same folder as the demo Python script.
- Sign up for an account at virustotal.com to get a free API key.
- To query the VirusTotal API, you'll need to set your API key as an environment variable to avoid hard-coding it into your demo Python script, which is currently set to call "API_KEY_VIRUSTOTAL" in place of your literal API key. You can always hard-code it at first for testing, but don't leave it that way!
- Set the variable `hash` to whatever MD5 hash you wish to VirusTotal to evaluate.

## Demo Code

```python
# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os

apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

os.system(query)
```
