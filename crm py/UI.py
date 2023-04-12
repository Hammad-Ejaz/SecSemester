import os
from BL import ProjectBL, SaleClientsBL
from BL import MuserBL
from BL import InfoClientsBL
from DL import MuserDL
from DL import ProjectDL
from DL import InfoLeadDL
from DL import SaleDL
from DL import HelperDL
class Helper:
    @staticmethod
    def printUsers():
        for i in MuserDL.myUsers:
            if(i.category != "admin"):
                print(">> " , i.name)
    @staticmethod 
    def Printprojects():
        for i in ProjectDL.allProjects:
            print(i.name)
    @staticmethod 
    def printScheduale():
        print("followup")
        print("visit")
        print("cold")
        print("meeting")
        print("hotclient")
    @staticmethod
    def clearScreen():
        input("press any key to back")
        os.system("cls")
class Main:
    @staticmethod
    def Header():
        print(" _________________________________________________________")
        print("|                                                         |")
        print("|      DREAM LANDS REAL ESTATE AND MARKETING COMPANY      |")
        print("|_________________________________________________________|")

    @staticmethod
    def Mainmenu():
        print("MAIN MENUE")
        print("1_ ADMIN ACCOUNT")
        print("2_ USER ACCOUNT ")
        print("3_EXIT")
        op = int(input())
        return op
    @staticmethod
    def Admin():
        valid = False
        print("LOGIN")
        email = input("EMAIL :  ")
        valid = HelperDL.isValidEMAIL(email)
        while (valid == False):
            print("INVALUD EMAIL ")
            email = input()
            valid = HelperDL.isValidEMAIL(email)
        password = input("PASSWORD : ")
        s = MuserBL(""  , email, password, "", "", "" , "" )
        os.system("cls")
        return s 
    @staticmethod
    def Worngpassword():
        print("WRONG PASSWORD")
        input("PRESS ANY KEY TO BACK")
        os.system("cls")
    @staticmethod
    def Adminmenu():
        print("ADMIN ACCOUNT")
        print("1_HOME")
        print("2_LEADS")
        print("3_SALES")
        print("4_INVENTORY")
        print("5_PROJECTS INFO")
        print("6_ADD USERS")
        print("7_BACK")
        op = int(input())
        while (op > 7 or op < 1):
            op = int(input("INVALID NUMBER "))
        os.system("cls")
        return op
    @staticmethod
    def Adminhome():
        print("ADMIN ACCOUNT > HOME")
        tfollow = int(InfoLeadDL.getClientNoBySchedule("followup" , InfoLeadDL.TodayTotalLeads()))
        tvisit = int(InfoLeadDL.getClientNoBySchedule("visit" , InfoLeadDL.TodayTotalLeads()))
        tlead = len(InfoLeadDL.TodayTotalLeads())
        print("TOTAL LEADS ~ " , tlead)
        print("TOTAL FOLLOW UPS ~ " , tfollow)
        print("TOTAL VISITS ~ " , tvisit)
        Helper.clearScreen()
