#!/usr/bin/env python3
""" This module instantiates an object of class DBStorage"""
from models.engine.db_storage import DBStorage

questions = {
        1: "Cuánto tiempo tienes invirtiendo tu capital?",
        2: "Cuanto conoces de otras alternativas de inversión \
            a parte de las que te puede ofrecer un banco?",
        3: "Cuánto tiempo esperas darles a tu inversión?",
        4: "Tu situación financiera te permite realizar una inversión y, si \
            se pierde parte de ésta, no tener problemas con tu presupuesto \
            personal o familiar?",
        5: "Si tu inversión empieza a perder valor, que harías?"
        }
answers = {1: {
               0: "Nunca he invertido",
               1: "No más de 1 año",
               2: "Entre 1 y 3 años",
               3: "entre 3 y 5 años",
               4: "Más de 5 años"
               },
           2: {
               0: "No conozco otras alternativas",
               1: "Muy poco",
               2: "Poco",
               3: "Regular",
               4: "Mucho"
               },
           3: {
               0: "Menos de 3 meses",
               1: "Entre 3 meses y 1 año",
               2: "Entre 1 y 3 años",
               3: "Entre 3 y 5 años",
               4: "Más de 5 años",
               },
           4: {
               0: "Tendría muchos problemas con mi presupuesto personal o familiar",
               2: "Tendría pocos problemas con mi presupuesto personal o familiar",
               4: "No se afectaría mi presupuesto personal o familiar"
               },
           5: {
               0: "De ser posible, retiraría mi inversión inmediatamente porque \
                   no tolero que se pierda nada de mi capital",
               2: "De ser posible, retiraría una parte de mi inversión \
                   inmediatamente y dejaría otra para ver si se recupera \
                   mi capital",
               3: "No retiraría mi inversión inmediatamente, pero si no se \
                   recupera en el corto plazo si lo retiraría",
               4: "No retiraría mi inversión inmediatamente, porque sé que \
                   hay ciclos en las inversiones y me quedaría a esperar la \
                   recuperación del valor en el mediano o largo plazo"
               }
        }

storage = DBStorage()
storage.reload()


