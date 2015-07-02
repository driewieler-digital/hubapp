#!/bin/env python

import string,cgi,time
from os import sep
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import pri
import sys
import urllib2
import random
import time
import socket       
from config import Config
    
                    
class MyHandler(BaseHTTPRequestHandler):     

    def do_GET(self):
            

        cur_dir = os.path.dirname(os.path.realpath(__file__))            
            
        try:               
        
            print self.path
            
            if self.path == "/":
                self.path = "/index.html"
        
            if self.path.endswith(".html") and "index.html" in self.path:
                f = open(cur_dir + sep + self.path) #self.path has index.html

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if self.path.endswith(".json"):
                f = open(cur_dir + sep + self.path) #self.path has index.html

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type',    'text/json')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if ".woff" in self.path or ".ttf" in self.path or ".svg" in self.path :
                f = open(cur_dir + sep + self.path) #self.path has index.html

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type', "font/opentype")
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return          
                
            if self.path.endswith(".gif"):
                
                f = open(cur_dir + sep + self.path) #self.path has index.html

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type', "image/gif")
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return                          

            if self.path.endswith(".png"):
                
                f = open(cur_dir + sep + self.path) #self.path has index.html

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type', "image/png")
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return 

            if self.path.endswith(".js"):
                f = open(cur_dir + sep + self.path) 

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type',    'application/javascript')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
                
            if self.path.endswith(".css"):
                f = open(cur_dir + sep + self.path) 

                # open index.html and send it to the client
                self.send_response(200)
                self.send_header('Content-type',    'text/css')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return                
                
            if self.spoof == "spoof":

                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()        
                spoof_data = 'Spoof';
                if "request=sysready" in self.path:
                    spoof_data = 'READY:1'         
                    spoof_data = 'ID:xxxxxxx\nREADY:1'                                    
                    """r0 = random.randint(0, 10)
                    if r0 < 5:
                        spoof_data = 'READY:0'       """

                elif "request=connect" in self.path:
                    spoof_data = 'HANDLE:8eff970\nSTATUS:OK'
                elif "request=folders" in self.path:
                    spoof_data = "0/4:(TYPE:email|NAME:email444|ADDR:testing2@mplus2.on-go.com)\n"
                    spoof_data += "1/4:(TYPE:feed|NAME:feed781|ADDR:testing2@mplus2.on-go.com)\n"
                    spoof_data += "2/4:(TYPE:group|NAME:group797|ADDR:testing2@mplus2.on-go.com)\n"
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735|ADDR:+12402046375)\n"                                                                                                 
                    
                elif "request=contacts" in self.path:
                    spoof_data = "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:tchen61@gmail.com|ADDR:tchen61@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert.van.engelen@gmail.com|ADDR:robert.van.enjhjjjjkhyglihlgyijjjjjyihgughyiljkjjjjygukgyuigelen@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:info@driewielerdigital.com|ADDR:info@driewielerdigital.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert@driewielerdigital.com|ADDR:robert@driewielerdigital.com|STATE:ONLINE)\n"                                                            
                    spoof_data += "1/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6596748463|ADDR:6596748463|STATE:ONLINE)\n"
                    
                    spoof_data += "2/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6597501749|ADDR:6597501149|STATE:OFFLINE)\n"                    
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735)(NICK:aliastest|NAME:6596748463|ADDR:6553245463|STATE:BUSY)\n"                    
                    
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:tchen61@gmail.com|ADDR:tchen61@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert.van.engelen@gmail.com|ADDR:robert.van.enjhjjjjkhyglihlgyijjjjjyihgughyiljkjjjjygukgyuigelen@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:info@driewielerdigital.com|ADDR:info@driewielerdigital.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert@driewielerdigital.com|ADDR:robert@driewielerdigital.com|STATE:ONLINE)\n"                                                            
                    spoof_data += "1/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6596748463|ADDR:6596748463|STATE:ONLINE)\n"
                    
                    spoof_data += "2/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6597501749|ADDR:6597501149|STATE:OFFLINE)\n"                    
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735)(NICK:aliastest|NAME:6596748463|ADDR:6553245463|STATE:BUSY)\n"                    
                    
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:tchen61@gmail.com|ADDR:tchen61@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert.van.engelen@gmail.com|ADDR:robert.van.enjhjjjjkhyglihlgyijjjjjyihgughyiljkjjjjygukgyuigelen@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:info@driewielerdigital.com|ADDR:info@driewielerdigital.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert@driewielerdigital.com|ADDR:robert@driewielerdigital.com|STATE:ONLINE)\n"                                                            
                    spoof_data += "1/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6596748463|ADDR:6596748463|STATE:ONLINE)\n"
                    
                    spoof_data += "2/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6597501749|ADDR:6597501149|STATE:OFFLINE)\n"                    
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735)(NICK:aliastest|NAME:6596748463|ADDR:6553245463|STATE:BUSY)\n"                    
                    
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:tchen61@gmail.com|ADDR:tchen61@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert.van.engelen@gmail.com|ADDR:robert.van.enjhjjjjkhyglihlgyijjjjjyihgughyiljkjjjjygukgyuigelen@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:info@driewielerdigital.com|ADDR:info@driewielerdigital.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert@driewielerdigital.com|ADDR:robert@driewielerdigital.com|STATE:ONLINE)\n"                                                            
                    spoof_data += "1/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6596748463|ADDR:6596748463|STATE:ONLINE)\n"
                    
                    spoof_data += "2/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6597501749|ADDR:6597501149|STATE:OFFLINE)\n"                    
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735)(NICK:aliastest|NAME:6596748463|ADDR:6553245463|STATE:BUSY)\n"                    
                    
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:tchen61@gmail.com|ADDR:tchen61@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert.van.engelen@gmail.com|ADDR:robert.van.enjhjjjjkhyglihlgyijjjjjyihgughyiljkjjjjygukgyuigelen@gmail.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:info@driewielerdigital.com|ADDR:info@driewielerdigital.com|STATE:ONLINE)\n"
                    spoof_data += "0/4:(TYPE:email|NAME:email444)(NICK:|NAME:robert@driewielerdigital.com|ADDR:robert@driewielerdigital.com|STATE:ONLINE)\n"                                                            
                    spoof_data += "1/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6596748463|ADDR:6596748463|STATE:ONLINE)\n"
                    
                    spoof_data += "2/4:(TYPE:sms|NAME:sms735)(NICK:|NAME:6597501749|ADDR:6597501149|STATE:OFFLINE)\n"                    
                    spoof_data += "3/4:(TYPE:sms|NAME:sms735)(NICK:aliastest|NAME:6596748463|ADDR:6553245463|STATE:BUSY)\n"                                                                                                    
                                                                                
                elif "request=send" in self.path:
                    randint = random.randint(1000, 9999)
                    spoof_data = "MSGID:{}\n\nSTATUS:2".format(randint)
                elif "request=chksend" in self.path:
                    r0 = random.randint(0, 10)
                    if r0 < 7:
                        return
                    spoof_data = "STATUS:3:DELIVERED"
                elif "request=recv" in self.path:
                    r0 = random.randint(0, 10)
                    if r0 < -1:
                        return              
                    spoof_data = "TYPE:email\n\nFROM:tchen61@gmail.com\n\nBODY:Test message #"
                    spoof_data += "{}".format(random.randint(0, 10))

                    
                elif "request=polling" in self.path:
                    #pick random events.
                    mail_addr = ['6596748463','6597501749','tchen61@gmail.com', 'mobius@wheel.nl']
                    states = ['OFFLINE', 'AVAILABLE', 'ONLINE', 'BUSY', 'IDLE', 'AWAY']
                    
                
                    r0 = random.randint(0, 10)
                    if r0 < -1:
                        return
                
                    r1 = random.randint(0, 3)
                    r2 = random.randint(0, 5)
                                    
                    spoof_data = "1/2:(TYPE:email|NAME:gtalk946)(NICK:AlexChen|NAME:alex98chengmailcom|ADDR:"
                    spoof_data += mail_addr[r1]
                    spoof_data += "|STATE:"
                    spoof_data += states[r2]
                    spoof_data += ")"
                    
                    r1 = random.randint(0, 3)
                    r2 = random.randint(0, 5)
                                    
                    spoof_data += "2/2:(TYPE:email|NAME:gtalk946)(NICK:AlexChen|NAME:alex98chengmailcom|ADDR:"
                    spoof_data += mail_addr[r1]
                    spoof_data += "|STATE:"
                    spoof_data += states[r2]
                    spoof_data += ")"    
                    
                elif "request=get_history" in self.path:
                    #time.sleep(10)
                    spoof_data = "(0/2) TIMESTAMP:Thu Mar 19 12:40:44 2015 DIRECTION:OUT BODY:this is a test"
                    spoof_data += "(1/2) TIMESTAMP:Fri Mar 27 11:31:00 2015 DIRECTION:OUT BODY:Tttttwew wwerwrwerwr"
                    spoof_data += "(1/2) TIMESTAMP:Fri Mar 27 11:31:00 2015 DIRECTION:OUT BODY:Tttttwew wwerwrwerwr"
                    spoof_data += "(1/2) TIMESTAMP:Fri Mar 27 11:31:00 2015 DIRECTION:OUT BODY:Tttttwew wwerwrwerwr"
                    spoof_data += "(1/2) TIMESTAMP:Fri Mar 27 11:31:00 2015 DIRECTION:OUT BODY:Tttttwew wwerwrwerwr"                                                            
                elif "request=close" in self.path:
                    time.sleep(1)
                    spoof_data = "Ok, logged out."   
                elif "request=forget_password" in self.path:
                    spoof_data = "Question(4):\n"
                    spoof_data += "1) Question #1\n"
                    spoof_data += "2) Question #2\n"
                    spoof_data += "3) Question #3\n"                                                                       
                    spoof_data += "4) Question #4 which, as it happens, is a very long question so we can test how our newly born view reacts to this.\n"                                                                                           
                elif "request=reset_password":
                    time.sleep(2)
                    spoof_data = "STATUS: "
                    r0 = random.randint(0, 10)
                    if r0 < 5:
                        spoof_data += "OK\n"
                    else:
                        spoof_data += "FAIL\n"
                                        
                self.wfile.write(spoof_data)
                r = spoof_data
                print "Response: "+r                
                return
            
            else:
                self.send_response(200)
                
                #get response from the server
                try:
                    args = self.path.split("request=",1)[1]
                except:
                    #print 'Index error.'
                    return
                    args = ''

                #dto = socket.getdefaulttimeout()
                #socket.setdefaulttimeout(60)

                print "Opening "+self.servername+":"+self.server_port+"/?request="+args

                r = urllib2.urlopen("http://"+self.servername+":"+self.server_port+"/?request="+args).read()
                """Python 3.x:

                import urllib.request
                urllib.request.urlopen("http://example.com/foo/bar").read()             
                   """                        
                
                self.send_header('Content-type', 'text/html')
                self.end_headers()        
                self.wfile.write(r)
                #print "Response: "+r
                
                return        
                
                
            return
                
        except:
            #self.send_error(404,'File Not Found')
            print "Network log"

            
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass


try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


print (sys.version)

print 'Usage: python ./webserver.py [portnumber] [server address] [server port]'
print 'Configuration in config.py and config.js'

# get the configuration file
cfg = Config()    
    
if len(sys.argv) > 1:
    print sys.argv[1]
    port = int(sys.argv[1])
    print 'Port {}'.format(port)
    
else:
    port = cfg.port

MyHandler.spoof = "nospoof"        
if len(sys.argv) > 2:
    MyHandler.servername = sys.argv[2]        
else:
    MyHandler.servername = cfg.servername
            
if len(sys.argv) > 3:
    MyHandler.server_port = sys.argv[3]                    
else:
    MyHandler.server_port = cfg.serverport
    
if MyHandler.servername == "spoof":
    MyHandler.spoof = "spoof"   

server = ThreadingSimpleServer(('', int(port)), MyHandler)

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")
    server.socket.close()