class adminLeadUI:
    @staticmethod
    def Adminleads(): 
        print("ADMIN ACCOUNT > LEADS ")
        print("1_ADD LEADS")
        print("2_TOTAL LEADS")
        print("3_DELETE LEADS")
        print("4_BACK")
        op = int(input())
        while (op > 4 or op < 0):
            op = int(input("INVALID NUMBER "))
        os.system("cls")    
        return op
    @staticmethod
    def Adminleads1():
        print("ADMIN ACCOUNT > LEADS > ADD LEADS")
        if(len(MuserDL.myUsers) > 0):
            print("SPOs : ")
            Helper.printUsers()
            spoName = input("Enter spo name")    
            Name = input("NAME : ")
            Phone = input("PHONE NUMBER : ")
            while (len(Phone) != 11):
                print("INVALID NUMBER ")
                Phone = input()
            print("ENTER PROJECTS FROM FOLLOWING : ")
            Helper.Printprojects()
            Project = input()
            source = input("SOURCE : ")
            Leads = InfoClientsBL(spoName,Name,Phone,Project,source)
            Helper.clearScreen()
            return Leads
        else:
            print("no user have been added yet")
            Helper.clearScreen()
    @staticmethod
    def Admintotalleads2():
        print("ADMIN ACCOUNT > LEADS > TOTAL LEADS")
        print("---------------------------------------------------------------------------------------------------------")
        print("s.no" , "name" , " number " ,"spo" , "project" , "source")
        print("---------------------------------------------------------------------------------------------------------")
        for j in range(len(InfoLeadDL.infoClientsList)):
            i = InfoLeadDL.infoClientsList[j]
            print(j + 1 ,  i.spoName  , i.name  , i.phone , i.project  , i.source  )
        Helper.clearScreen()
    @staticmethod
    def DeleteLead3():
        adminLeadUI.Admintotalleads2()
        index = int(input("enter number"))
        InfoLeadDL.delLead(index - 1)
        Helper.clearScreen()
class adminSaleUI: 
    @staticmethod
    def Sales():
        print("ADMIN ACCOUNT > SALES")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
        print("|" , "\t" , "TOTAL SALES             " , len(SaleDL.salesList)+1 , "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" , "|")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
        print("|" , "\t" , "DETAILS  " , "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" , "|")
        sortedList = sorted(SaleDL.salesList, key = lambda x: x.name)
        for i in sortedList:
            print("name" , " _ " , "cnic" , " _ " , "price" , " _ " , "project")
            print(i.name , " _ " , i.cnic , " _ " , i.price , " _ " , i.project)
        Helper.clearScreen()
class adminInv:
    @staticmethod
    def Admininv():
        print("ADMIN ACCOUNT > INVENTORY")
        print("1_PLOTS INFO")
        print("2_VIEW PLOTS INFO")
        print("3_BACK")
        op = int(input())
        while (op > 3 or op < 0):
            print("INVALID NUMBER ")
            op = int(input())
        Helper.clearScreen()
        return op
    @staticmethod
    def Admininv1():
        print("ADMIN ACCOUNT > INVENTORY > EDIT PLOTS")
        name1 = input("ENTER PROJECT NAME : ")
        city = input("ENTER CITY NAME")
        i = ProjectDL.getSpecificProject(name1 , city)
        if( i != None):
            threeMarla =  input("ENTER 3 MARLA PLOTS  : ")
            i.Area.append(threeMarla)
            fiveMarla =  input("ENTER 5 MARLA PLOTS  : ")
            i.Area.append(fiveMarla)
            tenMarla = input("ENTER 10 MARLA PLOTS  : ")
            i.Area.append(tenMarla)
            kannal = input("ENTER 1 KANNAL PLOTS  : ")
            i.Area.append(kannal)
        else:
            print("SOMETHING WENT WRONG")
        Helper.clearScreen()
    @staticmethod
    def Viewplotsinfo():
        print("ADMIN ACCOUNT > PROJECTS > VIEW RPOJECTS INFO")
        for i in ProjectDL.allProjects :
            print("                      " , i.name)
            print("\n")
            print("-----------------------------------------------------------")
            print("|" , "\t" , "AVAILABLE PLOTS" , "                                   |")
            print("|---------------------------------------------------------|")
            print("|" , "\t" , "3_marla plots   " , "\t\t\t" , i.area[0] , "\t" , "  |")
            print("|---------------------------------------------------------|")
            print("|" , "\t" , "5_marla plots   " , "\t\t\t" + i.area[1] , "\t" , "  |")
            print("|---------------------------------------------------------|")
            print("|" , "\t" , "10_marla plots   " , "\t\t\t" , i.area[2] , "\t" , "  |")
            print("|---------------------------------------------------------|")
            print("|" , "\t" , "1_kannal   " , "\t\t\t\t" , i.area[3] , "\t" , "  |")
            print("-----------------------------------------------------------")
        Helper.clearScreen()
