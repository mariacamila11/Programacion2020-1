#------------MENSAJES----------#
PREGUNTA_PACIENTE= "Ingrese el numero de pacientes : "
PRIM_RIESGO=" El riesgo es bajo"
SEG_RIESGO= "El riesgo es medio"
TER_RIESGO= "El riesgo es alto"
PACIENTE_UCI= "Ingrese el numero de pacientes en UCI : "
#------------ENTRADAS---------
_pacientes= 1
_pacientesUCI= 1
#------------CODIGO-----------
_pacientes= int(input(PREGUNTA_PACIENTE))
_pacientesUCI= int(input(PACIENTE_UCI))
if ((_pacientes >0) and (_pacientes <=1000)):
    print (PRIM_RIESGO)
elif ((_pacientes >1000) and (_pacientes <=5000)):
    if (_pacientesUCI >=1000):
        print(TER_RIESGO)
    else: 
        print(SEG_RIESGO)
else:
    print(TER_RIESGO)