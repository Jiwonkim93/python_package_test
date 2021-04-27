from setuptools import setup

setup(
    name='uipath_api_lib',
    version='0.0.1',
    description='uipath orchestrator pip install test pack',
    url='https://github.com/Jiwonkim93/python_package_test.git',
    author='jiwonKim93',
    author_email='akaddak@gmail.com',
    license='jiwon',
    packages=['uipath_api_lib'],
    zip_safe=False,
    install_requires=[
        'requests==2.23.0',
        'urllib3==1.25.8',
        'pandas==1.0.1'
    ]
)