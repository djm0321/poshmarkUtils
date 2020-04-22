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
        minPriceTxt = wx.StaticText(panel, -1, "Minimum Price:")
        minPrice.Add(minPriceTxt, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.minP = wx.TextCtrl(panel)
        minPrice.Add(self.minP, 1, wx.EXPAND | wx.CENTER | wx.ALL, 5)
        self.vbox.Add(minPrice)

        #Creates dropdown menu for sort-by choice
        sortByBox = wx.BoxSizer(wx.HORIZONTAL)
        sortByText = wx.StaticText(panel, -1, "Sort By:")
        sortByBox.Add(sortByText, 1, wx.EXPAND | wx.CENTER| wx.ALL, 5)
        choices = ["Price Low to High", "Price High to Low", "Just Shared", "Just In", "Recently Price Dropped", "Relevance"]
        self.sortBy = wx.Choice(panel, choices=choices)
        sortByBox.Add(self.sortBy, 1, wx.EXPAND | wx.LEFT | wx.ALL, 5)
        self.vbox.Add(sortByBox)



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
            (wx.CheckBox(panel, label = "Accessories"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label = "Jackets And Coats"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Jeans"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Pants"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shirts"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shoes"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Shorts"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Sweaters"), 1, wx.EXPAND | wx.RIGHT | wx. ALL),
            (wx.CheckBox(panel, label="Swim"), 1, wx.EXPAND | wx.RIGHT | wx. ALL)
        ])

        self.maleCheckBoxes.Add(self.subBox)

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
        self.SetSize(400, 251)

    def getCheckBoxes(self):
        male = self.male.GetValue()
        female = self.female.GetValue()
        maleVals = [False] * 10
        maleVals[0] = male
        femaleVals = [False] * 14
        femaleVals[0] = female
        children = self.children.GetValue()
        if male:
            x = 1
            for control in self.subBox.GetChildren():
                cbox = control.GetWindow()
                if isinstance(cbox, wx.CheckBox):
                    maleVals[x] = cbox.GetValue()
                x = x + 1
        if female:
            x = 1
            for control in self.subBox2.GetChildren():
                cbox = control.GetWindow()
                if isinstance(cbox, wx.CheckBox):
                    femaleVals[x] = cbox.GetValue()
                x = x + 1
        doThis = male or female or children
        return [doThis, maleVals, femaleVals, [children]]
    
    def on_press(self, event):
        enter1 = self.username.GetValue()
        enter2 = self.pwd.GetValue()
        enter3 = self.minP.GetValue()
        enter4 = ""
        sortBySelection = self.sortBy.GetSelection()
        if sortBySelection == 0:
            enter4 = "price_asc"
        elif sortBySelection == 1:
            enter4 = "price_desc"
        elif sortBySelection == 2:
            enter4 = "best_match"
        elif sortBySelection == 3:
            enter4 = "added_desc"
        elif sortBySelection == 4:
            enter4 = "price_drop"
        elif sortBySelection == 5:
            enter4 = "relevance"
        enter5 = self.getCheckBoxes()
        if not enter1 or not enter2:
            print("Please enter a username and password")
        elif enter3.isdigit():
            pRelist.begin(enter1, enter2, int(enter3), enter4, enter5)
        else:
            pRelist.begin(enter1, enter2, None, enter4, enter5)

    def resize(self):
        maleVal = self.male.GetValue()
        femaleVal = self.female.GetValue()
        if (femaleVal and maleVal):
            self.SetSize(401, 450)
        elif (femaleVal):
            self.SetSize(400, 450)
        elif (maleVal):
            self.SetSize(400, 370)
        else:
            self.SetSize(400, 251)

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
        self.resize()



    



def startUp():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

startUp()