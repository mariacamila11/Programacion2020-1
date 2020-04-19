import funciones_lectura as funciones_lectura
lineas= funciones_lectura.leer_archivo("noticia.txt")
funciones_lectura.mostrar_lineas(lineas)

Texto = ["Aqui estara mi opinion sobre la noticia:\n",
"Este es el momento para buscar soluciones a otras problematicas serias que afectan nuestro pais\n"
"el gobierno no solo puede estar enfocado en una sola situacion porque se le saldran de las manos otras \n"
"este es el momento de darle paso fumigar cultivos sabiendo que la gente esta en sus casas y se pueden utilizar mas medidas por la cuarentena."]

funciones_lectura.escritura_archivo("Opinion.txt",Texto)
funciones_lectura.agregar_lineas_archivo("noticia.txt","\n17 de Abril")