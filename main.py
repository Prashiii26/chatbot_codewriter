import os
from voice import speak
import shutil
from listen import listen
from datetime import datetime
import webbrowser
import pyautogui
import time
from codeassistant import write_code_file_and_type
from chat import chat
global last_command_time
global last_context
global last_action






last_action=None
last_context=None
last_command_time=0
BASE_DIR = "C:/assistant_files"
LOG_FILE = os.path.join(BASE_DIR, "command_log.txt")
os.makedirs(BASE_DIR,exist_ok=True)
def log_command(command):
    """Logs the command with a timestamp to the log file"""
    with open(LOG_FILE, "a") as f:  # append mode
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {command}\n")


def assistant():
    global last_command_time, last_context,last_action
    speak("i am online... plase tell keyword to use my services")
    active=False
    history=[]

    while True:
      #  user_input = listen()
      #  if not user_input:
      #         speak("sorry i couldnt hear it please type the message")
       user_input=input(">>")
       user_input = user_input.lower().strip()
       log_command(user_input)
       now=time.time()
       if now-last_command_time<1.5:
          continue
       last_command_time=now   
        
          
       if not active:
         
          if user_input=="motherfucker":
            speak("password accepted.... whats my order")
            active=True    
          else:
             speak("wrong keyword")


       else:
           if user_input == "motherfucker":
              speak("already active")
              continue

           elif "create folder" in user_input:
              folder_name=user_input.replace("create folder","").strip()
              path=os.path.join(BASE_DIR,folder_name)
              if not folder_name:
                 speak("please say a folder name")
              else:
                 os.makedirs(path,exist_ok=True)
                 speak(f"folder {folder_name} created") 

           elif "open folder" in user_input:
              folder_name=user_input.replace("open folder","").strip()
              path=os.path.join(BASE_DIR,folder_name)
              if os.path.exists(path) and os.path.isdir(path):
                 os.startfile(path)
                 speak(f"folder {folder_name} opened")
              else:
                 speak("folder not found")   
                 
           elif "create file" in user_input:
              file_name=user_input.replace("create file","").strip()
              path=os.path.join(BASE_DIR,file_name+".txt")
              with open(path,"w") as f:
                 f.write("created by assisstant")
                 speak(f"file {file_name} created")

           elif "open file" in user_input:
              file_name=user_input.replace("open file","").strip()
              path=os.path.join(BASE_DIR,file_name+".txt") 
              if os.path.exists(path):
                 with open(path,"r") as f:
                    content=f.read()
                    speak(content)     

              else:
                 speak("file doesnt exist")

           elif "delete folder" in user_input:
                folder_name=user_input.replace("delete folder","").strip()
                path=os.path.join(BASE_DIR,folder_name)
                if not folder_name:
                   speak("please say the folder name")
                elif not os.path.exists(path) or not os.path.isdir(path):
                   speak("folder not found")
                else:
                   if not os.listdir(path):
                      os.rmdir(path)
                      speak(f"folder {folder_name} deleted")
                  
                   else:
                      speak("folder is not empty.. do u still want to delete?")
                      confirm=input("yes or no").lower()
                      if confirm=="yes":
                         shutil.rmtree(path)
                         speak(f"folder {folder_name} deleted permanently")
                      else:
                         speak("folder is safe")                          
           elif "delete file" in user_input:
                file_name = user_input.replace("delete file", "").strip()
                path = os.path.join(BASE_DIR, file_name + ".txt")

                if not file_name:
                  speak("Please say the file name")
                elif os.path.exists(path):
                  os.remove(path)
                  speak(f"file {file_name} deleted")
                else:
                  speak("file not found")


           elif any(word in user_input.lower() for word in ["write code","stop", "next", "pause", "play", "previous",
                                                                "close tab", "close browser", "reopen tab", "next tab", "previous tab",
                                                                "shutdown", "restart", "volume", "brightness","open bluetooth","close bluetooth",
                                                                "open chrome", "search google", "open youtube", "open website","screenshot"]): 
             
              if "write code" in user_input:
                  write_code_file_and_type(user_input.replace("write code to", "").strip())

              elif "screenshot" in user_input:
                 try:
                    filename=os.path.join(BASE_DIR,f"screenshot_{int(time.time())}.png")  
                    screenshot=pyautogui.screenshot()
                    screenshot.save(filename)
                    speak("screenshot taken")

                 except Exception as e:
                    speak("Sorry, I couldn't take the screenshot")
                    print(e)    


              elif user_input=="next":
                 if last_context=="youtube":
                    
                  pyautogui.hotkey("shift", "n")
                  speak("Playing next video")

                 else:
                    speak("youtube is not active") 

              elif user_input== "pause" or user_input== "play" or user_input=="stop":
                 if last_context=="youtube":
                    
                  pyautogui.press("k")
                  speak("done")

                 else:
                    speak("no video active") 

              elif user_input=="previous":
                 if last_context=="youtube":
                    
                  pyautogui.hotkey("shift","p")
                  speak("playing previous video")  

                 else:
                    speak("no video active")  

              elif "close tab" in user_input:
                  pyautogui.hotkey("ctrl", "w")
                  speak("Closing the current tab") 
                  last_context=None

              elif "close browser" in user_input or "close chrome" in user_input:
                  pyautogui.hotkey("alt", "f4")
                  speak("Closing the browser")    
                  last_context=None

              elif "reopen tab" in user_input:
                  pyautogui.hotkey("ctrl", "shift", "t")
                  speak("Reopening the last closed tab") 

              elif "next tab" in user_input:
                  pyautogui.hotkey("ctrl", "tab")
                  speak("Switching to next tab")   

              elif "previous tab" in user_input:
                  pyautogui.hotkey("ctrl", "shift", "tab")
                  speak("Switching to previous tab")
   



              elif "shutdown" in user_input or "restart" in user_input:
                  if "shutdown" in user_input:
                    action = "shutdown"
                    command = "shutdown /s /t 5"
                    speak_text = "Shutting down the laptop"
                  elif "restart" in user_input:
                    action = "restart"
                    command = "shutdown /r /t 5"
                    speak_text = "Restarting the laptop"
    

                  speak(f"Do you really want to {action}? Please say yes or no.")
                  confirm=input().lower()
                  # confirm = listen().lower()
                  if confirm == "yes":
                     speak(speak_text)
                     os.system(command)
                     last_action=None
                     
                     last_context=None
                  else:
                     speak(f"{action.capitalize()} cancelled")
    
              elif "open bluetooth" in user_input or "close bluetooth" in user_input:
                     pyautogui.hotkey("win","a")
                     time.sleep(0.5)
                     pyautogui.press("right")
                     time.sleep(0.5)
                     pyautogui.press("enter")
                     speak("bluetooth status updated")


              elif "volume" in user_input:
                 
                  
                     try:
                        if any(char.isdigit() for char in user_input):

                          vol = int(''.join(filter(str.isdigit, user_input)))
                          if 0<=vol<=100:
                             for i in range(50):
                       
                               pyautogui.press("volumedown")
                               time.sleep(0.02)
                             presses=vol//2
                             for i in range(int(presses)):
                                pyautogui.press("volumeup")
                                time.sleep(0.01)
                             speak(f"volume set to {vol}")

                          else:
                             speak("say proper volume level")

                        elif any(word in user_input for word in ["increase", "up", "louder", "raise"]) :
                           for i in range(10):
                              pyautogui.press("volumeup")
                              time.sleep(0.01)    
                           speak("volume increased")
                        
                        elif any(word in user_input for word in ["decrease", "down", "lower", "quieter"]) :
                           for i in range(10):
                              pyautogui.press("volumedown")
                              time.sleep(0.01)    
                           speak("volume decreased")


                                 

                     except ValueError:
                        speak("couldnt understand the volume setup")

              elif "brightness" in user_input:
                 
                   
                      try:
                       if any(char.isdigit() for char in user_input):
                         vol=int(''.join(filter(str.isdigit,user_input)))
                         if 0<=vol<=100:
                            pyautogui.hotkey("win","a")
                            for i in range (4):  
                             pyautogui.press("tab")
                            for i in range(100):
                             pyautogui.press("left") 
                             time.sleep(0.03)
                            for i in range(int(vol)):
                               pyautogui.press("right")
                               time.sleep(0.03)
                            speak(f"brightness set to {vol}")
                            pyautogui.press("esc")

                         else:
                            speak("say proper brightness level")   

                       elif any(word in user_input for word in ["increase", "brighter", "up"] ):
                          pyautogui.hotkey("win","a")
                          time.sleep(0.01)
                          for i in range (4):  
                             pyautogui.press("tab")

                          for i in range(15):
                             pyautogui.press("right")
                             time.sleep(0.01)  
                          speak("brightness increased")
                          pyautogui.press("esc")


                       elif any(word in user_input for word in ["decrease", "dimmer", "down","lower"] ):
                          pyautogui.hotkey("win","a")
                          time.sleep(0.01)
                          for i in range (4):  
                             pyautogui.press("tab")

                          for i in range(15):
                             pyautogui.press("left")
                             time.sleep(0.01)   
                          speak("brightness decreased")
                          pyautogui.press("esc")       
                             
                       

                      except ValueError:
                         speak("couldnt understand brightness level")   
                      

     
              elif "open chrome" in user_input:
                 os.system("start chrome")
                 speak("Opening chrome")

              elif user_input == "sleep":
                 active = False
                 speak("Going to sleep")
                 last_action=None
                 
                 last_context=None

              elif user_input == "exit":
                 speak("Goodbye")
                 break
           
              elif "search google" in user_input:
                 query=user_input.replace("search google","").strip()
                 if query:
                   url=f"https://www.google.com/search?q={query.replace(' ', '+')}"
                   webbrowser.open(url)
                   time.sleep(5)
                   for _ in range(22):
                     pyautogui.press( 'tab')

                   pyautogui.press('enter')
                   speak(f"opening {query}")
                 else:
                   speak("what should i search")

              elif "open youtube" in user_input:
                 query=user_input.replace("open youtube","").strip()
                 if query:
                   url=f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                   webbrowser.open(url)
                   time.sleep(6)
                   pyautogui.click(500,300) 
                   speak(f"opening {query}")
                   last_action="playing"+query
                   
                   last_context="youtube"
                 else:
                   speak("what should i search in youtube")     


              elif "open website" in user_input:
                 query=user_input.replace("open website","").strip()
                 if query:  
                   site="https://"+query+".com" 
                   webbrowser.open(site)
                   speak(f"opening {query}")
                   last_action=f"opened {query} site"
                 else:
                   speak("which website to open?")
                           
              else:
                  speak("I did not understand that command")

           else:
              history.append(f"User: {user_input}")
              response = chat(user_input, history)
              speak(response)
              history.append(f"AI: {response}")
                  


assistant()    


