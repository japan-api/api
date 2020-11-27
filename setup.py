from setuptools import setup

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except Exception as e:
        print(e)


setup(name='japan-api',
      version='1.0.0',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='japan api',
      description='Japan REST API with info about prefectures',
      long_description=readme(),
      url='github.com/japan-api/api',
      author='Ilya Revenko',
      author_email='ilya.revenko17@gmail.com',
      license='MIT',
      packages=['janap-api'],
      install_requires=['Flask', 'Flask-Limiter', 'requests', 'beatifulsoup4'],
      include_package_data=True,
      zip_safe=False)