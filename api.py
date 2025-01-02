import json
import requests
from dotenv import dotenv_values
from log import log
from datetime import datetime
import io
import mimetypes
import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger # Manipulação com PDF

config = dotenv_values(".env")

def procurar_pagamentos():
    url = "https://app-api.holmesdoc.io/v2/search"
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = {
       
        "query":{
      "from":0,
      "size":50,
      "context":"search_task",
      "groups":[
         {
            "match_all":True,
            "terms":[
               {
                  "name":"Fluxos",
                  "value":"672bb26421488ff13bf7eac3",
                  "type":"is",
                  "filter":"HProcessFilter",
                  "field":"template_id",
                  "label":"4"
               },
               {
                  "field":"status",
                  "label":"Aberto",
                  "name":"Situação da tarefa",
                  "type":"is",
                  "value":"opened",
                  "filter":"HProcessStatusFilter",
                  "nested":False
               },
               {
                  "field":"task_id",
                  "name":"Tarefa",
                  "type":"terms",
                  "value":[
                    "Activity_1f4g2te",
                     "Activity_0abnbvh",
                     "Activity_1oc3fzl",
                     "Activity_08n366z"
                  ],
                  "filter":"HTaskFilter",
                  "label":"Pagamento de Taxas (+3)",
                  "nested":False,
                  "id":"6beb05f0-c6f0-11ef-b095-231f427efff2"
               }
            ],
            "properties":[
               None,
               None,
               None,
               None,
               {
                  "name":"Autor",
                  "filter":"HAuthorFilter",
                  "field":"author_id",
                  "type":"is"
               },
               {
                  "name":"Data de criação",
                  "filter":"HDateRange",
                  "field":"created_at",
                  "type":"today"
               },
               {
                  "name":"Concluído em",
                  "filter":"HDateRange",
                  "field":"completed_at",
                  "type":"today"
               },
               {
                  "name":"Situação",
                  "filter":"HProcessStatusFilter",
                  "field":"status",
                  "type":"is"
               },
               {
                  "name":"Título",
                  "filter":"HStringFilter",
                  "field":"identifier",
                  "type":"is"
               },
               {
                  "name":"Protocolo",
                  "filter":"HStringFilter",
                  "field":"protocol",
                  "type":"is"
               },
               {
                  "name":"Status do processo",
                  "filter":"HProcessTestFilter",
                  "field":"test",
                  "type":"is"
               },
               {
                  "name":"ID do processo",
                  "filter":"HMatchFilter",
                  "field":"_id",
                  "type":"is"
               }
            ],
            "not_used":False
         },
         {
            "match_all":True,
            "terms":[
               {
                  "name":"Fluxos",
                  "value":"67448262207222c1a6cc0693",
                  "type":"is",
                  "filter":"HProcessFilter",
                  "field":"template_id",
                  "label":"4"
               },
               {
                  "field":"status",
                  "label":"Aberto",
                  "name":"Situação da tarefa",
                  "type":"is",
                  "value":"opened",
                  "filter":"HProcessStatusFilter",
                  "nested":False
               },
               {
                  "field":"task_id",
                  "name":"Tarefa",
                  "type":"terms",
                  "value":[
                    "Activity_1f4g2te",
                     "Activity_0abnbvh",
                     "Activity_1oc3fzl",
                     "Activity_08n366z"
                  ],
                  "filter":"HTaskFilter",
                  "label":"Pagamento de Taxas (+3)",
                  "nested":False,
                  "id":"6beb05f0-c6f0-11ef-b095-231f427efff2"
               }
            ],
            "properties":[
               None,
               None,
               None,
               None,
               {
                  "name":"Autor",
                  "filter":"HAuthorFilter",
                  "field":"author_id",
                  "type":"is"
               },
               {
                  "name":"Data de criação",
                  "filter":"HDateRange",
                  "field":"created_at",
                  "type":"today"
               },
               {
                  "name":"Concluído em",
                  "filter":"HDateRange",
                  "field":"completed_at",
                  "type":"today"
               },
               {
                  "name":"Situação",
                  "filter":"HProcessStatusFilter",
                  "field":"status",
                  "type":"is"
               },
               {
                  "name":"Título",
                  "filter":"HStringFilter",
                  "field":"identifier",
                  "type":"is"
               },
               {
                  "name":"Protocolo",
                  "filter":"HStringFilter",
                  "field":"protocol",
                  "type":"is"
               },
               {
                  "name":"Status do processo",
                  "filter":"HProcessTestFilter",
                  "field":"test",
                  "type":"is"
               },
               {
                  "name":"ID do processo",
                  "filter":"HMatchFilter",
                  "field":"_id",
                  "type":"is"
               }
            ],
            "not_used":False
         },
         {
            "match_all":True,
            "terms":[
               {
                  "name":"Fluxos",
                  "value":"67448e5ba890a529fa8da35a",
                  "type":"is",
                  "filter":"HProcessFilter",
                  "field":"template_id",
                  "label":"4"
               },
               {
                  "field":"status",
                  "label":"Aberto",
                  "name":"Situação da tarefa",
                  "type":"is",
                  "value":"opened",
                  "filter":"HProcessStatusFilter",
                  "nested":False
               },
               {
                  "field":"task_id",
                  "name":"Tarefa",
                  "type":"terms",
                  "value":[
                    "Activity_1f4g2te",
                     "Activity_0abnbvh",
                     "Activity_1oc3fzl",
                     "Activity_08n366z"
                  ],
                  "filter":"HTaskFilter",
                  "label":"Pagamento de Taxas (+3)",
                  "nested":False,
                  "id":"6beb05f0-c6f0-11ef-b095-231f427efff2"
               }
            ],
            "properties":[
               None,
               None,
               None,
               None,
               {
                  "name":"Autor",
                  "filter":"HAuthorFilter",
                  "field":"author_id",
                  "type":"is"
               },
               {
                  "name":"Data de criação",
                  "filter":"HDateRange",
                  "field":"created_at",
                  "type":"today"
               },
               {
                  "name":"Concluído em",
                  "filter":"HDateRange",
                  "field":"completed_at",
                  "type":"today"
               },
               {
                  "name":"Situação",
                  "filter":"HProcessStatusFilter",
                  "field":"status",
                  "type":"is"
               },
               {
                  "name":"Título",
                  "filter":"HStringFilter",
                  "field":"identifier",
                  "type":"is"
               },
               {
                  "name":"Protocolo",
                  "filter":"HStringFilter",
                  "field":"protocol",
                  "type":"is"
               },
               {
                  "name":"Status do processo",
                  "filter":"HProcessTestFilter",
                  "field":"test",
                  "type":"is"
               },
               {
                  "name":"ID do processo",
                  "filter":"HMatchFilter",
                  "field":"_id",
                  "type":"is"
               }
            ],
            "not_used":False
         },
         {
            "match_all":True,
            "terms":[
               {
                  "name":"Fluxos",
                  "value":"67534ce5ecaac6715aa9caba",
                  "type":"is",
                  "filter":"HProcessFilter",
                  "field":"template_id",
                  "label":"4"
               },
               {
                  "field":"status",
                  "label":"Aberto",
                  "name":"Situação da tarefa",
                  "type":"is",
                  "value":"opened",
                  "filter":"HProcessStatusFilter",
                  "nested":False
               },
               {
                  "field":"task_id",
                  "name":"Tarefa",
                  "type":"terms",
                  "value":[
                    "Activity_1f4g2te",
                     "Activity_0abnbvh",
                     "Activity_1oc3fzl",
                     "Activity_08n366z"
                  ],
                  "filter":"HTaskFilter",
                  "label":"Pagamento de Taxas (+3)",
                  "nested":False,
                  "id":"6beb05f0-c6f0-11ef-b095-231f427efff2"
               }
            ],
            "properties":[
               None,
               None,
               None,
               None,
               {
                  "name":"Autor",
                  "filter":"HAuthorFilter",
                  "field":"author_id",
                  "type":"is"
               },
               {
                  "name":"Data de criação",
                  "filter":"HDateRange",
                  "field":"created_at",
                  "type":"today"
               },
               {
                  "name":"Concluído em",
                  "filter":"HDateRange",
                  "field":"completed_at",
                  "type":"today"
               },
               {
                  "name":"Situação",
                  "filter":"HProcessStatusFilter",
                  "field":"status",
                  "type":"is"
               },
               {
                  "name":"Título",
                  "filter":"HStringFilter",
                  "field":"identifier",
                  "type":"is"
               },
               {
                  "name":"Protocolo",
                  "filter":"HStringFilter",
                  "field":"protocol",
                  "type":"is"
               },
               {
                  "name":"Status do processo",
                  "filter":"HProcessTestFilter",
                  "field":"test",
                  "type":"is"
               },
               {
                  "name":"ID do processo",
                  "filter":"HMatchFilter",
                  "field":"_id",
                  "type":"is"
               }
            ],
            "not_used":False
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


def anexar_documento():    
    url = "https://app-api.holmesdoc.io/v1/documents"
    headers = {
        'api_token': config.get("API_TOKEN")
    }

        
    data =  {
                 'index': 'false'
            }
    files = {
                    'file': ('PDF_Mesclado.pdf', open('C:\\Users\\adriana.almeida\\Documents\\GitLab\\Automação Pagamentos\\documentos_baixados\\PDF_Mesclado.pdf', 'rb'), 'application/pdf')
            } 
    try:
        response = requests.post(url, headers=headers, data=data, files=files)

        if response.status_code in [200, 201]:
            log.info("Processos encontrados com sucesso.")
            response_json = response.json()
            # Acessar o 'id' do documento
            id_file = response_json.get('id')
            print(f"ID file do documentoooooooooooooooooooo: {id_file}")

            return id_file
        else:
            log.error(f"Erro ao buscar processos. Status: {response.status_code}")
            return {}
    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return {}

def criar_processo(dados_processo, id_file):
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
            "documents": [
                {
            "usage_id":"2a5eee90-5e3b-11ee-8459-ab06c4a21f7f",
            "file_id":id_file
         }
        
      ],
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
            
            response_data = response.json()

            # Verifica se existem atividades abertas em "current_activities"
            current_activities = response_data.get("current_activities", [])
            if not current_activities:
                log.error(f"Nenhuma atividade encontrada para o processo {novo_processo_id}.")
                return None

            for activity in current_activities:
                if activity.get("status") == "opened":
                    id_task = activity.get("id")
                    log.info(f"Tarefa encontrada com ID: {id_task}")
                    return id_task

            log.error(f"Nenhuma atividade aberta encontrada no processo {novo_processo_id}.")
            return None
        else:
            log.error(f"Erro ao consultar o processo {novo_processo_id}. Status: {response.status_code}")
            return None
    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return None
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return None
        
    

def inserir_item_tabela(id_task, item_data):
    url = f"https://app-api.holmesdoc.io/v1/tasks/{id_task}/tables/4524bcb0-bd7a-11ef-8655-952326b212d9/table_items"
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get("API_TOKEN")
    }
    payload = { "item": {
            "property_values": [
                {"id": "51dc5d70-9cfd-11ef-bc26-d53286ead034", "value": item_data["cliente"]},
                {"id": "5c5ecb70-9cfd-11ef-bc26-d53286ead034", "value": item_data["codigo"]},
                {"id": "634d1630-9cfd-11ef-bc26-d53286ead034", "value": item_data["CPF / CNPJ"]},
                {"id": "6ae42410-9cfd-11ef-bc26-d53286ead034", "value": item_data["placa"]},
                {"id": "d3d89980-bd6c-11ef-ab18-b159b6633aaa", "value": item_data["chassi"]},
                {"id": "1039e2b0-9cfe-11ef-bc26-d53286ead034", "value": item_data["loja"]},
                {"id": "e4710fd0-c3b0-11ef-acd7-771d0e5c06cd", "value": item_data["tipo_de_servico"]},
                {"id": "1ca735e0-bd6d-11ef-ab18-b159b6633aaa", "value": item_data["pagar"]},
                {"id": "24cd4fe0-c1f8-11ef-acc2-bbf857ae428c", "value": item_data["taxas_detran"]},
                {"id": "9be44cd0-bd6d-11ef-ab18-b159b6633aaa", "value": item_data["responsavel_atual"], "text": ""}
            ]}}
   
   
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            log.info("Item inserido com sucesso no processo.")
            return response.json()
        else:
            log.error(f"Erro ao inserir item. Status: {response.status_code}. Detalhes: {response.text}")
            return {}

    except requests.RequestException as e:
        log.error(f"Erro na requisição: {e}")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Erro de decodificação JSON: {e}")
        return {}




def listar_documentos(process_id):
    """
    Lista os documentos de um processo e baixa cada documento encontrado.
    Retorna uma lista de documentos baixados (em bytes) com seus IDs.
    """
    url = f'https://app-api.holmesdoc.io/v1/processes/{process_id}/documents' 
    headers = {
        'Content-Type': 'application/json',
        'api_token':  config.get('API_TOKEN')
    }
    
    try:
        log.info(f"Listando documentos para o processo {process_id}.")
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        try:
            dados = response.json()
            documentos = dados.get('documents', [])
        
            # Formatando a saída como uma lista de dicionários
            log.info(f"{len(documentos)} documentos encontrados para o processo {process_id}.")
            return documentos
        except (json.JSONDecodeError, KeyError) as e:
            log.error(f"Erro ao processar a resposta da API para o processo {process_id}: {e}")
            return []

    except requests.exceptions.RequestException as e:
        log.error(f"Erro ao buscar documentos para o processo {process_id}: {e}")
        return []
    
    
    

        
def baixar_documento_da_api(document_id, pasta_destino):
    url = f'https://app-api.holmesdoc.io/v1/documents/{document_id}/download?base64=false'
    headers = {
        'Content-Type': 'application/json',
        'api_token': config.get('API_TOKEN')
    }
    
    try:
        log.info(f"Baixando PDF do documento {document_id} da API.")

        response_documento = requests.get(url, headers=headers)
        response_documento.raise_for_status()
        if 'application/pdf' in response_documento.headers.get('Content-Type', ''):
            return io.BytesIO(response_documento.content)  # Retorna o PDF como bytes
        else:
            log.error(f"Erro: O arquivo baixado não é um PDF")
            return None
    except requests.exceptions.RequestException as e:
        log.error(f"Erro ao baixar PDF da API: {e}")
        return None
    
def mesclar_pdfs(lista_arquivos, arquivo_saida):
    try:
        merger = PdfMerger()
        for arquivo in lista_arquivos:
            merger.append(arquivo)
        merger.write(arquivo_saida)
        merger.close()
        log.info(f"PDFs mesclados com sucesso em: {arquivo_saida}")
        return arquivo_saida
    except Exception as e:
        log.error(f"Erro ao mesclar PDFs: {e}")
        return None

def preencher_item_data(key, value, fluxo, item_data):
    mapeamento = {
        "empresa": {
            "Transferência Empresa": "7dd2b9f0-c3af-11ef-8644-afccd683324c",
            "Transferência Cliente": "1de3a4a0-c12a-11ef-809c-b18dcb819ed9",
        },
        "cliente": {
            "Transferência Empresa": "3a1aff10-ae4c-11ef-b1fc-a5a6a8166bca",
            "Transferência Cliente": "e245bae0-a0ff-11ef-8d5b-1f445e916c08",
        },
        "codigo": {
            "Transferência Empresa": "1440e290-b3d4-11ef-b692-b3bb4e8edf2e",
            "Transferência Cliente": "8e78d590-9de5-11ef-afb9-fbfd3d7e5422",
        },
        "CPF / CNPJ": {
            "Transferência Empresa": "4eef7c40-ae4c-11ef-b1fc-a5a6a8166bca",
            "Transferência Cliente": "6ac92c60-a1bb-11ef-aee5-7f20f4b11b97",
        },
        "placa": {
            "Transferência Empresa": "8d11b470-ae4c-11ef-b1fc-a5a6a8166bca",
            "Transferência Cliente": "064127e0-a100-11ef-8d5b-1f445e916c08",
        },
        "chassi": {
            "Transferência Empresa": "36d04b70-ae4d-11ef-92f1-a1a7c4c0009f",
            "Transferência Cliente": "fbaeb450-a0ff-11ef-8d5b-1f445e916c08",
        },
        "pagar": {
            "Transferência Empresa": "d38cbeb0-ae5e-11ef-b6f7-cd21e09e8d3f",
            "Transferência Cliente": "a47a9c40-a063-11ef-a4d5-5911ae28917d",
        },
        "responsavel_atual": {
            "Transferência Empresa": "bd933fb0-b3d3-11ef-b692-b3bb4e8edf2e",
            "Transferência Cliente": "3a3ae930-bbec-11ef-8186-8f4d11bdfdd0",
        },
        "taxas_detran": {
            "Transferência Empresa": "e3c86ed0-b95f-11ef-9661-fff35e180cdb",
            "Transferência Cliente": None,
        },
    }

    # Verificar se a chave é válida para o fluxo atual
    if key in mapeamento and fluxo in mapeamento[key]:
        id_esperado = mapeamento[key][fluxo]
        if id_esperado == value:
            item_data[key] = value
    else:
        log.warning(f"Chave {key} não mapeada para o fluxo {fluxo} ou valor não corresponde.")
