#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

# with open('README.md', "r") as readme_file:
#     readme = readme_file.read()
#
# with open('HISTORY.rst', "r") as history_file:
#     history = history_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read()

# setup_requirements = ['pytest-runner', 'vcversioner']

test_requirements = ['pytest>=3', ]

setup(
    author="Oded Shimon",
    author_email='audreyr@example.com',
    # vcversioner={'vcs_args': ['git', 'describe', '--tags', '--long']},
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="",
    install_requires=requirements,
    license="MIT license",
    # long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='hyperion_backend',
    name='hyperion_backend',
    packages=find_packages(include=['backend', 'hyperion_backend']),
    # setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/odedshimon/hyperion',
    zip_safe=False,
)