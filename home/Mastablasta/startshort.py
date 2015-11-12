import random
from java.lang import String
alice2 = Runtime.createAndStart("alice2", "ProgramAB")
alice2.startSession("ProgramAB", "default", "alice2")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
alice2.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
holygrail = Runtime.create("holygrail", "WebGUI")
holygrail.startService()
sleep(4)
resp = alice2.getResponse("HI")
