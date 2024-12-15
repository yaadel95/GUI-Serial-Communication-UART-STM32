from GUI_Master import RootGUI, ComGui
from Serial_Com_ctrl import SerialCtrl



# Initiate the Root class that will manage the other classes
MySerial = SerialCtrl()
RootMaster = RootGUI()

# Initiate the Communication Master class that will manage all the other GUI classes
ComMaster= ComGui(RootMaster.root, MySerial)

# Start the Graphic User Interface
RootMaster.root.mainloop()



