sessions_text = input("Number of sessions: ")
sessions = int(sessions_text)

study_text = input("Study minutes per session: ")
study_minutes = int(study_text)

break_text = input("Break minutes per session: ")
break_minutes = int(break_text)

study_only = sessions * study_minutes
total_minutes = sessions * (study_minutes + break_minutes)

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Study only: {study_only} minutes")
print(f"Including breaks: {total_minutes} minutes")
print(f"Total duration: {hours} hours and {minutes} minutes")
