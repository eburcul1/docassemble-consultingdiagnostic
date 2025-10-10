import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.consultingdiagnostic',
      version='0.1.0',
      description=('Word doc contains token counts - for testing purposes only'),
      long_description='launch from main_interview.yml\r\nrequires an OpenAI key in config file for AI gen\r\nIntroduces assessment_intelligence_agent (uses AI to show category help) \r\nIntroduces new prioritization screen for pain points. Only top 3 are considered for ouput.\r\n0.0.5 corrected video playback on VPS\r\n0.0.6 correct selection of top 3 offerings\r\n0.0.7 update main_interview to enable response and recommended next actions in the Word output file\r\n0.0.8 slight modifications to enable tracking of token usage for help and for response creation\r\n0.0.9 favicon files included in static directory (unable to test this in Docker playground - need to deply to prduction to test. Note config file needs to be updates to enable favicon to work)\r\n0.1.0 correct defect on selection of top 3 offereings. Update Word template (formatting still needs work)',
      long_description_content_type='text/markdown',
      author='System Administrator',
      author_email='burcul_elvis@hotmail.com',
      license='',
      url='https://github.com/eburcul1/docassemble-consultingdiagnostic.git',
      packages=find_namespace_packages(),
      install_requires=['matplotlib>=3.10.6', 'openai>=1.86.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/consultingdiagnostic/', package='docassemble.consultingdiagnostic'),
     )