class adminProjectUI:
    @staticmethod
    def Adminprojectinfo():
        print("ADMIN ACCOUT > PROJECT INFO ")
        print("1_ ADD PROJECT") 
        print("2_ VIEW PROJECTS") 
        print("3_ DELETE PROJECTS") 
        print("4_BACK") 
        op = int(input()) 
        while (op > 4):
            print("INVALID NUMBER") 
            op = int(input()) 
        os.system("cls")
        return op 
    @staticmethod
    def Addproject():
        print("ADMIN ACCOUT > ADD PROJECTS ") 
        name2 = input("ENTER YOUR PROJECT  : ") 
        city = input("ENTER THE CITY NAME : ")
        project = ProjectBL(name2 ,city)
        project.area.append(int(input("ENTER 3 MARLA PLOTS  : ")))
        project.area.append(int(input("ENTER 5 MARLA PLOTS  : ")))
        project.area.append(int(input("ENTER 10 MARLA PLOTS  : ")))
        project.area.append(int(input("ENTER 1 KANNAL PLOTS  : ")))
        Helper.clearScreen()
        return project
    @staticmethod
    def Showprojects():
        if len(ProjectDL.allProjects) > 0 :
            for i in ProjectDL.allProjects:
                print(i.name)
                print(i.city)
                print("- - - - - -")
        else:
            print("NO PROJECT IS ADDED")
    @staticmethod
    def deletprojects() :
        print("ADMIN ACCOUNT > PROJECT INFO  > DELETE PROJECT") 
        adminProjectUI.Showprojects()
        print("ENTER THE PROJECT NAME : ")
        name3 = input()
        print("ENTER THE CITY NAME : ")
        city = input()
        ProjectDL.deleteProject(name3 , city)
class adminAddUserUI:
    @staticmethod
    def Adminadduser():
        name4 = input("ENTER NAME : ")  
        email = input("ENTER EMAIL : ") 
        valid =  HelperDL.isValidEMAIL(email) 
        while (valid == False):
            print("INVALID EMAIL ") 
            email = input()
            valid = HelperDL.isValidEMAIL(email) 
        catagory = input("ENTER CATAGORY") 
        number = input("ENTER PHONE NUMBER : ") 
        while (len(number) != 11):
            print("INVALID NUMBER") 
            number = input() 
        password = input("ENTER PASSWORD : ") 
        cnic = input("ENTER THE CNIC :")
        city = input("ENTER THE CITY :")
        user = MuserBL(name4 ,email , password , catagory , number , cnic , city)
        return user
class UserMain:
    @staticmethod
    def Usermenue():
        print("USER ACCOUNT") 
        print("1_HOME") 
        print("2_LEADS") 
        print("3_SALES") 
        print("4_INVENTORY") 
        print("5_PROJECTS") 
        print("6_BACK") 
        op = int(input()) 
        while (op > 6 or op < 0):
            print("INVALID NUMBER") 
            op = int(input()) 
        return op 
    @staticmethod     
    def Userhome(name): 
        print("USER ACCOUNT > HOME") 
        print("TOTAL LEADS ~ " , ) 
        print("FOLLOW UPS ~ " , InfoLeadDL.getClientNoBySchedule("followup" , InfoLeadDL.getLeadofSpecificSPO(name))) 
        print("HOT CLIENTS ~ " ,  InfoLeadDL.getClientNoBySchedule("hotclient" , InfoLeadDL.getLeadofSpecificSPO(name))) 
        print("VISITS ~ " , InfoLeadDL.getClientNoBySchedule("visit" , InfoLeadDL.getLeadofSpecificSPO(name)))
        print("COLD CLIENTS ~ " , InfoLeadDL.getClientNoBySchedule("cold" , InfoLeadDL.getLeadofSpecificSPO(name))) 
        Helper.clearScreen()
