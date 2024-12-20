from api import *
from log import log
import json
from datetime import datetime

def main():

    processos_encontrados = procurar_pagamentos()

    docs = processos_encontrados.get("docs", [])
    if docs:  # Garantir que a lista não está vazia
        for doc in docs:
            process_id = doc.get("id")
        if process_id:
            print("ID do processo encontrado:", process_id)
        else:
            log.error("ID do processo não encontrado no documento.")
    else:
        log.error("Nenhum processo encontrado na lista de 'docs'.")
        
    dados_processo = [
       {"id": "a709d0a0-5e35-11ee-a079-1f098f945990", "value": "241219.134819.87"},
       {"id": "a2621a80-5e35-11ee-a079-1f098f945990", "value": "65a57321778210009d3aff8f"},
       {"id": "8b3e8060-5e39-11ee-8459-ab06c4a21f7f", "value": "64a4060258f25700a09f830d"},
       {"id": "9f339a10-5e39-11ee-8459-ab06c4a21f7f", "value": str(datetime.now().date())}
    ]
    
    novo_processo_id = criar_processo(dados_processo)
    if not novo_processo_id:
       log.error("Erro ao criar o novo processo.")
       return
    log.info(f"Processo criado com ID: {novo_processo_id}")
    
    tarefas = consulta_tarefa(novo_processo_id)
    
    if tarefas:
       # Acessa o 'current_activities' e filtra os que têm status 'opened'
       atividades_abertas = [
           atividade for atividade in tarefas.get('current_activities', [])
           if atividade.get('status') == 'opened'
       ]
       
       if atividades_abertas:
           # Pega o id da primeira atividade com status 'opened'
           id_task = atividades_abertas[0].get("id")
           print("ID da atividade aberta:", id_task)
       else:
           print("Nenhuma atividade aberta encontrada.")
           return   

    item_data = [

         {
            "id":"51dc5d70-9cfd-11ef-bc26-d53286ead034",
            "value":"Adriana Teste"
         },
         {
            "id":"5c5ecb70-9cfd-11ef-bc26-d53286ead034",
            "value":"2525"
         },
         {
            "id":"634d1630-9cfd-11ef-bc26-d53286ead034",
            "value":"07190908498"
         },
         {
            "id":"6ae42410-9cfd-11ef-bc26-d53286ead034",
            "value":"AOB2536"
         },
         {
            "id":"d3d89980-bd6c-11ef-ab18-b159b6633aaa",
            "value":"255566633333"
         },
         {
            "id":"1039e2b0-9cfe-11ef-bc26-d53286ead034",
            "value":"64aef588b883bc0080aeac24",
            "text":"DOC - RECIFE (PE)"
         },
         {
            "id":"042e6e40-9cff-11ef-bc26-d53286ead034",
            "value":"45.01"
         },
         {
            "id":"39422ad0-bd6c-11ef-b44a-7790c4069fda",
            "value":"1640.00"
         },
         {
            "id":"8a045cf0-9cff-11ef-bc26-d53286ead034",
            "value":"1500.00"
         },
         {
             "id":"479aa1f0-9cfd-11ef-bc26-d53286ead034",
            "value":None
         },
         {
            "id":"39422ad0-bd6c-11ef-b44a-7790c4069fda",
            "value":None
         },
         {
            "id":"47d936b0-bd6c-11ef-b44a-7790c4069fda",
            "value":None
         },
         {
            "id":"d3d89980-bd6c-11ef-ab18-b159b6633aaa",
            "value":"250.00"
         },
         {
            "id":"eb20e060-bd6d-11ef-ab18-b159b6633aaa",
            "value":"0.20"
         },
         {
            "id":"573c9dd0-bd6d-11ef-ab18-b159b6633aaa",
            "value":None
         },
         {
            "id":"9be44cd0-bd6d-11ef-ab18-b159b6633aaa",
            "value":"",
            "text":""
            },
         {
            "id":"b48e6310-bd6d-11ef-ab18-b159b6633aaa",
            "value":None
         },
         {
            "id":"c480e040-bd6d-11ef-ab18-b159b6633aaa",
            "value":None
         },
         {
            "id":"eb20e060-bd6d-11ef-ab18-b159b6633aaa",
            "value":None
         }
         
    ]
    
   # Processar documentos e armazenar itens na tabela
    for processo in docs:
        if isinstance(processo, dict):
            item_data = processo.get("props", []) 
            if item_data:
                for item in item_data:
                    # Construir dicionário no formato esperado
                    item_para_inserir = {
                        "identifier": item.get("codigo_do_cliente"),  
                        "value": item.get("2536")    
                    }
                    response = inserir_item_tabela(id_task, item_para_inserir)
                    if response:
                        log.info(f"Item inserido no processo {id_task}: {item_para_inserir}")
                    else:
                        log.error(f"Erro ao inserir item no processo {id_task}: {item_para_inserir}.")
            else:
                log.warning(f"Nenhum dado encontrado em 'props' para o processo {processo.get('id', 'desconhecido')}.")
        else:
            log.error("Estrutura inesperada no processo encontrado. Verifique o formato.")

    log.info(f"Todos os itens dos processos encontrados foram processados para o ID da tarefa {id_task}.")

if __name__ == "__main__":
    main()