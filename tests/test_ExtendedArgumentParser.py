"""test module."""
from itertools import product
from unittest import mock

import pytest


@pytest.mark.parametrize("platform, file", product(['win32', 'linux'], [None, mock.Mock()]))
def test_program_info(platform, file):
    """test method."""
    with mock.patch('buku.sys') as m_sys:
        import buku
        file = mock.Mock()
        if file is None:
            buku.ExtendedArgumentParser.program_info()
        else:
            buku.ExtendedArgumentParser.program_info(file)
        if platform == 'win32' and file == m_sys.stdout:
            m_sys.stderr.write.assert_called_once(prog_info_text)
        else:
            file.write.assert_called_once(prog_info_text)


def test_prompt_help():
    """test method."""
    file = mock.Mock()
    import buku
    buku.ExtendedArgumentParser.prompt_help(file)
    file.write.assert_called_once()


def test_print_help():
    """test method."""
    file = mock.Mock()
    import buku
    obj = buku.ExtendedArgumentParser()
    obj.program_info = mock.Mock()
    obj.print_help(file)
    obj.program_info.assert_called_once_with(file)
