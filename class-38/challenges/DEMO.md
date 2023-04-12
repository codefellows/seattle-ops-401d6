# Ops Challenge - XSS Vulnerability Detection with Python

## Demo Code

Copy the demo code below to Web Security Dojo. Complete all TODOs.

```python

#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: Add description 
# Date:        TODO: Add date
# Modified by: TODO: Add your name

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

```
