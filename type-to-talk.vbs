strText = inputbox("What should Sam say?","Sam")
Set objVoice = CreateObject ("SAPI.SpVoice")
ObjVoice.speak strText
