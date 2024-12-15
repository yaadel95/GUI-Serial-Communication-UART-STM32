from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Live Stream")
        self.root.geometry("360x120")
        self.root.config(bg="white")


####################################################################################################################################
##################################################        Com  interface   #########################################################
####################################################################################################################################

# Class to setup and create the communication manager with MCU
class ComGui():
    def __init__(self, root, serial):
        '''
        Initialize the connexion GUI and initialize the main widgets 
        '''
        # Initializing the Widgets
        self.root = root
        self.serial = serial
        self.frame = LabelFrame(root, text="Com Manager",
                                padx=5, pady=5, bg="white")
        self.label_com = Label(
            self.frame, text="Available Port(s): ", bg="white", width=15, anchor="w")
        self.label_bd = Label(
            self.frame, text="Baude Rate: ", bg="white", width=15, anchor="w")
        
        # Setup the Drop option menu
        self.baudOptionMenu()
        self.ComOptionMenu()

        # Add the control buttons for refreshing the COMs & Connect
        self.btn_refresh = Button(self.frame, text="Refresh",
                                  width=10,  command=self.com_refresh)
        self.btn_connect = Button(self.frame, text="Connect",
                                  width=10, state="disabled",  command=self.serial_connect)

        # Optional Graphic parameters
        self.padx = 20
        self.pady = 5

        # Put on the grid all the elements
        self.publish()

    def publish(self):
        '''
         Method to display all the Widget of the main frame
        '''
        self.frame.grid(row=0, column=0, rowspan=3,
                        columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)
        self.label_bd.grid(column=1, row=3)

        self.drop_baud.grid(column=2, row=3, padx=self.padx, pady=self.pady)
        self.drop_com.grid(column=2, row=2, padx=self.padx)
        
        self.btn_refresh.grid(column=3, row=2)
        self.btn_connect.grid(column=3, row=3)    

    def ComOptionMenu(self):
        '''
         Method to Get the available COMs connected to the PC
         and list them into the drop menu
        '''
        # Generate the list of available coms

        self.serial.getCOMList()

        self.clicked_com = StringVar()
        self.clicked_com.set(self.serial.com_list[0])
        self.drop_com = OptionMenu(
            self.frame, self.clicked_com, *self.serial.com_list, command=self.connect_ctrl)
        
        self.drop_com.config(width=10)

    def baudOptionMenu(self):
        '''
         Method to list all the baud rates in a drop menu
        '''
        self.clicked_bd = StringVar()
        bds = ["-",
               "300",
               "600",
               "1200",
               "2400",
               "4800",
               "9600",
               "14400",
               "19200",
               "28800",
               "38400",
               "56000",
               "57600",
               "115200",
               "128000",
               "256000"]
        self.clicked_bd .set(bds[0])
        self.drop_baud = OptionMenu(
            self.frame, self.clicked_bd, *bds, command=self.connect_ctrl)
        self.drop_baud.config(width=10)

    def connect_ctrl(self, widget):
        '''
        Mehtod to keep the connect button disabled if all the 
        conditions are not cleared
        '''
        print("Connect ctrl")

        # Checking the logic consistency to keep the connection btn
        if "-" in self.clicked_bd.get() or "-" in self.clicked_com.get():
            self.btn_connect["state"] = "disabled"
        else:
            self.btn_connect["state"] = "active"

    def com_refresh(self):
        print("Refresh")
        # Get the Widget destroyed
        self.drop_com.destroy()

        # Refresh the list of available Coms
        self.ComOptionMenu()

        # Publish the this new droplet
        self.drop_com.grid(column=2, row=2, padx=self.padx)

        # Just in case to secure the connect logic
        logic = []
        self.connect_ctrl(logic)


    def serial_connect(self):
        print("Connect")
        if self.btn_connect["text"] in "Connect":
            # Start the serial communication
            self.serial.SerialOpen(self)
         # If connection established move on
            if self.serial.ser.status:
                # Update the COM manager
                self.btn_connect["text"] = "Disconnect"
                self.btn_refresh["state"] = "disable"
                self.drop_baud["state"] = "disable"
                self.drop_com["state"] = "disable"
                InfoMsg = f"Successful UART connection using {self.clicked_com.get()}"
                messagebox.showinfo("showinfo", InfoMsg)

            else:
                ErrorMsg = f"Failure to estabish UART connection using {self.clicked_com.get()} "
                messagebox.showerror("showerror", ErrorMsg)

        else:

            # Closing the Serial COM
            # Close the serial communication
            self.serial.SerialClose(self)
            InfoMsg = f"UART connection using {self.clicked_com.get()} is now closed"
            messagebox.showwarning("showinfo", InfoMsg)
            self.btn_connect["text"] = "Connect"
            self.btn_refresh["state"] = "active"
            self.drop_baud["state"] = "active"
            self.drop_com["state"] = "active"

####################################################################################################################################
##################################################    Connect interface    #########################################################
####################################################################################################################################

class ConnGUI():
    def __init__(self, root, serial):
        '''
        Initialize main Widgets for communication GUI
        '''
       

        

    def ConnGUIOpen(self):
        '''
        Method to display all the widgets 
        '''
        

    def ConnGUIClose(self):
        '''
        Method to close the connection GUI and destorys the widgets
        '''
        # Must destroy all the element so they are not kept in Memory
        
    def start_stream(self):
        pass

    def stop_stream(self):
        pass

    def new_chart(self):
        pass

    def kill_chart(self):
        pass

    def save_data(self):
        pass


if __name__ == "__main__":
    RootGUI()
    ComGui()
    ConnGUI()