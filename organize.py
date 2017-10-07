import os
import shutil
import csv

def organizeFolderGAPED(original, pos, neg, neut):
  # Copies each image in the GAPED database to the corresponding folder
  # Make a dictionary of file names to valence
  dict = {}
  files = os.listdir(original)
  for file in files:
      if '.txt' in file and 'SD' not in file and 'readme' not in file:
          print(file)
          with open(os.path.join(original, file), 'r') as f:
              for l in f:
                  l = l.split()
                  dict[l[0][:-4]] = l[1]

  # Walk through the images and categorize files as pos/neg/neut according to valence
  for roots, dirs, files, in os.walk(original):
      for file in files:
          if '.bmp' in file:
              if float(dict[file[:-4]]) < 40:
                  shutil.copy(os.path.join(roots, file), neg)
              elif float(dict[file[:-4]]) > 60:
                  shutil.copy(os.path.join(roots, file), pos)
              else:
                  shutil.copy(os.path.join(roots, file), neut)

def organizeFolderOASIS(original, pos, neg, neut):
  # Copies each image in the GAPED database to the corresponding folder
  # Make a dictionary of file names to valence
  dict = {}
  with open(os.path.join(original, 'OASIS.csv'), 'r') as file:
      reader = csv.reader(file)
      for row in reader:
          dict[row[1].strip()] = row[4]

  # Walk through the images and categorize files as pos/neg/neut according to normalized valence
  for roots, dirs, files, in os.walk(original):
      for file in files:
          if '.jpg' in file:
              if (float(dict[file[:-4]])-1)*100/6 < 40:
                  shutil.copy(os.path.join(roots, file), neg)
              elif (float(dict[file[:-4]])-1)*100/6 > 60:
                  shutil.copy(os.path.join(roots, file), pos)
              else:
                  shutil.copy(os.path.join(roots, file), neut)

if __name__ == '__main__' :
  project_path = os.getcwd()
  gaped = os.path.join(project_path, 'GAPED/GAPED')
  oasis = os.path.join(project_path,'oasis')
  pos = os.path.join(project_path, 'Positive')
  neg = os.path.join(project_path, 'Negative')
  neut = os.path.join(project_path, 'Neutral')
  organizeFolderOASIS(oasis, pos, neg, neut)
  organizeFolderGAPED(gaped, pos, neg, neut)
