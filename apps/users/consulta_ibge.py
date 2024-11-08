from ibge.localidades import *


def unidade_federativa():
    uf_estado = Estados()
    siglas = uf_estado.getSigla()
    nomes = uf_estado.getNome()
    estados = list(zip(siglas, nomes))  # Cria uma lista de tuplas (sigla, nome)
    return estados


def municipios_por_uf(unidade_federativa):    
    estado_por_uf = MunicipioPorUF(unidade_federativa)
    nome_municipios = estado_por_uf.getNome()
    return nome_municipios
