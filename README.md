cordova-icon-splash-generator
=============

Creating all of the icons and splash screens for cordova/phonegap projects is
a pain, but it doesn't have to be.

This project makes it easy to create one icon and one splash then generate all
of the different assets needed for generating a cordova project that supports
all the various devices.

## Prerequisites:
Requires python and imagemagick. You can install python and imagemagick with
most package managers.

On Mac:
`brew install imagemagick`

## Usage:
`python generate.py -h`

~~~
Usage: generate.py [options]

Options:
  -h, --help            show this help message and exit
  -v                    log all the things
  --icon=ICON           relative path to your icon image
  --splash=SPLASH       relative path to your splash image
  --destination=DESTINATION
                        relative path where you want the output created
~~~

## Configuration
All configuration is set in config.py with fairly straightforward settings.
Essentially each platform section includes a list of file formats and sizes to
apply.

### Icon Sizes
Icon sizes can be specified as 1-tuples (width and height) or 2-tuples
(width/height, dpi_level).

### Splash Sizes
Similarly, splash sizes can be specified as 1-tuples (both width and height), 2-tuples
(width, height), or 3-tuples (width, height, dpi_level).

### Converting Image Types
If your settings are converting images to a format that doesn't support
transparency (like jpg splash screens for winphone), you can specify a
`background` key with a color name which imagemagick will use to fill in the
transparency.

## Cordova/Phonegap config.xml
Here is the icon and splash section of the matching config.xml file for the
default configuration.

~~~
    <icon gap:platform="android" gap:qualifier="ldpi" src="www/res/icon/android/icon-36-ldpi.png" />
    <icon gap:platform="android" gap:qualifier="mdpi" src="www/res/icon/android/icon-48-mdpi.png" />
    <icon gap:platform="android" gap:qualifier="hdpi" src="www/res/icon/android/icon-72-hdpi.png" />
    <icon gap:platform="android" gap:qualifier="xhdpi" src="www/res/icon/android/icon-96-xhdpi.png" />
    <icon gap:platform="blackberry" src="www/res/icon/blackberry/icon-80.png" />
    <icon gap:platform="blackberry" gap:state="hover" src="www/res/icon/blackberry/icon-80.png" />
    <icon gap:platform="ios" height="57" src="www/res/icon/ios/icon-57.png" width="57" />
    <icon gap:platform="ios" height="72" src="www/res/icon/ios/icon-72.png" width="72" />
    <icon gap:platform="ios" height="114" src="www/res/icon/ios/icon-57-2x.png" width="114" />
    <icon gap:platform="ios" height="144" src="www/res/icon/ios/icon-72-2x.png" width="144" />
    <icon gap:platform="webos" src="www/res/icon/webos/icon-64.png" />
    <icon gap:platform="winphone" src="www/res/icon/windows-phone/icon-48.png" />
    <icon gap:platform="winphone" gap:role="background" src="www/res/icon/windows-phone/icon-173-tile.png" />
    <gap:splash gap:platform="android" gap:qualifier="port-ldpi" src="www/res/screen/android/screen-ldpi-portrait.png" />
    <gap:splash gap:platform="android" gap:qualifier="port-mdpi" src="www/res/screen/android/screen-mdpi-portrait.png" />
    <gap:splash gap:platform="android" gap:qualifier="port-hdpi" src="www/res/screen/android/screen-hdpi-portrait.png" />
    <gap:splash gap:platform="android" gap:qualifier="port-xhdpi" src="www/res/screen/android/screen-xhdpi-portrait.png" />
    <gap:splash gap:platform="blackberry" src="www/res/screen/blackberry/screen-225.png" />
    <gap:splash gap:platform="ios" height="480" src="www/res/screen/ios/screen-iphone-portrait.png" width="320" />
    <gap:splash gap:platform="ios" height="960" src="www/res/screen/ios/screen-iphone-portrait-2x.png" width="640" />
    <gap:splash gap:platform="ios" height="1136" src="www/res/screen/ios/screen-iphone-portrait-568h-2x.png" width="640" />
    <gap:splash gap:platform="ios" height="1024" src="www/res/screen/ios/screen-ipad-portrait.png" width="768" />
    <gap:splash gap:platform="ios" height="768" src="www/res/screen/ios/screen-ipad-landscape.png" width="1024" />
    <gap:splash gap:platform="winphone" src="www/res/screen/windows-phone/screen-portrait.jpg" />

~~~
