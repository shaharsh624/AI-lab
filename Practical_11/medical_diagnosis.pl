symptom(cough).
symptom(sore_throat).
symptom(runny_nose).
symptom(headache).
symptom(muscle_aches).
symptom(fatigue).

diagnosis(cold) :-
    symptom(fever),
    symptom(cough),
    symptom(runny_nose),
    not(symptom(headache)),
    not(symptom(muscle_aches)),
    not(symptom(sore_throat)),
    not(symptom(fatigue)).

diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(runny_nose),
    symptom(headache),
    symptom(muscle_aches),
    symptom(fatigue),
    not(symptom(sore_throat)).
