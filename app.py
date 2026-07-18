import os
from flask import Flask, render_template, request, jsonify
from logics.database import Database
import shutil

# main flask app with the DB connection
app=Flask(__name__)
base_dir=os.path.dirname(os.path.abspath(__file__))

# Safely check if running inside the Android environment
if "ANDROID_ARGUMENT" in os.environ or "ANDROID_BOOTSTRAP" in os.environ:
    from android.content import Context
    from com.chaquo.python import Python
    context = Python.getPlatform().getApplication()
    db_path=os.path.join(str(context.getFilesDir().getAbsolutePath()), 'Calculator.sqlite3')
    pkg_db_path=os.path.join(base_dir, 'Calculator.sqlite3')
    if not os.path.exists(pkg_db_path):
      try:
        shutil.copy2(pkg_db_path, db_path)
      except Exception as e:
        print('Error cp in:', e)
else:
    db_path= os.path.join(base_dir, 'Calculator.sqlite3')

db=Database(db_path)

#----------------------------------------------------------- index.html ---------------------------------------------------
@app.route('/')
def index():
  return render_template('index.html')

#-----------------------------------------------------------  history.html ---------------------------------------------------
@app.route('/history') #see the entire history
def history_page():
  rec_datas=db.get_all_datas()
  return render_template('libs/history.html', datas=rec_datas)

@app.route('/save_to_database', methods=['POST', 'GET']) # after a calculation made this will going to save only valid calculations in the DB.......
def save_to_database():
  if request.method == 'POST':
 
    #recive sent datas
    recent_value=request.get_json()
    arguments=recent_value['arguments']
    result=recent_value['result']

    #save it to the database
    db.insert(datas=(arguments, result))
    return jsonify({'status': 'success'})
  else:
    return render_template('index.html')
  
#----------------------------------------------------------- export.html ---------------------------------------------------
@app.route('/export', methods=['POST', 'GET'])
def export_page():
  if request.method == 'POST':
    html_=request.form.get('html')
    csv_=request.form.get('csv')
    excel_=request.form.get('excel')
    rename=request.form.get('rename', '')
    rename=rename.replace('.','')

    # which ones are checked???????
    if html_ != None:
      db.export_html(rename)
    if csv_ != None:
      db.export_csv(rename)
    if excel_ != None:
      db.export_excel(rename)
    if not (html_ or csv_ or excel_):
      return None
    return render_template('libs/export.html', done='Successfully Exported!')
  else:
    return render_template('libs/export.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4501, debug=False)