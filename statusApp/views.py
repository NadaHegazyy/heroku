from django.shortcuts import render
from joblib import load
from datetime import datetime
model=load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        id=request.POST['id']
        entid=request.POST['entid']
        founded=datetime.strptime(request.POST['founded'], '%Y-%m-%d').year
        if(request.POST['closed']==""):
            closed=2021
        else:
            closed=datetime.strptime(request.POST['closed'], '%Y-%m-%d').year
        investmentrounds=request.POST['investmentrounds']
        fundingrounds=request.POST['fundingrounds']
        fundingtotal=request.POST['fundingtotal']
        milestones=request.POST['milestones']
        relationship=request.POST['relationship']
        created=datetime.strptime(request.POST['created'], '%Y-%m-%d').year
        updated=datetime.strptime(request.POST['updated'], '%Y-%m-%d').year
        roi=request.POST['roi']
        age=request.POST['age']
        categorycode=request.POST['categorycode']
        countrycode=request.POST['countrycode']
        
        if(countrycode=='AUS'):
            country_code_AUS=1
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='CAN'):
            country_code_AUS=0
            country_code_CAN=1
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='DEU'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=1
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0
        elif(countrycode=='ESP'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=1
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='FRA'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=1
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='GBR'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=1
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0 
        elif(countrycode=='IND'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=1
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0   
        elif(countrycode=='ISR'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=1
            country_code_NLD=0
            country_code_USA=0
            country_code_other=0    
        elif(countrycode=='NLD'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=1
            country_code_USA=0
            country_code_other=0  
        elif(countrycode=='USA'):
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=1
            country_code_other=0  
        else:
            country_code_AUS=0
            country_code_CAN=0
            country_code_DEU=0
            country_code_ESP=0
            country_code_FRA=0
            country_code_GBR=0
            country_code_IND=0
            country_code_ISR=0
            country_code_NLD=0
            country_code_USA=0
            country_code_other=1
        if(categorycode=='advertising'):
            category_code_advertising=1
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='biotech') :
            category_code_advertising=0
            category_code_biotech=1
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='consulting') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=1
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='ecommerce') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=1
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='enterprise') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=1  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='videogames') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=1
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='mobile') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=1
            category_code_other=0
            category_code_software=0
            category_code_web=0
        elif(categorycode=='software') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=1
            category_code_web=0
        elif(categorycode=='web') :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=0
            category_code_software=0
            category_code_web=1
        else :
            category_code_advertising=0
            category_code_biotech=0
            category_code_consulting=0
            category_code_ecommerce=0
            category_code_enterprise=0  
            category_code_games_video=0
            category_code_mobile=0
            category_code_other=1
            category_code_software=0
            category_code_web=0
        
        y_pred=model.predict([[id,entid,founded,closed,investmentrounds,
        fundingrounds,fundingtotal,milestones,relationship,created,
        updated,roi,age,category_code_advertising,category_code_biotech,
        category_code_consulting,category_code_ecommerce,category_code_enterprise,
        category_code_games_video,category_code_mobile,category_code_other,
        category_code_software,category_code_web,country_code_AUS,
        country_code_CAN,country_code_DEU,country_code_ESP,country_code_FRA,
        country_code_GBR,country_code_IND,country_code_ISR,country_code_NLD,
        country_code_USA,country_code_other]])
        if y_pred[0]==1:
            y_pred='Operating'
        else:
            y_pred='Not Operating'
            
        
        return render(request,'main.html',{'result':y_pred})

    return render(request,'main.html')

