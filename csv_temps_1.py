import matplotlib.pyplot as plt #'C:\Program' is not recognized as an internal or external command, operable program or batch file.
                                #this is happening because we have not established our own virtual environment yet
                                #this is pulling from the global python library, and not our local one, that we have to create.

plt.plot([1,2,3,4,5],color='red')

plt.show()