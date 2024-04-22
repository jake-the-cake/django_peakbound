from os import path
from flamingo.settings import BASE_DIR

pages = {
  'peakbound': '',
  'pbdeals': 'shop/'
}

def create_slug(string):
  return str(string).lower().split(' ')


def link_info(page='peakbound', title=None, url=None):
  if not url:
    url = '-'.join(create_slug(title))
  return {
    'title': title.upper(),
    'url': path.join(pages[page], url)
  }

footer = [
  link_info('peakbound', 'this page'),
  link_info('peakbound', 'that page')
]

def build_links(site='peakbound', data=[]):
  output = []
  for d in data:
    # if 
    print(d)
    output += d

  return output

footer = {
  # 'peakbound': [
  'peakbound': build_links(
    'peakbound',
    [
      ['home', '/'],
      'about'
    ]

  )
}
print(footer)