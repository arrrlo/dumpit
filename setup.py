from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='dumpit',
    version='0.5.0',

    description='Print python objects like a boss',
    long_description=readme(),
    long_description_content_type='text/markdown',

    url='https://github.com/arrrlo/dumpit',
    licence='MIT',

    author='Ivan Arar',
    author_email='ivan.arar@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='print, object',

    packages=find_packages(),
    install_requires=[
        'click~=7.0',
        'termcolor~=1.1.0',
        'terminaltables==3.1.0',
    ],

    project_urls={
        'Source': 'https://github.com/arrrlo/dumpit',
    },
)
