import json
import requests
from dotenv import dotenv_values
from log import log
from datetime import datetime

config = dotenv_values(".env")

def procurar_pagamentos():
    url = "https://app-api.holmesdoc.io/v2/search"
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = {
        "query": {
            "from": 0,
            "size": 50,
            "context": "search_task",
            "groups": [
                {
                    "terms": [
                        {
                            "field": "template_id",
                            "filter": "HProcessFilter",
                            "label": "TRANSFERÊNCIA EMPRESA",
                            "name": "Fluxos",
                            "nested": False,
                            "type": "is",
                            "value": "67448262207222c1a6cc0693"
                        },
                        {
                            "field": "status",
                            "filter": "HProcessStatusFilter",
                            "label": "Aberto",
                            "name": "Situação da tarefa",
                            "nested": False,
                            "type": "is",
                            "value": "opened"
                        },
                        {
                            "field": "task_id",
                            "filter": "HTaskFilter",
                            "label": "Pagamento de Taxas",
                            "name": "Tarefa",
                            "nested": False,
                            "type": "terms",
                            "value": ["Activity_0abnbvh"]
                        }
                    ]
                }
            ]
        }
    }
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code in [200, 201]:
            log.info("Processos encontrados com sucesso.")
            return response.json()
        else:
            log.error(f"Erro ao buscar processos. Status: {response.status_code}")
            return {}
    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return {}
    


def criar_processo(dados_processo):
    url = "https://app-api.holmesdoc.io/v1/workflows/6515d487bd795100650581e9/start"
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = {
        "workflow": {
            "start_event": "Event_1cnpha0",
            "property_values": dados_processo,
            "whats": "",
            "documents": [],
            "test": False
        }
    }
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code in [200, 201]:
            try:
                response_data = response.json()  
                process_id = response_data.get('id')
                if process_id:
                    log.info(f"Processo criado com sucesso. ID do processo: {process_id}")
                    return process_id  
                else:
                    log.error("Processo criado, mas o ID não foi retornado.")
                    return None
            except json.JSONDecodeError:
                log.error(f"Erro ao decodificar a resposta JSON: {response.text}")
                return None
        else:
            log.error(f"Erro ao criar processo. Status: {response.status_code} ")
            return None
    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return None
    
def consulta_tarefa(novo_processo_id):
    
    url = f"https://app-api.holmesdoc.io/v2/processes/{novo_processo_id}"    
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = {
       "return_tasks":True
   }
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code in [200, 201]:
            log.info(f"Consulta bem-sucedida para o processo {novo_processo_id}.")
            return response.json()
        else:
            log.error(f"Erro ao inserir item. Status: {response.status_code}")
            return {}
    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return {}
        
    

def inserir_item_tabela(id_task, item_data):
    url = f"https://app-api.holmesdoc.io/v1/tasks/{id_task}/tables/4524bcb0-bd7a-11ef-8655-952326b212d9/table_items"
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = {"item": {"property_values": item_data}}
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        
        if response.status_code in [200, 201]:
            log.info("Item inserido com sucesso no processo.")
            return response.json()
        else:
            log.error(f"Erro ao inserir item. Status: {response.status_code}. ")
            return {}

    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return {}