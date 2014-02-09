from datetime import timedelta


def match(marks, images, offset=0):
    matches = []
    for img, ts in images.items():
        ts += timedelta(seconds=offset)
        min_ts_difference = lambda a: abs(a['timestamp'] - ts)
        mark  = min(marks, key=min_ts_difference)
        mark['image'] = img
        matches.append(mark)
    return matches

if __name__ == '__main__':
    from exifparser import extract_dates
    from kmlparser import extract_marks
    images = extract_dates(['../G0010086.jpg'])
    marks = extract_marks(['../2013-07-25 19-54-04.tlog.kmz'])
    print match(marks, images, offset=400)
