from datetime import datetime

from exifread import process_file


def extract_dates(filenames):
    data = {}
    for filename in filenames:
        with open(filename, 'rb') as f:
            exif_date = process_file(f, details=False)['EXIF DateTimeOriginal']
        data[filename] = datetime.strptime(str(exif_date), "%Y:%m:%d %H:%M:%S")
    return data
