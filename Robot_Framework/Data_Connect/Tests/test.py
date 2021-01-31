# if resultsWithTimestamp == True: 
#   robot  --outputdir ResultsWithTimestamp/logfile_%date:~-4,4%%date:~-10,2%%date:~-7,2% --timestampoutputs Tests/Amazon.robot 
# else:
#    robot --outputdir Results Tests/Amazon.robot

# --resultsWithTimestamp True
# timestmp = createOutputDirectory(True)
# robot  --outputdir timestmp Tests/Amazon.robot

import os
import datetime
from pathlib import Path
import shutil
import zipfile


def logDateFormat():
    cdate = datetime.datetime.now()
    return cdate.strftime("%Y") + "-" + cdate.strftime("%m") + "-" + cdate.strftime("%d") + "_" + cdate.strftime(
        "%H") + "-" + cdate.strftime("%M") + "-" + cdate.strftime("%S")


def getNewlyCreatedFolderName():
    infilepath = ""
    # Get newly created folder name
    path = "C:/Demo/Robot/Data_Connect/Data_Connect/ResultsWithTimestamp"
    tfiles = sorted(Path(path).iterdir(), key=os.path.getmtime, reverse=True)
    for index, name in enumerate(tfiles):  # loop through all names
        zname = os.path.join(path, name)
        if index == 0:
            infilepath = zname
            print(infilepath)
            break
    return infilepath


def createOutputDirectory(resultsWithTimestampStatus):
    infilename = ""

    # Delete more than 10 zip files from ResultsZipFolder
    zip_root_path = Path(__file__).parent.parent
    path = os.path.join(zip_root_path, 'ResultsZipFolder')

    # Delete directories
    zip_dirfiles = sorted(Path(path).iterdir(), key=os.path.getmtime, reverse=True)
    for index, name in enumerate(zip_dirfiles):  # loop through all names
        dname = os.path.join(path, name)
        if os.path.dirname(dname):  # only the directory names
            if index > 8:
                if os.path.exists(dname):
                    os.remove(dname)

    if resultsWithTimestampStatus == True:

        # Create folder with timestamp
        os.mkdir("C:/Demo/Robot/Data_Connect/Data_Connect/ResultsWithTimestamp/logfile_{}".format(logDateFormat()))

        infilename = getNewlyCreatedFolderName()

        # Delete the folders older than 7 days old or Folder count greater than 20 from ResultsWithTimestamp directory
        dt = datetime.datetime.now()  # datetime now (system timestamp)
        delta = datetime.timedelta(10)  # seven days interval
        dt7 = dt - delta  # datetime seven days earlier than now

        root_path = Path(__file__).parent.parent
        path = os.path.join(root_path, 'ResultsWithTimestamp')  # the path to be checked
        # print(path)

        # Delete all files from ResultsWithTimestamp folder
        for name in os.listdir(path):
            fname = os.path.join(path, name)
            if os.path.isfile(fname):  # only the file names
                os.remove(fname)

        # Delete directories
        dirfiles = sorted(Path(path).iterdir(), key=os.path.getmtime,
                          reverse=True)  # sort the files in descending order of modification time
        for index, name in enumerate(dirfiles):  # loop through all names
            dname = os.path.join(path, name)
            if os.path.dirname(dname):  # only the directory names
                t = os.path.getmtime(dname)  # time of last modification in seconds
                dt = datetime.datetime.fromtimestamp(t)  # datetime representation
                # print("index date: ", (dt))
                if dt <= dt7 or index > 19:
                    # print('Deleting', repr(dname))
                    shutil.rmtree(dname)
    else:
        # Delete all files from Results folder
        res_root_path = Path(__file__).parent.parent
        res_filepath = os.path.join(res_root_path, 'Results')  # the path to be checked
        # print(res_filepath)
        for name in os.listdir(res_filepath):
            fname = os.path.join(res_filepath, name)
            if os.path.isfile(fname):  # only the file names
                os.remove(fname)
    # print(os.path.basename(infilename))
    return os.path.basename(infilename)


# print(createOutputDirectory(True))


def createResultsZip(resultsWithTimestampStatus):
    zipfilepath = ""
    infile = ""
    infilename = ""
    if resultsWithTimestampStatus == True:
        path = "C:/Demo/Robot/Data_Connect/Data_Connect/ResultsWithTimestamp"
        zipfiles = sorted(Path(path).iterdir(), key=os.path.getmtime,
                          reverse=True)  # sort the files in ascending order of modification time
        for index, name in enumerate(zipfiles):  # loop through all names
            zname = os.path.join(path, name)
            if index == 0:
                infile = os.path.basename(zname)
                # print(infile)
                break
        zipfilepath = "C:/Demo/Robot/Data_Connect/Data_Connect/ResultsZipFolder/Results_{}.zip".format(infile)
        infilename = "C:/Demo/Robot/Data_Connect/Data_Connect/ResultsWithTimestamp/{}".format(infile)
    else:
        zipfilepath = "C:/Demo/Robot/Data_Connect/Data_Connect/ResultsZipFolder/Results_{}.zip".format(logDateFormat())
        infilename = "C:/Demo/Robot/Data_Connect/Data_Connect/Results"

    zf = zipfile.ZipFile(zipfilepath, "w")
    for dirname, subdirs, files in os.walk(infilename):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, infilename))
    zf.close()


if __name__ == '__main__':
    createOutputDirectory(True)
    # createResultsZip(True)
