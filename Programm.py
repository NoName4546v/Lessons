import os
import shutil

os.chdir('Files')
inside = os.listdir()
List = {"Text", "Audio", "Picture", "Code", "Archive", "Other"}
for i in inside:
    print(i)
def sort(inside): #Сортировка файлов в папке
    #Создание папок сортировки
    try:
        os.mkdir("Text")
        os.mkdir("Audio")
        os.mkdir("Picture")
        os.mkdir("Code")
        os.mkdir("Archive")
        os.mkdir("Other")
    except Exception:
        pass

    #Сортировка
    for i in inside:
        a = os.listdir()
        if ".txt" in i or ".docx" in i or ".pdf" in i:
            try:
                shutil.copy(i, 'Text')
                os.remove(i)
            except Exception:
                print("Ошибка")
                exit
        elif ".png" in i or ".jpg" in i or ".jpeg" in i or ".psd" in i or ".psb" in i:
            try:
                shutil.copy(i, 'Picture')
                os.remove(i)
            except Exception:
                print("Ошибка")
                exit
        elif ".mp3" in i or ".flac" in i:
            try:
                shutil.copy(i, 'Audio')
                os.remove(i)
            except Exception:
                print("Ошибка")
                exit
        elif ".py" in i or ".c" in i or ".cpp" in i or ".C" in i:
            try:
                shutil.copy(i, 'Code')
                os.remove(i)
            except Exception:
                print("Ошибка")
                exit
        elif ".zip" in i or ".7z" in i or ".rar" in i:
            try:
                shutil.copy(i, 'Archive')
                os.remove(i)
            except Exception:
                print("Ошибка")
                exit
        else:
            try:
                shutil.copy(i, 'Other')
                os.remove(i)
            except Exception:
                exit

    #2 этап сортировки(по буквам)
    inside = os.listdir()
    for i in inside:
        os.chdir(i)
        ins = os.listdir()

        for a in ins:
            ins2 = os.listdir()
            try:
                if a[0] not in ins2:
                    os.mkdir(a[0])
                    shutil.copy(a, a[0])
                    os.remove(a)
                elif a[0] in ins2:
                    shutil.copy(a, a[0])
                    os.remove(a)
            except IsADirectoryError:
                shutil.rmtree(a)
            except Exception:
                continue

#Извлечение файлов из папок
for i in inside:
    if "." not in i:
        print(f"Папка {i}")
        try:
            os.chdir(i)
            print(f"Перешел в {i}")
            s = os.listdir()
            for a in s:
                try:
                    shutil.copy(a, "C:\\Users\\Study\\Desktop\\Prog\\Files")
                    print("Скопировал файл")
                except IsADirectoryError:
                    shutil.copytree(a, "C:\\Users\\Study\\Desktop\\Prog\\Files")
                    print("Скопировал папку")
            os.chdir("..")
            print("Перешел обратно")
            shutil.rmtree(i)
            print("Удалил")
        except PermissionError:
            print("Permission denied.")
        """except Exception:
            print("pass", str(Exception))
            pass
"""