class userLead:
    @staticmethod       
    def Userleads(name):
        if(len(InfoLeadDL.getLeadofSpecificSPO(name)) < 0):
            print("NO RECORD HAVE TO SHOW ENTER 0") 
        else:
            print("ADMIN ACCOUNT > LEADS > TOTAL LEADS")
            print("---------------------------------------------------------------------------------------------------------")
            print("s.no" , "name" , " number " ,"spo" , "project" , "source")
            print("---------------------------------------------------------------------------------------------------------")
            for j in range(len(InfoLeadDL.getLeadofSpecificSPO(name))):
                i = InfoLeadDL.getTodayLeadsOfSpecificSpo(name)[j]
                print(j + 1 ,  i.spoName  , i.name  , i.phone , i.project  , i.source)
        
    @staticmethod       
    def Useraddresponse(name):
        print("ENTER NUMBER : ") 
        o = int(input()) 
        i = InfoLeadDL.getLeadofSpecificSPO(name)[o-1]
        print("NAME  : " , i.name) 
        print("PHONE NO  : " , i.phone) 
        print("PROJECT  : " , i.project) 
        print("SOURCE  : " , i.source) 
        print("YOUR PREVIOUS RESPONSE : ") 
        for j in i.response:
            print(j) 
        print("-----------------------------------------------")
        print("ENTER YOUR NEW RESPONSE  : ") 
        i.response.append(input())
        Helper.printScheduale()
        print("ENTER SCHEDULE  : ") 
        Helper.clearScreen()
class userSale:          
    @staticmethod       
    def Usersales():
        print("USER ACCOUNT > SALES") 
        print("1_ADD SALE") 
        print("2_TOTAL SALE") 
        print("3_BACK") 
        op = int(input()) 
        while (op > 3 or op < 0):
            print("INVALID NUMBER") 
            op = int(input()) 
        os.system("cls")
        return op 

    @staticmethod       
    def Useraddsale(name):
        print("USER ACCOUNT > SALES > ADD SALES") 
        name1 = input("NAME : ") 
        cnic = input("CNIC : ") 
        city = input("CITY : ") 
        number = input("PHONE : ") 
        while (len(number) != 11):
            print("INVALID NUMBER") 
            number = input() 
        print("CHOOSE PROJECTS FROM FOLLOWING : ") 
        Helper.Printprojects()
        project = input()
        source = input("CHOOSE SOURCE")
        blockNo = input("ENTER THE BLOCK NO")
        area = input("Enter THE AREA : ") 
        plots = input("Enter NO OF PLOTS") 
        price = input("PRICE : ") 
        sale = SaleClientsBL(name , name1 , number , project , source , cnic , area , plots , price , blockNo , city)
        Helper.clearScreen()
        return sale
    @staticmethod           
    def Usertotalsale(name):
        print("USER ACCOUNT > SALES > TOTAL SALES") 
        s = len(SaleDL.getSaleofSpecificSPO(name))
        print("TOTAL NUMBER OF SALES ARE : " , s) 
        Helper.clearScreen() 
class UserInv:
    @staticmethod       
    def Userinv():
        print("USER ACCOUNT > INVENTORY > PLOTS") 
        if(len(ProjectDL.allProjects) <= 0):
            print("NO PROJECT IS ADDED FIRST ADD THE PROJECTS") 
        else:
            print("CHOOSE THE PROJECT : ") 
            Helper.Printprojects() 
            project  = input("name : ") 
            city = input("city : ")
            print("3 MARLA PLOTS ARE : " , ProjectDL.getSpecificProject(project , city).area[0]) 
            print("5 MARLA PLOTS ARE : " , ProjectDL.getSpecificProject(project , city).area[1]) 
            print("10 MARLA PLOTS ARE : " , ProjectDL.getSpecificProject(project , city).area[2]) 
            print("1 KANNAL PLOTS ARE : " , ProjectDL.getSpecificProject(project , city).area[3]) 
        Helper.clearScreen()

