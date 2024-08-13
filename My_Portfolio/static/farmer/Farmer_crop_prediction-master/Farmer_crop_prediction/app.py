from flask import Flask,render_template,url_for,request
import joblib
import pandas as pd
app=Flask(__name__)
std=joblib.load('./models/standard_scalar')
model=joblib.load('./models/kmeans_model')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/prediction',methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        N=int(request.form['n'])
        P=int(request.form['p'])
        K=int(request.form['k'])
        tempurature=float(request.form['temperature'])
        humidity=float(request.form['humidity'])
        ph=float(request.form['ph'])
        rainfall=float(request.form['rainfall'])
        unseen_data=[[N,P,K,tempurature,humidity,ph,rainfall]]
        converted_data=std.transform(unseen_data)
        prediction=model.predict(converted_data)[0]
        df=pd.read_csv(r'C:\Users\DeLL\Desktop\Data_Science\Farmer\models\app_data.csv')
        if prediction==0:
            cluster=df[df['cluster']==0]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_0.html')
        elif prediction==1:
            cluster=df[df['cluster']==1]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_1.html')
        elif prediction==2:
            cluster=df[df['cluster']==2]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_2.html')
        elif prediction==3:
            cluster=df[df['cluster']==3]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_3.html')
        elif prediction==4:
            cluster=df[df['cluster']==4]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_4.html')
        elif prediction==5:
            cluster=df[df['cluster']==5]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_5_6_7.html')
        elif prediction==6:
            cluster=df[df['cluster']==6]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_5_6_7.html')
        elif prediction==7:
            cluster=df[df['cluster']==7]
            ls=list(cluster['Label'].value_counts().keys())
            return render_template('cluster_5_6_7.html')
if __name__=='__main__':
    app.run(debug=True)
    