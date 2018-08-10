from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pyRedisMailGateway',
    version='0.0.1',
    license='MIT',
    url='https://github.com/sourceperl/pyRedisMailGateway',
    platforms='any',
    install_requires=required,
    scripts=[
        'scripts/mail_gw_receiver',
        'scripts/mail_gw_robot',
        'scripts/mail_gw_sender'
    ]
)
