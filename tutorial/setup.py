from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_packae_data=True,
    zip_sage=False,
    install_require=[
        'flask',
    ],
)