from distutils.core import setup
setup(
  name = 'TIR',
  packages = ['TIR'],
  version = '0.1',
  description = 'Telegram ID Recommender',
  long_description='''Telegram ID Recommender''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/TIR',
  download_url = 'https://github.com/sepandhaghighi/TIR/tarball/v0.1',
  keywords = ["Telegram","python","ID","Username","User","Recommender","Generator"],
  install_requires=[
      'art',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
