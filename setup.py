from setuptools import setup, find_packages

setup(
    name='vgphrase',
    version='0.0.1',
    description='VG Phrase Cut Dataset',
    packages=find_packages(include=['utils', 'utils.*']),  # Include only the contact_graspnet module
    include_package_data=True,
    license='MIT License',
    long_description=open('README.md').read(),
)