import streamlit as st
import pandas as pd
import joblib
import sklearn


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(SeniorCitizen, Partner, Dependents, tenure, PhoneService,MultipleLines, InternetService, OnlineSecurity, OnlineBackup,DeviceProtection,
  TechSupport, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges, TotalCharges,tenure_MonthlyCharges_Segment, Streaming):

    
    
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"SeniorCitizen"] = SeniorCitizen
    test_df.at[0,"Partner"] = Partner
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"tenure"] = tenure
    test_df.at[0,"PhoneService"] = PhoneService
    test_df.at[0,"MultipleLines"] = MultipleLines
    test_df.at[0,"InternetService"] = InternetService
    test_df.at[0,"OnlineSecurity"] = OnlineSecurity
    test_df.at[0,"OnlineBackup"] = OnlineBackup
    test_df.at[0,"DeviceProtection"] = DeviceProtection
    test_df.at[0,"TechSupport"] = TechSupport
    test_df.at[0,"Contract"] = Contract
    test_df.at[0,"PaperlessBilling"] = PaperlessBilling
    test_df.at[0,"PaymentMethod"] = PaymentMethod
    test_df.at[0,"MonthlyCharges"] = MonthlyCharges
    test_df.at[0,"TotalCharges"] = TotalCharges
    test_df.at[0,"tenure_MonthlyCharges_Segment"] = tenure_MonthlyCharges_Segment
    test_df.at[0,"Streaming"] = Streaming

    
    
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result


    
def main():
    
    st.title("Telco Customer Churn")
    SeniorCitizen = st.selectbox("SeniorCitizen" , [0, 1])
    Partner = st.selectbox("Partner" , ['Yes', 'No'])
    Dependents = st.selectbox("Dependents" , ['Yes', 'No'])  
    tenure = st.slider("tenure" , min_value= 0 , max_value= 1000 , value=0,step=1)
    PhoneService = st.selectbox("PhoneService" , ['Yes', 'No'])
    MultipleLines = st.selectbox("MultipleLines" , ['Yes', 'No' , 'No phone service'])
    InternetService = st.selectbox("InternetService" , ['DSL' , 'Fiber optic' , 'No'])
    OnlineSecurity = st.selectbox("OnlineSecurity" , ['No' , 'Yes' , 'No internet service'])
    OnlineBackup = st.selectbox("OnlineBackup" , ['No' , 'Yes' , 'No internet service'])
    DeviceProtection = st.selectbox("DeviceProtection" , ['No' , 'Yes' , 'No internet service'])
    TechSupport = st.selectbox("TechSupport" , ['No' , 'Yes' , 'No internet service'])
    Contract = st.selectbox("Contract" , ['Month-to-month' , 'One year' , 'Two year'])
    PaperlessBilling = st.selectbox("PaperlessBilling" , ['Yes' , 'No']) 
    PaymentMethod = st.selectbox("PaymentMethod" , ['Electronic check' , 'Mailed check' , 'Bank transfer (automatic)', 'Credit card (automatic)'])
    MonthlyCharges = st.slider("MonthlyCharges" , min_value= 0 , max_value= 2000 , value=0,step=1)
    TotalCharges = st.slider("TotalCharges" , min_value= 0 , max_value= 20000 , value=0,step=1)
    tenure_MonthlyCharges_Segment = st.selectbox("tenure_MonthlyCharges_Segment" , ['Low Value Low Trust' , 'Low Value High Trust', 'High Value Low Trust' ,
    'High Value High Trust'])
    Streaming = st.selectbox("Contract" , ['No Streaming Service' , 'Yes All Streaming Services' , 'StreamingTV', 'No internet service' , 'StreamingMovies'])



    
    if st.button("predict"):
        
        result = prediction(SeniorCitizen, Partner, Dependents, tenure, PhoneService,MultipleLines, InternetService, OnlineSecurity,OnlineBackup,
        DeviceProtection,TechSupport, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges, TotalCharges,tenure_MonthlyCharges_Segment, Streaming)
        label = ["Fail" , "Success"]
        st.text(f"The Resturant will {label[result]}")
        

if __name__ == '__main__':
    main()
