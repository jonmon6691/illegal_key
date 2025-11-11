#!/usr/env python3


from urllib.request import urlopen, Request
import json


def get_illegal_number():
    url = "https://www.wikidata.org/wiki/Special:EntityData/Q12761277.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:144.0) Gecko/20100101 Firefox/144.0'}
    with urlopen(Request(url, headers=headers)) as resp:
        raw_data = json.load(
            resp)["entities"]["Q12761277"]["aliases"]["en"][0]["value"].replace(" ", "")
        return int(raw_data, 16)


if __name__ == "__main__":
    key = get_illegal_number()
    ocatal_bitting = f"{key:o}"
    print(f"// Paste this bitting into generate_key.scad")
    print(f"bitting = [{', '.join(ocatal_bitting)}];")
