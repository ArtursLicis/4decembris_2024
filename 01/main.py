""" Insert Name """
name = input("Whats your name: ")        # Ļauj ierakstīt jeb kādu vārdu

""" Insert age. Also convert age into an Integer value """
age = int(input("How old are you: "))    # Ļauj ierakstīt vecumu un pārvēš to vecumu par int vērtību

""" Do the math """
year = str((2018 - age)+100)             # Izdara matemātiku, lai izreiķinātu tavu vecumu 100 gados. Un to pārvēš to pa srt vērtību

""" Print the result """                 
print(name + " will be 100 years old in the year " + year) # Izdrukā rezultātus 
