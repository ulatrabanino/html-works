# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os 

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def get_meme_url(meme_choice):
    if meme_choice == 'creeper':
        url = 'https://static.turbosquid.com/Preview/2016/03/14__23_58_21/MinecraftCreeper02.jpg2a29f0cd-04de-4935-998b-8fe7735414efOriginal.jpg'
    elif meme_choice == 'kirby':
        url = 'https://vignette.wikia.nocookie.net/characterprofile/images/5/5c/Kirby.png/revision/latest/scale-to-width-down/210?cb=20160103100842'
    elif meme_choice == 'peach':
        url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ed991cf4-7c8c-4530-b6ba-a3abf3ab2eae/dc3uutk-328f7fa0-5de0-45cd-ba44-6c05b12fa681.png/v1/fill/w_600,h_875,strp/super_mario__princess_peach_2d_by_joshuat1306_dc3uutk-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODc1IiwicGF0aCI6IlwvZlwvZWQ5OTFjZjQtN2M4Yy00NTMwLWI2YmEtYTNhYmYzYWIyZWFlXC9kYzN1dXRrLTMyOGY3ZmEwLTVkZTAtNDVjZC1iYTQ0LTZjMDViMTJmYTY4MS5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.7aX60fQwjxdt06kYIx1ao2jZUyEV-UP28s8qt_zCvlE'
    elif meme_choice == 'isabelle':
        url = 'https://images-na.ssl-images-amazon.com/images/I/51csyS9liyL._SL1000_.jpg'
    return url

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        the_variable_dict = {
            "greeting": "Welcome!!!",
            "adjective": "splendid"
        }
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render(the_variable_dict))  # the response
# etc
    def post(self):
        self.response.write("POST request was made to the EnterInfoHandler")
        
class MainPage(webapp2.RequestHandler): 
    def get(self): 
        self.response.headers['Content-Type'] = 'text/plain' 
        self.response.write('Hello, World!')
        
class ShowMemeHandler(webapp2.RequestHandler):        
    def get(self):  
        results_template = the_jinja_env.get_template('templates/results.html')
        the_variable_dict = {
            "line1":"creeper",
            "line2":"aw man",
            "img_url":"https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
        }
        self.response.write(results_template.render(the_variable_dict))
        
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        
        meme_choice = self.request.get('meme-type')
        
        pic_url = get_meme_url(meme_choice)
        
        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": pic_url
                             }
         # the response
        self.response.write(results_template.render(the_variable_dict))
        
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/results', ShowMemeHandler),
], debug=True)
