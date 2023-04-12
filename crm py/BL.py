import datetime
# class AreaBL:
#     def __init__(self, marla , plots):
#         self.marla = marla
#         self.plots = plots
class LeadBL:
    def __init__(self, spoName,name,phone,project,source):
        self.spoName = spoName
        self.name = name
        self.phone = phone
        self.project = project
        self.source = source
    dealDone = False
  #  @abstractmethod 
    def SaleDone(self):
        pass
class InfoClientsBL(LeadBL):
    def __init__(self, spoName,name,phone,project,source):
        LeadBL.__init__(self , spoName, name, phone, project, source)
        self.date = datetime.date.today()
        self.schedule = "FOLLOW UPS"
        self.response.append("give info")
    response = []
    DealDone = False
    def SaleDone(self):
        self.DealDone = True
class SaleClientsBL(LeadBL):
    def __init__(self,spoName,name,phone,project,source,cnic, area, plotNo, price,blockNoOrAddress,city): 
        LeadBL.__init__(self,spoName, name, phone, project, source)
        self.Cnic = cnic
        self.area = area
        self.plotNo = plotNo
        self.price = price
        self.blockNoOrAddress = blockNoOrAddress
        self.city = city
        self.DealDone = False
    def SaleDone(self):
        self.DealDone = True
class MuserBL:
    #def __init__(self,email, password):
     #   self.email = email
      #  self.password = password
    def __init__(self,name , email, password , category , phoneNo , cnic , city):
        self.email = email
        self.password = password
        self.name = name
        self.category = category
        self.phoneNo = phoneNo
        self.city = city
        self.cnic = cnic
    def isAdmin(self):
        if (self.category == "Admin"):
            return True
        else : 
            return False

class ProjectBL:
    def __init__(self,name, city):
        self.name = name
        self.city = city
        self.area = []
  #  def areaExist(self , Area):
   #     for i in Area:
    #        if(i.Marla == self.area.Marla):
     #           return True
      #  return False






