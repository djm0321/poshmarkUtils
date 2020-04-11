import wx
import pRelist
class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(parent=None, title='Poshmark Utils')
        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # Creates username textbox
        usernameBox = wx.BoxSizer(wx.HORIZONTAL)
        user = wx.StaticText(panel, -1, "Username:")
        usernameBox.Add(user, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.username = wx.TextCtrl(panel)
        usernameBox.Add(self.username, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.vbox.Add(usernameBox)

        # Creates password textbox
        pwdBox = wx.BoxSizer(wx.HORIZONTAL)
        pwdTxt = wx.StaticText(panel, -1, "Password:")
        pwdBox.Add(pwdTxt, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.pwd = wx.TextCtrl(panel, style = wx.TE_PASSWORD)
        pwdBox.Add(self.pwd, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.vbox.Add(pwdBox)

        #Creates textbox that gets minimum price user wants to start selling at
        minPrice = wx.BoxSizer(wx.HORIZONTAL)
        minPriceTxt = wx.StaticText(panel, -1, "MinPrice:")
        minPrice.Add(minPriceTxt, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.minP = wx.TextCtrl(panel)
        minPrice.Add(self.minP, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.vbox.Add(minPrice)

        # Creates submit button which starts the process
        start = wx.Button(panel, label="Start")
        start.Bind(wx.EVT_BUTTON, self.on_press)
        self.vbox.Add(start, 0, wx.ALL | wx.CENTER, 5)

        # Creates Checkboxes in case user only wants to share specific categories
        checkboxes = wx.BoxSizer(wx.HORIZONTAL)
        self.maleCheckBoxes = wx.BoxSizer(wx.VERTICAL)
        self.male = wx.CheckBox(panel, label = "Male")
        self.maleCheckBoxes.Add(self.male, 1, wx. ALL)


        self.subBox = wx.BoxSizer(wx.VERTICAL)
        self.subBox.AddMany([
            (wx.CheckBox(panel, label = "Jackets And Coats"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Jeans"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Pants"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shirts"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shoes"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shorts"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Sweaters"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Swim"), 1, wx.EXPAND | wx.RIGHT | wx. ALL)
        ])

        self.maleCheckBoxes.Add(self.subBox, 1)

        self.femaleCheckBoxes = wx.BoxSizer(wx.VERTICAL)
        self.female = wx.CheckBox(panel, label = "Female")
        self.femaleCheckBoxes.Add(self.female, 1, wx. ALL)
        self.subBox2 = wx.BoxSizer(wx.VERTICAL)
        self.subBox2.AddMany([
            (wx.CheckBox(panel, label = "Accessories"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Bags"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Dresses"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Intimates And Sleepwear"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Jackets And Coats"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Jeans"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Pants"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Shoes"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Shorts"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Skirts"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Sweaters"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Swim"), 1, wx.EXPAND | wx.RIGHT | wx.ALL),
            (wx.CheckBox(panel, label="Tops"), 1, wx.EXPAND | wx.RIGHT | wx.ALL)
        ])
        self.femaleCheckBoxes.Add(self.subBox2)

        childCheckBoxes = wx.BoxSizer(wx.VERTICAL)
        self.children = wx.CheckBox(panel, label = "Children")
        childCheckBoxes.Add(self.children, 1, wx. ALL)
        self.Bind(wx.EVT_CHECKBOX, self.on_checked_main)

        checkboxes.Add(self.maleCheckBoxes, 5, wx.ALL | wx.ALIGN_LEFT)
        checkboxes.Add(self.femaleCheckBoxes, 5, wx.ALL | wx.ALIGN_LEFT)
        checkboxes.Add(childCheckBoxes, 5, wx.ALL | wx.ALIGN_LEFT)

        self.vbox.Add(checkboxes, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox)
        self.Show()
        self.maleCheckBoxes.Hide(self.subBox)
        self.femaleCheckBoxes.Hide(self.subBox2)
    
    def on_press(self, event):
        enter1 = self.username.GetValue()
        enter2 = self.pwd.GetValue()
        enter3 = self.minP.GetValue()
        if not enter1 or not enter2:
            print("Please enter a username and password")
        elif enter3.isdigit():
            pRelist.begin(enter1, enter2, int(enter3))
        else:
            pRelist.begin(enter1, enter2, None)
        # value = self.text_ctrl.GetValue()
        # if not value:
        #     print("You didn't enter anything!")
        # else:
        #     print(f'You typed: "{value}"')

    def on_checked_main(self, event):
        cb = event.GetEventObject()
        category = cb.GetLabel()
        val = cb.GetValue()
        if (val):
            if (category == "Male"):
                self.maleCheckBoxes.Show(self.subBox)
            elif (category == "Female"):
                self.femaleCheckBoxes.Show(self.subBox2)
        else: 
            if (category == "Male"):
                self.maleCheckBoxes.Hide(self.subBox)
            elif (category == "Female"):
                self.femaleCheckBoxes.Hide(self.subBox2)  


    



def startUp():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

startUp()