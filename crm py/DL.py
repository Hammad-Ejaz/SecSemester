import datetime
class HelperDL:
    @staticmethod
    def isValidEMAIL(text):
        atIndex = -1
        dotIndex = -1
        for i in range(len(text)):
            if (text[i] == '@'):
                atIndex = i
                break
        if (atIndex != -1):
            for i in range(len(text)):
                if (text[i] == '.'):
                    dotIndex = i
                    break
        if (atIndex != -1 and dotIndex != -1):
            return True
        return False

class InfoLeadDL:
    infoClientsList = [] 
    @staticmethod   
    def addLeadToList(Lead):
        InfoLeadDL.infoClientsList.append(Lead)
    @staticmethod
    def getLeadofSpecificSPO(name):
        Leads = []
        Leads = [Leads.append(i) for i in InfoLeadDL.infoClientsList if (i.SpoName == name)]
        return Leads
    @staticmethod
    def delLead(index):
        InfoLeadDL.infoClientsList.pop(index)
    @staticmethod
    def editLead(previous , update):
        for i in InfoLeadDL.infoClientsList:
            if (i.Name == previous.Name):
                i.Name = update.Name
                i.Phone = update.Phone
                i.Project = update.Project
                i.Source = update.Source
                i.SpoName = update.SpoName
                i.date = update.date
    @staticmethod
    def getTodayLeadsOfSpecificSpo(name):
        todayLeads = []
        totalLeads = InfoLeadDL.getLeadofSpecificSPO(name)
        date = datetime.date.today()
        todayLeads = [todayLeads.append(i) for i in totalLeads if (i.date == date)]
        return todayLeads
    @staticmethod
    def TodayTotalLeads():
        TtodayLead = []
        date = datetime.date.today()
        TtodayLead = [TtodayLead.append(i) for i in InfoLeadDL.infoClientsList if (i.date == date)]
        return TtodayLead
    @staticmethod
    def getSpecificLead(name):
        for i in InfoLeadDL.infoClientsList:
            if (i.Name == name):
                return i
        return None
    @staticmethod
    def getClientNoBySchedule(schedule ,Lead):
        no = 0 
        for i in Lead:
            if i.Schedule == schedule:
                no += 1
        return no


    #    
  #  @staticmethod
  #  def saveData(path):
  #      StreamWriter file = new StreamWriter(path);
  #          foreach (InfoClientsBL i in InfoClientsList)
  #          {
  #              file.WriteLine(i.Name + "," + i.SpoName + "," + i.Phone + "," + i.Project + "," + i.Schedule + "," + i.Source + "," + i.DealDone + "," + i.Response + "," + i.Date);
          #  }#
          #  file.Flush();
#            file.Close();
#        }
#        @staticmethod
#        public static void loadData(string path)
#        {
#            infoClientsList = new List<InfoClientsBL>();
#            if (File.Exists(path))
#            {
#                string record;
##                StreamReader newfile = new StreamReader(path);
#                while ((record = newfile.ReadLine()) != null)
#                {
#                    string[] splittedRecord = record.Split(',');
#                    string name = splittedRecord[0];
#                    string spoName = splittedRecord[1];
#                    string phone = splittedRecord[2];
#                    string project = splittedRecord[3];
#                    string schedule = splittedRecord[4];
#                    string source = splittedRecord[5];
#                    bool DealDone = bool.Parse(splittedRecord[6]);
#                    string Response = splittedRecord[7];
#                    DateTime Date = DateTime.Parse(splittedRecord[8]);
#                    InfoClientsBL lead = new InfoClientsBL(spoName, name, phone, project, source);
#                    lead.Schedule = schedule;
#                    lead.Response = Response;
#                    lead.DealDone = DealDone;
#                    lead.Date = Date;
#                    InfoClientsList.Add(lead);
#                }
#                newfile.Close();
      #      }
     #   }
    #} 


class MuserDL:
    myUsers = []
    @staticmethod
    def delUser(index):
        MuserDL.myUsers.pop(index)
    @staticmethod    
    def editUser(previous ,update):
        for i in MuserDL.myUsers:
            if(i.Email == previous.Email and i.Password == previous.Password and i.Category == previous.Category):
                i.Name = update.Name
                i.Email = update.Email
                i.Password = update.Password
                i.City = update.City
                i.Cnic = update.Cnic
                i.Category = update.Category
                i.PhoneNo = update.PhoneNo
    @staticmethod
    def myEmployes():
        employes = []
        for i in MuserDL.myUsers:
            if (i.Category != "Admin"):
                employes.append(i)
        return employes
    @staticmethod
    def isValidUser(email, password):
        for i in MuserDL.myUsers:
            if (email == i.Email and password == i.Password):
                return i
        return None
    @staticmethod
    def adduseritoList(user):
        MuserDL.myUsers.append(user)
class ProjectDL :
    allProjects = []
    @staticmethod
    def getSpecificProject(name , city):
        for i in ProjectDL.allProjects:
            if (i.name == name and i.city == city):
                return i
        return None
    @staticmethod
    def EditProject(previous , update):
        for i in ProjectDL.allProjects:
            if (i.Name == previous.Name and i.City == previous.City):
                for j in i.Area:
                    if(j.Marla == update.Area[0].Marla):
                        j.Plots = update.Area[0].Plots
    @staticmethod
    def addProject(project):
        ProjectDL.allProjects.append(project)
    @staticmethod
    def deleteProject(name , city):
        project = ProjectDL.getSpecificProject(name , city)
        if (project != None):
            ProjectDL.allProjects.remove(project)
    @staticmethod 
    def allplots():
        total = 0
        for i in ProjectDL.allProjects:
            for j in i.area:
                total = total + int(j)
        return total
class SaleDL:
    salesList = []
    @staticmethod
    def addSalesToList(sale):
        SaleDL.salesList.append(sale)
    @staticmethod
    def getTotalSalesList():
        return SaleDL.salesList
    @staticmethod
    def getSaleofSpecificSPO(name):
        sale = []
        sale = [sale.append(i) for i in SaleDL.salesList if (i.spoName == name)]
        return sale