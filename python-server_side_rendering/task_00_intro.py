import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Xəta: template sətir (string) olmalıdır. Verilən tip: {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Xəta: attendees lüğətlərdən ibarət siyahı (list of dicts) olmalıdır.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    placeholders = ['name', 'event_title', 'event_date', 'event_location']
    for index, attendee in enumerate(attendees, start=1):
        personalized_template = template
        for placeholder in placeholders:
            value = str(attendee.get(placeholder, "N/A"))
            personalized_template = personalized_template.replace(f"{{{placeholder}}}", value)

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(personalized_template)
            print(f"Uğurla yaradıldı: {filename}")
        except Exception as e:
            print(f"Fayl yaradılarkən xəta baş verdi ({filename}): {e}")
template_text = """
Hörmətli {name},
Sizi {event_title} tədbirinə dəvət edirik!
Tarix: {event_date}
Məkan: {event_location}
"""
data = [
    {"name": "Əli", "event_title": "Python Seminarı", "event_date": "20 May", "event_location": "Bakı"},
    {"name": "Leyla", "event_title": "AI Konfransı", "event_location": "Gəncə"},
    {"name": "Murad", "event_date": "25 İyun"}
]
generate_invitations(template_text, data)
