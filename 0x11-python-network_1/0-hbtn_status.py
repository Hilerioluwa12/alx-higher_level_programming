#!/usr/bin/python3
""" use urllib to get information from a web-site
"""
if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            ty = type(result)
            con = result
            con_u = result.decode('utf-8')
            print("Body response:")
            print("\t- type: {}".format(ty))
            print("\t- content:".format(con))
            print("\t- utf8 content: {}".format(con_u))
    except urllib.error.URLError as e:
        print(e.reason)
