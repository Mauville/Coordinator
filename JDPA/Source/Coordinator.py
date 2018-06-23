#JDPA
import csv
import time
import re
import sys
import os
import win_unicode_console
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pathlib import Path


win_unicode_console.enable() #Enable tilde and non ASCII characters


def diditexist(oseedpath):
    oseedpath = os.path.expanduser(oseedpath)
    if not os.path.exists(oseedpath):
        os.makedirs(oseedpath)
        return False
    else:
        return True


def screenshooter(WorkingIndex, browser, imagefolder):
    WorkingIndex = str(WorkingIndex)
    pather = imagefolder + "/#" + WorkingIndex + ".png"
    browser.maximize_window()
    browser.find_element_by_class_name("widget-pane-toggle-button-container").click()
    time.sleep(3)
    browser.save_screenshot(pather)


def indexexception(error, Index, query, outputfolder):
    Exception = open(outputfolder + "exceptions.txt", "a")
    Exception.write("\n" + "#" + str(Index) + "\n" + query + "Error: " + error + "\n")
    Exception.close()
    print("Exception Indexed!\n"
          "Entry skipped.\n"
          "Error: " + error)


def parser(SAUCE, WorkingIndex, Index, outputfolder, Dialect):
    # parses coordinates
    coordinatefile = outputfolder + "coordinates.csv"
    if "/place" in SAUCE:
        # Verifies SAUCE is a place and gets coords
        coordinate1 = re.findall("[\d.]{2,10}\d(?=,-)", SAUCE)[0]
        coordinate2 = re.findall("[-][\d.]+", SAUCE)[0]
        coordinate1 += "N"
        coordinate2 += "O"

        # writes successful coordinates to file
        csvoutput = open(coordinatefile, "a", newline="")
        csvwriter = csv.writer(csvoutput, Dialect)
        csvwriter.writerow((data[WorkingIndex][0], coordinate1, coordinate2))
        csvoutput.close()

    else:
        # Leaves row blank
        csvoutput = open(coordinatefile, "a", newline="")
        csvwriter = csv.writer(csvoutput, Dialect)
        csvwriter.writerow((Index, "", "", ""))
        csvoutput.close()
        mistake = True

        return mistake


def saucer(query, WorkingIndex, Index, Wait, outputfolder, imagefolder, businessname):
    URL = "https://www.google.com.mx/maps/search/" + query
    gcwd = os.getcwd() + "\geckodriver.exe"
    lcwd = os.getcwd() + "\geckodriver.log"
    driver = webdriver.Firefox(executable_path=gcwd, log_path=lcwd)
    driver.get(URL)
    print("===============================\n"
          "Indexing entry #" + data[WorkingIndex][0] + ". " + str(WorkingIndex + 1) + " out of "
          + str(LastIndex + 1) + ".\n")
    noscreenshot = False
    time.sleep(Wait)

    try:
        driver.find_element_by_class_name("section-bad-query-title")  # NR
        print("Magic Results!")
        URL = "https://www.google.com.mx/maps/search/" + query
        URL = re.sub(businessname, "", URL)
        driver.quit()
        driver = webdriver.Firefox(executable_path=gcwd, log_path=lcwd)
        driver.get(URL)
        time.sleep(Wait)
        try:
            driver.find_element_by_class_name("section-bad-query-title")
            indexexception("No Results", Index, query, outputfolder)
            noscreenshot = True
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        pass

    try:
        element = driver.find_element_by_xpath(
            "id('pane')/div/div[2]/div/div/div[3]/div/div[2]/span/span[2]")
        intelement = int(element.text)  # Using Xpath it lookes for the amount of results
        #Since the path is absolute, it breaks easily
        if intelement >= 10:  # If TMR it adds number to the query
            indexexception("Too many results", Index, query, outputfolder)
            noscreenshot = True
        else:  # TR
            elem = driver.find_element_by_class_name("section-result")
            elem.send_keys(Keys.RETURN)
            time.sleep(3) #TODO instead of waiting for time, wait for an element
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("id('loading-pane-div')/div[2]")#Again, since its absolute path, it breaks easily
        # for timeouts on weird results (Farmacon J ortiz de Dominguez 2063 L2 y 3 Sinaloa)
        indexexception("Timeout", Index, query, outputfolder)
        noscreenshot = True
    except NoSuchElementException:
        pass




    if noscreenshot is False:
        screenshooter(Index, driver, imagefolder)

    SAUCE = driver.current_url
    SAUCE = re.sub("\/data[\s\S]{2,}", "", SAUCE)
    driver.quit()
    return SAUCE


