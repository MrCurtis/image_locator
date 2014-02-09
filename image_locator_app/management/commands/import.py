from optparse import make_option
from os import makedirs, path
from shutil import copyfile

from django.core.management.base import BaseCommand, CommandError
from image_locator_app.models import DroneImage

from util.exifparser import extract_dates
from util.kmlparser import extract_marks
from util.imagematcher import match


class Command(BaseCommand):
    args = 'kml_track image [image ...]'
    help = 'Import a KML drone track and corresponding images'
    option_list = BaseCommand.option_list + (
        make_option('--offset', type=int, dest='offset', default=0,
                    help='Optional image time stamps offset relative to KML\
                    track in seconds'), )

    def handle(self, *args, **options):
        if len(args) < 2:
            raise CommandError('You need to provide at least one image!')
        marks = extract_marks([args[0]])
        images = extract_dates(args[1:])
        dst = path.join('media', 'drone_images')
        if not path.exists(dst):
            makedirs(dst)
        for m in match(marks, images, options['offset']):
            if not path.exists(m['image']):
                raise CommandError('Image "%s" does not exist!' % m['image'])
            head, tail = path.split(m['image'])
            copyfile(m['image'], path.join(dst, tail))
            DroneImage(image=path.join('drone_images', tail),
                       latitude=m['location']['latitude'],
                       longitude=m['location']['longitude'],
                       altitude=m['location']['altitude'],
                       heading=m['orientation']['heading'],
                       tilt=m['orientation']['tilt'],
                       roll=m['orientation']['roll']).save()
