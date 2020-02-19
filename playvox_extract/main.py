from ExtractPII import ExtractPII
import pprint


def create_urls_test(subdomains):
    urls = []
    for subdomain in good_subdomains:
        urls.append(f"http://{subdomain}.playvox.com")
        urls.append(f"https://{subdomain}.playvox.com")
        urls.append(f"http://www.{subdomain}.playvox.com")
        urls.append(f"https://www.{subdomain}.playvox.com")
        urls.append(f"https://{subdomain}")
        urls.append(f"http://{subdomain}")
        urls.append(f"{subdomain}.playvox.com")
        urls.append(f"www.{subdomain}.playvox.com")
        urls.append(f"{subdomain}")
    return urls


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    text_test = """409-52-2002 409522002d  X4012888888881881 X409522002d x409-52-2002y , hoahaf,asdf fjdwqanvqr 3{{wgflñw}}
    vevw v fgr t54yh64  078-05-1120g5ty245 gffsdv  123-45-6789)  219-09-9999, feve 078-05-1120 378282246310005
    uferugf24384f 1cf ,xz,.VW. ,33R23| 409-52-2002 KKK 000-00-0000, 111-11-1111, 222-22-2222, 371449635398431
	grghtbh534 378734493671000  gh45bh54 f30569309025904,
	fergfqewr  38520000023237 , gtbgtr 6011111111111117,  3530111333300000 tbbt v 4012888888881881	 g
	gfewfvwrv3g XXXXXXXXX kayla= 609324948
    X409522002d hoahaf,asdf fjdwqanvqr 3{{wgflñw}}
    vevw v fgr t54yh64  078051120g5ty245 gffsdv  12345-6789)  219-09-999, feve 078051120 
	36042258651439
	5555555555554444,grev re 5105105105105100 vewdvwe ñ-ñp., 4111111111111111
    30569309025904
    409522002 6011111111111117"""

    """
    response = ExtractPII(text_test)
    print("*" * 60)
    print("ALL SSN WITH '-' \n")
    pp.pprint(response.extract_ssn())
    print("*" * 60)
    print("ALL SSN WITHOUT '-' \n")
    pp.pprint(response.extract_ssn(stripe=False))
    print("*" * 60)
    print("ALL CREDIT CARDS NUMBERS \n")
    pp.pprint(response.extract_credit_card_numbers())
    """
    response = ExtractPII()

    good_subdomains = [
        "cristian",
        "cristian123",
        "cristian-123",
        "cristian-n1",
        "cristian_123",
        "cristian_n1",
        "123cristian",
        "123-cristian",
        "n1-cristian-n1",
        "123_cristian",
        "n1_cristian",
        "cristian;",
    ]

    bad_subdomains = [
        "cristian.",
        "cristian;",
        "cristian,",
        "cristian+",
        "cristian?",
        "cristian n",
        "cristian}¿!",
        "crsitian@$%#",
    ]
    good_urls = create_urls_test(good_subdomains)

    bad_urls = create_urls_test(bad_subdomains)
    response = ExtractPII()
    # print(response.extract_playvox_subdomain("cristian..com"))
    # Check good domains

    for good_url in good_urls:
        subdomain = response.extract_playvox_subdomain(good_url)
        if subdomain not in good_subdomains:
            print(f"Error: {subdomain}")
    print("Good domains test succesful")

    # Check bad domains
    for bad_url in bad_urls:
        subdomain = response.extract_playvox_subdomain(bad_url)
        if subdomain in bad_subdomains:
            print(f"Error: {subdomain}")
    print("Bad domains test succesful")

