import services.database as db


def Incluir(plantao)
    db.plantoes.insertOne(
        {
            Dia: plantao.dia,
            Dia_da_semana: plantao.dia_da_semana,
            Setor: plantao.setor,
            Turno: plantao.turno,
            Valor: plantao.valor
        }
    )    
    
