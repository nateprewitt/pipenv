import os

import pytest
import delegator

class TestPipenv():

    def test_install_in_another_venv(self):
        delegator.run('mkdir test_pipenv_in_venv')
        os.chdir('test_pipenv_in_venv')

        os.environ['PIPENV_VENV_IN_PROJECT'] = '1'

        assert delegator.run('python -m virtualenv env').return_code == 0
        
        c1 = delegator.run('env/bin/pip install pipenv')
        print('------------- INSTALL PIPENV --------------')
        print(c1.out)
        print(c1.err)
        assert c1.return_code == 0

        c = delegator.run('env/bin/pipenv install pyramid')
        print('------------- INSTALL PYRAMID -------------')
        print(c.out)
        print(c.err)
        assert c.return_code == 0

        os.chdir('..')
        delegator.run('rm -fr test_pipenv_in_venv')
