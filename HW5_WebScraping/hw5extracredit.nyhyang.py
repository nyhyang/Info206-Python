import urllib.request as req
import json
import oauth2
import pprint as pp
import operator

# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = 'iamXp_CQmayvluHFHUTgWQ'
CONSUMER_SECRET = 'EdZD8y2p71W8mN5JykjCNJP51aI'
TOKEN = 'pj6evHLYirjcLenP4HRuoVJc9d8kouJA'
TOKEN_SECRET = 'Y_JCcep2wjE16LM_EtHu7cEnzEs'

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API


def yelp_req(url, final_dic, offset):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    
    result = {}

    result['location'] = 'San Francisco'
    result['offset'] = offset
    result['sort'] = 2
    result['term']='restaurant'


    oauth_request = oauth2.Request('GET', url, parameters=result)
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = req.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read().decode("utf-8"))
    finally:
        conn.close()
    # print(response)
    # print(type(response))
    
    restaurant_biz = response['businesses']
    for i in range(len(restaurant_biz)):
        reviews = restaurant_biz[i]['review_count']
        restaurant_name = restaurant_biz[i]['name']

        final_dic[restaurant_name] = reviews
    # pp.pprint(restaurant_biz[0]['review_count'])
    # pp.pprint(restaurant_biz[0]['name'])
    # restaurant_biz[0])
    # print(final_dic)


    return final_dic

#################################################################################
# Your code goes here

def main():

    final_dic = {}
    url = 'http://api.yelp.com/v2/search'
    final_dic = yelp_req(url, final_dic, offset=0)
    final_dic = yelp_req(url,final_dic,offset=20)
    result = sorted(final_dic.items(), key=operator.itemgetter(1), reverse = True)
    print(result)

    with open('restaurants2.nyhyang.txt', 'w') as fout:
        for restaurant_name, reviews in result:
            fout.write(restaurant_name + ", " + str(reviews)+ "\n")


if __name__ == '__main__':
    main()


