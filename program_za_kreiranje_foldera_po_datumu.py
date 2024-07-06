from datetime import date
import os

today = date.today().strftime("%y-%m-%d")

path = os.path.abspath(__file__)
dirname = os.path.dirname(path)
folder = dirname + '\\sesion 20' + today
os.mkdir(folder)