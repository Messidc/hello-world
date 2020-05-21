from urllib import request
from html.parser import HTMLParser
# from html.entiti
# es import name2codepoint

class MyHTMLParser(HTMLParser):
    yes=0
    recent=0
    def handle_starttag(self, tag, attrs):
        attrs1=dict(attrs)
        if tag=='h3' and 'class' in attrs1 and attrs1['class']=='event-title':
            self.yes=1
        if tag=='div' and 'class' in attrs1 and attrs1['class']=='most-recent-events':
            self.recent=1
        if tag=='h3' and 'class' in attrs1 and attrs1['class']=='widget-title just-missed':
            self.recent=0
                
        # print('<%s>' % tag)

    def handle_endtag(self, tag):
        pass
        # print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        pass
        # if yes==1
        # print('<%s/>' % tag)

    def handle_data(self, data):
        if self.yes==1 and self.recent==1:
            print(data)
            self.yes=0

    def handle_comment(self, data):
        pass
        

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass
        


if __name__ == "__main__":
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # print('Data:', data.decode('utf-8'))
        parser = MyHTMLParser()
        parser.feed(data.decode('utf-8'))

   


