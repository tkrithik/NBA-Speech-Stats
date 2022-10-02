#-----------Import Commands-----------
from io import BytesIO
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os, os.path
import speech_recognition as sr
from nba_stats import nba_stats
from gtts import gTTS

#Speech Recognition Instantiation
r = sr.Recognizer()

#Flask config and db config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#DB upload class
class Upload(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  filename = db.Column(db.String(50))
  data = db.Column(db.LargeBinary)

@app.route("/", methods=["GET", "POST"])
def index():
  ''' This function lets you create a local flask page, which we have assigned to /, 
  thus meaning the route is simply the local host, without any subdomain to navigate to. 
  The index function starts by getting the file the user uploaded, and then creates a new copy of the file locally. 
  Then, using other functions, it converts from sound to text, then to sound again and pushes back to the user.'''
  if request.method == "POST":
    file_object = request.files["file_name"]
    print('file_object:' + file_object.filename)
    #upload = Upload(name=file_object.filename, data=file_object.read())
    file_object.save(os.path.join('/Users/krithikt/Documents/Hackathon/Slam Dunk Hacks 2/Input', secure_filename(file_object.filename)))

    mytext=speech_to_text('/Users/krithikt/Documents/Hackathon/Slam Dunk Hacks 2/Input/' + file_object.filename)
    print(mytext)
    mytext = bball(str(mytext).rstrip())
    print(mytext)
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save('/Users/krithikt/Documents/Hackathon/Slam Dunk Hacks 2/Output/' + "output.mp3")
    # files = glob.glob('/Users/krithikt/Documents/Hackathon/Slam Dunk Hacks 2/Input')
    # for f in files:
    #   os.remove(f)
    # db.session.add(upload)
    # db.session.commmit()
    return f"Uploaded: {file_object.filename}"
  return render_template('index.html') # Html template

@app.route("/download/<upload_id>")
def download(upload_id):
  ''' This function helps download the file the user uploads, and saves it locally.'''
  print("in download")
  upload = Upload.query.filter_by(id=upload_id).first()
  return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)

def speech_to_text(audio_file_path):
  ''' This function uses the speech regonition API to convert the given audio by the user into text. This text is then returned to be used in other functions.'''
  # files = glob.glob('/Users/krithikt/Documents/Hackathon/Slam Dunk Hacks 2/Output')
  # for f in files:
  #     os.remove(f)
  audio_obj = sr.AudioFile(audio_file_path)
  with audio_obj as source:
    audio = r.record(source)
  audio_text = (r.recognize_google(audio))
  print(audio_text)
  return audio_text

def bball(speech_input):
  try:
    #''' This function analyzes the user's speech and determines if the user can retreive stats, and what stats to retireve. The nba_stats module webscrapes on yahoo for these stats.'''
    user_input = speech_input.lower()
    user_input_list = []
    
    
    for word in user_input:
      user_input_list = list(user_input.split(" "))
    
    #'''If the user does not input a related input in the correct format a recording will play back to them, letting them know.'''
    
    nba_list = []
    nba_list2 = []
    
    for word in user_input_list:
      if word.lower() == "player" or word.lower() == "team":
        nba_list.append(word)
        index = user_input_list.index(word) + 1
        while index < len(user_input_list):
          nba_list.append(user_input_list[index])
          index += 1
        break
  #''' After getting all the necessary strings and thouroughly analyzing the user's input, the code then determiens if the user is asking for a player, a team, and what stats'''
    
    #for user_input
    print(nba_list)
    search_type = nba_list[0]
    nba_list.pop(0)
    
    
    if nba_list[-1].lower() == 'goals' or nba_list[-1].lower() == "pointers":
      nba_list.pop(-1)
    
    search_thing = nba_list[-1]
    nba_list.pop(-1)
    
    search_string = ""
    
    
    for word in nba_list:
      search_string += word
      search_string += " "
    
    search_string = search_string.rstrip()
    if (search_string[-2]+search_string[-1]).lower() == "'s":
      search_string = search_string[:len(search_string) - 2]
    
    
    name_string = search_string.rstrip()
    
    
    print(name_string)
    
    
    #'''The above code tests if the user asks for player, and the below code will 
      #test if the user asks for a team stat or specific stat.'''
    stats_dictionary = {}
    
    for word in nba_list:
      print(search_type)
      if search_type.lower() == 'player':
        print("happy")
        player = nba_stats.Player(name_string)
        if search_thing.lower() == "stats":
          stats_dictionary['Team'] = player.team
          stats_dictionary["Number"] = player.position
          stats_dictionary["Points"] = player.avg_pt
          stats_dictionary["Rebounds"] = player.avg_reb
          stats_dictionary["Assists"] = player.avg_ast
          stats_dictionary["College"] = player.college
        elif search_thing.lower() == "team":
          stats_dictionary['Team'] = player.team
        elif search_thing.lower() == "number":
          stats_dictionary["Number"] = player.position
        elif search_thing.lower() == "points":
          stats_dictionary["Points"] = player.avg_pt
        elif search_thing.lower() == "rebounds":
          stats_dictionary["Rebounds"] = player.avg_reb
        elif search_thing.lower() == "assists":
          stats_dictionary["Assists"] = player.avg_ast
        elif search_thing.lower() == "college":
          stats_dictionary["College"] = player.college
        
      elif search_type.lower() == "team":
        team = nba_stats.Team(name_string)
        if search_thing.lower() == "stats":
          stats_dictionary["Wins"] = team.win
          stats_dictionary["Losses"] = team.loss
          stats_dictionary["Points"] = team.pt
          stats_dictionary["Rebounds"] = team.reb
          stats_dictionary["Field Goals"] = team.fg
          stats_dictionary["Three Pointers"] = team.percent_3pt
          stats_dictionary["Standings"] = team.standing
        elif search_thing.lower() == "wins":
          stats_dictionary["Wins"] = team.win
        elif search_thing.lower() == "losses":
          stats_dictionary["Losses"] = team.loss
        elif search_thing.lower() == "points":
          stats_dictionary["Points"] = team.pt
        elif search_thing.lower() == "rebounds":
          stats_dictionary["Rebounds"] = team.reb
        elif search_thing.lower() == "field":
          stats_dictionary["Field Goals"] = team.fg
        elif search_thing.lower() == "three":
          stats_dictionary["Three Pointers"] = team.percent_3pt
        elif search_thing.lower() == "standings":
          stats_dictionary["Standings"] = team.standing
    
    print(stats_dictionary) 

    #After determing what stats the user is asking for, the code turns to compile all these stats into one single string, which will later be returned, in order to turn that string into audio for the user. '''
      
    final_string = ""
    for stat in stats_dictionary:
      if stats_dictionary[stat] == "":
        continue
      else:
        try:
          stats_dictionary[stat] = float(stats_dictionary[stat])
          stats_dictionary[stat] = str(stats_dictionary[stat]) + ' per game'
          final_string += name_string.title()+"'s " + str(stat) + " is "+ str(stats_dictionary[stat]) + ". "
        except:
          final_string += name_string.title()+"'s " + str(stat) + " is "+ str(stats_dictionary[stat]) + ". "
    
    return final_string
      
  except:
    return "You did not speak a valid input! Please try again."




  
  
  