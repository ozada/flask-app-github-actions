from setuptools import find_packages
from setuptools import setup

setup(
    name='flask_app',
    description="Flask app for test CI",
    author='ozada',
    url='',
    packages=find_packages('src'),
    package_dir={
        '': 'src'},
    include_package_data=True,
    keywords=[
        'web_app', 'test', 'flask'
    ],
    entry_points={
        'console_scripts': [
            'web_server = app:main']},
)
