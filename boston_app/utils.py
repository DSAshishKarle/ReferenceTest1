import numpy as np
import pandas as pd
import pickle
import json
import config

class Boston():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B, LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)
        
        with open(config.SCALE_FILE_PATH,"rb") as f:
            self.std = pickle.load(f)

    def get_price(self):
        self.load_model()

        # test_array = np.zeros(len(self.json_data["columns"]))
        test_array = np.array([self.CRIM, self.ZN, self.INDUS, self.CHAS, self.NOX, self.RM, self.AGE, 
                       self.DIS, self.RAD, self.TAX,self.PTRATIO, self.B, self.LSTAT])
        test_array = np.array(test_array,ndmin=2)
        test_array[0] = self.CRIM
        test_array[0][1] = self.ZN
        test_array[0][2] = self.INDUS
        test_array[0][3] = self.CHAS
        test_array[0][4] = self.NOX
        test_array[0][5] = self.RM
        test_array[0][6] = self.AGE
        test_array[0][7] = self.DIS
        test_array[0][8] = self.RAD
        test_array[0][9] = self.TAX
        test_array[0][10] = self.PTRATIO
        test_array[0][11] = self.B
        test_array[0][12] = self.LSTAT


        print("Test Array: ", test_array)
        scaled_test_array = self.std.transform(test_array)
        predict_price = self.model.predict(scaled_test_array)[0]

        
        return predict_price

if __name__ == "__main__":
        CRIM       =   0.05724
        ZN         =  0.00000
        INDUS      =  4.24000
        CHAS       =  0.00000
        NOX        =  0.46000
        RM         =  6.33300
        AGE        = 15.20000
        DIS        =  7.21460
        RAD        =  2.00000
        TAX        = 450.00000
        PTRATIO    = 17.90000
        B          = 370.21000
        LSTAT      =  8.34000   

        bos_child = Boston(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B, LSTAT)
        bos_child.get_price()


