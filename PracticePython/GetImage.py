import urllib.request
import re
import inspect
import chardet


def get_current_function_name():
    return inspect.stack()[1][3]


def getUrl(url):
    if (url == ""):
        print("url should be inputed " + get_current_function_name())
        return
        pass
    header = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0'
    }
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0'
    )
    response = urllib.request.urlopen(req).read()
    page = response.decode("utf-8")
    rex = re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>')
    urllist = re.findall(rex, page)
    return urllist


def downImage(urList, imgPath):
    for url in urList:
        urllib.request.urlretrieve(url,
                                   '%s/%s.jpg' % (imgPath, url[-8:-5]))  #下载图片
        pass


if __name__ == "__main__":
    url = 'http://tieba.baidu.com/p/2166231880?see_lz=1'
    path = "./image"
    url_list = getUrl(url)
    downImage(url_list, path)
