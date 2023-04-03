strText = inputbox("What should I say?","Type to Talk")
Set objVoice = CreateObject ("SAPI.SpVoice")
ObjVoice.Rate=-3
ObjVoice.speak strText
