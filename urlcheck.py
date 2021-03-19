import urllib.parse as urlparse
from urllib.parse import parse_qs
url = 'https://www.recreation.gov/api/permits/234624/divisions/378/availability?start_date=2020-05-28T06:00:00.000Z&end_date=2020-12-31T00:00:00.000Z&commercial_acct=false&is_lottery=false'
parsed = urlparse.urlparse(url)
print(parse_qs(parsed.query)['start_date'])
import urllib
import urllib.parse


url  = "https://www.recreation.gov/api/permits/"
#url = "http://stackoverflow.com/search?q=question"
params = {'lang':'en','tag':'python'}
# http://stackoverflow.com/search?tag=python&q=question&lang=en
#params = {'234624','tag':'python'}

url_parts = list(urllib.parse.urlparse(url))
query = dict(urllib.parse.parse_qsl(url_parts[4]))
query.update(params)

url_parts[4] = urllib.parse.urlencode(query)

print(urllib.parse.urlunparse(url_parts))


url1 = "https://www.recreation.gov/api/permits/"
url2 = "234624/divisions/378/availability?start_date=2020-05-28T06:00:00.000Z&end_date=2020-12-31T00:00:00.000Z"
print(urlparse.urljoin(url1, url2))