diditexist("~\\Documents\\Coordinator")
diditexist("~\\Documents\\Coordinator\\Output")
diditexist("~\\Documents\\Coordinator\\Output\\Images")

if not diditexist("~\\Documents\\Coordinator\\Input"):
    print("Se han creado directorios en la carpeta Documentos. Ingresa los archivos necesarios en la carpeta Input.\n"
          "Para mas información, consulta el manual.")
    time.sleep(7)
    sys.exit()

InputFolder = os.path.expanduser("~\\Documents\\Coordinator\\Input\\")
ImageFolder = os.path.expanduser("~\\Documents\\Coordinator\\Output\\Images")
OutputFolder = os.path.expanduser("~\\Documents\\Coordinator\\Output\\")

command = input("==========================================================="
                "\nBienvenido a Coordinator 5.2.\n Comandos: Empezar  Ayuda\n"
                "===========================================================\n")

if command.lower() == "ayuda":
    drive = os.getcwd() + "\README.txt"
    os.startfile(drive)
    sys.exit()

# Check to see if exceptions.txt is a file and asks for confirmation
pather = OutputFolder + "exceptions.txt"
exceptions = Path(pather)
# asks for last index on the csv file

if exceptions.is_file():
    continuar = input(
        "Si ejecutas de nuevo Coordinator, los datos de exceptions.txt, coordinates.csv y todas las imagenes se sobreescribiran. ¿Continuar? Y/N\n")
    yes = ('yes', 'y', 'Y', 'si')
    no = ('no', 'n', "N")
    if continuar in no:
        sys.exit()
LastIndex = int(input("Por favor ingresa el ultimo numero de fila existente en el archivo .csv\n"))
LastIndex -= 1

# initializes exceptions.txt
exceptions = open(OutputFolder + "exceptions.txt", "w")
exceptions.write('=========================================================\n'
                 'Sucursales no encontradas. Al final se encuentra el total\n'
                 '=========================================================\n')
exceptions.close()

# Initializes coordinates.csv
csvoutput = open(OutputFolder + "coordinates.csv", "w", newline="")
csvoutput.close()

# loads csv file
csvinput = open(InputFolder + "data.csv", "r")
dialect = csv.Sniffer().sniff(csvinput.read(1024), delimiters=";,")
csvinput.seek(0)
csvreader = csv.reader(csvinput,dialect)
data = list(csvreader)
WorkingIndex = 0
mistakenumber = 0
connection = str(input("Tu conexion a Internet es Excelente (0) Buena (1) Regular (2) Mala (3)\n"))
# determines time to wait before doing anything on the page
wait = 5
if connection == "0":
    wait = 3
elif connection == "1":
    wait = 5
elif connection == "2":
    wait = 10
elif connection == "3":
    wait = 15

while WorkingIndex <= LastIndex:

    Index = str(data[WorkingIndex][0])
    BusinessName = str(data[WorkingIndex][1]) + " "
    Branch = str(data[WorkingIndex][2]) + " "
    Address = str(data[WorkingIndex][3]) + " "
    Number = str(data[WorkingIndex][2]) + " "
    State = str(data[WorkingIndex][5]) + " "

    query = BusinessName + Branch + Address + State

    SAUCE = saucer(query, WorkingIndex, Index, wait, OutputFolder, ImageFolder, BusinessName)
    mistake = parser(SAUCE, WorkingIndex, Index, OutputFolder, dialect)

    if mistake:
        mistakenumber += 1

    print("Done! \n"
          "===============================")
    WorkingIndex += 1

exceptions = open(OutputFolder + "exceptions.txt", "a")
exceptions.write("=========================================================\n"
                 "=========================================================\n"
                 "Errores: " + str(mistakenumber) + "\n"
                 "=========================================================")
exceptions.close()
csvinput.close()
print("\nFinished!")
input("Press enter to continue!")
final = os.path.expanduser("~\\Documents\\Coordinator\\Output\\")
os.startfile(final)
sys.exit()