import os
from glob import glob
from setuptools import setup

package_name = 'smart_template'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),        
        ('share/' + package_name + '/files', glob('files/*')),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pedro Moreira (BWH), Mariana Bernardes (BWH)',
    maintainer_email='plopesdafrotamoreira@bwh.harvard.edu, mcostabernardesmatias@bwh.harvard.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'template = smart_template.template:main',
            'virtual_template = smart_template.virtual_template:main',
            'keypress = smart_template.keypress:main',
        ],
    },
)
