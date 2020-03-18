from django.shortcuts import render
import pyshorteners
#inheiting the Shorteners class from pyshorteners
class shorteners(pyshorteners.Shortener):
    
    def chilpit_shortener(self,url):
        '''tries to short the URL and returns
        if fails than it returns that it cannot 
        further short the URL'''
        try:
            return self.chilpit.short(url)
        except:
            return "This Cannot be further shortened"
    def clckru_shortener(self,url):
        try:
            return self.clckru.short(url)
        except:
            return "This URL cannot be further shortened"
    def dagd_shortener(self,url):
        try:
            return self.dagd.short(url)
        except:
            return "This URL cannot be further shortened"
    
    def gitio_shortener(self,url):
        try:
            return self.gitio.short(url)
        except:
            return "This URL cannot be further shortened"
    def isgd_shortener(self,url):
        try:
            return self.isgd.short(url)
        except:
            return "This URL cannot be further shortened"
    def osdb_shortener(self,url):
        try:
            return self.osdb.short(url)
        except:
            return "This URL cannot be further shortened"
    def owly_shortener(self,url):
        try:
            return self.owly.short(url)
        except:
            return "This URL cannot be further shortened"
    def qpsru_shortener(self,url):
        try:
            return self.qpsru.short(url)
        except:
            return "This URL cannot be further shortened"
    def tinyUrl_shortener(self,url):
        try:
            return self.tinyurl.short(url)                    
        except:
            return "This URL cannot be further shortened"


def generate_url(server_name,url):
    '''generates short URL accorind to the shorteners passed as a
    argument'''
    url_shortener = shorteners()            #instance of shorteners class
    if server_name == "chilpit":
        return url_shortener.chilpit_shortener(url)
    elif server_name == "clckru":    
        return url_shortener.clckru_shortener(url)
    else:
        if server_name == "dagd":
            return url_shortener.dagd_shortener(url)
        if server_name == "gitio":
            return url_shortener.gitio_shortener(url)
        if server_name == "isgd":
            return url_shortener.isgd_shortener(url)
        if server_name == "osdb":
            return url_shortener.osdb_shortener(url)
       
        if server_name == "qpsru":
            return url_shortener.qpsru_shortener(url)
        elif server_name == 'tinyUrl':
            return url_shortener.tinyUrl_shortener(url)
   
    

def index(request):
    '''Handling the request that has been passed'''
    if request.method == "POST":
        server_name = request.POST["shorteners"]    #fetching shortener name
        url = request.POST["url"]                       #fetching long URL given by user
        data = {'short_url':generate_url(server_name,url),'long_url':url} #dict containing short and long URL
        return render(request,"index.html",data)
    else:
        return render(request,"index.html",{})    