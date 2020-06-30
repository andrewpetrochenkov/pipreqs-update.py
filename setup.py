import setuptools

setuptools.setup(
    name='pipreqs-update',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pipreqs-update']
)
