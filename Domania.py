import requests
import time
import urllib3
import sys



def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True, help='Target Domain.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output to file.')
    return parser.parse_args()

def banner():
   print('                                                         ')
   print('                                                         ')
   print('                                                         ')
   print('██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ ')
   print('██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗')
   print('██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║███████║')
   print('██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║')
   print('██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║')
   print('╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝')
   print('                                                         ')
   print('                                                         ')
   print('                  Coded By :- Parshwa Bhavsar            ')
   print('                                                         ')
   print('                                                         ')
    


def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print('[*] Invalid domain, try again..')
        sys.exit(1)
    return host

def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        fp.close()


def main():
    banner()
    subdomains = []

    args = parse_args()
    target = parse_url(args.domain)
    output = args.output

    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

    if req.status_code != 200:
        print('[*] Information not available!')
        sys.exit(1)

    for (key,value) in enumerate(req.json()):
        subdomains.append(value['name_value'])

    print(f"\n[!] ****** TARGET: {target} ****** [!] \n")


    subs = sorted(set(subdomains))

    for s in subs:
        print(f'[*] {s}\n')
        if output is not None:
            write_subs_to_file(s, output)

    print("\n\n[**] Scan Completed.")


if __name__=='__main__':
    main()
