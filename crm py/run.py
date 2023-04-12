from DL import InfoLeadDL, MuserDL, ProjectDL, SaleDL
from UI import (Helper, Main, UserInv, UserMain, adminAddUserUI, adminInv, adminLeadUI, adminProjectUI,
                adminSaleUI, userLead, userSale)


def main():
    Main.Header()
    mainOp = 0
    while(mainOp != 3):
        mainOp = Main.Mainmenu()
        if(mainOp == 1):
            a = Main.Admin()
            if(a.email == "admin@gmail.com" and a.password == "123"):
                adminOp = 0
                while(adminOp != 7):
                    adminOp = Main.Adminmenu()
                    if(adminOp == 1):
                        Main.Adminhome()
                    if(adminOp == 2):
                        adminLeadOp = 0
                        while(adminLeadOp != 4):
                            adminLeadOp = adminLeadUI.Adminleads()
                            if(adminLeadOp == 1):
                                InfoLeadDL.addLeadToList(adminLeadUI.Adminleads1())
                            if(adminLeadOp == 2):
                                adminLeadUI.Admintotalleads2()
                                Helper.clearScreen()
                            if(adminLeadOp == 3):
                                adminLeadUI.Admintotalleads2()
                                adminLeadUI.DeleteLead3()
                    if(adminOp == 3):
                        adminSaleUI.Sales()
                    if(adminOp == 4):
                        adminInvOp = 0
                        while(adminInvOp != 3):
                            adminInvOp = adminInv.Admininv()
                            if(adminInvOp == 1):
                                adminInv.Admininv1()
                            if(adminInvOp == 2):
                                adminInv.Viewplotsinfo()
                    if(adminOp == 5):
                        adminProOp = 0
                        while(adminProOp != 4):
                            adminProOp = adminProjectUI.Adminprojectinfo()
                            if(adminProOp == 1):
                                ProjectDL.addProject(adminProjectUI.Addproject())
                            if(adminProOp == 2):
                                adminProjectUI.Showprojects()
                                Helper.clearScreen()
                            if(adminProOp == 3):
                                adminProjectUI.Showprojects()
                                adminProjectUI.deletprojects()
                    if(adminOp == 6):
                        MuserDL.adduseritoList(adminAddUserUI.Adminadduser()) 
            else:
                Main.Worngpassword()                 
        elif(mainOp == 2):
            s = Main.Admin()
            userOp = 0
            while(userOp != 6):
                userOp = UserMain.Usermenue()
                if(userOp == 1):
                    UserMain.Userhome(s.name)
                if(userOp == 2):
                    userLead.Userleads(s.name)
                    userLead.Useraddresponse(s.name)
                if(userOp == 3):
                    userSaleOp = 0
                    while(userSaleOp != 3):
                        userSaleOp = userSale.Usersales()
                        if(userSaleOp == 1):
                            SaleDL.addSalesToList(userSale.Useraddsale(s.name))
                        if(userSaleOp == 2):
                            userSale.Usertotalsale(s.name)
                if(userOp == 4):
                    UserInv.Userinv()
                if(userOp == 5):
                    adminProjectUI.Showprojects()
                    Helper.clearScreen()
if __name__ == "__main__":
    main()
