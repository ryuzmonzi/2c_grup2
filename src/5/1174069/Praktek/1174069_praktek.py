# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:38:25 2019

@author: FannyCantik
"""
import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()
