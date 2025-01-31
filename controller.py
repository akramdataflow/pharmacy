from view import *
from model import *


class Controller:
    def __init__(self):
        self.view = MyView(self)
        self.model = Model()

    def show_list(self):
        self.show_list_add = Lists(self)
        self.show_list_add.show() 

    
    def show_sales(self):
        self.show_sales_add = Sales(self)
        self.show_sales_add.show() 

   


    def show_Purchases(self):
        self.show_Purchases_add = Purchases(self)
        self.show_Purchases_add.show() 

    def show_deferred(self):
        self.show_deferred_add = deferred(self)
        self.show_deferred_add.show() 


      
    def show_materials (self):
        self.show_materials_add =  Materials(self)
        self.show_materials_add.show() 

     
      
    def show_closet(self):
        self.show_closet_add = Closet(self)
        self.show_closet_add.show() 


         
    def show_Data_analysis(self):
        self.show_Data_analysis_add = Data_analysis(self)
        self.show_Data_analysis_add.show()

   
   #################mat
   
   
    def add_mat_to_model(self,name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.model.add_mat(name_mat, name_com, type_mat, count, expiry, Suitable_age)

    def del_mat_show(self):
        self.show_del_mat = DelMat(self)
        self.show_del_mat.show()

    def update_mat_show(self):
        self.show_update_mat = UpdateMat(self)
        self.show_update_mat.show()


    

    def get_mat_from_model(self):
        mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age = self.model.get_mat()
        return mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age
    
    def del_mat_from_model(self, mat_id):
        self.model.del_mat(mat_id)
        self.show_mat()


    def update_mat_to_model(self, mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.model.update_mat(mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age)
        self.show_mat()





        #############################  المؤجل




    def del_defer_show(self):
        self.show_del_defer = DelDefer(self)
        self.show_del_defer.show()

    def update_defer_show(self):
        self.show_update_defer = UpdateDefer(self)
        self.show_update_defer.show()

        
    def add_deferred_to_model(self, cos_name, cos_phone, cos_location , price):
        self.model.add_deferred(cos_name, cos_phone, cos_location , price, price)


    
    def get_deferred_from_model(self):
        defe_id, cos_name, cos_phone, cos_location , price = self.model.get_deferred()
        return defe_id, cos_name, cos_phone, cos_location , price
    
    def del_deferred_from_model(self,deferred_id):
        self.model.del_deferred(deferred_id)
        self.show_deferred()


    def update_deferred_to_model(self, deferred_id, cos_name, cos_phone, cos_location , price):
        self.model.update_deferred(deferred_id, cos_name, cos_phone, cos_location , price)
        self.show_deferred()    
    