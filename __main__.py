import sys
from Application import Application
from MainWindows import MainWindows

app = Application(sys.argv)

main_windows = MainWindows()
main_windows.showMaximized()

result = app.exec()
sys.exit(result)
