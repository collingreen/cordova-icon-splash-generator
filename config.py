
# edit this configuration to change how things are generated
PLATFORMS = {
    'android': {
        'icon': [
            {
                'filename': 'icon-{size}-{dpi_level}.png',
                'sizes': [
                    (36, 'ldpi'),
                    (48, 'mdpi'),
                    (72, 'hdpi'),
                    (96, 'xhdpi')
                ]
            }
        ],
        'splash': [
            {
                'filename': 'screen-{dpi_level}-portrait.png',
                'sizes': [
                    (320, 426, 'ldpi'),
                    # (320, 470, 'mdpi'),
                    # (480, 640, 'hdpi'),
                    # (720, 960, 'xhdpi'),
                    (320, 480, 'mdpi'),
                    (480, 800, 'hdpi'),
                    (720, 1280, 'xhdpi'),
                ]
            }
        ]
    },
    'ios': {
        'icon': [
            {
                'filename': 'icon-{size}.png',
                'sizes': [57, 72]
            },
            {
                'filename': 'icon-{halfsize}-2x.png',
                'sizes': [114, 144]
            }
        ],
        'splash': [
            {
                'filename': 'screen-iphone-portrait.png',
                'sizes': [ (320, 480) ]
            },
            {
                'filename': 'screen-iphone-portrait-2x.png',
                'sizes': [ (640, 960) ]
            },
            {
                'filename': 'screen-iphone-portrait-3x.png',
                'sizes': [ (1242, 2208) ]
            },
            {
                'filename': 'screen-iphone-portrait-568h-2x.png',
                'sizes': [ (640, 1136) ]
            },
            {
                'filename': 'screen-ipad-portrait.png',
                'sizes': [ (768, 1024) ]
            },
            {
                'filename': 'screen-ipad-landscape.png',
                'sizes': [ (1024, 768) ]
            }
        ]
    },
    'blackberry': {
        'icon': [
            {
                'filename': 'icon-{size}.png',
                'sizes': [80]
            }
        ],
        'splash': [
            {
                'filename': 'screen-{width}.png',
                'sizes': [ (225, 225) ]
            }
        ]
    },
    'webos': {
        'icon': [
            {
                'filename': 'icon-{size}.png',
                'sizes': [64]
            }
        ]
    },
    'winphone': {
        'icon': [
            {
                'filename': 'icon-{size}.png',
                'sizes': [48]
            },
            {
                'filename': 'icon-{size}-tile.png',
                'sizes': [173]
            }
        ],
        'splash': [
            {
                'filename': 'screen-portrait.jpg',
                # jpgs have no transparency so you may
                # need to specify a background color
                'background': 'white',
                'sizes': [ (480, 800) ]
            }
        ]
    },
}

