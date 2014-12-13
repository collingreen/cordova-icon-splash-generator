"""
Creates all the various image sizes and file structure
for a cordova project.

`python generate.py`

"""

import os
import sys
import logging
import subprocess
import optparse

from config import PLATFORMS


class Converter(object):
    """
    Takes an icon image and splash image and generates a folder that includes
    all of the various filenames and resized images necessary for a
    multi-platform cordova build.

    Edit the platform configuration in config.py to adjust which files
    are created for each platform.

    TODO:
    - support more control over imagemagick settings
    - portrait vs landscape (include in naming schemes)
    - generate config.xml
    """

    def __init__(self, platform_config):
        self.platform_config = platform_config
        self.parse_command_line()
        self.verify_dependencies()
        logging.debug("initialized converter")

    def verify_dependencies(self):
        # http://stackoverflow.com/a/11270665
        try:
            from subprocess import DEVNULL # py3k
        except ImportError:
            DEVNULL = open(os.devnull, 'wb')

        # try to run convert command - if it fails, tell user and bail
        if subprocess.call(
                'convert -version',
                stdout=DEVNULL,
                stderr=DEVNULL,
                shell=True):
            logging.error("could not find ImageMagick " +
                    "`convert` method. Please install " +
                    "ImageMagick and/or add it to the path");
            sys.exit(1)

    def parse_command_line(self):

        parser = optparse.OptionParser()
        parser.add_option('-v',
                dest="verbose",
                action="store_true",
                default=False,
                help="log all the things"
            )
        parser.add_option('--icon',
                dest="icon",
                action="store",
                default="icon.png",
                help="relative path to your icon image"
            )
        parser.add_option('--splash',
                action="store",
                dest="splash",
                default="splash.png",
                help="relative path to your splash image"
            )
        parser.add_option('--destination',
                action="store",
                dest="destination",
                default=os.path.join('www','res'),
                help="relative path where you want the output created"
            )

        self.settings, args = parser.parse_args(sys.argv)

        # set logging verbosity from command line arguments
        level = logging.DEBUG if self.settings.verbose else logging.INFO
        logging.basicConfig(level=level)

    def generate(self):
        logging.info("Generating Icons and Splash Screens!")
        for platform, settings in self.platform_config.iteritems():
            self.generate_platform(platform, settings)

    def generate_platform(self, platform_name, settings):
        logging.info("processing %s" % platform_name)
        self.prep_platform(platform_name)
        if 'icon' in settings:
            self.generate_platform_icons(platform_name, settings['icon'])
        if 'splash' in settings:
            self.generate_platform_splashes(platform_name, settings['splash'])

    def prep_platform(self, platform_name):
        """Ensure folder is available for platform"""

        icon_path = self.get_icon_path(platform_name)
        logging.debug("- creating icon path %s if necessary" % icon_path)
        try: os.makedirs(icon_path)
        except OSError: pass

        splash_path = self.get_splash_path(platform_name)
        logging.debug("- creating splash path %s if necessary" % splash_path)
        try: os.makedirs(splash_path)
        except OSError: pass

    def get_icon_path(self, platform_name):
        return os.path.abspath(
                os.path.join(
                    self.settings.destination,
                    'icon',
                    platform_name
                )
            )

    def get_splash_path(self, platform_name):
        return os.path.join(
            self.settings.destination,
            'splash',
            platform_name
        )

    def generate_platform_icons(self, platform_name, icon_settings):
        logging.debug("- creating icons")
        for icon_type in icon_settings:
            for size_config in icon_type['sizes']:
                # parse size config into standard
                size, dpi_level = self._parse_icon_size_config(size_config)
                halfsize = int(size / 2)

                # create destination string from filename pattern
                filename = icon_type['filename'].format(
                    size=size,
                    halfsize=halfsize,
                    dpi_level=dpi_level
                )
                destination = os.path.join(
                    self.get_icon_path(platform_name),
                    filename
                )

                # if background is specified send it
                background = None
                if 'background' in icon_type:
                    background = icon_type['background']

                # resize icon and put it where it belongs
                self.resize(
                    self.settings.icon, destination, size, size, background
                )

    def _parse_icon_size_config(self, size_config):
        dpi_level = 'default'
        if type(size_config) == type(0):
            size = size_config
        elif len(size_config) > 1:
            size, dpi_level = size_config
        return size, dpi_level

    def generate_platform_splashes(self, platform_name, splash_settings):
        logging.debug("- creating splash screens")
        for splash_type in splash_settings:
            for size_config in splash_type['sizes']:
                # parse size config into standard
                width, height, dpi_level = self._parse_splash_size_config(size_config)
                halfwidth = int(width / 2)
                halfheight = int(height / 2)

                # create destination string from filename pattern
                filename = splash_type['filename'].format(
                    width=width,
                    height=height,
                    halfwidth=halfwidth,
                    halfheight=halfheight,
                    dpi_level=dpi_level
                )
                destination = os.path.join(
                    self.get_splash_path(platform_name),
                    filename
                )

                # if background is specified send it
                background = None
                if 'background' in splash_type:
                    background = splash_type['background']

                # resize spalsh and put it where it belongs
                self.resize(
                    self.settings.splash, destination, width, height, background
                )

    def _parse_splash_size_config(self, size_config):
        dpi_level = 'default'
        if type(size_config) == type(0):
            width = height = size_config
        else:
            if len(size_config) == 1:
                width = height = size_config[0]
            elif len(size_config) == 2:
                width, height = size_config
            elif len(size_config) == 3:
                width, height, dpi_level = size_config

        return width, height, dpi_level

    def resize(self, source, destination, width, height, background=None):
        logging.debug("- - Creating %s (%d, %d)" % (destination, width, height))

        # TODO: support other conversion types if desired (PIL?)
        self._resize_imagemagick(source, destination, width, height, background)

    def _resize_imagemagick(self, source, destination, width, height, background=None):
        # use imagemagick's convert method
        raw_command = 'convert -background {background} "{source}" -resize {bigger}x{bigger} -gravity center -extent {width}x{height} "{destination}"'
        command = raw_command.format(
            source=source,
            destination=destination,
            width=width,
            height=height,
            bigger=max(width, height),
            background=background or 'none'
        )

        logging.debug(command)
        subprocess.call(command, shell=True)

if __name__ == '__main__':
    converter = Converter(PLATFORMS)
    converter.generate()
