from datetime import datetime
from zipfile import ZipFile

from lxml import etree


def extract_marks(filenames):
    ns = '{http://www.opengis.net/kml/2.2}'
    m = ns + 'Model/'
    stripns = lambda tag: tag[len(ns):]
    to_dict = lambda tree: dict((stripns(e.tag), e.text) for e in tree)
    ts = lambda s: datetime.strptime(s[:-6], "%Y-%m-%dT%H:%M:%S")
    data = []
    for filename in filenames:
        def zopen(filename):
            if filename.endswith('kmz'):
                z = ZipFile(filename)
                return z.open(z.namelist()[0])
            return open(filename)
        with zopen(filename) as f:
            f.readline()
            doc = etree.parse(f)
            for p in doc.iter(ns + 'Placemark'):
                try:
                    data.append({
                        'timestamp': ts(p.find(ns + 'TimeStamp')[0].text),
                        'location': to_dict(p.find(m + ns + 'Location')),
                        'orientation': to_dict(p.find(m + ns + 'Orientation'))
                    })
                except:
                    # Skip malformed nodes
                    pass
    return data

if __name__ == '__main__':
    print extract_marks(['../static/images/2013-07-25 19-54-04.tlog.kml'])
