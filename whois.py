import os

def get_who_is(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process)
    return results


print(get_who_is('google.com'))
