import sys

from pycryptor.gui.application import Application

if __name__ == '__main__':
    app = Application('PyCryptor')
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
