shopNavLinks = {}

class Links():
	def __init__(self):
		
		self.shopHome = self.useLinkInfo('/', 'Home', [['/x', 'test'], ['test']],'red')

	def useLinkInfo(self, url, label, sublinkArray = None, color = None):
		return clearEmptyKeys({
			'url': url,
			'label': label,
			'sublinks': self.useSublinks(sublinkArray),
			'color': color
		})
	
	def useSublinks(self, linkArray):
		if not type(linkArray) is list: return None
		obj = {}
		for link in linkArray:
			if len(link) < 2: break
			obj[link[1]] = self.useLinkInfo(link[0], link[1])
		return obj
	
def clearEmptyKeys(obj):
	empty_keys = [k for k,v in obj.items() if not v]
	for k in empty_keys:
		del obj[k]
	return obj