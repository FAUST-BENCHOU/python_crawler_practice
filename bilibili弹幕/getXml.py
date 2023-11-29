import requests
import re

# Get the HTML content of the Bilibili video page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
res = requests.get("https://www.bilibili.com/bangumi/play/ep63860",headers=headers)

# Extract the first "cid" from the HTML content using regular expressions
cid_matches = re.findall(r'"cid":(.*?),', res.text)
if cid_matches:
    # Use the first cid found
    first_cid = cid_matches[0]
    print("First cid:", first_cid)

    # Construct the comment XML URL
    comment_url = f'https://comment.bilibili.com/{first_cid}.xml'

    # Get the comment XML content
    res_comment = requests.get(comment_url)

    # Save the comment XML content to a file
    with open(f'{first_cid}.xml', 'wb') as f:
        f.write(res_comment.content)
else:
    print("No cid found.")
